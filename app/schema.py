import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import Notification
from app import db

class NotificationType(SQLAlchemyObjectType):
    class Meta:
        model = Notification

class SendNotification(graphene.Mutation):
    notification = graphene.Field(NotificationType)

    class Arguments:
        user_id = graphene.Int(required=True)
        message = graphene.String(required=True)

    def mutate(self, info, user_id, message):
        notification = Notification(
            user_id=user_id,
            message=message
        )
        db.session.add(notification)
        db.session.commit()
        return SendNotification(notification=notification)

class MarkNotificationAsRead(graphene.Mutation):
    notification = graphene.Field(NotificationType)

    class Arguments:
        notification_id = graphene.Int(required=True)

    def mutate(self, info, notification_id):
        notification = Notification.query.get(notification_id)
        if not notification:
            raise ValueError("Notification not found")

        notification.read = True
        db.session.commit()

        return MarkNotificationAsRead(notification=notification)

class Query(graphene.ObjectType):
    notification = graphene.Field(NotificationType, id=graphene.Int())
    notifications = graphene.List(NotificationType, user_id=graphene.Int())

    def resolve_notification(self, info, id):
        return Notification.query.get(id)

    def resolve_notifications(self, info, user_id):
        return Notification.query.filter_by(user_id=user_id).all()

class Mutation(graphene.ObjectType):
    send_notification = SendNotification.Field()
    mark_notification_as_read = MarkNotificationAsRead.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
