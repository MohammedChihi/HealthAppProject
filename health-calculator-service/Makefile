.PHONY: init run test build clean

init:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

run:
	@echo "Running the Flask app..."
	python app.py

test:
	@echo "Running unit tests..."
	pytest tests/

build:
	@echo "Building the Docker image..."
	docker build -t health-calculator-service .

clean:
	@echo "Cleaning up..."
	docker system prune -f