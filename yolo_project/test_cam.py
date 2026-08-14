from ultralytics import YOLO
import cv2
import win32com.client
import time
import threading

#Using and loading the most accurate YOLO model from the training (source given)
model = YOLO('runs/detect/train-3/weights/best.pt') 

#Loaded my default camera using opencv (0 - default, may have other cameras)
capture = cv2.VideoCapture(0)

#Launch the windows SAPI voice engine from the win32com.client library
speaker = win32com.client.Dispatch("SAPI.SpVoice")

#Setting up an empty dictionary to store the class name and value
elements_dict = {} 

#function to out the classes using the windows text to speech engine 
def voice_call(): 
    #Has to run continuously so that it keeps on yelling out the names of the classes every 2 seconds
    while True:
        time.sleep(2)
        #threading.Lock() is used so that elements_dict which contains the detected classes is being accessed once at a time
        #A dictionary copy is created which is checked to see if there are elements in them and then the keys and values are yelled out by the engine
        with threading.Lock():
            speech_dict = elements_dict.copy()
            elements_dict.clear()
        if len(speech_dict) > 0:
            for keys, values in speech_dict.items():
                text = f"{keys}, {values}"
                speaker.Speak(text)

#threading is a major requirement because two processes are run where the main process is to set up a frame through which objects are detected and their name, id, confidence level are acquired
voice_thread = threading.Thread(target=voice_call, daemon=True)
voice_thread.start()

#Infinitely runs to continuously snap frames and detect objects 
while True:
    x_px = 1280
    y_px = 720
    ret, frame = capture.read() #ret - camera loaded or not, frame - frame of camera to detect objects
    resized_frame = cv2.resize(frame, (x_px, y_px)) #resized to 1280x720, can be changed to match the quality of the device camera
    #center required to determine where an object is places -> left or right?
    center_of_screen = x_px * 0.5
    results_window = model(resized_frame) #list containing the frame through which the model is loaded, more frames -> len(results_window) increases
    for boxes in results_window[0].boxes: #first element required as only frame is present
        x, y, w, h = boxes.xywh[0] #command to get center points along with width and height; width and height is required so that the engine also mentions their widths and heights in pixels (see bottom of code)
        classes = results_window[0].names  #dictionary of classes with keys as integers which is verified through print(classes)
        id = boxes.cls[0].item() #gets id
        cls_name = classes[int(id)] #converted to integer because it maybe float, was tensor before 
        confidence_value = float(boxes.conf[0].item()) #gets confidence value which is then rounded to 2 d.p as shown below
        rounded_confidence = round(confidence_value, 2)

        #Only uses and yells out objects with confidence of 0.60 or greater, bounding boxes may be shown on lower confidence but the width and height pixel will not be shown
        if rounded_confidence >= 0.60:
            cv2.putText(resized_frame, f"({int(w)}px, {int(h)}px)", (int(x-50),int(y)), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 255), 2)

            #temp variable is used which notes down the direction of the box or object which is detected and is then spoken out through the engine
            direction = ""
            if int(x) > center_of_screen:
                direction = "Right"
            elif int(x) < center_of_screen:
                direction = "Left"
            else:
                direction = "Center"
            with threading.Lock():  #so elements_dict is accessed once at a time as it is used at the main process (here) and above when the object is spoken out

                #dtype of elements_dict: dictionary; keys are classes and values are tuples containing width, height, and direction
                elements_dict[cls_name] = (f"{int(w)} pixels wide", f"{int(h)} pixels tall", f"direction: {direction}")


    resulted_frame = cv2.imshow("Program", results_window[0].plot())   #video frame displayed or plotted according to the frame size

    #Pressing 'e' within 1ms will stop the program, this exact script will continuously run so users can exit the program within the first millisecond of each frame when loaded
    if cv2.waitKey(1) == ord("e"): 
        break

#releases the camera and all windows associated with the program are stopped
capture.release()
cv2.destroyAllWindows()

'''
Vulnerability -> height and width in pixels because a calibrated camera is required for accurate measurement. It can be scaled which we did try, but the measurements were highly inaccurate.
Another model can be used, but it would result in two models colliding
Better camera can be used to improve the model 
'''
