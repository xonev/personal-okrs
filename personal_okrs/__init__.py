from flask import Flask


def create_app():
    app = Flask(__name__)

    from personal_okrs.root.routes import root
    app.register_blueprint(root)

    return app
