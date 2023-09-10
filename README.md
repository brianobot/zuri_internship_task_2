# zuri_internship_task_2

Task 2 Repo

# Person Webservice Documentation

## Introduction

The **Person Webservice** is a RESTful API that allows users to interact with a `Person` resource. This webservice provides basic CRUD (Create, Read, Update, Delete) operations for managing `Person` objects.

### Resource: Person

A `Person` object represents an individual with a name.

#### Fields

- `name` (String, max length 100): The name of the person. It is a required field and must be unique.

## API Endpoints

### 1. Create a Person

**Endpoint:** `POST /api/persons/`

**Request:**
```json
{
    "name": "John Doe"
}
```

**Response:**
```json
{
    "id": 1,
    "name": "John Doe"
}
```

### 2. Retrieve a Person

**Endpoint:** `GET /api/persons/{name}/`

**Response:**
```json
{
    "id": 1,
    "name": "John Doe"
}
```

### 3. Update a Person

**Endpoint:** `PUT /api/persons/{name}/`

**Request:**
```json
{
    "name": "John Smith"
}
```

**Response:**
```json
{
    "id": 1,
    "name": "John Smith"
}
```

### 4. Delete a Person

**Endpoint:** `DELETE /api/persons/{name}/`

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

url = "http://example.com/api/persons/"
payload = {
    "name": "Jane Doe"
}
response = requests.post(url, json=payload)
print(response.json())

# Retrieving a person
name = "Jane Doe"
url = f"http://example.com/api/persons/{name}/"
response = requests.get(url)
print(response.json())

# Updating a person
name = "Jane Doe"
url = f"http://example.com/api/persons/{name}/"
payload = {
    "name": "Jane Smith"
}
response = requests.put(url, json=payload)
print(response.json())

# Deleting a person
name = "Jane Doe"
url = f"http://example.com/api/persons/{name}/"
response = requests.delete(url)
print(response.json())
```

## Error Handling

- **400 Bad Request:** If the request is malformed or missing required fields or the name already exists.
- **404 Not Found:** If the requested `Person` does not exist.
- **405 Method Not Allowed:** If an unsupported HTTP method is used on an endpoint.

## Conclusion

The Person Webservice provides a simple and easy-to-use interface for managing `Person` objects. It allows for creating, retrieving, updating, and deleting `Person` records through a RESTful API. Use the provided endpoints to interact with the service and manage your `Person` data.

### Maintainer:
- Brian Obot <brianobot9@gmail.com>