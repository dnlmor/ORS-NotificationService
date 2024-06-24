import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from .models import Notification as NotificationModel, NotificationStatus
from .resolvers import (
    resolve_send_notification, resolve_get_notification, resolve_list_notifications
)

class NotificationStatusEnum(graphene.Enum):
    PENDING = "PENDING"
    SENT = "SENT"
    FAILED = "FAILED"

class Notification(SQLAlchemyObjectType):
    class Meta:
        model = NotificationModel

class Query(graphene.ObjectType):
    get_notification = graphene.Field(Notification, id=graphene.Int(required=True))
    list_notifications = graphene.List(Notification, user_id=graphene.Int())

    def resolve_get_notification(self, info, id):
        return resolve_get_notification(info, id)

    def resolve_list_notifications(self, info, user_id=None):
        return resolve_list_notifications(info, user_id)

class SendNotification(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int(required=True)
        message = graphene.String(required=True)

    notification = graphene.Field(lambda: Notification)

    def mutate(self, info, user_id, message):
        return resolve_send_notification(info, user_id, message)

class Mutation(graphene.ObjectType):
    send_notification = SendNotification.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
