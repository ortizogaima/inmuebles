import os
import psycopg2
from flask import Blueprint, jsonify
from dotenv import load_dotenv

# Cargar variables del .env
load_dotenv()

# Crear blueprint
inmuebles_bp = Blueprint("inmuebles", __name__, url_prefix="/api/inmuebles")

# Función para conectar a PostgreSQL
def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

# Endpoint para listar inmuebles
@inmuebles_bp.route("/", methods=["GET"])
def listar_inmuebles():
    try:
        conn = get_db_connection()
        print("Conectando a la base de datos...")  # 👈 debug
        cur = conn.cursor()
        cur.execute("SELECT * FROM inmueble;")
        filas = cur.fetchall()
        print("Cantidad de filas:", len(filas))  # 👈 debug
        columnas = [desc[0] for desc in cur.description]
        datos = [dict(zip(columnas, fila)) for fila in filas]
        cur.close()
        conn.close()
        return jsonify(datos)
    except Exception as e:
        return jsonify({"error": str(e)})
