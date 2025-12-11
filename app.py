from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = "kuncirahasia123"

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data_pengguna.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
        nama_dari_form = request.form["nama_input"]
        data_baru = Pengunjung(nama=nama_dari_form)
        db.session.add(data_baru)
        db.session.commit()
        session['orang_aktif'] = nama_dari_form
    orang_saat_ini = session.get('orang_aktif', None)
    list_pengunjung = Pengunjung.query.all()        

    return render_template("index.html", daftar=list_pengunjung, orang=orang_saat_ini)

@app.route("/hapus/<int:id_pengunjung>")
def hapus_data(id_pengunjung):
    data_yang_mau_dihapus = Pengunjung.query.get(id_pengunjung)
    if data_yang_mau_dihapus:
        db.session.delete(data_yang_mau_dihapus)
        db.session.commit()

    return redirect("/")

@app.route('/edit/<int:id_pengunjung>', methods=['GET', 'POST'])
def edit_data(id_pengunjung):
    data_yang_mau_di_edit = Pengunjung.query.get_or_404(id_pengunjung)
    if request.method == 'POST':
        nama_baru_diinput = request.form['nama_edit']
        data_yang_mau_di_edit.nama = nama_baru_diinput
        db.session.commit()

        return redirect("/")
    return redirect("/")

@app.route("/ganti_nama")
def ganti_nama():
    session.pop('orang_aktif', None)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)