# 📈 Health Calculator Service

A simple Python Flask-based web application and API to calculate BMI and BMR values. Built to demonstrate cloud deployment using Docker, GitHub Actions CI/CD, and Azure App Service.

---

## 👉 Features

- 🏢 Deployable as a Docker container
- 💡 Exposes REST API endpoints for BMI and BMR calculation
- 📈 Includes a simple web form (front-end) to interact with the service
- 📅 Automated CI/CD pipeline using GitHub Actions
- 🌍 Deployed on Azure App Service

---

## 💡 How it works

- **/bmi** endpoint (POST): Calculates Body Mass Index (BMI)
- **/bmr** endpoint (POST): Calculates Basal Metabolic Rate (BMR)
- **/** route (GET): Displays a simple HTML form to calculate BMI and BMR from the browser.

---

## 🔧 Technologies Used

- **Python 3.9**
- **Flask** for the web server
- **Docker** for containerization
- **GitHub Actions** for CI/CD
- **Azure App Service** for hosting

---

## 🔄 Running Locally

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the Flask app:

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## 👷️ Docker Commands

1. Build the Docker image:

```bash
docker build -t health-calculator-service .
```

2. Run the Docker container:

```bash
docker run -p 5000:5000 health-calculator-service
```

Then open `http://localhost:5000` to use the application.

---

## 📆 Deployment Process

1. Push the code to the GitHub repository.
2. GitHub Actions pipeline will:
   - Build and test the app
   - Build the Docker image
   - Push the Docker image to Docker Hub
   - Deploy the new image to Azure App Service automatically.

---

## 🔗 Important URLs

- **API Endpoint for BMI**: `POST /bmi`
- **API Endpoint for BMR**: `POST /bmr`
- **Front-End Form**: Visit the root URL `/`

---

## 📊 Example Requests

**POST BMI Calculation (JSON Body):**

```bash
curl -X POST http://localhost:5000/bmi \
-H "Content-Type: application/json" \
-d '{"height": 1.75, "weight": 70}'
```

**POST BMR Calculation (JSON Body):**

```bash
curl -X POST http://localhost:5000/bmr \
-H "Content-Type: application/json" \
-d '{"height": 175, "weight": 70, "age": 25, "gender": "male"}'
```

---

## 📖 License

This project is licensed under the MIT License.
