from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    # Inisialisasi Login Manager
    login_manager.init_app(app)
    login_manager.login_view = 'admin.login' # Rute jika user belum login
    login_manager.login_message = "Silakan login terlebih dahulu untuk mengakses halaman ini."
    login_manager.login_message_category = "info"

    # User loader untuk mengambil user dari ID session
    from app.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from app.routes_main import main
    from app.routes_admin import admin
    app.register_blueprint(main)
    app.register_blueprint(admin, url_prefix='/admin')

    return app