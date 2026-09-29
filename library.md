# Essential Python Computer Vision Libraries

A curated guide to widely used Python libraries and frameworks for image processing, computer vision, and deep learning. Each entry summarizes its type, strengths, core tasks, and a practical example.

## Image Processing and Classical Computer Vision

### OpenCV
- **Type:** General-purpose computer vision and image-processing library with Python bindings.
- **Description:** OpenCV provides optimized tools for working with images and video, from basic pixel operations to feature detection and camera calibration.
- **Key tasks:** Image and video I/O, filtering, color conversion, geometric transforms, feature detection, camera calibration, and real-time video processing.
- **Example use case:** Read frames from a camera, detect edges or contours, and highlight objects that meet chosen shape or size criteria.
- **Project:** [opencv/opencv](https://github.com/opencv/opencv) | [Documentation](https://docs.opencv.org/)

### Scikit-Image
- **Type:** Scientific image-processing library built on NumPy and SciPy.
- **Description:** Scikit-Image offers composable algorithms and utilities that fit naturally into Python scientific-computing workflows.
- **Key tasks:** Image filtering, morphology, segmentation, feature measurement, transformations, and image restoration.
- **Example use case:** Clean a microscopy image with morphological operations, segment regions of interest, and measure their area and shape.
- **Project:** [scikit-image/scikit-image](https://github.com/scikit-image/scikit-image) | [Documentation](https://scikit-image.org/docs/stable/)

## Deep Learning Frameworks

### PyTorch
- **Type:** Open-source machine-learning and deep-learning framework.
- **Description:** PyTorch provides tensor computation, automatic differentiation, and neural-network building blocks for research and production computer vision.
- **Key tasks:** Build and train image classifiers, detectors, segmenters, and custom vision models; fine-tune pretrained networks; run GPU inference.
- **Example use case:** Fine-tune a pretrained convolutional network to classify product images into catalog categories.
- **Project:** [pytorch/pytorch](https://github.com/pytorch/pytorch) | [Documentation](https://pytorch.org/docs/)

### TensorFlow
- **Type:** End-to-end machine-learning and deep-learning framework.
- **Description:** TensorFlow provides APIs for building and training neural networks, with deployment options spanning servers, browsers, and edge devices.
- **Key tasks:** Train image classifiers and segmentation models, prepare data pipelines, export models, and deploy inference with TensorFlow Lite.
- **Example use case:** Train a defect classifier on factory images and export a compact model for on-device inspection.
- **Project:** [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) | [Documentation](https://www.tensorflow.org/)

## Object Detection

### YOLO
- **Type:** Family of real-time object-detection models and associated software implementations; Ultralytics provides a popular Python package.
- **Description:** YOLO models predict object locations and classes in images or video in a single model pass, supporting fast detection workflows.
- **Key tasks:** Object detection, instance segmentation, image classification, pose estimation, tracking workflows, and model export, depending on model and package version.
- **Example use case:** Train a detector on annotated warehouse images, then process a video stream to locate and count packages.
- **Project:** [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) | [Documentation](https://docs.ultralytics.com/)

## Real-Time Perception and Landmarks

### MediaPipe
- **Type:** Cross-platform framework and set of ready-to-use perception tasks, with Python APIs.
- **Description:** MediaPipe makes it straightforward to run real-time perception pipelines for common tasks, often using pretrained models and hardware-accelerated processing.
- **Key tasks:** Hand and pose landmark detection, face detection and landmarks, image classification, object detection, and video processing.
- **Example use case:** Track hand landmarks from a webcam feed to build a gesture-controlled interface.
- **Project:** [google-ai-edge/mediapipe](https://github.com/google-ai-edge/mediapipe) | [Documentation](https://ai.google.dev/edge/mediapipe/solutions/guide)
