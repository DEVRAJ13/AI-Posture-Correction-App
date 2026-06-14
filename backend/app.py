import cv2

from camera.webcam import Webcam

from vision.pose_detector import PoseDetector

from graph.workflow import workflow

camera = Webcam()

detector = PoseDetector()

bad_count = 0

while True:

    frame = camera.read_frame()

    if frame is None:
        continue

    results = detector.detect(
        frame
    )

    posture = "good"

    if results.pose_landmarks:
        posture = "bad"

    state = {
        "posture": posture,
        "bad_count": bad_count,
        "advice": ""
    }

    result = workflow.invoke(
        state
    )

    bad_count = result["bad_count"]

    cv2.putText(
        frame,
        f"Posture: {posture}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    cv2.imshow(
        "AI Posture Assistant",
        frame
    )

    if cv2.waitKey(1) == 27:
        break

camera.release()

cv2.destroyAllWindows()