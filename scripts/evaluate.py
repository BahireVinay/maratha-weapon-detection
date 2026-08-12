from pathlib import Path
import argparse
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "configs" / "maratha_weapons.yaml"

parser = argparse.ArgumentParser(description="Evaluate Maratha weapon detector")
parser.add_argument("--weights", required=True, help="Path to trained .pt weights")
args = parser.parse_args()

model = YOLO(args.weights)

metrics = model.val(
    data=str(DATA),
    split="test",
    imgsz=640,
    plots=True,
    project=str(ROOT / "runs"),
    name="evaluation",
    exist_ok=True,
)

print("\n=== Evaluation Results ===")
print(f"Precision      : {metrics.box.mp:.4f}")
print(f"Recall         : {metrics.box.mr:.4f}")
print(f"mAP@0.50       : {metrics.box.map50:.4f}")
print(f"mAP@0.50:0.95  : {metrics.box.map:.4f}")
