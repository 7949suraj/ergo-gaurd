# src/capture_landmarks.py
import cv2, mediapipe as mp, csv, os, time, argparse
mp_pose = mp.solutions.pose

parser = argparse.ArgumentParser()
parser.add_argument('--out', default='data/landmarks.csv')
parser.add_argument('--label', required=True)   # good / warning / bad
parser.add_argument('--frames', type=int, default=100)
args = parser.parse_args()

os.makedirs(os.path.dirname(args.out), exist_ok=True)
cap = cv2.VideoCapture(0)
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

fieldnames = ['label'] + [f'{p}_{axis}' for p in range(33) for axis in ('x','y','z','v')]
# (BlazePose has 33 landmarks)
if not os.path.exists(args.out):
    with open(args.out,'w',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fieldnames)

count = 0
print("Press SPACE to start recording frames for label:", args.label)
while True:
    ret, frame = cap.read()
    if not ret: break
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = pose.process(rgb)
    cv2.putText(frame, f"Label: {args.label} Frames: {count}/{args.frames}", (10,30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255),2)
    cv2.imshow('capture', frame)
    k = cv2.waitKey(1)
    if k == 32:  # space to start
        while count < args.frames:
            ret, frame = cap.read()
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            res = pose.process(rgb)
            row = [args.label]
            if res.pose_landmarks:
                for lm in res.pose_landmarks.landmark:
                    row += [lm.x, lm.y, lm.z, lm.visibility]
            else:
                row += [0]* (33*4)
            with open(args.out,'a',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(row)
            count += 1
            cv2.putText(frame, f"Recording... {count}/{args.frames}", (10,60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0),2)
            cv2.imshow('capture', frame)
            cv2.waitKey(100)  # 100 ms between frames
        print("Done")
        break
    elif k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
