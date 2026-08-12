from pathlib import Path
from PIL import Image
import yaml

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "configs" / "maratha_weapons.yaml"

with open(CONFIG, "r", encoding="utf-8") as f:
    cfg = yaml.safe_load(f)

DATA_ROOT = ROOT / "data" / "processed"
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}
NUM_CLASSES = len(cfg["names"])

total = 0
missing_labels = 0
invalid_labels = 0
bad_images = 0
empty_labels = 0

print("=== Maratha Weapon Dataset Validation ===")

for split in ("train", "val", "test"):
    image_dir = DATA_ROOT / "images" / split
    label_dir = DATA_ROOT / "labels" / split

    images = [p for p in image_dir.rglob("*") if p.suffix.lower() in IMAGE_EXTENSIONS]
    split_count = 0

    for image_path in images:
        split_count += 1
        total += 1
        label_path = label_dir / f"{image_path.stem}.txt"

        try:
            with Image.open(image_path) as img:
                img.verify()
        except Exception:
            bad_images += 1
            print(f"[BAD IMAGE] {image_path}")

        if not label_path.exists():
            missing_labels += 1
            print(f"[MISSING LABEL] {image_path}")
            continue

        content = label_path.read_text(encoding="utf-8").strip()
        if not content:
            empty_labels += 1
            print(f"[EMPTY LABEL] {label_path}")
            continue

        for line_no, line in enumerate(content.splitlines(), start=1):
            parts = line.split()
            if len(parts) != 5:
                invalid_labels += 1
                print(f"[INVALID FORMAT] {label_path}:{line_no}")
                continue

            try:
                class_id = int(parts[0])
                coords = [float(x) for x in parts[1:]]
            except ValueError:
                invalid_labels += 1
                print(f"[NON-NUMERIC] {label_path}:{line_no}")
                continue

            if not (0 <= class_id < NUM_CLASSES):
                invalid_labels += 1
                print(f"[INVALID CLASS] {label_path}:{line_no}")
                continue

            if any(x < 0 or x > 1 for x in coords):
                invalid_labels += 1
                print(f"[INVALID COORDINATE] {label_path}:{line_no}")

    print(f"{split}: {split_count} images")

print("\n=== Summary ===")
print(f"Total images      : {total}")
print(f"Missing labels    : {missing_labels}")
print(f"Empty labels      : {empty_labels}")
print(f"Invalid labels    : {invalid_labels}")
print(f"Unreadable images : {bad_images}")

if any((missing_labels, empty_labels, invalid_labels, bad_images)):
    raise SystemExit("\nDataset validation found issues. Review the messages above.")

print("\nDataset validation completed successfully.")
