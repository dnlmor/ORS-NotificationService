from flask import Blueprint
from flask_graphql import GraphQLView
from .schema import schema

notification_blueprint = Blueprint('notification', __name__)

notification_blueprint.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)
