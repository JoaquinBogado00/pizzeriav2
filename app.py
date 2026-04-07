from flask import Flask
from routes.clientes import cliente_bp
from routes.admin import admin_bp

app = Flask(__name__)

app.config["SECRET_KEY"] = "mi_pizzeria_secreta_123"
app.register_blueprint(cliente_bp)
app.register_blueprint(admin_bp, url_prefix="/admin")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    