from flask import Flask, render_template
from flask_login import LoginManager
from .views import views
from .auth import auth
from .models import User, db


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kdfkdkfdfkdk dkfdkfkd'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:localhost/dbName'
    db.init_app(app)
   
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    db.create_all(app=app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html")

    return app

    
    
        
    