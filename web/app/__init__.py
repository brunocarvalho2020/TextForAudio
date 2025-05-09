from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuração do app, se necessário
    app.config.from_object('config')

    # Importa e registra os blueprints
    from app.routes.main_routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
