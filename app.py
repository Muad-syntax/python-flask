from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def halaman_utama():
    if request.method == "POST":
        nama_dari_from = request.form["nama_input"]
        return render_template("index.html", orang=nama_dari_from)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)