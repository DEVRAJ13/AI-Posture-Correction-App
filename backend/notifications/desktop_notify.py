import platform
import subprocess


class DesktopNotifier:

    def send(self, title, message):

        system = platform.system()

        try:

            if system == "Darwin":

                subprocess.run([
                    "osascript",
                    "-e",
                    f'display notification "{message}" with title "{title}"'
                ])

            elif system == "Linux":

                subprocess.run([
                    "notify-send",
                    title,
                    message
                ])

            else:

                print(f"[{title}] {message}")

        except Exception as e:

            print("Notification Error:", e)