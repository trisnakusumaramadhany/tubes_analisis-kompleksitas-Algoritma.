from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

def hitung_kapital_iteratif(teks):
    return sum(1 for c in teks if c.isupper())

def hitung_kapital_rekursif(teks, i=0):
    if i == len(teks):
        return 0
    return (1 if teks[i].isupper() else 0) + hitung_kapital_rekursif(teks, i + 1)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json(force=True)
        teks = data.get("text", "")

        start = time.perf_counter()
        iteratif = hitung_kapital_iteratif(teks)
        time_iter = time.perf_counter() - start

        start = time.perf_counter()
        rekursif = hitung_kapital_rekursif(teks)
        time_rek = time.perf_counter() - start

        return jsonify({
            "iteratif": iteratif,
            "rekursif": rekursif,
            "time_iteratif": round(time_iter * 1000, 5),
            "time_rekursif": round(time_rek * 1000, 5),
            "complexity": "O(n)"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
