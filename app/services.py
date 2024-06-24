from .models import Notification, NotificationStatus
from .database import db_session
from .utils import send_notification_to_user
from sqlalchemy.exc import IntegrityError

class NotificationService:
    @staticmethod
    def send_notification(user_id, message):
        try:
            notification = Notification(
                user_id=user_id,
                message=message,
                status=NotificationStatus.PENDING
            )
            
            db_session.add(notification)
            db_session.commit()
            
            # Simulate sending notification
            success = send_notification_to_user(user_id, message)
            notification.status = NotificationStatus.SENT if success else NotificationStatus.FAILED
            db_session.commit()
            
            return notification
        except IntegrityError:
            db_session.rollback()
            raise ValueError("Failed to send notification")

    @staticmethod
    def get_notification_by_id(id):
        notification = Notification.query.get(id)
        if not notification:
            raise ValueError("Notification not found")
        return notification

    @staticmethod
    def list_notifications(user_id=None):
        query = Notification.query
        if user_id:
            query = query.filter_by(user_id=user_id)
        return query.all()
