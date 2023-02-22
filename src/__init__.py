from flask import Flask
import os
from src.auth import auth
from src.bookmarks import bookmarks
from src.database import db
from flask_jwt_extended import JWTManager
def create_app(test_config=None):

    app=Flask(__name__,
              instance_relative_config=True)
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DB_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY')
        )
    else:
        app.config.from_mapping(test_config)

    @app.get('/')
    def hello_world():  # put application's code here
        return 'Hello World!'

    @app.get('/hello')
    def say_hello():  # put application's code here
        return {"message": "Hello world"}

    JWTManager(app)
    app.register_blueprint(auth)
    app.register_blueprint(bookmarks)
    # if __name__ == '__main__':
    #     app.run()
    db.app=app
    db.init_app(app)
    app.app_context()
    app.run(debug=True)
    return app
