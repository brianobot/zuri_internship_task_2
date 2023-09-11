# zuri_internship_task_2

Task 2 Repo

[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)](https://github.com/brianobot/zuri_internship_task_2)
[![Tests Passed](https://img.shields.io/badge/Tests-Passed-brightgreen.svg)](https://your-test-results-url)
[![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-000000.svg)](https://github.com/psf/black)


## 🌐 BASE URL: https://brianobot.pythonanywhere.com/

# Person Webservice Documentation

## Introduction

The **Person Webservice** is a RESTful API that allows users to interact with a `Person` resource. This webservice provides basic CRUD (Create, Read, Update, Delete) operations for managing `Person` objects.

### Resource: Person

A `Person` object represents an individual with a name.

#### Fields

- `name` (String, max length 100): The unique identifier of the person. It is a required field and must be a string.

## API Endpoints

### 1. Create a Person

**Endpoint:** `POST /api/`

**Request:**
```json
{
    "name": "Mark Essien"
}
```

**Response:**
```json
{
    "id": 1,
    "name": "Mark Essien"
}
```

### 2. Retrieve a Person

**Endpoint:** `GET /api/{user_id}/`

**Response:**
```json
{
    "id": 1,
    "name": "Mark Essien"
}
```

### 3. Update a Person

**Endpoint:** `PUT /api/{user_id}/`

**Request:**
```json
{
    "name": "Mark Essien Updated"
}
```

**Response:**
```json
{
    "id": 1,
    "name": "Mark Essien Updated"
}
```

### 4. Delete a Person

**Endpoint:** `DELETE /api/{user_id}/`

**Response:**
```json
{
    "message": "Person with id 1 has been deleted"
}
```


## Example Usage

```python
# Creating a new person
import requests

url = "https://brianobot.pythonanywhere.com/api"
payload = {
    "name": "Mark Essien"
}
response = requests.post(url, json=payload)
print(response.json())

# Retrieving a person
user_id = 1
url = f"https://brianobot.pythonanywhere.com/api/{user_id}/"
response = requests.get(url)
print(response.json())

# Updating a person
user_id = 1
url = f"https://brianobot.pythonanywhere.com/api/{user_id}/"
payload = {
    "name": "Mark Essien Updated"
}
response = requests.put(url, json=payload)
print(response.json())

# Deleting a person
user_id = 1
url = f"https://brianobot.pythonanywhere.com/api/{user_id}/"
response = requests.delete(url)
print(response.json())


```
---

## ⚙️ Setting Up and Deploying the API

### Locally:

#### Prerequisites:

1. Python (3.6 or higher)
2. Pip (Python package installer)
3. Git (for cloning the repository)

#### Steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/brianobot/zuri_internship_task_2.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd zuri_internship_task_2
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**

   ```bash
   python manage.py runserver
   ```

   The API should now be running locally at `http://127.0.0.1:8000/`.

---

### On a Server:

#### Prerequisites:

1. A server (e.g., AWS, Google Cloud, PythonAnywhere, etc.)
2. SSH access to the server
3. Python and Pip installed on the server

#### Steps:

1. **Connect to the Server via SSH:**

   ```bash
   ssh your_username@your_server_ip
   ```

2. **Clone the Repository on the Server:**

   ```bash
   git clone https://github.com/brianobot/zuri_internship_task_2.git
   ```

3. **Navigate to the Project Directory:**

   ```bash
   cd zuri_internship_task_2
   ```

4. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application:**

   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

   The API should now be running on the server.

6. **Optional: Use a Web Server for Production (e.g., Nginx)**

   If you want to serve the API over HTTP or HTTPS, consider using a web server like Nginx as a reverse proxy.

   - Install Nginx and configure it to forward requests to the API.

---

### Accessing the API:

- Local: Visit `http://127.0.0.1:8000/` in your web browser or make API requests using tools like Postman or cURL.
- Server: Use the server's IP address or domain name to access the API, e.g., `http://your_server_ip/` or `http://your_domain_name/`.

---

### API Endpoints:

- Create a Person: `POST /api/`
- Retrieve a Person: `GET /api/{user_id}/`
- Update a Person: `PUT /api/{user_id}/`
- Delete a Person: `DELETE /api/{user_id}/`

Please note that these instructions assume a basic setup. Depending on your specific server environment and requirements, additional steps or configurations may be necessary. Always ensure security best practices are followed, especially when deploying on a public server.

---

## Error Handling

- **400 Bad Request:** If the request is malformed or missing required fields.
- **404 Not Found:** If the requested `Person` does not exist.
- **405 Method Not Allowed:** If an unsupported HTTP method is used on an endpoint.
- **500 Method Server Error** Something you will not see from this project.

---

## Testing

To Run the Automated Test, run the command (from within the project directory terminal)
```python
python test.py
```

## Conclusion

The Person Webservice provides a simple and easy-to-use interface for managing `Person` objects. It allows for creating, retrieving, updating, and deleting `Person` records through a RESTful API. Use the provided endpoints to interact with the service and manage your `Person` data.

---

### Maintainer:

- Brian Obot
- Email: brianobot9@gmail.com

---