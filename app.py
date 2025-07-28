from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Ruta absoluta a la base de datos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB1_PATH = os.path.join(BASE_DIR, "resultados.db")
DB2_PATH = os.path.join(BASE_DIR, "resultados2.db")

def get_resultados():
    conn = sqlite3.connect(DB1_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM resultados")
    datos = cursor.fetchall()
    conn.close()
    return datos

def get_resultados2():
    conn = sqlite3.connect(DB2_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM resultados2")
    datos = cursor.fetchall()
    conn.close()
    return datos

@app.route("/")
def index():
    resultados = get_resultados()
    return render_template("index.html", resultados=resultados)

@app.route("/pantalla1")
def pantalla1():
    resultados2 = get_resultados2()
    return render_template("pantalla1.html", resultados2=resultados2)

@app.route("/sueños")
def sueños():
    return render_template("sueños.html")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        for key in request.form:
            if key.startswith("numero"):
                _, campo, loteria_id = key.split("_")
                valor = request.form[key]
                conn = sqlite3.connect(DB1_PATH)
                cursor = conn.cursor()
                cursor.execute(f"UPDATE resultados SET {campo} = ? WHERE id = ?", (valor, loteria_id))
                conn.commit()
                conn.close()
        return redirect("/admin")
    resultados = get_resultados()
    return render_template("admin.html", resultados=resultados)

@app.route("/admin2", methods=["GET", "POST"])
def admin2():
    if request.method == "POST":
        for key in request.form:
            if key.startswith("numero"):
                _, campo, loteria_id = key.split("_")
                valor = request.form[key]
                conn = sqlite3.connect(DB2_PATH)
                cursor = conn.cursor()
                cursor.execute(f"UPDATE resultados2 SET {campo} = ? WHERE id = ?", (valor, loteria_id))
                conn.commit()
                conn.close()
        return redirect("/admin2")
    resultados = get_resultados()
    return render_template("admin2.html", resultados=resultados)

if __name__ == "__main__":
    app.run(debug=True)
