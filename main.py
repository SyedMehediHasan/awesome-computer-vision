"""Build a Markdown directory of popular computer vision repositories."""

from datetime import datetime, timezone
import os
from pathlib import Path
import time

import requests
from dotenv import load_dotenv

from config import CATEGORIES, GITHUB_SEARCH_URL, RESULTS_PER_CATEGORY


PROJECT_DIR = Path(__file__).resolve().parent
PROJECT_PATH = PROJECT_DIR / "PROJECT.md"
PLACEHOLDER_TOKEN = "your_github_personal_access_token_here"


def get_github_token():
    """Return a configured token, ignoring the checked-in template value."""
    load_dotenv(PROJECT_DIR / ".env")
    token = os.getenv("GITHUB_TOKEN", "").strip()
    if token.lower() == PLACEHOLDER_TOKEN:
        return None
    return token or None


def fetch_repositories(session, query, token=None):
    """Fetch up to five repositories, sorted by stars, for one topic query."""
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": RESULTS_PER_CATEGORY,
    }

    for attempt in range(2):
        response = session.get(
            GITHUB_SEARCH_URL,
            headers=headers,
            params=params,
            timeout=30,
        )
        if response.status_code == 403 and response.headers.get("X-RateLimit-Remaining") == "0":
            if attempt == 0:
                reset_at = int(response.headers.get("X-RateLimit-Reset", "0"))
                time.sleep(max(0, reset_at - int(time.time())) + 1)
                continue
        response.raise_for_status()
        return response.json().get("items", [])

    return []


def markdown_cell(value):
    """Keep values safe to display inside a Markdown table cell."""
    return str(value or "N/A").replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def render_repository_table(repositories):
    lines = [
        "| Repository | Description | Stars | Language | Last updated |",
        "| --- | --- | ---: | --- | --- |",
    ]
    if not repositories:
        lines.append("| No matching repositories found | | | | |")
        return "\n".join(lines)

    for repository in repositories:
        name = markdown_cell(repository.get("full_name"))
        url = repository.get("html_url", "")
        description = markdown_cell(repository.get("description"))
        stars = repository.get("stargazers_count", 0)
        language = markdown_cell(repository.get("language"))
        updated = markdown_cell((repository.get("updated_at") or "")[:10])
        lines.append(
            f"| [{name}]({url}) | {description} | {stars:,} | {language} | {updated} |"
        )
    return "\n".join(lines)


def build_project(results):
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Awesome Computer Vision Repositories",
        "",
        "A curated directory of popular, Python-based computer vision tools and libraries, "
        "collected from GitHub repository topics.",
        "",
        f"Generated: {generated_at}",
        "",
        "## Table of Contents",
        "",
    ]

    for category in CATEGORIES:
        anchor = category.lower().replace(" ", "-")
        lines.append(f"- [{category}](#{anchor})")

    lines.extend([
        "",
        "## Categories",
        "",
    ])

    for category, subcategories in CATEGORIES.items():
        lines.extend([f"## {category}", ""])
        for subcategory, query, _tools in subcategories:
            repositories, error = results.get((category, subcategory), ([], None))
            lines.extend([f"### {subcategory}", "", f"Search: `{query}`", ""])
            if error:
                lines.extend([f"> Could not fetch results: {markdown_cell(error)}", ""])
            lines.extend([render_repository_table(repositories), ""])

    lines.extend([
        "## About this list",
        "",
        "Repositories are selected by GitHub's repository search using the topic shown above, "
        f"sorted by stars, with up to {RESULTS_PER_CATEGORY} results per sub-category. "
        "Search results depend on repository topics and may change over time.",
        "",
    ])
    return "\n".join(lines)


def main():
    token = get_github_token()
    results = {}
    with requests.Session() as session:
        for category, subcategories in CATEGORIES.items():
            for subcategory, query, _tools in subcategories:
                try:
                    repositories = fetch_repositories(session, query, token)
                    results[(category, subcategory)] = (repositories, None)
                    print(f"Fetched {len(repositories)} repositories: {category} / {subcategory}")
                except (requests.RequestException, ValueError) as error:
                    results[(category, subcategory)] = ([], str(error))
                    print(f"Failed: {category} / {subcategory}: {error}")

    PROJECT_PATH.write_text(build_project(results), encoding="utf-8")
    print(f"\nProject overview written to {PROJECT_PATH}")


if __name__ == "__main__":
    main()