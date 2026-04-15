from flask import Flask, jsonify

app = Flask(__name__)

airport_data = {
    "LFLL": {
        "name": "Lyon Saint-Exupery Airport",
        "city": "Lyon",
        "country": "FR"
    }
}

@app.route('/')
def home():
    return "Hello Test 123"

@app.route('/airport/<string:icao>')
def get_airport(icao):
    icao = icao.upper()

    if icao in airport_data:
        airport = airport_data[icao]
        return jsonify({
            "icao": icao,
            "name": airport["name"],
            "city": airport["city"],
            "country": airport["country"]
        })
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)