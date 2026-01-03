import cv2
import time
import numpy as np
import pygame
from ultralytics import YOLO
from twilio.rest import Client

# -------------------------------
# Twilio setup
# -------------------------------
account_sid = "your_twilio_account_sid_here"
auth_token = "your_twilio_auth_token_here"
twilio_number = "+1234567890"
target_number = "+1234567890"
client = Client(account_sid, auth_token)

# -------------------------------
# Camera location (manual per camera)
# -------------------------------
camera_location = "Mananthavady South"  # change manually per camera

# -------------------------------
# Flags for single alert & deterrent per animal
# -------------------------------
alert_sent_animals = set()
deterrent_triggered_animals = set()
first_detection_logged = False

# -------------------------------
# Alert via Twilio (per animal)
# -------------------------------
def send_alert_once(animal):
    if animal not in alert_sent_animals:
        try:
            message = client.messages.create(
                body=f"⚠️ Alert! A {animal} was detected at {camera_location}.",
                from_=twilio_number,
                to=target_number
            )
   
   
            print(f"✅ Alert sent: {animal} at {camera_location} - SID: {message.sid}")
            alert_sent_animals.add(animal)
        except Exception as e:
            print("❌ Error sending alert:", e)

# -------------------------------
# Setup Pygame for sounds
# -------------------------------
pygame.mixer.init()

elephant_sound = r"C:\Users\alish\Downloads\mix_35s (audio-joiner.com).mp3"
tiger_sound    = r"C:\Users\alish\Downloads\tigerdeterrent.mp3.mp3"
boar_sound     = r"C:\Users\alish\Downloads\boardeterrent.mp3.mp3"

def play_sound(file):
    try:
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    except Exception as e:
        print("⚠️ Could not play sound:", e)

# -------------------------------
# Light Effects
# -------------------------------
def red_white_strobe(duration=15):
    end_time = time.time() + duration
    while time.time() < end_time:
        for color in [(0,0,255), (255,255,255)]:
            frame = np.full((500, 800, 3), color, dtype=np.uint8)
            cv2.imshow("Light Effect", frame)
            if cv2.waitKey(200) & 0xFF == ord('q'):
                return

def white_strobe(duration=15):
    end_time = time.time() + duration
    while time.time() < end_time:
        for color in [(255,255,255), (0,0,0)]:
            frame = np.full((500, 800, 3), color, dtype=np.uint8)
            cv2.imshow("Light Effect", frame)
            if cv2.waitKey(150) & 0xFF == ord('q'):
                return

def white_green_strobe(duration=15):
    end_time = time.time() + duration
    while time.time() < end_time:
        for color in [(255,255,255), (0,255,0)]:
            frame = np.full((500, 800, 3), color, dtype=np.uint8)
            cv2.imshow("Light Effect", frame)
            if cv2.waitKey(200) & 0xFF == ord('q'):
                return

# -------------------------------
# Species-specific deterrent (per animal)
# -------------------------------
def trigger_deterrent(animal):
    if animal not in deterrent_triggered_animals:
        if animal == "elephant":
            print("🐘 Elephant detected! Activating deterrent for 15s.")
            play_sound(elephant_sound)
            red_white_strobe(duration=15)
        elif animal == "tiger":
            print("🐅 Tiger detected! Activating deterrent for 15s.")
            play_sound(tiger_sound)
            white_strobe(duration=15)
        elif animal == "boar":
            print("🐗 Boar detected! Activating deterrent for 15s.")
            play_sound(boar_sound)
            white_green_strobe(duration=15)

        pygame.mixer.music.stop()
        deterrent_triggered_animals.add(animal)

# -------------------------------
# Load YOLO model
# -------------------------------
model = YOLO(r"D:\wild animal project\tiger-elephant-boar.v2i.yolov8\runs\detect\train\weights\best.pt")

# -------------------------------
# OpenCV video capture
# -------------------------------
cap = cv2.VideoCapture(r"C:\Users\alish\Desktop\videos\elephant.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # -------------------------------
    # 🌙 Auto Low-Light Enhancement
    # -------------------------------
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    brightness = np.mean(gray)

    if brightness < 50:  # threshold for dark frames
        print("🌙 Low-light frame detected — enhancing visibility...")
        frame = cv2.convertScaleAbs(frame, alpha=1.8, beta=40)

    # -------------------------------
    # Run YOLO detection (suppress default printing)
    # -------------------------------
    results = model(frame, conf=0.5, verbose=False)  # verbose=False prevents YOLO from printing counts

    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])

            if conf > 0.5:
                animal = model.names[cls]

                if animal not in ["elephant", "tiger", "boar"]:
                    continue

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{animal} {conf:.2f}", (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

                # Only log first detection once
                if not first_detection_logged:
                    print(f"🎯 SUMMARY: {animal} detected with confidence {conf:.2f} at {camera_location}")
                    first_detection_logged = True

                send_alert_once(animal)
                trigger_deterrent(animal)

    # -------------------------------
    # Show Detection Frame
    # -------------------------------
    cv2.imshow("Wild Animal Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
