from flask import Flask, render_template, Response, redirect, url_for
import cv2
import threading
import time

from proctoring.face_detection import detect_faces
from proctoring.head_movement import detect_head_movement
from proctoring.mobile_detection import detect_mobile
from proctoring.logger import log_event
from questions.python_questions import questions

app = Flask(__name__)

camera = cv2.VideoCapture(0)
count = 0
exam_active = False

# Global status for frontend polling
exam_status = {
    "alarm": False,
    "message": "Monitoring Active"
}

def generate_frames():
    global count, exam_active, exam_status
    start_head_time = None

    while exam_active:
        success, frame = camera.read()
        if not success:
            break

        faces = detect_faces(frame)
        mobile = detect_mobile(frame)
        
        # Reset current frame status
        current_alarm = False
        current_message = "Monitoring Active"
        violation_detected = False

        # 1. Multiple Faces Detection
        if faces > 1:
            violation_detected = True
            current_message = "Multiple faces detected!"
            log_event("Multiple faces detected")

        # 2. No Face Detected (Moving Away)
        elif faces == 0:
            if start_head_time is None:
                start_head_time = time.time()
            elif time.time() - start_head_time >= 3: # 3 seconds tolerance
                violation_detected = True
                current_message = "Face not visible! Please return to frame."
                log_event("Face not visible")
        else:
            # Face present (1 face) - Reset timer
            start_head_time = None

        # 3. Mobile Detection
        if mobile:
            violation_detected = True
            current_message = "Mobile phone detected!"
            log_event("Mobile phone detected")

        # Warning Logic
        if violation_detected:
            # If this is a new violation (we weren't alarming before), increment count
            # Use 'count' as the persistent warning counter
             if not exam_status["alarm"]:
                count += 1
                current_alarm = True # Trigger alarm for this frame
             else:
                # Alarm was already active, keep it active but don't increment count yet
                current_alarm = True
        
        # Update global status
        exam_status["alarm"] = current_alarm
        exam_status["message"] = f"{current_message}"
        exam_status["warnings"] = count

        # Auto terminate Logic (Terminate if warnings >= 2)
        if count >= 2:
            exam_active = False
            exam_status["terminate"] = True # Signal frontend to redirect
            camera.release()
            break

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/status')
def get_status():
    return exam_status

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/start_exam')
def start_exam():
    global exam_active, count
    count = 0
    exam_active = True

    # threading.Thread(target=detect_noise, daemon=True).start()
    return render_template('exam.html', questions=questions)

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/completed')
def completed():
    return render_template('completed.html')

if __name__ == "__main__":
    app.run(debug=True)
