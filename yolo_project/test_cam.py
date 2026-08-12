from ultralytics import YOLO
import cv2
import win32com.client
import time
import threading

model = YOLO('runs/detect/train-3/weights/best.pt')
cap = cv2.VideoCapture(0)
speaker = win32com.client.Dispatch("SAPI.SpVoice")
elements_set = set()

def voice_call():
    while True:
        time.sleep(1)
        with threading.Lock():
            elements_list = list(elements_set)
            elements_set.clear()
        if len(elements_list) > 0:
            text = "".join(elements_list) + "nearby"
            speaker.Speak(text)

voice_thread = threading.Thread(target=voice_call, daemon=True)
voice_thread.start()

while True:
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (1280, 720))
    results_window = model(resized_frame)
    for boxes in results_window[0].boxes:
        classes = results_window[0].names  #dictionary with keys as integers I believe
        #print(classes)
        id = boxes.cls[0].item()
        cls_name = classes[int(id)] #converted to integer because it maybe float 
        confidence_value = float(boxes.conf[0].item())
        rounded_confidence = round(confidence_value, 2)
        if rounded_confidence >= 0.60:
            with threading.Lock():
                elements_set.add(cls_name)
    resulted_frame = cv2.imshow("test", results_window[0].plot())
    if cv2.waitKey(1) == ord("e"):
        #voice_thread.stop()
        break

cap.release()
cv2.destroyAllWindows()

#model.predict(source=0, show=True, conf=0.5)