#This file is solely used to run the training of the model

from ultralytics import YOLO

if __name__ == '__main__':   #ensures that model is trained only if clicked run
    model = YOLO('yolo11s.pt')  #trained using yolo11s (YOLO 11 small) model

    model.train(
        data='data.yaml',
        epochs=60,   #number of times the model was trained
        imgsz=640,   #size of the image that was used, higher sizes take up more memory
        batch=4,     #images were trained in 4 batches
        workers=2,   #two workers were assigned to process the images in the background
        device=0     #first gpu (cuda), can use cpu (device=cpu), but will be slow
    )

'''
Note: The epochs, imgsz, batch and workers solely depend on the specification of the hardware you use. Having a GPU with higher VRAM allows you to increase these values (epochs, imgsz, batch), which was not possible for me
due to having only 4gb of VRAM on my GPU. This is why each epoch took me approximately 8 minutes, which in total was 8 hours worth of training. The value of workers can be changed based on the CPU being used and the RAM.
'''