from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "databaseTrackBox.db"


def create_app():
    app = Flask(__name__)
    app.secret_key = 'many random bytes'
    
    app.config['SQLAlchemy_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    
    app.register_blueprint(views, url_prefix='/')
    
    return app