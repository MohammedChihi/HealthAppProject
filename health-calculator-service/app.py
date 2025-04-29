from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi():
    data = request.get_json()
    height = data.get('height')
    weight = data.get('weight')

    if height is None or weight is None:
        return jsonify({'error': 'Height and weight are required.'}), 400

    bmi_value = calculate_bmi(height, weight)
    return jsonify({'bmi': round(bmi_value, 2)})

@app.route('/bmr', methods=['POST'])
def bmr():
    data = request.get_json()
    height = data.get('height')
    weight = data.get('weight')
    age = data.get('age')
    gender = data.get('gender')

    if None in [height, weight, age, gender]:
        return jsonify({'error': 'Height, weight, age, and gender are required.'}), 400

    bmr_value = calculate_bmr(height, weight, age, gender)
    return jsonify({'bmr': round(bmr_value, 2)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
