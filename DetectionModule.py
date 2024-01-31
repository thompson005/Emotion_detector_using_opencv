def DetectionModule(path):
    
    import cv2
    from deepface import DeepFace
    import numpy as np
    from ultralytics import YOLO
    # Intitialize variables
    angry, disgust, fear, happy, sad, suprise, neutral = 0, 0, 0, 0, 0, 0, 0
    # Load the YOLO object detection model
    model = YOLO("yolov5nu.pt")

    objects = model.names
    # Read the input video
    if path != 0:
        cap = cv2.VideoCapture(path or 0)
        while (cap.isOpened()):
            ret, frame = cap.read()
            if not ret:
                break
            try:
                # Detect emotions using DeepFace
                emotion = DeepFace.analyze(frame, actions=['emotion'])
                print(emotion[0]['dominant_emotion'])
                # Add to the corresponding emotion counter
                if emotion[0]['dominant_emotion'] == 'angry':
                    angry += 1
                elif emotion[0]['dominant_emotion'] == 'disgust':
                    disgust += 1
                elif emotion[0]['dominant_emotion'] == 'fear':
                    fear += 1
                elif emotion[0]['dominant_emotion'] == 'happy':
                    happy += 1
                elif emotion[0]['dominant_emotion'] == 'sad':
                    sad += 1
                elif emotion[0]['dominant_emotion'] == 'suprise':
                    suprise += 1
                elif emotion[0]['dominant_emotion'] == 'neutral':
                    neutral += 1

            except:
                print("No Face Detected")
            # Detect objects using YOLO object detection model
            results = model(frame)
            for result in results:
                for box in result.boxes:
                    if box.cls != None:
                        # print(objects[int(box.cls)])
                        # Draw a rectangle around the detected person
                        for (x, y, w, h) in [(int(i) for i in j)
                                             for j in box.xywh]:
                            if objects[int(box.cls)] == 'person':
                                # print("x: ", x, "y: ", y, "w: ", w, "h: ", h)
                                #Calculating the x and y coordinate 
                                x, y = int(x - w / 2), int(y - h / 2)

                                # Adds rectangle around the object
                                cv2.rectangle(img=frame,
                                              pt1=(x, y),
                                              pt2=(x + w, y + h),
                                              color=(255, 255, 255),
                                              thickness=2)

                                 # Add the detected emotion label above the rectangle
                                cv2.putText(
                                    img=frame,
                                    text=emotion[0]['dominant_emotion'],
                                    org=(x, y + 20),
                                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=1,
                                    color=(0, 0, 0),
                                    thickness=2,
                                    lineType=cv2.LINE_AA,
                                )

                                # Add the accuracy percentage to the label
                                cv2.putText(
                                    img=frame,
                                    text=f"Accuracy: {int(box.conf * 100)}%",
                                    org=(x, y + 40),
                                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=0.5,
                                    color=(255, 0, 0),
                                    thickness=2,
                                    lineType=cv2.LINE_AA,
                                )
            # Display the output
            cv2.imshow('frame', frame)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
    # Find and Print gthe most common Emotion shown
        if angry > disgust and angry > fear and angry > happy and angry > sad and angry > suprise and angry > neutral:
            print("The most repeated Emotion is Anger")
        if disgust > angry and disgust > fear and disgust > happy and disgust > sad and disgust > suprise and disgust > neutral:
            print("The most repeated Emotion is Disgust")
        if fear > disgust and fear > angry and fear > happy and fear > sad and fear > suprise and fear > neutral:
            print("The most repeated Emotion is Fear")
        if happy > disgust and happy > fear and happy > angry and happy > sad and happy > suprise and happy > neutral:
            print("The most repeated Emotion is Happy")
        if sad > disgust and sad > fear and sad > happy and sad > angry and sad > suprise and sad > neutral:
            print("The most repeated Emotion is Sad")
        if suprise > disgust and suprise > fear and suprise > happy and suprise > sad and suprise > angry and suprise > neutral:
            print("The most repeated Emotion is Suprise")
        if neutral > disgust and neutral > fear and neutral > happy and neutral > sad and neutral > suprise and neutral > angry:
            print("The most repeated Emotion is Neutral")
