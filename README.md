# Django API for Monitoring and Metrics Collection

This project is a **Django-based application** for monitoring and collecting metrics, featuring a REST API, MySQL support, and Docker deployment.

## 📌 Features
- REST API for collecting and retrieving metrics.
- MySQL database for data storage.
- Containerization with Docker.
- Configuration management via `.env`.

## 🛠️ Technologies Used
- **Framework:** Django, Django REST Framework
- **Database:** MySQL
- **Containerization:** Docker, Docker Compose
- **DevOps:** dotenv, Gunicorn

## 📂 Installation and Setup

### 1. **Clone the Repository**
```sh
git clone https://github.com/diankaaaa21/monitoring.git
cd monitoring
```

### 2. **Create Configuration File**
```sh
🛠 Example .env File

Create a `.env` file in the project root:

```ini
MYSQL_DATABASE=monitoring
MYSQL_USER=root
MYSQL_PASSWORD=yourpassword
DB_HOST=db
DEBUG=True
SECRET_KEY=your_secret_key
```

### 3. **Run the Project with Docker**
```sh
docker-compose up --build
```

### 4. **Apply Database Migrations**
```sh
docker exec -it <container_id> python manage.py migrate
```

### 5. **Run API Without Docker**
```sh
python manage.py runserver
```

## 📖 Project Structure
- `manage.py` — Django management script.
- `settings.py` — Project settings.
- `models.py` — Database models.
- `views.py` — API logic.
- `urls.py` — API routing.
- `metrics.py` & `monitor.py` — Monitoring services.
- `Dockerfile` & `docker-compose.yml` — Containerization files.
- `requirements.txt` — Project dependencies.
- `tests/` — Directory for unit tests.

## 🚀 Running and Testing
API will be accessible at:
```sh
http://localhost:8000/api/incidents/
```

### **API Documentation**
API documentation is available at:
```sh
http://localhost:8000/docs/
```
or (if using DRF):
```sh
http://localhost:8000/api/schema/
```

### **Testing the API**
Run tests using `pytest`:
```sh
pytest
```

Run tests inside a Docker container:
```sh
Find the container ID:
```bash
docker ps
Then run:
```bash
docker exec -it <container_id> pytest
```

Example API request using `curl`:
```sh
curl -X POST http://localhost:8000/api/metrics/ -H "Content-Type: application/json" -d '{
  "machine_id": "server-1",
  "cpu": 75,
  "mem": "60%",
  "disk": "45%",
  "uptime": "2 days"
}'
```

## 📜 License
This project is distributed under the MIT License.
