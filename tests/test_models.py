import unittest
from app.models import Notification, NotificationStatus
from app.database import db_session

class TestNotificationModel(unittest.TestCase):
    def setUp(self):
        self.notification = Notification(
            user_id=1,
            message="Your order has been shipped!",
            status=NotificationStatus.PENDING
        )

    def test_create_notification(self):
        db_session.add(self.notification)
        db_session.commit()
        self.assertIsNotNone(self.notification.id)

    def tearDown(self):
        db_session.remove()

if __name__ == '__main__':
    unittest.main()
