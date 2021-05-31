# pip install py-notifier

from pynotifier import Notification

Notification(
    title="Drink Water",
    description = "One must drink water frequently",
    #icon_path = 'currently leaving blank'

    # On Windows .icois required, on linux - .png

    duration = 10   # Duration in seconds

).send()