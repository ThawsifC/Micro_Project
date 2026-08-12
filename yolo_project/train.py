from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('yolo11s.pt')

    model.train(
        data='data.yaml',
        epochs=60,
        imgsz=640,
        batch=4,
        workers=2,
        device=0
    )