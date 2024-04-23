from ultralytics import YOLO

#train/runs/detect/train4/weights/yolo_last.pt
model = YOLO('yolov8x')

result = model.track('input_videos/sinner-v-med.mp4', conf = 0.2, save = True)
#print(result)
#print("boxes:")
#for box in result[0].boxes:
#    print(box)

    
