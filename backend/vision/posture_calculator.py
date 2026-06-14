import math

class PostureCalculator:

    def get_angle(self, shoulder, ear):

        dx = ear.x - shoulder.x
        dy = shoulder.y - ear.y

        angle = math.degrees(
            math.atan2(dy, dx)
        )

        return abs(angle)

    def analyze(self, landmarks):

        shoulder = landmarks.landmark[11]
        ear = landmarks.landmark[7]

        angle = self.get_angle(
            shoulder,
            ear
        )

        if angle < 35:
            return "bad", angle

        return "good", angle