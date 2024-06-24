from .services import NotificationService

def resolve_send_notification(info, user_id, message):
    return NotificationService.send_notification(user_id, message)

def resolve_get_notification(info, id):
    return NotificationService.get_notification_by_id(id)

def resolve_list_notifications(info, user_id=None):
    return NotificationService.list_notifications(user_id)
