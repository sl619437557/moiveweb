from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
db=SQLAlchemy()
bootstrap=Bootstrap()
def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY'] = '123456'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/filmdb'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    db=SQLAlchemy()
    db.init_app(app)
    bootstrap.init_app(app)
    from . import views
    from .views import init_views
    init_views(app)
    return app