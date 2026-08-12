from pathlib import Path
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "configs" / "maratha_weapons.yaml"

# Change the model here if your final project used another YOLO version.
MODEL = "yolov8n.pt"

model = YOLO(MODEL)

results = model.train(
    data=str(DATA),
    epochs=25,
    imgsz=640,
    batch=16,
    project=str(ROOT / "runs"),
    name="maratha_weapon_detection",
    exist_ok=True,
    patience=10,
    pretrained=True,
)

print("\nTraining completed.")
print("Best weights should be available under:")
print(ROOT / "runs" / "maratha_weapon_detection" / "weights" / "best.pt")
