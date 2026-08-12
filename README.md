# Maratha Weapon Detection

**Final Year Project | Computer Vision | Dataset Development | YOLO Object Detection**

A computer-vision project for identifying and classifying six categories of traditional Maratha weapons. The project emphasizes the complete dataset-development workflow: image collection, organization, quality review, annotation, preprocessing, training preparation, evaluation, and inference testing.

## Project Overview

The system is designed around a custom image dataset containing six weapon categories:

- Bhala
- Cannon
- Dhal
- Khanjeer
- Talwar
- Waghnakhe

The project was completed as a sponsored final-year project, with major involvement in dataset collection and preparation. The dataset was published on Stinger, and the work resulted in a research paper published at ICT4SDSO.

## Key Contributions

- Collected and curated images from diverse sources according to project requirements.
- Organized images into consistent class-wise structures.
- Reviewed images for quality, relevance, duplicates, and class consistency.
- Prepared object-detection annotations in YOLO format.
- Performed preprocessing and dataset preparation for model training.
- Created train/validation/test splits.
- Validated annotation and dataset structure before training.
- Evaluated the trained detection model using standard object-detection metrics.
- Tested the resulting system on previously unseen images.
- Documented the complete dataset-to-inference workflow.

## Repository Structure

```text
Maratha-Weapon-Detection/
│
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
│
├── configs/
│   └── maratha_weapons.yaml
│
├── data/
│   ├── raw/
│   │   └── .gitkeep
│   ├── processed/
│   │   └── .gitkeep
│   └── README.md
│
├── models/
│   └── .gitkeep
│
├── scripts/
│   ├── check_dataset.py
│   ├── split_dataset.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── reports/
│   └── .gitkeep
│
└── assets/
    └── .gitkeep
```

## Dataset

The dataset is **not bundled with this repository**. Add the dataset locally according to the structure below.

```text
data/processed/
├── images/
│   ├── train/
│   ├── val/
│   └── test/
└── labels/
    ├── train/
    ├── val/
    └── test/
```

Each YOLO label file should contain:

```text
class_id x_center y_center width height
```

with normalized coordinates in the range `[0, 1]`.

### Class Mapping

| ID | Class |
|---:|---|
| 0 | Bhala |
| 1 | Cannon |
| 2 | Dhal |
| 3 | Khanjeer |
| 4 | Talwar |
| 5 | Waghnakhe |


## Dataset Publication

The project dataset was published on **Stinger**.

Add the exact public dataset URL here if you want visitors to access it:

```text
Dataset: <insert exact Stinger URL>
```

## Research Publication

The project resulted in a research paper published at **ICT4SDSO**.

Add the exact paper URL/DOI here:

```text
Paper: <insert exact publication URL or DOI>
```

## Project Workflow

```text
Image Sources
     ↓
Image Collection
     ↓
Image Review & Cleaning
     ↓
Class-wise Organization
     ↓
Annotation
     ↓
Annotation Validation
     ↓
Preprocessing
     ↓
Train / Validation / Test Split
     ↓
Model Training
     ↓
Evaluation
     ↓
Inference Testing
     ↓
Results & Documentation
```

## Limitations

- Performance depends strongly on dataset diversity and annotation quality.
- Similar-looking weapon shapes may create class confusion.
- Images with severe occlusion, unusual viewpoints, poor lighting, or very small objects may be harder to detect.
- Results should be interpreted using the exact held-out test set and recorded evaluation configuration.

## Future Improvements

- Expand the dataset with more viewpoints and environments.
- Increase representation of difficult/rare visual conditions.
- Add stronger data-quality checks and automated duplicate detection.
- Compare multiple object-detection architectures.
- Add a lightweight web interface for demonstration.
- Package the model for edge or real-time inference.

## Technologies

- Python
- YOLO / Ultralytics
- OpenCV
- Pillow
- NumPy
- Matplotlib
- Computer Vision
- Object Detection
- Dataset Development
- Data Annotation
