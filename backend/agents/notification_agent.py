from notifications.desktop_notify import DesktopNotifier

notify = DesktopNotifier()


class NotificationAgent:

    def execute(self, state):

        try:

            advice = state.get("advice")

            if advice:

                notify.send(
                    "Posture Alert",
                    advice
                )

        except Exception as e:

            print("Notification Failed:", e)

        return state