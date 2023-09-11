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

## Error Handling

- **400 Bad Request:** If the request is malformed or missing required fields.
- **404 Not Found:** If the requested `Person` does not exist.
- **405 Method Not Allowed:** If an unsupported HTTP method is used on an endpoint.

## Testing

To Run the Automated Test, run the command (from within the project directory terminal)
```python
python test.py
```

## Conclusion

The Person Webservice provides a simple and easy-to-use interface for managing `Person` objects. It allows for creating, retrieving, updating, and deleting `Person` records through a RESTful API. Use the provided endpoints to interact with the service and manage your `Person` data.

### Maintainer:
- Brian Obot <brianobot9@gmail.com>
