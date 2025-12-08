from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data_pengguna.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

class Pengunjung(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Pengunjung {self.nama}>'
    
with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def halaman_utama():
    if request.method == "POST":

        nama_dari_from = request.form["nama_input"]

        data_baru = Pengunjung(nama=nama_dari_from)

        db.session.add(data_baru)
        db.session.commit()

        list_pengunjung =Pengunjung.query.all()
        return render_template("index.html", daftar=list_pengunjung)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)