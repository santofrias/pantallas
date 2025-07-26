from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_resultados():
    conn = sqlite3.connect("resultados.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM resultados")
    datos = cursor.fetchall()
    conn.close()
    return datos

@app.route("/")
def index():
    resultados = get_resultados()
    return render_template("index.html", resultados=resultados)


def get_resultados2():
    conn = sqlite3.connect("resultados2.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM resultados2")
    datos = cursor.fetchall()
    conn.close()
    return datos



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
                conn = sqlite3.connect("resultados.db")
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
                conn = sqlite3.connect("resultados2.db")
                cursor = conn.cursor()
                cursor.execute(f"UPDATE resultados2 SET {campo} = ? WHERE id = ?", (valor, loteria_id))
                conn.commit()
                conn.close()
        return redirect("/admin2")
    resultados = get_resultados()
    return render_template("admin2.html", resultados=resultados)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


