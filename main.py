from joblib import load
from flask import Flask, request, render_template, url_for

app = Flask(__name__)
clf = load("models/model.pkl")

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method=="POST":
    hasil_prediksi = clf.predict([[request.form['palo'],
                                  request.form['lelo'],
                                  request.form['pako'],
                                  request.form['leko']]])

    return render_template("index.html", hasil = hasil_prediksi[0])

  else:
    return render_template("index.html")

@app.route('/modeling')
def modeling():
  return render_template("modeling.html")

# KALAU DI-ONLINE'KAN BARIS DI BAWAH INI DIHAPUS SAJA
app.run(debug=True)