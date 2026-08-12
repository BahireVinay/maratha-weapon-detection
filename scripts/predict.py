from pathlib import Path
import argparse
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parents[1]

parser = argparse.ArgumentParser(description="Run inference on Maratha weapon images")
parser.add_argument("--weights", required=True, help="Path to trained .pt weights")
parser.add_argument("--source", required=True, help="Image, folder, or video source")
parser.add_argument("--conf", type=float, default=0.25)
args = parser.parse_args()

model = YOLO(args.weights)

results = model.predict(
    source=args.source,
    conf=args.conf,
    save=True,
    save_txt=True,
    save_conf=True,
    project=str(ROOT / "runs"),
    name="predict",
    exist_ok=True,
)

print("\n=== Prediction Summary ===")
for result in results:
    print(f"Source: {result.path}")
    if result.boxes is None or len(result.boxes) == 0:
        print("  No detections.")
        continue

    for box in result.boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        name = model.names.get(cls_id, str(cls_id))
        print(f"  {name}: confidence={conf:.3f}")

print("\nPrediction outputs saved under:")
print(ROOT / "runs" / "predict")
