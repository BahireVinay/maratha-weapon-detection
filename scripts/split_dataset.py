from pathlib import Path
import random
import shutil

ROOT = Path(__file__).resolve().parents[1]
RAW_IMAGES = ROOT / "data" / "raw" / "images"
RAW_LABELS = ROOT / "data" / "raw" / "labels"
OUT = ROOT / "data" / "processed"

SEED = 42
TRAIN_RATIO = 0.70
VAL_RATIO = 0.20
TEST_RATIO = 0.10

assert abs(TRAIN_RATIO + VAL_RATIO + TEST_RATIO - 1.0) < 1e-9

EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

images = [p for p in RAW_IMAGES.rglob("*") if p.suffix.lower() in EXTENSIONS]
random.Random(SEED).shuffle(images)

n = len(images)
train_end = int(n * TRAIN_RATIO)
val_end = train_end + int(n * VAL_RATIO)

splits = {
    "train": images[:train_end],
    "val": images[train_end:val_end],
    "test": images[val_end:],
}

for split, items in splits.items():
    image_out = OUT / "images" / split
    label_out = OUT / "labels" / split
    image_out.mkdir(parents=True, exist_ok=True)
    label_out.mkdir(parents=True, exist_ok=True)

    for image_path in items:
        label_path = RAW_LABELS / f"{image_path.stem}.txt"

        if not label_path.exists():
            print(f"[SKIP] Missing label for {image_path.name}")
            continue

        shutil.copy2(image_path, image_out / image_path.name)
        shutil.copy2(label_path, label_out / label_path.name)

    print(f"{split}: {len(items)} images")

print("\nDataset split completed.")
print("Train:", len(splits["train"]))
print("Val  :", len(splits["val"]))
print("Test :", len(splits["test"]))
