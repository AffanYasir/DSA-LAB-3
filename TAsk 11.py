class NotificationsQueue:
    def __init__(self, max_size=5):
        self.notifications = []
        self.max_size = max_size

    def add_notification(self, notification):
        if len(self.notifications) >= self.max_size:
            self.notifications.pop(0)
        self.notifications.append(notification)

    def clear_all(self):
        self.notifications = []

    def view_notifications(self):
        print("Latest Notifications:")
        for i, notification in enumerate(self.notifications, 1):
            print(f"{i}. {notification}")


queue = NotificationsQueue()
queue.add_notification("New friend request")
queue.add_notification("You have a new message")
queue.view_notifications()
queue.clear_all()
queue.view_notifications()