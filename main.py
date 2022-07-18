import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink water !",
            message = "You are suffering from sun stroke Please Drink water",
            app_icon = r'icon.ico',
            timeout=8
        )
        time.sleep(90*60)


# to run python in background run pythonw .\main.py in terminal