import pickle

import cv2
import mediapipe as mp
import numpy as np
import time
from flask import Flask, jsonify, render_template, url_for, redirect, flash, session, request, Response
model_dict = pickle.load(open('./models/models/svm/model.p', 'rb'))
model = model_dict['model']

app=Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('index.html')



@app.route('/generate_frames', methods = ['POST'])
def generate_frames():
    cap = cv2.VideoCapture(0)

    mp_hands = mp.solutions.hands   
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles

    hands = mp_hands.Hands(max_num_hands=1, static_image_mode=True, min_detection_confidence=0.9)

    labels_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 10: 'K', 11: "L", 12: "M", 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y'}
    test = ''
    hello = 'V'
    last_update_time = time.time()
    update_interval = 1.5  # Delay in seconds

    while True:

        data_aux = []
        x_ = []
        y_ = []

        ret, frame = cap.read()

        H, W, _ = frame.shape

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            # for hand_landmarks in results.multi_hand_landmarks:
            #     mp_drawing.draw_landmarks(
            #         frame,  # image to draw
            #         hand_landmarks,  # model output
            #         mp_hands.HAND_CONNECTIONS,  # hand connections
            #         landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2),
            #         connection_drawing_spec=mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2))

            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

            x1 = int(min(x_) * W) - 10
            y1 = int(min(y_) * H) - 10

            x2 = int(max(x_) * W) - 10
            y2 = int(max(y_) * H) - 10

            data_aux += [0] * (84 - len(data_aux))
            
            try:
                prediction = model.predict([np.asarray(data_aux)])

                predicted_character = labels_dict[int(prediction[0])]
                
                # Check if enough time has elapsed to update the test string
                if time.time() - last_update_time >= update_interval:
                    test += predicted_character
                    
                    if (len(test) > 8):
                        test = ""
                
                    last_update_time = time.time()

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
                cv2.putText(frame, test, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3, cv2.LINE_AA)
            except Exception as e:
                pass
            
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            
            
            
            
        # cv2.imshow('frame', frame)
        # cv2.waitKey(25)
        # if cv2.waitKey(25) == ord('q'):
        #     break
        
@app.route('/video_feed')        
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

    # cap.release()
    # cv2.destroyAllWindows()
    
if __name__ == '__main__':
    app.run(debug=True)