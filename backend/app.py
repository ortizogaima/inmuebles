from flask import Flask
from flask_cors import CORS
from routes.inmuebles import inmuebles_bp

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

# Registrar blueprint de inmuebles
app.register_blueprint(inmuebles_bp)

if __name__ == "__main__":
    app.run(debug=True)