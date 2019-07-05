from flask import Flask
from flask_sqlalchemy import SQLAlchemy




def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////code/db.sqlite'
    db = SQLAlchemy(app)

    from personal_okrs.root.routes import root
    app.register_blueprint(root)

    return app, db


app, db = create_app()
