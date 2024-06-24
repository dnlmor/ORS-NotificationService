from flask import Flask
from .database import db_session, init_db
from .controllers import notification_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Initialize the database
    init_db()
    
    # Register the notification blueprint
    app.register_blueprint(notification_blueprint)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app
