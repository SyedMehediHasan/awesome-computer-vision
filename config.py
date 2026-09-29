"""Computer vision category queries and curated tool recommendations."""

CATEGORIES = {
    "Image Classification": [
        (
            "Binary Classification",
            "topic:binary-classification language:Python",
            [
                ("Roboflow", "https://roboflow.com", "Prepare datasets and train image classifiers."),
                ("PyTorch", "https://pytorch.org", "Build and train custom binary classifiers."),
            ],
        ),
        (
            "Multi-Class Classification",
            "topic:multi-class-classification language:Python",
            [
                ("Label Studio", "https://labelstud.io", "Annotate images with multiple classes."),
                ("timm", "https://github.com/huggingface/pytorch-image-models", "Use pretrained image classification models."),
            ],
        ),
        (
            "General Image Classification",
            "topic:image-classification language:Python",
            [
                ("Roboflow", "https://roboflow.com", "Manage image datasets and classification workflows."),
                ("OpenVINO", "https://github.com/openvinotoolkit/openvino", "Optimize and deploy classification inference."),
            ],
        ),
    ],
    "Object Detection": [
        (
            "Object Detection",
            "topic:object-detection language:Python",
            [
                ("Ultralytics", "https://github.com/ultralytics/ultralytics", "Train and run YOLO object detectors."),
                ("Roboflow", "https://roboflow.com", "Annotate, manage, and deploy detection datasets."),
                ("LabelImg", "https://github.com/HumanSignal/labelImg", "Create bounding-box annotations."),
            ],
        ),
        (
            "Face Detection",
            "topic:face-detection language:Python",
            [
                ("OpenCV", "https://opencv.org", "Run classical and neural face detection pipelines."),
                ("InsightFace", "https://github.com/deepinsight/insightface", "Use face analysis and detection models."),
            ],
        ),
        (
            "Text Detection",
            "topic:text-detection language:Python",
            [
                ("PaddleOCR", "https://github.com/PaddlePaddle/PaddleOCR", "Detect and recognize text in images."),
                ("Label Studio", "https://labelstud.io", "Annotate text regions for custom detection datasets."),
            ],
        ),
    ],
    "Image Segmentation": [
        (
            "Semantic Segmentation",
            "topic:semantic-segmentation language:Python",
            [
                ("MMSegmentation", "https://github.com/open-mmlab/mmsegmentation", "Train semantic segmentation models."),
                ("Roboflow", "https://roboflow.com", "Annotate and manage pixel-mask datasets."),
            ],
        ),
        (
            "Instance Segmentation",
            "topic:instance-segmentation language:Python",
            [
                ("Ultralytics", "https://github.com/ultralytics/ultralytics", "Train instance segmentation models."),
                ("CVAT", "https://www.cvat.ai", "Annotate instance masks and computer vision datasets."),
            ],
        ),
        (
            "Medical Image Segmentation",
            "topic:medical-image-segmentation language:Python",
            [
                ("MONAI", "https://monai.io", "Build medical imaging AI and segmentation workflows."),
                ("3D Slicer", "https://www.slicer.org", "Visualize and annotate medical images in 3D."),
            ],
        ),
    ],
    "Object Tracking": [
        (
            "Object Tracking",
            "topic:object-tracking language:Python",
            [
                ("Supervision", "https://github.com/roboflow/supervision", "Compose detection and tracking workflows."),
                ("Norfair", "https://github.com/tryolabs/norfair", "Track detected objects across video frames."),
            ],
        ),
        (
            "Multi-Object Tracking",
            "topic:multi-object-tracking language:Python",
            [
                ("ByteTrack", "https://github.com/FoundationVision/ByteTrack", "Associate detections for multi-object tracking."),
                ("BoxMOT", "https://github.com/mikel-brostrom/boxmot", "Compare and run multi-object tracking methods."),
            ],
        ),
        (
            "Visual Tracking",
            "topic:visual-tracking language:Python",
            [
                ("PyTracking", "https://github.com/visionml/pytracking", "Run visual object tracking algorithms."),
                ("OpenCV", "https://opencv.org", "Build video processing and tracking pipelines."),
            ],
        ),
    ],
    "Pose Estimation": [
        (
            "Pose Estimation",
            "topic:pose-estimation language:Python",
            [
                ("MMPose", "https://github.com/open-mmlab/mmpose", "Train and evaluate pose estimation models."),
                ("OpenVINO", "https://github.com/openvinotoolkit/openvino", "Optimize pose inference for deployment."),
            ],
        ),
        (
            "Human Pose Estimation",
            "topic:human-pose-estimation language:Python",
            [
                ("OpenPose", "https://github.com/CMU-Perceptual-Computing-Lab/openpose", "Estimate human body keypoints in images and video."),
                ("MMPose", "https://github.com/open-mmlab/mmpose", "Use a broad collection of human pose models."),
            ],
        ),
        (
            "Hand Pose Estimation",
            "topic:hand-pose-estimation language:Python",
            [
                ("MediaPipe", "https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker", "Detect hands and estimate hand landmarks."),
                ("MMPose", "https://github.com/open-mmlab/mmpose", "Train and evaluate hand keypoint models."),
            ],
        ),
    ],
    "Optical Character Recognition": [
        (
            "OCR",
            "topic:ocr language:Python",
            [
                ("PaddleOCR", "https://github.com/PaddlePaddle/PaddleOCR", "Recognize text in images and documents."),
                ("Tesseract", "https://github.com/tesseract-ocr/tesseract", "Run open-source optical character recognition."),
            ],
        ),
        (
            "Scene Text Recognition",
            "topic:scene-text-recognition language:Python",
            [
                ("EasyOCR", "https://github.com/JaidedAI/EasyOCR", "Read text in natural scene images."),
                ("docTR", "https://github.com/mindee/doctr", "Detect and recognize text in documents."),
            ],
        ),
        (
            "Document Understanding",
            "topic:document-understanding language:Python",
            [
                ("LayoutParser", "https://github.com/Layout-Parser/layout-parser", "Analyze and extract document layouts."),
                ("Label Studio", "https://labelstud.io", "Annotate document regions and text labels."),
            ],
        ),
    ],
    "Image Restoration": [
        (
            "Image Denoising",
            "topic:image-denoising language:Python",
            [
                ("OpenCV", "https://opencv.org", "Apply image filtering and denoising methods."),
                ("BasicSR", "https://github.com/XPixelGroup/BasicSR", "Train image restoration and denoising models."),
            ],
        ),
        (
            "Image Super-Resolution",
            "topic:super-resolution language:Python",
            [
                ("Real-ESRGAN", "https://github.com/xinntao/Real-ESRGAN", "Enhance image resolution with pretrained models."),
                ("OpenVINO", "https://github.com/openvinotoolkit/openvino", "Optimize super-resolution inference."),
            ],
        ),
        (
            "Image Deblurring",
            "topic:image-deblurring language:Python",
            [
                ("BasicSR", "https://github.com/XPixelGroup/BasicSR", "Train image deblurring and restoration models."),
                ("OpenCV", "https://opencv.org", "Prototype image enhancement and filtering pipelines."),
            ],
        ),
    ],
    "Image Generation and Editing": [
        (
            "Image Generation",
            "topic:image-generation language:Python",
            [
                ("Diffusers", "https://github.com/huggingface/diffusers", "Build and run diffusion-based image generation."),
                ("ComfyUI", "https://github.com/comfyanonymous/ComfyUI", "Compose node-based image generation workflows."),
            ],
        ),
        (
            "Image Inpainting",
            "topic:image-inpainting language:Python",
            [
                ("Diffusers", "https://github.com/huggingface/diffusers", "Run diffusion-based inpainting pipelines."),
                ("LaMa", "https://github.com/advimman/lama", "Restore image regions with large-mask inpainting."),
            ],
        ),
        (
            "Image-to-Image Translation",
            "topic:image-to-image-translation language:Python",
            [
                ("Diffusers", "https://github.com/huggingface/diffusers", "Run image-to-image diffusion pipelines."),
                ("ControlNet", "https://github.com/lllyasviel/ControlNet", "Guide image generation with spatial conditions."),
            ],
        ),
    ],
    "3D Computer Vision": [
        (
            "3D Reconstruction",
            "topic:3d-reconstruction language:Python",
            [
                ("COLMAP", "https://github.com/colmap/colmap", "Reconstruct 3D scenes from image collections."),
                ("Nerfstudio", "https://github.com/nerfstudio-project/nerfstudio", "Build neural radiance field reconstructions."),
            ],
        ),
        (
            "Depth Estimation",
            "topic:depth-estimation language:Python",
            [
                ("Depth Anything V2", "https://github.com/DepthAnything/Depth-Anything-V2", "Estimate depth maps from images."),
                ("OpenVINO", "https://github.com/openvinotoolkit/openvino", "Optimize depth model inference."),
            ],
        ),
        (
            "Point Clouds",
            "topic:point-cloud language:Python",
            [
                ("Open3D", "https://www.open3d.org", "Process and visualize 3D data and point clouds."),
                ("PCL", "https://pointclouds.org", "Use point cloud processing algorithms and tools."),
            ],
        ),
    ],
}

GITHUB_SEARCH_URL = "https://api.github.com/search/repositories"
RESULTS_PER_CATEGORY = 5