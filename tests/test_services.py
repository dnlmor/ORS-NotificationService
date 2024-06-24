import unittest
from app.services import NotificationService
from app.models import Notification, NotificationStatus
from app.database import db_session

class TestNotificationService(unittest.TestCase):
    def setUp(self):
        self.notification_data = {
            'user_id': 1,
            'message': "Your order has been shipped!"
        }

    def test_send_notification(self):
        notification = NotificationService.send_notification(**self.notification_data)
        self.assertIsNotNone(notification.id)
        self.assertEqual(notification.user_id, self.notification_data['user_id'])
        self.assertEqual(notification.message, self.notification_data['message'])
        self.assertIn(notification.status, [NotificationStatus.SENT, NotificationStatus.FAILED])

    def tearDown(self):
        db_session.remove()

if __name__ == '__main__':
    unittest.main()
