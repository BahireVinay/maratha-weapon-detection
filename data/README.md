# Dataset Directory

The repository intentionally does not contain the full dataset.

Expected processed structure:

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

For every image, there should be a matching `.txt` annotation file with the same base filename.

Example:

```text
images/train/talwar_001.jpg
labels/train/talwar_001.txt
```

YOLO annotation format:

```text
class_id x_center y_center width height
```

All bounding-box coordinates must be normalized to `[0, 1]`.
