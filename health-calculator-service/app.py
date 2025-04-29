from flask import Flask, request, jsonify, render_template
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bmi', methods=['POST'])
def bmi():
    # Si la requête vient du formulaire HTML
    if request.content_type == 'application/x-www-form-urlencoded':
        height = float(request.form.get('height'))
        weight = float(request.form.get('weight'))
    else:
        data = request.get_json()
        height = data.get('height')
        weight = data.get('weight')

    if height is None or weight is None:
        return jsonify({'error': 'Height and weight are required.'}), 400

    bmi_value = calculate_bmi(height, weight)

    # Si la requête vient du formulaire HTML, retourner directement la page
    if request.content_type == 'application/x-www-form-urlencoded':
        return f"<h2>Result BMI: {round(bmi_value, 2)}</h2>"

    return jsonify({'bmi': round(bmi_value, 2)})

@app.route('/bmr', methods=['POST'])
def bmr():
    # Si la requête vient du formulaire HTML
    if request.content_type == 'application/x-www-form-urlencoded':
        height = float(request.form.get('height'))
        weight = float(request.form.get('weight'))
        age = int(request.form.get('age'))
        gender = request.form.get('gender')
    else:
        data = request.get_json()
        height = data.get('height')
        weight = data.get('weight')
        age = data.get('age')
        gender = data.get('gender')

    if None in [height, weight, age, gender]:
        return jsonify({'error': 'Height, weight, age, and gender are required.'}), 400

    bmr_value = calculate_bmr(height, weight, age, gender)

    # Si la requête vient du formulaire HTML, retourner directement la page
    if request.content_type == 'application/x-www-form-urlencoded':
        return f"<h2>Result BMR: {round(bmr_value, 2)}</h2>"

    return jsonify({'bmr': round(bmr_value, 2)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)