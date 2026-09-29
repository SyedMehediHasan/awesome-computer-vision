# Recommended Tools & Platforms

Curated tools and platforms organized by the computer vision categories and sub-categories used by this project. This file is maintained separately from the generated GitHub repository directory in `PROJECT.md`.

## Image Classification

### Binary Classification
| Tool / Platform | Recommended use |
| --- | --- |
| [Roboflow](https://roboflow.com) | Prepare datasets and train image classifiers. |
| [PyTorch](https://pytorch.org) | Build and train custom binary classifiers. |

### Multi-Class Classification
| Tool / Platform | Recommended use |
| --- | --- |
| [Label Studio](https://labelstud.io) | Annotate images with multiple classes. |
| [timm](https://github.com/huggingface/pytorch-image-models) | Use pretrained image classification models. |

### General Image Classification
| Tool / Platform | Recommended use |
| --- | --- |
| [Roboflow](https://roboflow.com) | Manage image datasets and classification workflows. |
| [OpenVINO](https://github.com/openvinotoolkit/openvino) | Optimize and deploy classification inference. |

## Object Detection

### Object Detection
| Tool / Platform | Recommended use |
| --- | --- |
| [Ultralytics](https://github.com/ultralytics/ultralytics) | Train and run YOLO object detectors. |
| [Roboflow](https://roboflow.com) | Annotate, manage, and deploy detection datasets. |
| [LabelImg](https://github.com/HumanSignal/labelImg) | Create bounding-box annotations. |

### Face Detection
| Tool / Platform | Recommended use |
| --- | --- |
| [OpenCV](https://opencv.org) | Run classical and neural face detection pipelines. |
| [InsightFace](https://github.com/deepinsight/insightface) | Use face analysis and detection models. |

### Text Detection
| Tool / Platform | Recommended use |
| --- | --- |
| [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | Detect and recognize text in images. |
| [Label Studio](https://labelstud.io) | Annotate text regions for custom detection datasets. |

## Image Segmentation

### Semantic Segmentation
| Tool / Platform | Recommended use |
| --- | --- |
| [MMSegmentation](https://github.com/open-mmlab/mmsegmentation) | Train semantic segmentation models. |
| [Roboflow](https://roboflow.com) | Annotate and manage pixel-mask datasets. |

### Instance Segmentation
| Tool / Platform | Recommended use |
| --- | --- |
| [Ultralytics](https://github.com/ultralytics/ultralytics) | Train instance segmentation models. |
| [CVAT](https://www.cvat.ai) | Annotate instance masks and computer vision datasets. |

### Medical Image Segmentation
| Tool / Platform | Recommended use |
| --- | --- |
| [MONAI](https://monai.io) | Build medical imaging AI and segmentation workflows. |
| [3D Slicer](https://www.slicer.org) | Visualize and annotate medical images in 3D. |

## Object Tracking

### Object Tracking
| Tool / Platform | Recommended use |
| --- | --- |
| [Supervision](https://github.com/roboflow/supervision) | Compose detection and tracking workflows. |
| [Norfair](https://github.com/tryolabs/norfair) | Track detected objects across video frames. |

### Multi-Object Tracking
| Tool / Platform | Recommended use |
| --- | --- |
| [ByteTrack](https://github.com/FoundationVision/ByteTrack) | Associate detections for multi-object tracking. |
| [BoxMOT](https://github.com/mikel-brostrom/boxmot) | Compare and run multi-object tracking methods. |

### Visual Tracking
| Tool / Platform | Recommended use |
| --- | --- |
| [PyTracking](https://github.com/visionml/pytracking) | Run visual object tracking algorithms. |
| [OpenCV](https://opencv.org) | Build video processing and tracking pipelines. |

## Pose Estimation

### Pose Estimation
| Tool / Platform | Recommended use |
| --- | --- |
| [MMPose](https://github.com/open-mmlab/mmpose) | Train and evaluate pose estimation models. |
| [OpenVINO](https://github.com/openvinotoolkit/openvino) | Optimize pose inference for deployment. |

### Human Pose Estimation
| Tool / Platform | Recommended use |
| --- | --- |
| [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) | Estimate human body keypoints in images and video. |
| [MMPose](https://github.com/open-mmlab/mmpose) | Use a broad collection of human pose models. |

### Hand Pose Estimation
| Tool / Platform | Recommended use |
| --- | --- |
| [MediaPipe](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker) | Detect hands and estimate hand landmarks. |
| [MMPose](https://github.com/open-mmlab/mmpose) | Train and evaluate hand keypoint models. |

## Optical Character Recognition

### OCR
| Tool / Platform | Recommended use |
| --- | --- |
| [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | Recognize text in images and documents. |
| [Tesseract](https://github.com/tesseract-ocr/tesseract) | Run open-source optical character recognition. |

### Scene Text Recognition
| Tool / Platform | Recommended use |
| --- | --- |
| [EasyOCR](https://github.com/JaidedAI/EasyOCR) | Read text in natural scene images. |
| [docTR](https://github.com/mindee/doctr) | Detect and recognize text in documents. |

### Document Understanding
| Tool / Platform | Recommended use |
| --- | --- |
| [LayoutParser](https://github.com/Layout-Parser/layout-parser) | Analyze and extract document layouts. |
| [Label Studio](https://labelstud.io) | Annotate document regions and text labels. |

## Image Restoration

### Image Denoising
| Tool / Platform | Recommended use |
| --- | --- |
| [OpenCV](https://opencv.org) | Apply image filtering and denoising methods. |
| [BasicSR](https://github.com/XPixelGroup/BasicSR) | Train image restoration and denoising models. |

### Image Super-Resolution
| Tool / Platform | Recommended use |
| --- | --- |
| [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) | Enhance image resolution with pretrained models. |
| [OpenVINO](https://github.com/openvinotoolkit/openvino) | Optimize super-resolution inference. |

### Image Deblurring
| Tool / Platform | Recommended use |
| --- | --- |
| [BasicSR](https://github.com/XPixelGroup/BasicSR) | Train image deblurring and restoration models. |
| [OpenCV](https://opencv.org) | Prototype image enhancement and filtering pipelines. |

## Image Generation and Editing

### Image Generation
| Tool / Platform | Recommended use |
| --- | --- |
| [Diffusers](https://github.com/huggingface/diffusers) | Build and run diffusion-based image generation. |
| [ComfyUI](https://github.com/comfyanonymous/ComfyUI) | Compose node-based image generation workflows. |

### Image Inpainting
| Tool / Platform | Recommended use |
| --- | --- |
| [Diffusers](https://github.com/huggingface/diffusers) | Run diffusion-based inpainting pipelines. |
| [LaMa](https://github.com/advimman/lama) | Restore image regions with large-mask inpainting. |

### Image-to-Image Translation
| Tool / Platform | Recommended use |
| --- | --- |
| [Diffusers](https://github.com/huggingface/diffusers) | Run image-to-image diffusion pipelines. |
| [ControlNet](https://github.com/lllyasviel/ControlNet) | Guide image generation with spatial conditions. |

## 3D Computer Vision

### 3D Reconstruction
| Tool / Platform | Recommended use |
| --- | --- |
| [COLMAP](https://github.com/colmap/colmap) | Reconstruct 3D scenes from image collections. |
| [Nerfstudio](https://github.com/nerfstudio-project/nerfstudio) | Build neural radiance field reconstructions. |

### Depth Estimation
| Tool / Platform | Recommended use |
| --- | --- |
| [Depth Anything V2](https://github.com/DepthAnything/Depth-Anything-V2) | Estimate depth maps from images. |
| [OpenVINO](https://github.com/openvinotoolkit/openvino) | Optimize depth model inference. |

### Point Clouds
| Tool / Platform | Recommended use |
| --- | --- |
| [Open3D](https://www.open3d.org) | Process and visualize 3D data and point clouds. |
| [PCL](https://pointclouds.org) | Use point cloud processing algorithms and tools. |
