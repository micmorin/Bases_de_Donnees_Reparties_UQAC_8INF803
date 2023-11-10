from flask import Flask, redirect, url_for
from flask_login import LoginManager
import Routes

if __name__ == "__main__":
    app = Flask(__name__)
    app.config.from_object('config.DevConfig')
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(user_id):
        return Routes.Controller.obj.obj.User.get(user_id)
    app.register_blueprint(Routes.route_main)
    app.register_blueprint(Routes.route_user)

    app.run(host='0.0.0.0',port=5000)


