## **FastAPI**

FastAPI is a modern, high-performance web framework for building APIs with Python. It leverages type hints to provide automatic data validation and serialization, leading to fewer errors and improved developer experience. Key features include:

- **High Performance:** Built on Starlette and Pydantic, FastAPI boasts exceptional speed, rivaling Node.js and Go frameworks.
- **Automatic Interactive API Documentation:** Swagger UI and ReDoc automatically generate interactive API documentation from your code, making it easy to explore and test your API.
- **Data Validation:** Type hints are used for data validation, catching errors early and ensuring data integrity.
- **Asynchronous Programming Support:** Built-in support for asynchronous programming with `async` and `await` keywords, enhancing performance for I/O-bound operations.
- **Easy to Learn:** FastAPI's intuitive design and clear documentation make it relatively easy to learn and use, even for developers new to web frameworks.
- **Extensible:** A rich ecosystem of extensions and plugins allows you to add functionality as needed.

FastAPI is suitable for building a wide range of APIs, from small microservices to large, complex applications. Its combination of performance, ease of use, and robust features makes it a popular choice for modern API development.

<br>

## **Virtual Environment:**

A virtual environment in Python is an isolated space where you can install packages and dependencies without affecting your system-wide Python.

In short:
✅ It keeps your project’s dependencies separate and organized
✅ Prevents version conflicts between different projects
✅ Common tools: venv, virtualenv, conda

You activate it, install what you need, and everything stays clean and project-specific.

## **Creating Virtual Environemnt in Python**

1. **Using venv (Built-in Module)**

venv is a built-in module in Python 3.3+ for creating virtual environments.

```python
# Create a virtual environment
python -m venv myenv

# Activate the virtual environment
# On Windows:
myenv\Scripts\activate

# On macOS/Linux:
source myenv/bin/activate

# Deactivate the virtual environment
deactivate
```

2. **Using virtualenv (Third-Party Tool)**

virtualenv is a popular third-party tool for creating virtual environments. It works with both Python 2 and 3.

```python
# Install virtualenv
pip install virtualenv

# Create a virtual environment
virtualenv myenv

# Activate the virtual environment
# On Windows:
myenv\Scripts\activate

# On macOS/Linux:
source myenv/bin/activate

# Deactivate the virtual environment
deactivate
```

3. **Using conda (Anaconda/Miniconda)**

If you are using Anaconda or Miniconda, you can create virtual environments using conda.

```python
# Create a virtual environment
conda create --name myenv

# Activate the virtual environment
conda activate myenv

# Deactivate the virtual environment
conda deactivate
```

```python
Creating and Managing a Virtual Environment Using Conda

# 1. Create a Conda Virtual Environment
conda create --name my_env python=3.10
# Replace 'my_env' with your desired environment name.
# Replace 'python=3.10' with the Python version you need.

# 2. Activate the Conda Environment
conda activate my_env

# 3. Deactivate the Conda Environment
conda deactivate

# 4. Remove a Conda Environment (Optional)
conda remove --name my_env --all

# 5. List All Conda Environments
conda env list  # OR
conda info --envs

-------------------------------------------

Using the '-p' (Prefix) Flag in Conda

# 1. Creating a Conda Environment with a Specific Path
conda create -p /path/to/custom_env python=3.10
# This creates a virtual environment at '/path/to/custom_env'.
# Useful for organizing environments in a custom directory instead of Conda's default location.

# 2. Activating a Path-Based Conda Environment
conda activate /path/to/custom_env

# 3. Removing a Path-Based Conda Environment
conda remove -p /path/to/custom_env --all

# This method is helpful when working in projects where you want the environment inside the project folder.
```

4. **Using pipenv (Dependency Management Tool)**

pipenv combines virtual environment creation and dependency management.

```python
# Install pipenv
pip install pipenv

# Create a virtual environment and install dependencies
pipenv install

# Activate the virtual environment
pipenv shell

# Exit the virtual environment
exit

```

5. **Using pyenv (Python Version Management)**

pyenv is used to manage multiple Python versions and can also create virtual environments.

```python
# Install pyenv and pyenv-virtualenv
# Follow installation instructions for your OS: https://github.com/pyenv/pyenv

# Create a virtual environment
pyenv virtualenv 3.9.0 myenv

# Activate the virtual environment
pyenv activate myenv

# Deactivate the virtual environment
pyenv deactivate
```

6. **Using poetry (Dependency Management and Packaging Tool)**

poetry is a modern tool for dependency management and packaging that automatically creates virtual environments.

```python
# Install poetry
pip install poetry

# Create a new project and virtual environment
poetry new myproject

# Activate the virtual environment
poetry shell

# Exit the virtual environment
exit
```

---

<br>

## **Basic FastAPI App**

```python
from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI()

@app.get("/")
async def root():
    """
    Asynchronous function that handles requests to the root URL.
    Returns a JSON response with a welcome message.
    """
    return {"message": "Hello World!!"}
```

```python
from fastapi import FastAPI
```

- **`from fastapi import FastAPI`**
  - This imports the `FastAPI` class from the **FastAPI** framework.
  - `FastAPI` is used to create a web application that can handle API requests and responses.
  - It allows defining **routes** (`GET`, `POST`, etc.), request handling, and response generation.

```python
# Create an instance of FastAPI
app = FastAPI()
```

- **`app = FastAPI()`**
  - This creates an instance of the `FastAPI` class, which serves as the **main application**.
  - The `app` object will be used to define API routes, middleware, and configurations.
  - When running the server (`uvicorn main:app --reload`), this instance (`app`) listens for incoming HTTP requests and directs them to the correct route handler.

```python
@app.get("/")
```

- **`@app.get("/")`**
  - This is a **decorator** that registers a route in FastAPI.
  - It tells FastAPI:
    - **Accept `GET` requests** on the root (`"/"`) URL.
    - When a user visits `http://127.0.0.1:8000/` (default FastAPI address), this function gets executed.
  - The **decorator pattern** is used here to modify the function's behavior by attaching metadata about the route.

```python
async def root():
```

- **`async def root():`**
  - This defines an **asynchronous function** (`async def`).
  - The use of `async` makes it **non-blocking**, meaning it can handle multiple requests simultaneously without waiting for previous ones to finish.
  - This is useful for **high-performance applications** that involve database queries, file I/O, or external API calls.

```python
return {"message": "Hello World!!"}
```

- **`return {"message": "Hello World!!"}`**
  - This function **returns a dictionary**, which FastAPI **automatically converts into a JSON response**.
  - The response will look like this in the browser or when called via an API client:
    ```json
    {
      "message": "Hello World!!"
    }
    ```
  - FastAPI **handles JSON serialization** internally using `pydantic` and `jsonable_encoder`.

## **Inner Working of `@app.get("/")`**

### **How FastAPI Registers and Handles the Route**

1. **Route Registration**

   - When `@app.get("/")` is used, FastAPI **adds an entry to its internal routing table**, mapping `"/"` to the `root()` function.
   - Under the hood, it uses **Starlette**, the ASGI framework that FastAPI is built on.

2. **When a Request Comes In:**

   - When a `GET` request is made to `/`, FastAPI:
     - Looks up its routing table.
     - Finds that `/` is handled by `root()`.
     - Calls `root()` asynchronously.
     - Converts the return value into a JSON response.
     - Sends the response back to the client.

3. **Why `async` Matters**
   - If `root()` had blocking operations (e.g., database queries), `async` allows other requests to be processed while waiting.
   - This makes FastAPI highly **scalable and efficient**, especially under heavy loads.

## **Summary**

| Line                                  | Explanation                                                 |
| ------------------------------------- | ----------------------------------------------------------- |
| `from fastapi import FastAPI`         | Imports FastAPI to create a web API.                        |
| `app = FastAPI()`                     | Creates the FastAPI application instance.                   |
| `@app.get("/")`                       | Registers a route that listens for GET requests at `/`.     |
| `async def root():`                   | Defines an asynchronous function to handle requests.        |
| `return {"message": "Hello World!!"}` | Returns a JSON response that FastAPI automatically formats. |

<br>

---

<br>

## **Running the FastAPI Server**

To run the FastAPI application, follow these steps:

1. **Ensure FastAPI and Uvicorn are installed** (if not already installed):
   ```sh
   pip install fastapi uvicorn
   ```
2. **Save the script as `main.py`**.
3. **Run the FastAPI server using Uvicorn**:

   ```sh
   uvicorn main:app --reload
   ```

   - `main` refers to the Python filename (`main.py`).
   - `app` is the FastAPI instance (`app = FastAPI()`).
   - `--reload` enables **auto-reloading** for development (restarts server on code changes).

4. **Open in the browser**:

   - Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - You should see: `{ "message": "Hello World!!" }`

5. **Access the Interactive API Docs**:
   - Open: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (Swagger UI).
   - Open: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) (ReDoc).

<br>

---

<br>

## **What is an API?**

- API stands for Application Programming Interface.
- It is a set of rules and protocols that allows one software application to communicate with another.
- APIs act as an intermediary, enabling applications to send requests and receive responses to perform operations or exchange data.

### Examples of APIs

- **Payment Gateway APIs:** Stripe or PayPal for payment processing.
- **Weather APIs:** Retrieve current weather data.
- **Social Media APIs:** Post updates or retrieve user data.

<br>

## **What is a REST API?**

- REST API stands for Representational State Transfer API.
- It is a type of API that adheres to the principles of REST architecture, a stateless and resource-based approach for designing networked applications.
- REST APIs typically use HTTP methods to perform operations on resources.

<br>

### Principles of REST API

1. **Stateless**  
   Each request is independent, containing all necessary information. The server does not store client state, improving scalability.

   "The server does not remember anything about the client between requests."

- Every request from a client must contain all the necessary information (authentication, data, etc.).

- The server does not store session information between requests.

- Each request is independent, so the server does not rely on past interactions.

**Example:**

- If you log in to a website, your browser sends a request with your credentials.

- The server responds with a token (e.g., JWT).

-For every future request, you must send the token, as the server does not remember who you are.

**What Happens if the Server Stores Information?**

- If the server stores client session data, it **remembers past interactions** between requests. This is called a **stateful system** (opposite of REST's stateless principle).

**Benefits of Storing Information (Stateful Server)**

- **Personalized Experience** – The server can store user sessions, preferences, and progress (e.g., shopping carts, logged-in sessions).

- **Less Data in Each Request** – Clients don’t need to send authentication or state-related data every time.

- **Better Performance for Some Use Cases** – Reduces redundant processing (e.g., caching session data instead of verifying credentials every request).

**Disadvantages of Storing Information (Stateful Server)**

- **Scalability Issues** – Each server must track user sessions, making it hard to scale horizontally (e.g., load balancing becomes complex).
- **Increased Server Load** – More memory and storage are required to maintain sessions for multiple users.
- **Session Persistence Problems** – If a server crashes, session data may be lost unless stored externally (e.g., in Redis).

**Benefits of Not Storing Information (Stateless Server, like REST APIs)**

- **Easier Scaling** – Any server can handle any request without tracking user state (good for microservices and cloud computing).

- **Fault Tolerance** – No risk of session loss since requests are independent.

- **Simpler Design** – No need to manage or synchronize session data across multiple servers.

**Disadvantages of Not Storing Information (Stateless Server)**

- **More Data in Requests** – Clients must send authentication tokens and required data with every request.
- **Repetitive Processing** – The server may repeatedly verify user authentication, increasing CPU load.
- **Harder to Provide Real-Time Personalization** – Requires extra mechanisms (like cookies, tokens, or database lookups) for personalized experiences.

**Final Takeaway**

- **Stateful servers** are better for **interactive applications** (e.g., gaming, banking, live sessions).
- **Stateless servers** are ideal for **scalable and distributed systems** (e.g., REST APIs, microservices).

2. **Client-Server Architecture**  
   Separation of client (UI/UX) and server (data/logic), allowing independent development and maintenance.

3. **Uniform Interface**  
   Consistent resource access using standard HTTP methods (`GET`, `POST`, etc.), predictable URIs, and response formats (e.g., JSON).

- Every resource (data entity) is identified using a unique URL (Uniform Resource Locator).

- The same HTTP methods (GET, POST, PUT, DELETE) are used across different resources.

  **Benefits:**

- Consistency (easy to understand API structure).
- Predictability (clients know how to interact with the API).
- Scalability (allows caching and optimizations).

4. **Cacheable**  
   Responses can include caching instructions to improve performance and reduce server load.

5. **Layered System**  
   Allows intermediaries (e.g., proxies, load balancers) without the client knowing, enhancing scalability and modularity.

6. **Code on Demand (Optional)**  
   Servers can send executable code (e.g., JavaScript) to extend client functionality.

<br>

### **Structure of a REST API**

#### **Base URL**

- The entry point to the API.
  **Example:** https://api.example.com

#### **Endpoints**

- Paths to access specific resources.
  **Example:** /users, /products/123

#### **HTTP Methods**

- Used to define the type of operation to perform:
  **GET:** Retrieve data.
  **POST:** Create new data.
  **PUT:** Update existing data (entire resource).
  **PATCH:** Update part of a resource.
  **DELETE:** Remove data.

#### **Headers**

- Additional information sent with requests.

**Examples:**

- **Content-Type:** Format of the data (e.g., JSON, XML).
- **Authorization:** Token for authentication.

#### **Request Body**

- Data sent with requests like POST, PUT, or PATCH.
  **Example (JSON):**

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

#### **Response**

- The data returned by the API.
- Typically in JSON format.

**Example response for GET /users/1:**

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

<br>

### **How REST APIs Work**

#### **Request:**

- A client sends an HTTP request to the API endpoint.
- Includes method, headers, and optionally a body.

#### **Processing:**

- The server receives the request, processes it, and performs the requested action (e.g., fetching, creating, or updating data).

#### **Response:**

- The server sends back a response to the client.
- Contains status code, headers, and optionally a body.
  <br>

###Example REST API Workflow\*\*

#### **Client Request:**

```http
POST /users HTTP/1.1
Host: api.example.com
Content-Type: application/json


{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

#### **Server Response:**

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### **REST API Status Codes**

- **2xx Success:** The request was successful.
- **200 OK:** Successful GET or PUT.
- **201 Created:** Resource was successfully created.
- **4xx Client Errors:** Issues with the request.
- **400 Bad Request:** Malformed request syntax.
- **401 Unauthorized:** Authentication is required.
- **404 Not Found:** Resource not found.
- **5xx Server Errors:** Issues on the server.
- **500 Internal Server Error:** Generic server error.

<br>

### **Advantages of REST APIs**

- **Scalable:** Stateless nature makes it easier to scale.
- **Flexible:** Can handle multiple types of calls and data formats.
- **Interoperable:** Works over HTTP, making it accessible across platforms.

<br>

## \*\*Resources in REST API:

In a REST API, resources are the key entities or objects that the API exposes and operates on. Each resource represents a specific piece of data or collection of data, such as users, products, or orders. They are typically identified by URLs (endpoints).

### **Key Points:**

- **Representation:** Resources can be represented in formats like JSON or XML.
- **Operations:** Resources are acted upon using HTTP methods:
  - **GET:** Retrieve a resource.
  - **POST:** Create a resource.
  - **PUT/PATCH:** Update a resource.
  - **DELETE:** Remove a resource.

### **Examples of Resources:**

- /users (collection of all users)
- /users/123 (a single user with ID 123)
- /products/456/reviews (reviews of a product with ID 456)
- Nouns, Not Verbs: Resources are typically named using nouns, not verbs, e.g., /orders instead of /createOrder.

---

<br>
<br>

## **Path Operations in FastAPI**

In **FastAPI**, **path operations** are the **core building blocks** of an API — they define how your application responds to different HTTP requests (like `GET`, `POST`, `PUT`, `DELETE`, etc.) sent to specific **URL paths**. In other words, a **path operation** is the combination of:
✅ an **HTTP method** (operation) → e.g., `GET`, `POST`, `PUT`, `DELETE`
✅ and a **path (URL)** → e.g., `/items`, `/users/{id}`

<br>
<br>

### 🔹 Definition

A **path operation** is simply a function (called a _path operation function_) that handles a specific route and HTTP method.

In FastAPI:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
def get_items():
    return {"message": "List of items"}
```

Here:

- `@app.get("/items")` → defines a **path operation**
- `"GET"` → HTTP method
- `"/items"` → path
- `get_items()` → function that executes when this route is called

<br>
<br>

### 🔹 Common Path Operation Decorators

| HTTP Method | FastAPI Decorator      | Typical Use                    |
| ----------- | ---------------------- | ------------------------------ |
| `GET`       | `@app.get("/path")`    | Retrieve data                  |
| `POST`      | `@app.post("/path")`   | Create new data                |
| `PUT`       | `@app.put("/path")`    | Update existing data (replace) |
| `PATCH`     | `@app.patch("/path")`  | Partially update existing data |
| `DELETE`    | `@app.delete("/path")` | Delete data                    |

<br>
<br>

### 🔹 Path Parameters

You can include **dynamic values** in paths:

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

- `{item_id}` is a **path parameter**
- `item_id: int` → FastAPI automatically validates and converts it to an integer

---

### 🔹 Query Parameters

Query parameters are handled automatically:

```python
@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

Accessed as → `/items/?skip=10&limit=50`

<br>
<br>

### 🔹 Combining Both

```python
@app.get("/users/{user_id}/orders")
def read_user_orders(user_id: int, q: str | None = None):
    return {"user_id": user_id, "query": q}
```

- `user_id` → path parameter (mandatory)
- `q` → query parameter (optional)

<br>
<br>

### 🔹 Request Body with `POST` or `PUT`

When sending JSON data:

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price}
```

FastAPI automatically:

- Parses the JSON body
- Validates it using Pydantic
- Converts it into a Python object

<br>
<br>

### 🔹 Summary

| Concept              | Description                 | Example                      |
| -------------------- | --------------------------- | ---------------------------- |
| **Path**             | URL endpoint                | `/items/{id}`                |
| **Operation**        | HTTP method                 | `GET`, `POST`, etc.          |
| **Path Operation**   | Combination of both         | `@app.get("/items/{id}")`    |
| **Handler Function** | Executes for that operation | `def get_item(id: int): ...` |

<br>
<br>

---

<br>
<br>

## **FastAPI POST Request**

```python
from fastapi import FastAPI, Body
```

- **`from fastapi import FastAPI, Body`**
  - Imports `FastAPI` to create the application instance.
  - Imports `Body` to explicitly define request body parameters.

```python
app = FastAPI()
```

- **`app = FastAPI()`**
  - Creates an instance of the FastAPI class, which will be used to define routes and handle API requests.

```python
@app.post("/submit/")
```

- **`@app.post("/submit/")`**
  - Registers a route that listens for **POST** requests at the `"/submit/"` endpoint.
  - When a `POST` request is made to this endpoint, the corresponding function `submit_data` will be executed.

```python
def submit_data(data: dict = Body(...)):
```

- **`def submit_data(data: dict = Body(...)):`**

  - Defines a function `submit_data` that accepts a request body.
  - **`data: dict`** specifies that the function expects a dictionary as input.
  - **`Body(...)`** explicitly declares `data` as part of the request body.
  - Body(...) automatically converts the incoming JSON data from the request body into a Python dictionary (or a Pydantic model, if you specify one).

  - The **`...`** inside `Body(...)` means the request body is **required**, and FastAPI will return an error if it is missing.

```python
return {"message": "Received data", "data": data}
```

- **`return {"message": "Received data", "data": data}`**
  - Returns a JSON response containing:
    - A success message.
    - The received data as part of the response.
  - FastAPI automatically converts the returned Python dictionary into a valid JSON response.

### **Expected JSON Response**

```json
{
  "message": "Received data",
  "data": {
    "name": "John",
    "age": 30
  }
}
```

---

## **Summary**

| Line                                                | Explanation                                      |
| --------------------------------------------------- | ------------------------------------------------ |
| `from fastapi import FastAPI, Body`                 | Imports FastAPI and Body for request handling.   |
| `app = FastAPI()`                                   | Creates the FastAPI application instance.        |
| `@app.post("/submit/")`                             | Defines a POST endpoint `/submit/`.              |
| `def submit_data(data: dict = Body(...)):`          | Function accepting a dictionary as request body. |
| `return {"message": "Received data", "data": data}` | Returns received data in JSON format.            |

## **Handling POST Requests in FastAPI (All Variations)**

### **1. Handling Raw Request Body**

```python
from fastapi import FastAPI, Request
app = FastAPI()
@app.post("/submit/")
async def submit_data(request: Request):
    data = await request.json()
    return {"message": "Post request received", "data": data}
```

- Uses `Request` to access the raw request body.
- `await request.json()` asynchronously reads and parses the incoming JSON payload.
- Best used when the request structure is unknown or highly dynamic.

### **2. Handling JSON Data Using a Dictionary**

```python
from fastapi import FastAPI
app = FastAPI()
@app.post("/submit/")
async def submit_data(data: dict):
    return {"message": "Post request received", "data": data}
```

- The `data` parameter automatically converts incoming JSON into a Python dictionary.
- Easier to work with than raw body handling, as it provides direct access to structured data.

### **3. Handling JSON Data with `Body(...)`**

```python
from fastapi import FastAPI, Body
app = FastAPI()
@app.post("/submit/")
async def submit_data(data: dict = Body(...)):
    return {"message": "Post request received", "data": data}
```

- Similar to dictionary input but explicitly instructs FastAPI to extract the request body using `Body(...)`.
- Helps with documentation and API schema generation.

### **4. Handling Form Data**

```python
from fastapi import FastAPI, Form
app = FastAPI()
@app.post("/submit/")
async def submit_data(name: str = Form(...), age: int = Form(...)):
    return {"message": "Post request received", "name": name, "age": age}
```

- Uses `Form` to handle `application/x-www-form-urlencoded` data (common for web forms).
- Automatically parses and validates form fields.

### **5. Handling File Uploads**

```python
from fastapi import FastAPI, File, UploadFile
app = FastAPI()
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
```

- Uses `UploadFile` for efficient handling of uploaded files.
- `File(...)` ensures FastAPI correctly interprets the request as `multipart/form-data`.

### **6. Handling Query Parameters in POST Requests**

```python
from fastapi import FastAPI
app = FastAPI()
@app.post("/submit/")
async def submit_data(name: str, age: int):
    return {"message": "Post request received", "name": name, "age": age}
```

- Extracts parameters from the request URL query string, even in a POST request.
- Useful when sending optional or additional metadata.

### **Expected JSON Response**

```json
{ "message": "Post request received", "data": { "name": "John", "age": 30 } }
```

### **Summary of Variations**

| Method                          | Description                                                                                        |
| ------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Raw Request Body**            | Uses `Request` to manually extract JSON data. Useful for dynamic payloads.                         |
| **Dictionary Input**            | Directly accepts JSON data as a dictionary (`data: dict`). More structured than raw body handling. |
| **Dictionary with `Body(...)`** | Explicitly tells FastAPI to extract JSON from the request body, improving schema generation.       |
| **Form Data**                   | Uses `Form` to handle `application/x-www-form-urlencoded` data from web forms.                     |
| **File Uploads**                | Uses `UploadFile` to handle file uploads with `multipart/form-data`.                               |
| **Query Parameters in POST**    | Accepts parameters from the URL query string, useful for optional metadata.                        |

<br>

---

<br>

## 🔍 What is Pydantic in Python?

**Pydantic** is a powerful library for:

- Data **validation**
- Data **parsing**
- **Settings management**  
  All using **Python type hints**.

It’s commonly used with **FastAPI**, **SQLModel**, and other frameworks that rely on structured data input/output.

## ⚙️ Core Concepts

### **1. BaseModel**

BaseModel is the core class provided by the Pydantic library. All Pydantic models are subclasses of BaseModel.

When you inherit from BaseModel, you get:

- Automatic data validation

- Automatic type conversion (e.g., '123' to int)

- Helpful error messages if data is invalid

- Easy methods like .dict(), .json(), .copy(), etc.

- Support for default values and optional fields

You define a data structure using `BaseModel`:

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

user = User(id='1', name='Alice', email='alice@example.com')
print(user.id)  # Output: 1 (auto-converted str to int)
```

### **2. Optional Fields**

Use `Optional` from the `typing` module to mark fields as not required.

```python
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: Optional[str] = None  # This field is optional
```

If `email` is missing when creating a `User`, it's still valid.

### **3. Printing vs `.dict()`**

```python
user = User(id=1, name='Alice', email='alice@example.com')
print(user)
print(user.dict())
```

**Output:**

```python
# print(user)
id=1 name='Alice' email='alice@example.com'

# print(user.dict())
{'id': 1, 'name': 'Alice', 'email': 'alice@example.com'}
```

- `print(user)` shows a **string representation** with field values.
- `.dict()` returns a **real Python dictionary**, useful for JSON responses, DB insertions, etc.

### **4. Nested Models**

```python
class Address(BaseModel):
    city: str
    zip_code: int

class User(BaseModel):
    name: str
    address: Address

data = {
    "name": "Bob",
    "address": {
        "city": "New York",
        "zip_code": "10001"
    }
}

user = User(**data)
print(user.address.zip_code)  # Output: 10001 (converted to int)
```

### **5. Custom Validation**

```python
from pydantic import validator

class User(BaseModel):
    name: str

    @validator('name')
    def name_must_not_be_blank(cls, v):
        if not v.strip():
            raise ValueError('Name must not be blank')
        return v
```

1. **`User` class** → Inherits from `BaseModel` (Pydantic model used by FastAPI for validation).
2. **`name: str`** → Declares a required string field called `name`.
3. **`@validator('name')`** → Decorator that tells Pydantic to run this function to validate the `name` field.
4. **`def name_must_not_be_blank(cls, v):`**

   - `cls` → Reference to the model class (`User`).
   - `v` → The value provided for the `name` field.

5. **`if not v.strip():`** → Removes spaces and checks if the name is empty (e.g., `"   "`).
6. **`raise ValueError('Name must not be blank')`** → Raises an error if the field is empty or only whitespace.
7. **`return v`** → Returns the valid (non-empty) value to be stored in the model.

**In short:**
✅ Ensures the `name` field is **not empty or whitespace**.
✅ Automatically triggered during model creation or request validation in FastAPI.

## 🚀 Using Pydantic in FastAPI POST Request

### ✅ **Old way (using dict):**

```python
from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/createPost")
async def create_post(body_data: dict = Body(...)):
    return {
        "message": "Post successfully created",
        "post": {
            "title": body_data["title"],
            "content": body_data["content"]
        }
    }
```

This works, but **you lose** automatic validation, documentation, and type safety.

### ✅ **Recommended way (using Pydantic):**

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    author: Optional[str] = None  # Optional field

@app.post("/createPost")
async def create_post(post: Post):
    return {
        "message": "Post successfully created",
        "post": post.dict()  # Convert to dict if needed
    }
```

- In Pydantic with FastAPI, you don’t need to use = Body(...) when the parameter is a Pydantic model. FastAPI will automatically treat it as a request body.

**Benefits:**

- Automatic **validation**
- Built-in **error handling**
- Auto-generated **docs with OpenAPI**
- Cleaner code

<br>

---

<br>

## **CRUD Operations in FastAPI**

In **FastAPI**, CRUD operations—**Create, Read, Update, Delete**—are handled using HTTP methods: `POST`, `GET`, `PUT`/`PATCH`, and `DELETE`. Here's a simple example using an in-memory list to simulate a database.

### **Complete FastAPI CRUD Example**

## **FastAPI CRUD Example with Comments**

```python
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published:bool=True
    rating: Optional[int]=None

# saving posts in memory instead of DB
my_posts=[]




@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
async def get_posts():
    return {
        "message": "Your alll posts",
        "Posts":my_posts
        }

# ---function that takes a required JSON object from the request body,
#  turns it into a Python dictionary, and makes it available as body_data.
#
# ---Body(...) automatically converts the incoming JSON data from the request body into a Python dictionary
#  (or a Pydantic model, if you specify one).
#
# @app.post("/createPost")
# async def create_post(body_data:dict=Body(...)):
#     return {"message":"Post successfully created",
#             "post":{
#                 "title":body_data["title"],
#                 "content":body_data["content"]
#             }}

# ---in Pydantic with FastAPI, you don’t need to use = Body(...) when the parameter is a Pydantic model.
#  ---FastAPI will automatically treat it as a request body.
#
@app.post("/posts",status_code=status.HTTP_201_CREATED) #to change default status code just pass status code to decorator
async def create_post(post: Post):
    # print(type(new_post))
    # print(new_post)
    # print(new_post.dict())
    post_dict=post.dict()
    post_dict["id"]=1 if len(my_posts)==0 else my_posts[-1]["id"]+1
    my_posts.append(post_dict)
    return{
        "message":"Post successfully created",
        "Post":post_dict

        }


@app.get("/posts/{id}")
def get_post(id: int, response:Response):
    post = list(filter(lambda post: id == post["id"], my_posts))
    if not post:
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {
        #     "message": f"post with id: {id} not found"
        # }
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")

    return {
        "post": post
    }


@app.delete("/posts/{id}")
def delete_post(id:int, response:Response):

    ########ANOTHER WAY TO DELETE#############
    # # Find the index of the post
    # post_index = next((index for index, post in enumerate(my_posts) if post["id"] == id), None)

    # if post_index is None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")

    # # Delete the post
    # deleted_post = my_posts.pop(post_index)

    global my_posts
    # The keyword global is only needed when you reassign the entire variable, like this:
    # my_posts = [new list]  # <-- THIS is a reassignment.
    # But if you only modify the existing list, like .pop(), .append(), .remove(), .clear(), etc., you don't need global.

    no_of_posts=len(my_posts)
    my_posts=list(filter(lambda post: id!=post["id"], my_posts))
    if len(my_posts)==no_of_posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT) # when we delete something fastApi dont expect to send anything



# PUT replaces the entire resource (full update).
# PATCH updates only specific fields (partial update).
#
# Use PUT when you want to replace the whole object.
# Use PATCH when you want to modify only a part of the object.
#
# For PUT, send the full object (all fields) in the request body (usually JSON).
# For PATCH, Only the fields that need to be updated are passed. If a field is omitted, it is left unchanged.

# PUT request to update an entire post by id
@app.put("/posts/{id}")
def update_post(id: int, post_updates: Post):
    # Find the index of the post with matching id
    post_index = next((index for index, post in enumerate(my_posts) if post["id"] == id), None)

    # If post not found, raise 404 error
    if post_index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
    else:
        # Convert incoming Post model to dictionary
        post_dict = post_updates.dict()
        # Keep the original id (do not allow user to change it)
        post_dict["id"] = id
        # Replace the old post completely with new data
        my_posts[post_index] = post_dict
        # Return the updated post
        return {
            "updated post": post_dict
        }

# PATCH request to update specific fields of a post by id
@app.patch("/posts/{id}")
def patch_post(id: int, post_updates: Post):
    # Find the index of the post with matching id
    post_index = next((index for index, post in enumerate(my_posts) if post["id"] == id), None)

    # If post not found, raise 404 error
    if post_index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
    else:
        # Convert incoming Post model to dictionary
        post_dict = post_updates.dict(exclude_unset=True)  # ensures that fields not provided in the request retain their previous values (i.e., the default values or values that were already set before). These fields will be excluded from the update and will not be overwritten with the default values during the operation.


        # Update the existing post, keeping the original id and other data intact
        my_posts[post_index].update(post_dict)
        # Return the updated post
        return {
            "updated post": my_posts[post_index]
        }

```

### **Quick Summary**

| Operation | Method | Endpoint           | Description                  |
| --------- | ------ | ------------------ | ---------------------------- |
| Create    | POST   | `/items/`          | Add a new item               |
| Read All  | GET    | `/items/`          | Retrieve all items           |
| Read One  | GET    | `/items/{item_id}` | Retrieve a single item by ID |
| Update    | PUT    | `/items/{item_id}` | Fully update an item         |
| Patch     | PATCH  | `/items/{item_id}` | Partially update an item     |
| Delete    | DELETE | `/items/{item_id}` | Delete an item by ID         |

---

<br>

---

**1. How to change status code and default status code?**

Use `status_code` parameter inside the decorator:

```python
@app.delete("/posts/{id}", status_code=204)
```

This changes the default status code for that route.
Each HTTP method has its own default (e.g., `POST` is 201, `DELETE` is 204).

**2. Why pass `response: Response` to function?**

To manually modify the response properties like status code or headers inside your function.
Example:

```python
from fastapi import Response

def delete_post(id: int, response: Response):
    response.status_code = 204
```

**3. How `id: int` works?**

It tells FastAPI to:

- Extract `id` from URL path.
- Convert it to an `int` automatically.
- Validate it (if not an int, FastAPI returns a 422 error automatically).

**4. Path operation order matters?**

Yes, order matters.
Example:

```python
@app.get("/posts/{id}")
@app.get("/posts/special")
```

Here, `/posts/special` would not work correctly because `/posts/{id}` catches it first.
Always place static paths before dynamic paths.

**5. Does FastAPI send response automatically unlike Node.js?**

Yes, FastAPI automatically returns and sends the response when you `return` from the function.
In Node.js (e.g., Express), you must manually call `res.send()` or `res.json()`.

<br>

---

<br>

## **What Are Databases?**

A **database** is an organized collection of structured information or data that is stored electronically, typically in a computer system. It allows for efficient storage, retrieval, and manipulation of data.

- **Example:** A school database may contain tables like `Students`, `Courses`, and `Grades`.
- **Purpose:** Databases ensure data integrity, consistency, and quick access for applications and users.

## **What Is DBMS and How Is Database Interaction Done?**

### **DBMS (Database Management System):**

A **DBMS** is software that manages databases. It acts as an interface between the user (or application) and the database itself.

- **Functions of a DBMS:**
  - Data storage and retrieval
  - Ensuring data integrity and security
  - Handling concurrent access
  - Backup and recovery

### **Database Interaction Process:**

1. A user or application sends a **query** (typically written in SQL).
2. The **DBMS** processes this query.
3. The **DBMS** fetches or modifies data in the database and returns the result.

- **For developers**, this typically means using SQL queries in their applications.
- **For backend systems**, database drivers (like `psycopg2` for PostgreSQL in Python, or `pg` in Node.js) handle these interactions programmatically.

![img](https://photos.fife.usercontent.google.com/pw/AP1GczNQwklXWfexfh6u52R9fD76dTDgKRbecmq_rw_z4w6sMSOk66hen0s=w521-h232-no?authuser=0)

## **Relational vs NoSQL Databases**

| Feature             | **Relational Databases (RDBMS)**          | **NoSQL Databases**                              |
| ------------------- | ----------------------------------------- | ------------------------------------------------ |
| **Data Model**      | Tables with rows and columns (structured) | Key-Value, Document, Column, or Graph (flexible) |
| **Schema**          | Fixed schema                              | Schema-less or dynamic schema                    |
| **Query Language**  | SQL                                       | Varies (MongoDB uses JSON-like queries)          |
| **Examples**        | MySQL, PostgreSQL, Oracle                 | MongoDB, Cassandra, Redis                        |
| **Best Use Case**   | Structured data with relationships        | Unstructured/semi-structured data, scalability   |
| **ACID Compliance** | Strong                                    | Eventual consistency, but may trade off ACID     |

## **What Is SQL and How Does It Play a Role in DB Interaction?**

### **SQL (Structured Query Language):**

SQL is the standard language used to interact with relational databases.

- **Used For:**
  - Querying data: `SELECT * FROM users WHERE age > 25;`
  - Inserting data: `INSERT INTO users (name, age) VALUES ('Alice', 30);`
  - Updating data: `UPDATE users SET age = 31 WHERE name = 'Alice';`
  - Deleting data: `DELETE FROM users WHERE name = 'Alice';`
  - Defining schemas: `CREATE TABLE users (id INT, name TEXT);`

### **Role in DB Interaction:**

SQL commands are parsed and executed by the DBMS to perform operations like reading or modifying data.

![img](https://photos.fife.usercontent.google.com/pw/AP1GczNxDBBchFuSC6V5UNJqC79bTkqVvX61ckEltQWjQWKC9_m28lOJiOI=w1366-h610-s-no-gm?authuser=0)

## **What Is PostgreSQL and What Is a PostgreSQL Instance?**

### **PostgreSQL:**

PostgreSQL (often shortened to Postgres) is a powerful, open-source **relational database management system (RDBMS)** known for:

- Advanced SQL compliance
- Support for JSON, arrays, full-text search, etc.
- Extensibility and strong community
- ACID compliance and transactional support

### **PostgreSQL Instance:**

A **PostgreSQL instance** refers to a single running **PostgreSQL server process** on a machine. It includes:

- The **database engine** (handling queries, transactions)
- One or more **databases** (collections of schemas, tables, etc.)
- Configuration and runtime settings
- Background processes (autovacuum, WAL writer, etc.)

> Think of a PostgreSQL instance as the _running environment_ for one or more databases on a server.

![img](https://photos.fife.usercontent.google.com/pw/AP1GczNLvTjMQ7iQJ-PAl4T8mkugAqT1CwNDi_IrQiQ8zRopIB6WAr4sFBE=w1164-h641-s-no-gm?authuser=0)

<br>

---

<br>

## **PostgreSQL Core Concepts**

### **1. Tables**

A **table** is a collection of **rows** and **columns** in PostgreSQL used to store data.

**Syntax to create a table:**

```sql
CREATE TABLE table_name (
    column1 datatype constraints,
    column2 datatype constraints,
    ...
);
```

### **2. Columns**

**Columns** define the **schema** (structure) of the table. Each column has:

- A **name**
- A **data type**
- Optional **constraints**

**Example:**

```sql
name VARCHAR(100),
age INT,
created_at TIMESTAMP
```

### **3. Rows**

Each **row** is a record in the table containing values for each column.

**Example:**

```sql
INSERT INTO users (name, age) VALUES ('Alice', 30);
```

### **4. Data Types**

PostgreSQL supports a variety of data types, including:

#### **Numeric Types**

- `INT`, `INTEGER`, `SMALLINT`, `BIGINT`
- `NUMERIC(precision, scale)` — for exact decimals
- `REAL`, `DOUBLE PRECISION`

#### **Character Types**

- `CHAR(n)` – fixed length
- `VARCHAR(n)` – variable length
- `TEXT` – unlimited length

#### **Date/Time Types**

- `DATE`, `TIME`, `TIMESTAMP`, `INTERVAL`

#### **Boolean**

- `BOOLEAN` — `TRUE`, `FALSE`, or `NULL`

#### **Others**

- `UUID`, `BYTEA`, `JSON`, `ARRAY`, `ENUM`, `GEOMETRY` (with PostGIS)

### **5. Primary Key**

A **Primary Key** uniquely identifies each row in a table. It must be:

- **Unique**
- **NOT NULL**

**Syntax:**

```sql
CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,
    name TEXT
);
```

Or declared separately:

```sql
CREATE TABLE employees (
    emp_id SERIAL,
    name TEXT,
    PRIMARY KEY (emp_id)
);
```

### **6. Constraints**

Constraints define rules for data in columns:

| Constraint    | Description                                  |
| ------------- | -------------------------------------------- |
| `PRIMARY KEY` | Uniquely identifies each row                 |
| `UNIQUE`      | Ensures all values in a column are different |
| `NOT NULL`    | Prevents `NULL` values                       |
| `CHECK`       | Ensures values meet a condition              |
| `DEFAULT`     | Sets a default value                         |
| `FOREIGN KEY` | Enforces link between tables                 |

**Example:**

```sql
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price NUMERIC CHECK (price > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

<br>

---

<br>

## 📂 Database Creation

```sql
-- Create a new database
CREATE DATABASE company_db;
```

## 📋 Table Creation

```sql
-- Connect to the database first: \c company_db
-- Create a table named employees
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary NUMERIC(10, 2),
    joined_on DATE
);
```

## ➕ Inserting Rows

### Insert a **single row**:

```sql
INSERT INTO employees (name, department, salary, joined_on)
VALUES ('Alice Johnson', 'Engineering', 75000.00, '2022-06-15');
```

### Insert **multiple rows**:

```sql
INSERT INTO employees (name, department, salary, joined_on)
VALUES
  ('Bob Smith', 'HR', 55000.00, '2023-01-12'),
  ('Cathy Adams', 'Engineering', 80000.00, '2021-11-03');
```

## 🔍 Selecting Data

```sql
-- Select all columns
SELECT * FROM employees;

-- Select specific columns
SELECT name, salary FROM employees;
```

## 🎯 Filtering with WHERE

```sql
SELECT * FROM employees
WHERE department = 'Engineering';

SELECT * FROM employees
WHERE salary > 60000;
```

## 🔣 SQL Operators

- `=`, `!=`, `<`, `>`, `<=`, `>=`
- `AND`, `OR`, `NOT`

```sql
SELECT * FROM employees
WHERE department = 'Engineering' AND salary > 70000;
```

## 🔘 IN Operator

```sql
SELECT * FROM employees
WHERE department IN ('Engineering', 'HR');
```

## 🔍 Pattern Matching with LIKE

- `%` = any number of characters
- `_` = exactly one character

```sql
SELECT * FROM employees
WHERE name LIKE 'A%';  -- names starting with A

SELECT * FROM employees
WHERE name LIKE '%son';  -- names ending with 'son'
```

## 📊 Sorting with ORDER BY

```sql
SELECT * FROM employees
ORDER BY salary DESC;  -- descending order

SELECT * FROM employees
ORDER BY joined_on ASC;
```

## 🎛️ LIMIT and OFFSET

```sql
SELECT * FROM employees
ORDER BY salary DESC
LIMIT 5;  -- top 5 highest paid

SELECT * FROM employees
ORDER BY id
LIMIT 5 OFFSET 5;  -- skip first 5, fetch next 5
```

## 🛠️ Update Records

```sql
-- Update salary and return updated row
UPDATE employees
SET salary = salary + 5000
WHERE name = 'Alice Johnson'
RETURNING *;
```

## ❌ Delete Records

```sql
-- Delete a record and return it
DELETE FROM employees
WHERE name = 'Bob Smith'
RETURNING *;
```

## ✅ Get Records Back Using RETURNING

- Works with `INSERT`, `UPDATE`, and `DELETE`

### Insert + RETURNING:

```sql
INSERT INTO employees (name, department, salary, joined_on)
VALUES ('David Warner', 'Sales', 62000.00, '2023-04-01')
RETURNING *;
```

### Update + RETURNING:

```sql
UPDATE employees
SET department = 'Marketing'
WHERE name = 'Cathy Adams'
RETURNING *;
```

### Delete + RETURNING:

```sql
DELETE FROM employees
WHERE name = 'David Warner'
RETURNING *;
```

<br>

---

<br>

## **psycopg2 Overview**

**`psycopg2`** is a popular PostgreSQL adapter for the Python programming language. It allows your Python programs to connect to and interact with a PostgreSQL database.

### **Key Features of psycopg2:**

- **DB-API 2.0 Compliant**: It follows Python’s standard database API specification (PEP 249).
- **Thread-safe and efficient**: It is designed for multi-threaded applications and performs well under concurrent database access.
- **Support for advanced PostgreSQL features**: Includes server-side cursors, COPY command, asynchronous notifications, large objects, etc.

### **Basic Usage Example**

```python
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="your_db",
    user="your_user",
    password="your_password",
    host="localhost",
    port="5432"
)

# Create a cursor object
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM your_table")

# Fetch results
rows = cur.fetchall()
for row in rows:
    print(row)

# Clean up
cur.close()
conn.close()
```

### **Installation**

```bash
pip install psycopg2-binary
```

> Use `psycopg2-binary` for simpler installation. Use `psycopg2` if you want to compile from source (more control, fewer compatibility issues in production environments).

<br>

## **psycopg3 vs psycopg2**

**`psycopg3`** is the modern successor to `psycopg2`, redesigned with flexibility, modern Python practices, and performance in mind. Here's a breakdown of the key differences:

### **1. Modern Python Compatibility**

- **psycopg3**: Fully compatible with Python 3.7+ and supports modern features like `async`/`await`, context managers, and type hints.
- **psycopg2**: Older design; lacks built-in async support and modern syntax.

### **2. Asynchronous Support**

- **psycopg3**: Natively supports asynchronous programming using `asyncpg`-style APIs.

```python
import asyncio
import psycopg

async def main():
    async with await psycopg.AsyncConnection.connect("dbname=test user=postgres") as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM my_table")
            rows = await cur.fetchall()
            print(rows)

asyncio.run(main())
```

- **psycopg2**: No native async support (requires workarounds like `psycopg2` + `gevent`).

### **3. Better Typing and Adaptation**

- **psycopg3**: Allows custom data types and better type adaptation using `Python <-> PostgreSQL` mapping.
- **psycopg2**: More rigid type handling, less extensible.

### **4. Prepared Statements**

- **psycopg3**: Offers efficient, explicit support for prepared statements and server-side cursors.
- **psycopg2**: Limited, implicit support.

### **5. Installation and Distribution**

- **psycopg3**: Lightweight, pure Python base with optional C-accelerated components (`psycopg[binary]`).
- **psycopg2**: Installation issues common due to binary dependencies; `psycopg2-binary` used to simplify.

### **6. Memory and Performance**

- **psycopg3**: More memory-efficient and designed with high-performance patterns (e.g., batch execution, pipeline mode).
- **psycopg2**: Still performant, but less flexible and less memory-efficient in modern async/multi-core workloads.

<br>

---

<br>

## **PostgreSQL Database Connection Using psycopg2 (Explained)**

This Python script attempts to establish a **resilient connection** to a PostgreSQL database using `psycopg2`. It includes retry logic to keep trying until the connection is successful.

```python
import psycopg2
from psycopg2.extras import RealDictCursor
import time


while True:
    try:
        conn = psycopg2.connect(
          dbname="your_db",
          user="your_user",
          password="your_password",
          host="localhost",
          port="5432"
        )
        cursor=conn.cursor()
        print("Databaase connection was successfull")
        print("connection: ", conn)

        break

    except Exception as err:
        print("Databaase connection failed")
        print("error: ", err)
        time.sleep(2)
```

### **📦 Imports**

```python
import psycopg2
from psycopg2.extras import RealDictCursor
import time
```

- `psycopg2`: Main PostgreSQL adapter for Python.
- `RealDictCursor`: Returns rows as Python dictionaries (with column names as keys).
- `time`: Adds delay between retries on failure.

### **🔁 Connection Retry Loop**

```python
while True:
```

- Infinite loop that keeps trying to connect until successful.

### **🔌 Establishing the Connection**

```python
conn = psycopg2.connect(
    host="localhost",
    database="fastapi",
    user="<username>",
    password="<password>",
    cursor_factory=RealDictCursor
)
```

- **host**: PostgreSQL server location (local machine).
- **database**: Name of the database ("fastapi").
- **user/password**: Credentials for authentication.
- **cursor_factory**: Specifies that results should be returned as dictionaries instead of tuples for better readability and JSON compatibility.

### **🧠 Create a Cursor Object**

```python
cursor = conn.cursor()
```

- A cursor is a control structure used to interact with the PostgreSQL database through SQL commands.

- It allows you to execute queries, fetch results, and manage transactions.

- In this case, because we used RealDictCursor, the cursor returns query results as dictionaries — with column names as keys and row values as dictionary values.

- This makes it easier to work with structured data, especially when returning results as JSON in web applications (e.g., FastAPI).

### **🟢 Success Feedback**

```python
print("Database connection was successful")
print("connection: ", conn)
```

- Confirms successful connection and prints the connection object.

### **❌ Error Handling and Retry**

```python
except Exception as err:
    print("Database connection failed")
    print("error: ", err)
    time.sleep(2)
```

- Catches any exceptions during connection attempt.
- Prints error message and retries after a 2-second delay.
- Useful in environments like Docker where the database might take time to initialize.

<br>

---

<br>

## **CRUD Operations with FastAPI & Psycopg2**

### **1. Setup and Database Connection**

```python
# Import necessary modules
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from pprint import pprint

# Initialize FastAPI app
app = FastAPI()

# Define Pydantic model for post data validation
class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # default value True
```

```python
# Establish a PostgreSQL connection using psycopg2 with retry logic
while True:
    try:
        conn = psycopg2.connect(
        host="localhost",
        database="fastapi",
        user="<username>",
        password="<password>",
        cursor_factory=RealDictCursor
      )
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as err:
        print("Database connection failed")
        print("Error:", err)
        time.sleep(2)  # Retry after 2 seconds
```

<br>

### **2. Read All Posts (GET `/posts`)**

```python
@app.get("/posts")
async def get_posts():
    # Fetch all rows from the 'posts' table
    cursor.execute('SELECT * FROM posts')
    posts = cursor.fetchall()

    # Return posts in JSON format
    return {
        "message": "All your posts",
        "Posts": posts
    }
```

<br>

### **3. Create a New Post (POST `/posts`)**

```python
@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    # Insert new post and return the inserted row using RETURNING *
    cursor.execute('''
        INSERT INTO posts (title, content, published)
        VALUES (%s, %s, %s)
        RETURNING *
    ''', (post.title, post.content, post.published))

    new_post = cursor.fetchone()
    conn.commit()  # Commit the transaction to save changes

    return {
        "message": "Post successfully created",
        "Post": new_post
    }
```

### Why parameterize data (`%s`, values in tuple) — Prevent SQL Injection

- **Without parameterization**, if you directly insert user input into SQL strings (e.g., using string concatenation or f-strings), a malicious user could inject SQL commands into the input.

  ```python
  # ❌ Vulnerable example
  cursor.execute(f"UPDATE posts SET title='{title}' WHERE id={id}")
  ```

  If `title` = `"Hacked', published = TRUE; DROP TABLE posts; --"`, it could **delete your entire table**.

- **With parameterization**, you safely separate **SQL logic** from **user data**:

  ```python
  cursor.execute("UPDATE posts SET title=%s WHERE id=%s", (title, id))
  ```

  Here:

  - The database driver sends the SQL and parameters **separately** to the database engine.
  - The engine treats the parameters purely as **data**, not executable SQL.
  - ✅ Prevents SQL injection automatically.

So, parameterization = **secure binding of values** to placeholders (`%s`) inside the query.

<br>

### **4. Read a Single Post by ID (GET `/posts/{id}`)**

```python
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    # Query a specific post by ID
    cursor.execute('SELECT * FROM posts WHERE id = %s', (str(id),))
    post = cursor.fetchone()

    # If no post is found, raise 404 error
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} not found"
        )

    return {"post": post}
```

<br>

### **5. Delete a Post by ID (DELETE `/posts/{id}`)**

```python
@app.delete("/posts/{id}")
def delete_post(id: int, response: Response):
    # Delete the post with the given ID
    cursor.execute('DELETE FROM posts WHERE id = %s RETURNING *', (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()  # Apply the deletion

    # If no post was deleted, return 404
    if deleted_post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} not found"
        )

    # Return 204 No Content (deletion successful)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
```

> **Note:** You had a bug:

```python
if delete_post == None:  # Incorrect
```

It should be:

```python
if deleted_post is None:
```

<br>

### **6. Update a Post by ID (PUT `/posts/{id}`)**

```python
@app.put("/posts/{id}")
def update_post(id: int, post_updates: Post):
    # Update a post by ID with new data
    cursor.execute('''
        UPDATE posts
        SET title = %s, content = %s, published = %s
        WHERE id = %s
        RETURNING *
    ''', (post_updates.title, post_updates.content, post_updates.published, str(id)))

    updated_post = cursor.fetchone()
    conn.commit()

    # If no post was updated, return 404
    if updated_post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} not found"
        )

    return {"updated post": updated_post}
```

<br>

---

<br>

## **What is ORM?**

**ORM (Object-Relational Mapping)** is a programming technique used to convert data between incompatible type systems in object-oriented programming languages and relational databases. It allows you to interact with the database using Python classes and objects instead of writing raw SQL queries.

## **Advantages of ORM**

1. **Abstraction of SQL**: You don't need to write raw SQL queries; instead, you use class methods and attributes.
2. **Code Readability**: Code becomes cleaner and easier to understand with models representing tables.
3. **Reusability & DRY Principle**: ORM encourages the reuse of code through models and relationships.
4. **Security**: Reduces risk of SQL injection since queries are auto-generated safely.
5. **Cross-Database Compatibility**: ORMs often support multiple database backends (e.g., PostgreSQL, MySQL, SQLite) with minimal configuration change.
6. **Productivity**: Reduces boilerplate and speeds up development.
7. **Maintainability**: Schema changes are easier to manage via migrations.
8. **Relationships Handling**: Built-in support for handling relationships like One-to-Many, Many-to-Many.

## **How FastAPI interacts with database using ORM**

FastAPI commonly uses **SQLAlchemy** (a powerful ORM) with **Pydantic models** for request and response validation. Here’s a step-by-step overview of interaction:

### **1. Define Database Models using SQLAlchemy (ORM layer)**

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
```

### **2. Create Pydantic Schemas (for request/response validation)**

```python
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class UserRead(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True  # Enables compatibility with ORM models
```

### **3. Set up a Database Session**

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

### **4. Dependency Injection in FastAPI Route**

```python
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

<br>

---

<br>

## **SQLAlchemy ORM Setup**

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL='postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'

engine=create_engine(SQLALCHEMY_DATABASE_URL)

sessionlocal=sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base=declarative_base()
```

<br>

```python
from sqlalchemy import create_engine
```

- **What it does:** Imports the `create_engine` function from SQLAlchemy.
- **Why it’s needed:** This function creates an **engine**, which is the core interface to your database. It manages the database connections and is essential for interacting with the database.

<br>

```python
from sqlalchemy.ext.declarative import declarative_base
```

- **What it does:** Imports the `declarative_base` function.
- **Why it’s needed:** It returns a base class for your ORM models. All models (i.e., classes representing tables) should inherit from this base class so that SQLAlchemy can keep track of them.

---

```python
from sqlalchemy.orm import sessionmaker
```

- **What it does:** Imports the `sessionmaker` factory.
- **Why it’s needed:** This factory is used to create new session objects. A session is how SQLAlchemy manages database transactions and operations.

<br>

```python
SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'
```

- **What it does:** Defines the connection URL to the PostgreSQL database.
- **Why it’s needed:** SQLAlchemy uses this string to connect to the correct database. It follows the pattern:

  ```
  dialect+driver://username:password@host:port/database
  ```

  - `postgresql`: Database dialect
  - `<username>` / `<password>`: Your credentials
  - `<ip-address/hostname>`: Server address
  - `<database_name>`: Target database

<br>

```python
engine = create_engine(SQLALCHEMY_DATABASE_URL)
```

- **What it does:** Creates the SQLAlchemy **engine** using the connection URL.
- **Why it’s needed:** The engine manages the connection pool and handles the actual interaction with the database backend.

<br>

```python
sessionlocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
```

- **What it does:** Creates a **configured session class**.
- **Why it’s needed:**

  - `autoflush=False`: Changes are not auto-pushed to the DB until you commit or flush explicitly.
  - `autocommit=False`: Manual control over commits; changes won’t persist unless committed.
  - `bind=engine`: Connects the session to the engine so it knows what DB to interact with.

- **How it’s used:** You’ll later use `db = sessionlocal()` to create a session for querying and persisting data.

<br>

```python
Base = declarative_base()
```

- **What it does:** Creates a base class for defining models.
- **Why it’s needed:** Every ORM class (representing a table) will inherit from `Base`. This enables SQLAlchemy to map the classes to actual tables and manage their metadata.

- It’s the starting point for creating ORM models in SQLAlchemy.

- It acts like a blueprint maker — you use it to define your database tables as Python classes.

<br>

---

<br>

## **Understanding Engine and Session in SQLAlchemy ORM with FastAPI**

### 🔧 **What is an Engine?**

The **engine** is the **bridge between your Python code and the database**.

- It handles the **connection** to your database (like SQLite, PostgreSQL, etc.)
- It uses a **database URL** to connect
- It powers all the communication with the database under the hood

**Example:**

```python
from sqlalchemy import create_engine

engine = create_engine("sqlite:///./mydb.db", echo=True)
```

Think of the engine as the **car engine** — it powers everything behind the scenes.

<br>

### 📦 **What is a Session?**

A **session** is how you **talk to the database** to run commands.

- You use it to **add**, **update**, **delete**, and **query** data
- It's like a **temporary conversation** with the database
- You typically **open** a session, **do your work**, then **commit** or **close** it

**Example:**

```python
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

user = db.query(User).filter(User.id == 1).first()
```

Think of the session as a **messenger** — it carries your instructions to the database and brings results back.

<br>

### 🧩 **How Engine and Session Work in FastAPI**

In FastAPI, you usually:

- Create the **engine once** at app startup
- Use a **new session per request**

**Example setup:**

```python
# Create the engine
engine = create_engine("sqlite:///./mydb.db")
SessionLocal = sessionmaker(bind=engine)

# Dependency to get DB session in FastAPI
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

**Use in route:**

```python
from sqlalchemy.orm import Session

@app.get("/users")
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()
```

<br>

### ✅ **Summary**

| Concept     | Meaning                          |
| ----------- | -------------------------------- |
| **Engine**  | Connects to the database         |
| **Session** | Reads/writes data via the engine |

<br>

---

<br>

## Step-by-step Setup of SQLAlchemy ORM with FastAPI and PostgreSQL

### 1. Install Required Packages

```bash
pip install fastapi sqlalchemy psycopg2-binary uvicorn
```

- `sqlalchemy`: ORM library
- `psycopg2-binary`: PostgreSQL adapter
- `fastapi`: Web framework
- `uvicorn`: ASGI server

<br>

### 2. Define Your Database URL

Inside a file like `core/config.py`:

```python
DATABASE_URL = "postgresql://username:password@localhost:5432/dbname"
```

Replace with your actual PostgreSQL credentials and details.

<br>

### 3. Create SQLAlchemy Engine and Session

In `db/session.py`:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
```

- `engine`: connects to the database
- `SessionLocal`: creates sessions
- `Base`: base class for models

<br>

### 4. Create a Model

In `models/user.py`:

```python
from sqlalchemy import Column, Integer, String
from db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
```

<br>

### 5. Create the Database Tables on App Startup

In `db/init_db.py`:

```python
from db.session import engine, Base
from models import user  # ensure all models are imported

def create_tables():
    Base.metadata.create_all(bind=engine)
```

In `main.py`:

```python
from fastapi import FastAPI
from db.init_db import create_tables

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_tables()
```

<br>

### 6. Create a Dependency for DB Session

In `db/deps.py`:

```python
from db.session import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

In your route (e.g. `routers/user_routes.py`):

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.deps import get_db
from models.user import User

router = APIRouter()

@router.get("/users")
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()
```

<br>

### 7. Folder Structure (Recommended)

```
project/
│
├── main.py
├── core/
│   └── config.py
├── db/
│   ├── session.py
│   ├── deps.py
│   └── init_db.py
├── models/
│   └── user.py
├── routers/
│   └── user_routes.py
```

<br>

### ✅ Summary of the Order

1. Configure `DATABASE_URL`
2. Set up `engine`, `SessionLocal`, and `Base`
3. Create your models inheriting from `Base`
4. Create `init_db.py` to create tables using `Base.metadata.create_all`
5. Add FastAPI `startup` event to trigger table creation
6. Set up a dependency function (`get_db`) for DB session injection
7. Use `Depends(get_db)` in your API routes

<br>

---

<br>

## **Understanding `get_db` with `Depends` and `yield` in FastAPI**

### **Concepts Involved**

**✅ `Depends`**

- FastAPI uses `Depends()` to **inject dependencies** into your path operations or functions.
- It’s a way to **automatically provide inputs**, like database sessions, auth checks, etc., to your routes.

**✅ `yield` in Dependencies**

- `yield` is used in dependencies to manage **setup and teardown logic**.
- What comes **before** `yield` is **setup** (like opening a DB session).
- What comes **after** `yield` is **teardown/finalization** (like closing the DB session).

### **Function Explained: `get_db`**

```python
def get_db():
    db = SessionLocal()         # Setup: Create a new database session
    try:
        yield db               # Yield: Provide the session to the request
    finally:
        db.close()            # Teardown: Close the session after the request is done
```

**What it does:**

- **Creates a DB session** using `SessionLocal()`.
- **Yields** that session so the path operation function can use it.
- **Closes** the session automatically when the request is done (even if there’s an exception).

### **Using with Depends:**

```python
@app.get("/items/")
def read_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return items
```

**How it works:**

1. **FastAPI sees `Depends(get_db)`**, so it calls the `get_db()` generator.
2. It gets the `db` session **from `yield db`**.
3. It **passes `db` to the `read_items` function**.
4. When the function returns or the request ends, FastAPI runs the **`finally: db.close()`** block to **clean up**.

### **Analogy**

Imagine `get_db` is like handing someone a rental car (`db`) with:

- **Setup:** Give them the car keys (`yield db`)
- **Teardown:** Automatically take back and park the car after the ride (`finally: db.close()`)

<br>

---

<br>

## **Understanding `models.Base.metadata.create_all(bind=engine)` in SQLAlchemy**

### **1. `models.Base.metadata`**

- `Base` is typically created with:

  ```python
  from sqlalchemy.orm import declarative_base
  Base = declarative_base()
  ```

- `Base.metadata` is a **MetaData** object that holds a catalog of all the table definitions created using the ORM.

- Any model class inheriting from `Base` automatically gets its table registered in this `metadata` object.

<br>

### **2. `.create_all(bind=engine)`**

- Tells SQLAlchemy to **create all tables** defined in `Base.metadata` **in the database**.
- Uses the given `engine` (a DB connection object) to execute the DDL statements.

<br>

### **What Happens Internally**

1. **Table Discovery**:

   - SQLAlchemy finds all table definitions registered in `Base.metadata.tables`.

2. **Existence Check**:

   - It checks if each table already exists in the connected database.

3. **DDL Generation**:

   - For tables that don’t exist, SQLAlchemy generates `CREATE TABLE` SQL statements.

4. **Execution**:

   - It sends these DDL statements to the database engine and creates the missing tables.

<br>

### **Important Notes**

- **Does NOT drop or modify** existing tables — only creates missing ones.
- Useful for **initial schema setup** in development or testing.
- For **schema migrations** (changing table structures), use a tool like **Alembic**.

<br>

### **Example**

Suppose you define this model:

```python
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
```

When you call:

```python
Base.metadata.create_all(bind=engine)
```

SQLAlchemy internally:

- Checks if `users` table exists.
- If not, runs something like:

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR
);
```

<br>

- `create_all()` is a declarative way to sync ORM models with the database.
- Best used in **non-production** environments.
- Behind the scenes, it maps Python class definitions to SQL `CREATE TABLE` commands.

<br>

---

<br>

## **Understanding SQLAlchemy `db.query()`, `.delete()`, and `.update()`**

### **1. What Does `db.query()` Return?**

```python
post = db.query(models.Post).filter(models.Post.id == id)
```

- This returns a **`Query` object**, not the actual data.
- It is a **lazy query**: it does not execute until you explicitly request the result.

#### ✅ To Execute the Query:

- `.all()` → Fetches all matching records as a list
- `.first()` → Returns the first matched record
- `.one()` / `.one_or_none()` → For exactly one result
- `.scalar()` → For a single value

```python
post_list = db.query(models.Post).filter(...).all()   # Returns a list
post_obj = db.query(models.Post).filter(...).first()  # Returns a single record
```

<br>

### **2. How `.delete()` Works on a Query Object**

```python
post.delete(synchronize_session=False)
```

- This **deletes rows directly from the database** based on the filter condition.
- It executes a SQL like:

```sql
DELETE FROM posts WHERE id = ...
```

#### ✅ Notes:

- You **don’t need to fetch** the rows before deleting.
- It is a **bulk delete operation**.

#### ✅ synchronize_session Options:

- `False`: No session sync (fast, best for large deletes)
- `'evaluate'`: Tries to match in-memory ORM objects using filter conditions
- `'fetch'`: Fetches rows to sync with session

<br>

### **3. How `.update()` Works on a Query Object**

```python
post_query.update(post_updates.dict(), synchronize_session=False)
```

- This executes a SQL `UPDATE` on the matching rows.
- You update **without fetching** the rows first.

#### ✅ Example:

```python
post_query = db.query(models.Post).filter(models.Post.id == id)
post_query.update({"title": "New Title"}, synchronize_session=False)
```

- Executes SQL like:

```sql
UPDATE posts SET title = 'New Title' WHERE id = ...
```

#### ✅ synchronize_session Options:

Same as `.delete()` — it controls how SQLAlchemy syncs the in-memory session with the DB changes.

<br>

| Operation                   | Description                                          |
| --------------------------- | ---------------------------------------------------- |
| `db.query(Model)`           | Returns a lazy `Query` object                        |
| `.filter(...)`              | Adds WHERE clause to query                           |
| `.all()` / `.first()`       | Executes and returns result(s)                       |
| `.delete()`                 | Executes DELETE directly in DB                       |
| `.update({...})`            | Executes UPDATE directly in DB                       |
| `synchronize_session=False` | Skips syncing in-memory ORM with DB changes (faster) |

<br>

---

<br>

## **Understanding `synchronize_session` in SQLAlchemy**

### **What is `synchronize_session`?**

In SQLAlchemy, `synchronize_session` is a parameter used during **bulk update** and **delete** operations to determine how SQLAlchemy should sync the in-memory ORM session with changes made directly in the database.

SQLAlchemy tracks objects in memory, and if you change something directly in the DB using `.update()` or `.delete()`, the in-memory state can become stale or incorrect. `synchronize_session` helps manage this.

<br>

### **Why Synchronization Matters**

When you perform a bulk operation, SQLAlchemy bypasses the ORM and executes raw SQL like `UPDATE` or `DELETE`. The session still holds references to old data unless explicitly told how to handle them.

`Synchronize_session` tells SQLAlchemy:

- Whether to update the in-memory state
- How to find affected objects

<br>

### **Options for `synchronize_session`**

| Option       | Description                                          | Performance | Accuracy               | Use Case                                                |
| ------------ | ---------------------------------------------------- | ----------- | ---------------------- | ------------------------------------------------------- |
| `False`      | No synchronization. Session may have stale data.     | 🔥 Fastest  | ❌ Not synced          | When you don’t need ORM state afterward                 |
| `'evaluate'` | SQLAlchemy evaluates filter conditions in Python.    | ⚡ Fast     | ⚠️ Simple filters only | Use when filters are basic (e.g., column == value)      |
| `'fetch'`    | Performs a `SELECT` to fetch and sync affected rows. | 🐢 Slowest  | ✅ Safest              | Use when filter is complex or session must stay in sync |

<br>

### **Usage Examples**

#### `synchronize_session=False`

```python
db.query(User).filter(User.age < 18).delete(synchronize_session=False)
```

- Deletes users under 18 in the database
- Session may still hold stale `User` objects

#### `synchronize_session='evaluate'`

```python
db.query(User).filter(User.active == False).update({"banned": True}, synchronize_session='evaluate')
```

- SQLAlchemy tries to match and update ORM objects in memory
- Works only with simple filters

#### `synchronize_session='fetch'`

```python
db.query(User).filter(User.score < 50).update({"rank": "low"}, synchronize_session='fetch')
```

- Safely fetches and updates in-memory objects
- More accurate but slower due to extra SELECT

<br>

| synchronize_session | Speed      | Safety      | Recommended When                                  |
| ------------------- | ---------- | ----------- | ------------------------------------------------- |
| `False`             | 🚀 Fastest | ❌ Not safe | ORM objects aren’t reused afterward               |
| `'evaluate'`        | ⚡ Fast    | ⚠️ Limited  | Filters are simple Python-compatible expressions  |
| `'fetch'`           | 🐢 Slower  | ✅ Safest   | Filters are complex or ORM state must stay synced |

---

### ✅ Final Note

Use `False` for performance-critical tasks when you don’t care about session accuracy afterward. Use `'fetch'` when accuracy is more important than speed. Use `'evaluate'` when filters are simple and performance also matters.

<br>

---

<br>

## **`default` vs `server_default` in SQLAlchemy**

In SQLAlchemy, both `default` and `server_default` specify default values for model columns, but they operate in different contexts and serve different purposes.

<br>

### **Key Differences**

| Feature              | `default`                 | `server_default`                            |
| -------------------- | ------------------------- | ------------------------------------------- |
| **Applied By**       | Python/SQLAlchemy ORM     | Database engine                             |
| **Execution Timing** | Before insert (in Python) | At insert time (in DB)                      |
| **Schema Impact**    | No SQL schema change      | Adds DEFAULT clause to SQL table definition |
| **Usage**            | Python value or callable  | SQL expression via `text()` or `func()`     |

<br>

### **✅ `default`: Python-Side Defaults**

```python
from sqlalchemy import Column, String

class User(Base):
    __tablename__ = 'users'
    name = Column(String, default='anonymous')
```

- This sets a default value in the Python code only.
- The default value is applied when the object is created via SQLAlchemy.
- **Does not affect raw SQL or database-side inserts**.

<br>

### **✅ `server_default`: Database-Side Defaults**

```python
from sqlalchemy import Column, String, text

class User(Base):
    __tablename__ = 'users'
    name = Column(String, server_default=text("'anonymous'"))
```

- Adds a `DEFAULT 'anonymous'` clause to the table schema in the database.
- Ensures that default values are applied **even if the insert is done via raw SQL or another tool**.
- Required for full schema visibility and Alembic migrations.

<br>

### **Use Case Comparison**

| Scenario                       | Prefer `default` | Prefer `server_default` |
| ------------------------------ | ---------------- | ----------------------- |
| Pure SQLAlchemy ORM usage      | ✅               |                         |
| Raw SQL or external DB clients |                  | ✅                      |
| Using Alembic migrations       |                  | ✅                      |
| DB-side timestamp defaults     |                  | ✅                      |

<br>

### **Example with Timestamps**

```python
from sqlalchemy import Column, DateTime, func, text

# Python-side default
created_at = Column(DateTime, default=func.now())

# Database-side default
created_at_db = Column(DateTime, server_default=func.now())
```

- The Python-side default only works if the object is created through SQLAlchemy.
- The DB-side default works in all cases and is part of the actual table definition.

<br>

- Use `default` when you only insert using SQLAlchemy and don’t need database-side enforcement.
- Use `server_default` when you want the database to apply defaults reliably across all interfaces, or when working with Alembic migrations.

For consistent and reliable schema management, especially in production environments, **`server_default` is generally the preferred choice**.

<br>
<br>

---

<br>
<br>

## **CRUD Operations with SQLAlchemy ORM in FastAPI (PostgreSQL)**

This document describes how each CRUD operation is implemented using SQLAlchemy ORM in a FastAPI application backed by PostgreSQL.

<br>

### **1. Read All Posts (GET `/posts`)**

```python
@app.get("/posts")
async def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"message": "Your all posts", "Posts": posts}
```

- **Operation:** READ (all records)
- **Query:** `SELECT * FROM posts;`
- **Explanation:** Retrieves all post records from the database using SQLAlchemy ORM and returns them as a list.

<br>

### **2. Create New Post (POST `/posts`)**

```python
@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post, db: Session = Depends(get_db)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"message": "Post successfully created", "Post": new_post}
```

- **Operation:** CREATE
- **Query:** `INSERT INTO posts (...) VALUES (...);`
- **Explanation:**

  - Converts Pydantic model to dictionary.
  - Unpacks into ORM model.
  - Adds and commits to the database.
  - Refreshes to retrieve the newly created post including generated fields like `id`.

<br>

### **3. Read One Post by ID (GET `/posts/{id}`)**

```python
@app.get("/posts/{id}")
def get_post(id: int, response: Response, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=404, detail=f"post with id: {id} not found")
    return {"post": post}
```

- **Operation:** READ (one record)
- **Query:** `SELECT * FROM posts WHERE id = {id};`
- **Explanation:** Retrieves a specific post by ID. Raises 404 if not found.

<br>

### **4. Delete Post by ID (DELETE `/posts/{id}`)**

```python
@app.delete("/posts/{id}")
def delete_post(id: int, response: Response, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() is None:
        raise HTTPException(status_code=404, detail=f"Post with id {id} not found")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=204)
```

- **Operation:** DELETE
- **Query:** `DELETE FROM posts WHERE id = {id};`
- **Explanation:**

  - Checks existence.
  - Deletes the post using the query object.
  - Commits the changes and returns HTTP 204 (No Content).

<br>

### **5. Update Post by ID (PUT `/posts/{id}`)**

```python
@app.put("/posts/{id}")
def update_post(id: int, post_updates: Post, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post is None:
        raise HTTPException(status_code=404, detail=f"post with id: {id} not found")
    post_query.update(post_updates.dict(), synchronize_session=False)
    db.commit()
    return {"updated post": post_query.first()}
```

- **Operation:** UPDATE
- **Query:** `UPDATE posts SET ... WHERE id = {id};`
- **Explanation:**

  - Checks for post existence.
  - Updates fields using `update()` with dictionary unpacking.
  - Commits changes and returns updated post.

<br>

### **✅ Summary Table**

| Method | Endpoint      | Operation | SQL Equivalent                          | Notes               |
| ------ | ------------- | --------- | --------------------------------------- | ------------------- |
| GET    | `/posts`      | Read All  | `SELECT * FROM posts;`                  | Retrieves all posts |
| POST   | `/posts`      | Create    | `INSERT INTO posts (...) VALUES (...);` | Adds a new post     |
| GET    | `/posts/{id}` | Read One  | `SELECT * FROM posts WHERE id = ?;`     | Fetch post by ID    |
| DELETE | `/posts/{id}` | Delete    | `DELETE FROM posts WHERE id = ?;`       | Deletes post by ID  |
| PUT    | `/posts/{id}` | Update    | `UPDATE posts SET ... WHERE id = ?;`    | Updates post by ID  |

<br>

---

<br>

### 🔄 `db.refresh()` – Why and When to Use It

#### ✅ When Creating a New Record (INSERT)

```python
new_post = models.Post(**post.dict())
db.add(new_post)
db.commit()
db.refresh(new_post)
```

- After adding and committing `new_post`, SQLAlchemy does **not automatically update** the Python object with database-generated fields (like `id`, `created_at`, etc.).
- `db.refresh(new_post)` reloads the object from the database and updates its state with those fields.
- This is similar in effect to SQL’s `RETURNING *`, but at the ORM level.

#### 🔍 Under-the-Hood SQL Equivalent

```sql
INSERT INTO posts (title, content) VALUES ('abc', 'xyz') RETURNING *;
```

<br>

### ❓ Why `db.refresh()` is Not Used in Updates

#### 🔹 Updating a Record

```python
post_query = db.query(models.Post).filter(models.Post.id == id)
post_query.update(post_updates.dict(), synchronize_session=False)
db.commit()
return {"updated post": post_query.first()}
```

- `post_query.update(...)` modifies the record directly in the database.
- Calling `post_query.first()` **re-queries the updated object**, effectively getting the most recent data.
- Therefore, you do **not need `db.refresh()`** because you're already fetching the updated row from the DB.

#### 🧠 Summary

- `db.refresh(instance)` is used when you already have a Python object and want to update its fields from the DB.
- In UPDATE operations, it's common to just **re-fetch the record**, which is cleaner and serves the same purpose.

<br>

### ✅ When You Might Still Use `db.refresh()` in UPDATE

If you're not querying the object again and just want to update the in-memory object:

```python
post = db.query(models.Post).filter(models.Post.id == id).first()
# Apply updates manually
post.title = "Updated Title"
db.commit()
db.refresh(post)  # Now post has the latest DB state
```

This is valid but not as common as re-fetching the updated object.

<br>

---

<br>

## Purpose of Pydantic and SQLAlchemy Models, and How They Work Together

### **1. Purpose of SQLAlchemy Models**

SQLAlchemy is an ORM (Object-Relational Mapper) used to interact with a relational database using Python classes instead of raw SQL.

**Key Purpose:**

- Define **database schema** using Python classes.
- Map Python classes to **database tables**.
- Perform **CRUD operations** easily (Create, Read, Update, Delete).
- Support for database relationships, transactions, and queries.

![img](https://photos.fife.usercontent.google.com/pw/AP1GczOKIujjgd-DHzyr-KRk5vHzKoUbV5yDDC1kYzCEVyIiXtKXiij_aco=w881-h498-s-no-gm?authuser=0)

**Example SQLAlchemy Model:**

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
```

### **2. Purpose of Pydantic Models**

Pydantic is used for **data validation and serialization**. It does **not** interact with the database. It's often used in APIs to validate and serialize/deserialize data.

**Key Purpose:**

- Validate **incoming request data** (e.g., from a client via API).
- Serialize **outgoing response data**.
- Ensure data is structured correctly before processing.

![img](https://photos.fife.usercontent.google.com/pw/AP1GczOe55Ijzd1c-Iyk9zgIyjpJEz1JdbzkB6DcWCk7ZU8UQpxkCyQQ34o=w903-h514-s-no-gm?authuser=0)

**Example Pydantic Model:**

```python
from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str
    email: str
```

### **3. How They Work Together**

In a typical FastAPI or modern backend setup:

- **SQLAlchemy models** handle the **database layer**.
- **Pydantic models** handle the **API (request/response) layer**.

#### Workflow Example:

1. Client sends a JSON request to create a user.
2. FastAPI uses the **Pydantic model** to validate the request.
3. You convert the validated Pydantic object into a **SQLAlchemy model**.
4. Save the SQLAlchemy model to the database.
5. When returning a response, you convert the SQLAlchemy model back to a **Pydantic response model**.

### **Summary Table:**

| Feature    | SQLAlchemy Model   | Pydantic Model                                               |
| ---------- | ------------------ | ------------------------------------------------------------ |
| Role       | Database ORM       | Data validation / serialization                              |
| Used For   | DB schema, queries | API input/output                                             |
| Converts   | Data ↔ DB          | JSON ↔ Python objects                                        |
| Mandatory? | Yes (for DB)       | No, but very useful for clean code, security, and validation |

### ✅ Final Recommendation

- **Use both together** in modern API development.
- Let SQLAlchemy manage the DB.
- Let Pydantic handle safe and clean data flow between client and server.

<br>

---

<br>

## **Why Use Inherited Pydantic Models Instead of a Single Model?**

In modern FastAPI and Pydantic design patterns, we separate models like `BasePost`, `PostCreate`, and `PostResponse` for clarity, reusability, and correctness.

### ✅ **1. Reusability**

The `BasePost` model acts as a **common foundation** containing shared fields like `title`, `content`, and `published`. Instead of repeating these in every model, we inherit them:

- `PostCreate` for creating posts
- `PostUpdate` for updates
- `PostResponse` for returning posts from the API

This makes the code DRY (Don't Repeat Yourself).

### ✅ **2. Separation of Concerns**

Different operations require different fields:

- **Creating a post** needs just the post content.
- **Updating a post** may allow only partial data.
- **Reading a post** often includes DB-generated fields like `id`, `created_at`, `owner_id`.

Using separate models avoids confusing these responsibilities.

### ✅ **3. Clear Validation Boundaries**

Each Pydantic model serves a specific purpose:

- `PostCreate` ensures only the allowed fields are accepted during creation.
- `PostResponse` includes extra fields and enables conversion from ORM objects using `orm_mode = True`.
- You avoid exposing sensitive or unintended fields in the wrong context.

### ✅ **4. Example Design Pattern**

```python
from typing import Optional
from datetime import datetime
from pydantic import BaseModel

# Shared base model
class BasePost(BaseModel):
    title: str
    content: str
    published: bool = True

# For creating a post
class PostCreate(BasePost):
    pass

# For updating a post
class PostUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]
    published: Optional[bool]

# For returning a post
class PostResponse(BasePost):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# By default, Pydantic models only work with standard Python dict-like data.
# However, SQLAlchemy returns ORM objects (instances of classes, not plain dicts). orm_mode = True tells Pydantic:
# “Treat non-dict objects (like SQLAlchemy ORM instances) as if they were dicts when accessing fields.”

# Always use orm_mode = True in response models when you're returning SQLAlchemy ORM objects from the database. It makes sure that Pydantic can properly serialize those objects to JSON for API responses.
```

### ❌ **Why Not Use Just One `Post` Model?**

Using a single model like `Post` everywhere leads to problems:

- Exposes database fields (`id`, `created_at`) during creation or update.
- Makes the API hard to maintain or extend.
- Increases the risk of accepting/exposing unintended data.

### ✅ **Conclusion**

Using `BasePost` along with specialized models like `PostCreate`, `PostUpdate`, and `PostResponse` ensures:

- Clear separation of purpose
- Clean and safe validation
- Scalable and maintainable code structure

It's a best practice in any production-ready FastAPI project.

<br>

---

<br>

## What Is a Response Model in FastAPI?

A **response model** defines the structure of data returned to the client via an API endpoint.

### ✅ Purpose

- Controls which fields are included in the API response
- Hides internal/sensitive fields (e.g., password)
- Validates and structures output data

### ✅ Example

```python
class PostResponse(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        orm_mode = True

@app.get("/posts/{id}", response_model=PostResponse)
def get_post(id: int):
    return db.query(Post).get(id)
```

Even if the SQLAlchemy model has more fields, only the defined fields are sent to the client.

### ✅ Benefits

- **Security**: Exclude private/internal data
- **Consistency**: Ensures valid and uniform responses
- **Flexibility**: Customize output per route

Response models are a key feature in FastAPI for clean and safe API design.

<br>

---

<br>

## **🔐 Password Hashing in FastAPI**

### ✅ 1. Install dependencies

```bash
pip install passlib[bcrypt]
```

<br>

### ✅ 2. Create a password hashing utility

```python
from passlib.context import CryptContext

# Define hashing algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash a plain password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Verify a password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
```

<br>

### ✅ 3. Use it in your FastAPI user creation route

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserCreate(BaseModel):
    email: EmailStr
    password: str

@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user:schemas.UserCreate, db:Session=Depends(get_db)):

    # hash the password
    hashed_password=utils.hash_password(user.password)
    user.password=hashed_password


    new_user=models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
```

<br>

### 🔐 Summary

- Use `passlib[bcrypt]` for secure password hashing.
- Always store the **hashed** password, never the plain one.
- Use `pwd_context.verify()` during login to check if the entered password matches the stored hash.

<br>

---

<br>

## **FastAPI Routers: Overview and Internal Working**

### **What are Routers in FastAPI?**

Routers in **FastAPI** are components that help organize an application into smaller, manageable, and reusable modules. They are particularly useful for grouping related endpoints, improving readability and maintainability in larger projects.

```python
from fastapi import APIRouter

user_router = APIRouter()

@user_router.get("/profile")
def read_profile():
    return {"user": "profile data"}
```

<br>

### **How Routers Work Internally**

- Routers are instances of `APIRouter`, similar to the main `FastAPI` app.
- They collect route definitions using decorators like `.get()`, `.post()`, etc.
- Each route is encapsulated in a `fastapi.routing.APIRoute` object.
- When using `app.include_router(router)`, FastAPI adds all the router’s routes to the main app’s routing table.
- FastAPI leverages **Starlette** under the hood, which uses a `Router` to efficiently match incoming HTTP requests.

This structure allows:

- Modular route grouping
- Scoped dependencies
- Scoped middleware and event handlers

<br>

### **Prefix and Tags in Routers**

#### **1. Prefix**

- Adds a shared path prefix to all routes in a router.
- Useful for versioning or functional grouping.

```python
app.include_router(user_router, prefix="/users")
```

If a router route is `/profile`, it becomes `/users/profile` in the main app.

#### **2. Tags**

- Used for grouping routes in the **OpenAPI docs (Swagger UI)**.
- Improves API documentation readability.

```python
app.include_router(user_router, tags=["Users"])
```

This places all endpoints under the "Users" section in the docs.

<br>

- **Routers** modularize FastAPI applications.
- Internally, they behave like mini FastAPI apps until included.
- **Prefix**: Adds a common route path.
- **Tags**: Organize routes in documentation.

Routers are essential for scaling FastAPI applications in a clean and manageable way.

<br>

---

<br>

## **Authentication in Backend Development**

**Authentication** is the process of verifying the identity of a user or system trying to access a backend service. It ensures only authorized users can access protected resources. Two common authentication methods are:

<br>
<br>

## **1. Session-Based Authentication (Stateful)**

### **Overview:**

- The **server maintains a session** for each logged-in user.
- Upon successful login, the server creates a **session object** containing user information.
- A **session ID** is generated and stored on the server (e.g., in memory or a database).
- The session ID is sent to the client, typically stored in a **cookie**.
- On each request, the client sends the cookie; the server uses the session ID to retrieve the user session.

### **How it Works:**

1. User logs in.
2. Server creates a session and stores it.
3. Server sends session ID in a cookie to client.
4. Client includes cookie in future requests.
5. Server validates session ID and authenticates the user.

### **Pros:**

- Easy to invalidate sessions.
- Server has control over session lifecycle.

### **Cons:**

- Requires server-side storage (stateful).
- Less scalable without shared session store (e.g., Redis).

<br>
<br>

## **2. JWT (JSON Web Token) Authentication (Stateless)**

### **Overview:**

- JWTs are **self-contained tokens** that include user data and claims.
- Tokens are **signed** by the server and do not require storage.
- After login, the server sends the JWT to the client.
- The client stores the JWT (commonly in localStorage or HTTP-only cookies).
- The client includes the token in each request (usually in an `Authorization` header).
- The server **verifies** the token and **extracts user info** from it.

![img](https://photos.fife.usercontent.google.com/pw/AP1GczNYBsADnhoxWXIEFWuOf7qyk5f3VLHmWRaSope6wuKdOIBFFWDdMIg=w1599-h714-s-no-gm?authuser=0)

### **How it Works:**

1. User logs in.
2. Server creates and signs a JWT.
3. Server sends JWT to the client.
4. Client stores JWT and sends it with each request.
5. Server verifies signature and reads claims from JWT.

### **Pros:**

- Stateless (no server storage needed).
- Scales well across distributed systems.
- Can include custom metadata inside the token.

### **Cons:**

- Hard to revoke tokens early.
- Large token size.
- If stored in localStorage, vulnerable to XSS (HTTP-only cookies recommended).

<br>
<br>

| Feature                 | Session-Based Auth            | JWT-Based Auth (Stateless)      |
| ----------------------- | ----------------------------- | ------------------------------- |
| Server storage required | Yes (in-memory/DB/Redis)      | No                              |
| Scalable across servers | Harder (needs shared storage) | Easier (stateless)              |
| Token revocation        | Easy (delete session)         | Hard (need blacklist strategy)  |
| Token size              | Small (just session ID)       | Larger (user info + metadata)   |
| Security                | High with secure cookies      | High with HTTP-only JWT cookies |
| Ideal use cases         | Traditional web apps          | APIs, SPAs, mobile apps         |

<br>
<br>

---

<br>
<br>

## **JWT Authentication Deep Dive**

A **JWT (JSON Web Token)** is a compact, URL-safe token format used in stateless authentication. It is commonly used to securely transmit information between parties as a JSON object. This information can be verified and trusted because it is digitally signed.

<br>
<br>

## **Structure of a JWT Token**

![img](https://photos.fife.usercontent.google.com/pw/AP1GczMXSNFLojH0eytxxCIIGo_mkZc6ee78eACEa64J5c9P04AYjBoMvrE=w1599-h714-s-no-gm?authuser=0)

A JWT consists of **three Base64URL-encoded parts**, separated by dots (`.`):

```
HEADER.PAYLOAD.SIGNATURE
```

From the example image:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTYzODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

<br>
<br>

### **1. Header**

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

- **"alg"**: Specifies the algorithm used for signing the token (e.g., HS256 = HMAC + SHA256).
- **"typ"**: Specifies the token type, which is JWT.

**Base64URL-encoded Header:**

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
```

<br>
<br>

### **2. Payload**

```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}
```

This is the body of the token and contains the **claims** — information about the user or the token:

- **"sub"**: Subject (usually the user ID)
- **"name"**: Custom claim (e.g., user's name)
- **"iat"**: Issued At Time (Unix timestamp)

**Base64URL-encoded Payload:**

```
eyJzdWIiOiIxMjM0NTYzODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ
```

> ⚠️ Note: Payload is not encrypted, just encoded. Sensitive information should **not** be stored here.

<br>
<br>

### **3. Signature**

**Sample from image:**

```
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

**Computed as:**

```js
HMACSHA256(
  base64UrlEncode(header) + "." + base64UrlEncode(payload),
  your - 256 - bit - secret
);
```

The signature ensures that the token has not been tampered with. It uses the **header**, **payload**, and a **secret key** to generate a hash.

<br>
<br>

| Component | Role             | Contains                          | Secure?     |
| --------- | ---------------- | --------------------------------- | ----------- |
| Header    | Algorithm & Type | `alg`, `typ`                      | ❌ (Public) |
| Payload   | Claims / Info    | `sub`, `name`, `iat`, etc.        | ❌ (Public) |
| Signature | Integrity Check  | HMAC of header + payload + secret | ✅          |

<br>
<br>

## **Stateless Authentication Using JWT**

- Tokens are issued after a successful login.
- Stored on the **client side** (e.g., in **cookies** or **localStorage**).
- Sent in the `Authorization: Bearer <token>` header with every request.
- No need to store sessions on the server — the server just verifies the signature.

> ✅ **Stateless** and **scalable**, ideal for APIs and microservices.

<br>
<br>

---

<br>
<br>

## **Purpose of Signature in JWT (JSON Web Token)**

![img](https://photos.fife.usercontent.google.com/pw/AP1GczORTZXMgbW-9_ccdGDOT3vNSHb_u7LTKXibsgVbpWuu45KeBhH1Wjk=w1599-h714-s-no-gm?authuser=0)

The signature is a **crucial security mechanism** in JWT. This image illustrates **how signatures prevent tampering** of the token, particularly the payload, by unauthorized parties.

### **How a Valid JWT is Created and Verified**

1. **User Info (Payload)**:
   Contains claims like:

   ```json
   {
     "id": 5938,
     "role": "user"
   }
   ```

2. **Token Generation Process**:

   - The **header**, **payload**, and a **secret key** (only known to the server) are used to create a **signature** using a hashing algorithm (e.g., HMAC-SHA256).
   - This produces:

     ```
     Token = base64url(Header) + "." + base64url(Payload) + "." + Signature
     ```

3. **Resulting JWT Token**:

   - The final token contains the **header**, **payload**, and the computed **signature**.
   - This token is sent to the client, which may include it in API requests.

### **Tampering Attempt by Attacker (Bottom Left)**

1. **Attacker Modifies the Payload**:

   - Changes the role from `"user"` to `"admin"`:

     ```json
     {
       "id": 5938,
       "role": "admin"
     }
     ```

2. **Signature Problem**:

   - The attacker does **not have the secret key**, so they **cannot generate a valid signature** for the modified payload.
   - They attach the **original signature** (which no longer matches the modified payload).

### **API Signature Verification (Right Side)**

1. **API Receives Token**:

   - Extracts header and payload.
   - Recomputes the **test signature** using the header, payload, and the server's secret key.

2. **Comparison**:

   - Compares the **original signature** from the token with the **computed test signature**.
   - Since the payload was modified and the attacker couldn't sign it correctly, **the two signatures do not match**.

3. **Result**:

   - **Token is rejected** because signature verification fails.
   - This protects the API from unauthorized access.

<br>
<br>

| Function               | Purpose                                                                                    |
| ---------------------- | ------------------------------------------------------------------------------------------ |
| **Signature**          | Validates token integrity.                                                                 |
| **Secret Key**         | Used to generate and verify the signature. Must be kept private.                           |
| **Tamper Protection**  | Any modification to the header or payload **invalidates** the signature.                   |
| **Security Guarantee** | Attackers can’t forge or alter tokens without the secret, even if they decode the payload. |

<br>
<br>

---

<br>
<br>

# User Login Process

![img](https://photos.fife.usercontent.google.com/pw/AP1GczP6jxZ0BgXQuv7w3CFPriRDi16HUyI0GxRBslPr0Q1EmIecsucmv1Y=w1599-h714-s-no-gm?authuser=0)

<br>
<br>

## Step-by-Step Process

### 1. API Endpoint: `/login`

- **Request Type**: POST
- **Parameters**:
  - `email`: User's registered email address.
  - `password`: User's raw (unhashed) password.

### 2. User Lookup

- The system queries the database to **find the user by email**.
- If no user exists with the provided email, return an error (e.g., `404 Not Found`).

### 3. Password Verification

- **Stored Data**: The user's record contains a **hashed password** (e.g., hashed via bcrypt, SHA-256, etc.).
- **Process**:
  1. Hash the user-provided raw password using the **same cryptographic algorithm** as stored.
  2. Compare the newly generated hash with the stored hashed password.

### 4. Token Generation

- If the hashes match:
  - Generate a **token** (e.g., JWT, OAuth token) for authenticated sessions.
- If the hashes **do not match**: Return an error (e.g., `401 Unauthorized`).

### 5. Response

- Return the generated token to the client for future authenticated requests.

<br>
<br>

---

<br>
<br>

## **🔐 FastAPI Login, JWT Creation, and Verification Flow**

### ✅ 1. Login Endpoint and Input Handling

```python
@router.post("/login", response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
```

- `OAuth2PasswordRequestForm` is used to read `username` and `password` from `form-data`.
- `Depends()` lets FastAPI inject dependencies automatically (like form input and DB session).
- The `username` is treated as the user's email in this logic.

<br>
<br>

### ✅ 2. User Validation

```python
user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
if not user:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")

if not utils.verify_password(user_credentials.password, user.password):
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
```

- Looks up user by email (from form field `username`).
- Verifies password using hashing method (like bcrypt).

<br>
<br>

### ✅ 3. JWT Token Creation

```python
return {
    "access_token": oauth2.create_access_token({"id": user.id}),
    "token_type": "Bearer token"
}
```

- Creates JWT token with the user's ID as payload.
- Token returned to client for use in `Authorization` headers.

<br>
<br>

### ✅ 4. `create_access_token` Function

```python
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
```

- Adds expiration time to payload.
- Encodes data with `HS256` and secret key.
- Returns JWT string.

<br>
<br>

### ✅ 5. Token Verification

```python
def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
        id: str = str(payload.get("id"))
        if id is None:
            raise credentials_exception
        return schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception
```

- Decodes JWT token using secret.
- Extracts user ID.
- Raises an error if token is invalid or missing info.

<br>
<br>

### ✅ 6. Getting Current User from JWT Token

```python
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not validate credential",
        headers={"www-Authenticate": "Bearer"}
    )
    return verify_access_token(token, credentials_exception)
```

- Extracts token from `Authorization: Bearer <token>` header.
- Verifies and returns token data.

<br>
<br>

### ✅ Summary Flow

1. **Login Route**:
   - Accepts form-data (username + password).
   - Verifies credentials.
   - Returns JWT token.
2. **Client Sends Token**:
   - Uses header: `Authorization: Bearer <token>`
3. **Protected Routes**:
   - Use `Depends(get_current_user)` to extract user from token.
   - Access user's ID and fetch user details from DB.

<br>
<br>

### ✅ Example: Protected Route

```python
@router.get("/profile")
def read_profile(current_user: schemas.User = Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == current_user.id).first()
    return user
```

<br>
<br>

### ✅ Example Token Schemas

```python
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
```

<br>
<br>

---

<br>
<br>

## Detailed Explanation of `Depends()` and Dependency Injection in FastAPI

### ✅ What is `Depends()` in FastAPI?

`Depends()` is FastAPI’s way of implementing **Dependency Injection** (DI). Instead of manually calling helper functions to get things like a database session, current user, or form data, FastAPI calls those dependencies for you and "injects" the result into your endpoint.

This provides:

- Cleaner, modular code
- Reusability of logic (like authentication or database setup)
- Automatic management of resources like DB sessions
- Better testability (easier to mock dependencies)

<br>
<br>

### 🧠 How Does `Depends()` Work Internally?

When FastAPI sees `Depends(some_function)` in a route parameter:

1. It inspects the function `some_function`.
2. Executes it before calling your route function.
3. Takes its return value and passes it as an argument to your function.

FastAPI builds a dependency tree recursively and resolves everything in order.

<br>
<br>

### 🔍 Examples in Your Code

Let’s break down every `Depends()` used and explain it with detail:

<br>
<br>

### ✅ 1. `user_credentials: OAuth2PasswordRequestForm = Depends()`

- This injects a parsed form (not JSON) with `username` and `password`.
- Used in the login route:
  ```python
  @router.post("/login")
  def login(user_credentials: OAuth2PasswordRequestForm = Depends())
  ```
- Internally, FastAPI:
  - Parses the incoming request.
  - Extracts `form-data` (as required by OAuth2 spec).
  - Instantiates `OAuth2PasswordRequestForm` with `.username` and `.password`.

✅ **Benefit**: You don’t need to manually parse form fields; this standardizes input for OAuth2 password flow.

<br>
<br>
  
### ✅ 2. `db: Session = Depends(database.get_db)`

- Injects a SQLAlchemy session into your function.
- From this function:
  ```python
  def get_db():
      db = SessionLocal()
      try:
          yield db
      finally:
          db.close()
  ```
- FastAPI:
  - Detects this as a generator (because of `yield`).
  - Runs the code before `yield` to get the `db`.
  - Automatically closes it after the request ends.

✅ **Benefit**: Manages DB session lifecycle automatically — no need for manual opening/closing.

<br>
<br>

### ✅ 3. `token: str = Depends(oauth2_scheme)`

- Injects the **raw token string** from the `Authorization` header:
  ```
  Authorization: Bearer <JWT_TOKEN>
  ```
- `oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")` tells FastAPI where to find the token in the request.
- Used here:
  ```python
  def get_current_user(token: str = Depends(oauth2_scheme))
  ```

✅ **Benefit**: You don’t need to manually fetch headers or parse the bearer token.

<br>
<br>

### ✅ 4. `current_user = Depends(get_current_user)`

- Injects the current authenticated user info (e.g., ID).
- Uses the previously explained token to verify and decode it:
  ```python
  def get_current_user(token: str = Depends(oauth2_scheme)):
      payload = jwt.decode(...)
      return schemas.TokenData(id=id)
  ```

✅ **Benefit**: Makes your route automatically secured — if the token is missing or invalid, the request is blocked with a 401.

<br>
<br>

### ✅ 5. Chained Dependencies

FastAPI supports dependencies depending on other dependencies.

Example:

```python
def get_current_user(token: str = Depends(oauth2_scheme)):
```

⬆️ Here, `Depends(oauth2_scheme)` is itself a dependency used **inside** another dependency (`get_current_user`), and this can be nested multiple levels.

<br>
<br>

### ✅ Dependency Injection Benefits in Real Use

| Feature      | Manual Code                            | With Depends                          |
| ------------ | -------------------------------------- | ------------------------------------- |
| Form parsing | Parse each field from `request.form()` | `OAuth2PasswordRequestForm=Depends()` |
| DB Session   | Manually open/close sessions           | `db=Depends(get_db)`                  |
| Auth Token   | Manually parse header & verify JWT     | `Depends(get_current_user)`           |
| Reusability  | Reimplement logic everywhere           | Modular functions reused via Depends  |

<br>
<br>

### 🧪 Example: Custom Dependency

You can create dependencies for roles or permissions:

```python
def get_admin_user(user: schemas.User = Depends(get_current_user)):
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Admins only")
    return user
```

Then use it in routes:

```python
@router.get("/admin-dashboard")
def view_dashboard(current_user: schemas.User = Depends(get_admin_user)):
    ...
```

<br>
<br>

- `Depends()` means: “Run this function and give me its result.”
- FastAPI resolves all dependencies **before** calling your endpoint.
- Great for:
  - Form parsing
  - Auth/token validation
  - DB session management
  - Role-based access, permissions
- Keeps your code clean, modular, and testable.

<br>
<br>

<br>
<br>

---

<br>
<br>

## Understanding `Depends()` with `OAuth2PasswordRequestForm`

### ✅ The Confusion

In the login route, you might see:

```python
user_credentials: OAuth2PasswordRequestForm = Depends()
```

At first glance, it seems odd because no function is passed into `Depends()`. But it still works. Why?

<br>
<br>

### ✅ `Depends()` Can Accept Callable Classes

FastAPI’s `Depends()` doesn’t need a regular function. It can also accept **classes** — **as long as they implement `__call__()`**.

And that’s exactly what’s happening here:

```python
Depends(OAuth2PasswordRequestForm)
```

This is what FastAPI interprets when you write:

```python
user_credentials: OAuth2PasswordRequestForm = Depends()
```

<br>
<br>

### ✅ What is `OAuth2PasswordRequestForm`?

`OAuth2PasswordRequestForm` is a **helper class provided by FastAPI** to extract form data in compliance with the OAuth2 password flow.

It expects form fields:

- `username`
- `password`

And it assumes the content type is:

```
application/x-www-form-urlencoded
```

(as required by OAuth2 specs — **not** JSON)

<br>
<br>

### 🧠 What Happens Internally?

1. FastAPI sees `Depends()` with the type `OAuth2PasswordRequestForm`.
2. It treats it as:
   ```python
   Depends(OAuth2PasswordRequestForm)
   ```
3. It:
   - Instantiates the class with the incoming request
   - Calls the instance using its `__call__()` method
   - Extracts `username` and `password`
   - Passes the object into your function

So this line:

```python
user_credentials: OAuth2PasswordRequestForm = Depends()
```

Is really doing:

```python
form = OAuth2PasswordRequestForm()
user_credentials = form(request)
```

(Internally, handled by FastAPI)

Now you can access:

```python
user_credentials.username
user_credentials.password
```

<br>
<br>

- `Depends()` can work with classes that implement `__call__()`
- `OAuth2PasswordRequestForm` is such a class — it handles form parsing
- FastAPI does the work of instantiating and invoking it
- This enables clean, declarative parameter parsing in your routes

<br>
<br>

### 🔍 How `Depends(oauth2_scheme)` Works in FastAPI

```python
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
```

You're right — `oauth2_scheme` is **not a regular function**. It's an **instance** of the `OAuth2PasswordBearer` class. But here’s why it works with `Depends()`:

<br>
<br>

### ✅ `OAuth2PasswordBearer` is a Callable Class

Even though `oauth2_scheme` is a class instance, it defines a `__call__()` method, which makes it **callable like a function**.

So when FastAPI sees this:

```python
token: str = Depends(oauth2_scheme)
```

…it internally does something equivalent to:

```python
token: str = Depends(oauth2_scheme.__call__)
```

<br>
<br>

### ⚙️ What Happens Internally

When FastAPI processes the dependency:

1. It detects that `oauth2_scheme` is a callable object.
2. It automatically calls `oauth2_scheme(request)` under the hood.
3. This callable looks for the `Authorization` header in the request.
4. If it finds a `Bearer <token>`, it returns the token string.
5. This token string is passed into your function (`get_current_user`).

<br>
<br>

| What You Write                              | What FastAPI Does Internally                  |
| ------------------------------------------- | --------------------------------------------- |
| `Depends(oauth2_scheme)`                    | `Depends(oauth2_scheme.__call__)`             |
| `oauth2_scheme = OAuth2PasswordBearer(...)` | Creates a callable class that extracts tokens |
| `token: str = Depends(oauth2_scheme)`       | Injects token from header into `token` param  |

<br>
<br>

---

<br>
<br>

## **Relationships and Foreign Keys in PostgreSQL and SQLAlchemy**

In PostgreSQL and relational databases, **relations** refer to **tables**. Relationships between tables are defined using **foreign keys**, which are essential for maintaining **referential integrity**.

<br>
<br>

## **What is a Foreign Key?**

A **foreign key** is a column (or set of columns) in one table that refers to the **primary key** in another table. It helps:

- Enforce referential integrity
- Model real-world associations
- Prevent invalid data entries

<br>
<br>

## **Types of Relationships**

### **1. One-to-One (1:1)**

#### **Definition:**

Each row in **Table A** is linked to **only one row** in **Table B**, and vice versa.

#### **Key Characteristics:**

- Enforced using a **foreign key with a UNIQUE constraint**.
- Often used to separate optional or sensitive data.

#### **Use Case:**

An employee has one unique parking spot.

#### **PostgreSQL Example:**

```sql
CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE parking_spots (
    spot_id SERIAL PRIMARY KEY,
    emp_id INT UNIQUE REFERENCES employees(emp_id) ON DELETE CASCADE
);
```

#### **SQLAlchemy Example:**

```python
class ParkingSpot(Base):
    __tablename__ = 'parking_spots'
    spot_id = Column(Integer, primary_key=True)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'), unique=True)
    employee = relationship('Employee', back_populates='parking_spot')

class Employee(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    name = Column(String)
    parking_spot = relationship('ParkingSpot', back_populates='employee', uselist=False)
```

<br>
<br>

### **2. One-to-Many (1\:N)**

#### **Definition:**

One row in **Table A** is associated with **many rows** in **Table B**, but each row in **Table B** relates to only one in **Table A**.

#### **Key Characteristics:**

- Most common relationship.
- Foreign key is placed on the "many" side.

#### **Use Case:**

A department has many employees.

#### **PostgreSQL Example:**

```sql
CREATE TABLE departments (
    dept_id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,
    name TEXT,
    dept_id INT REFERENCES departments(dept_id) ON DELETE CASCADE
);
```

#### **SQLAlchemy Example:**

```python
class Department(Base):
    __tablename__ = 'departments'
    dept_id = Column(Integer, primary_key=True)
    name = Column(String)
    employees = relationship('Employee', back_populates='department')

class Employee(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    name = Column(String)
    dept_id = Column(Integer, ForeignKey('departments.dept_id'))
    department = relationship('Department', back_populates='employees')
```

<br>
<br>

### **3. Many-to-Many (M\:N)**

#### **Definition:**

Multiple rows in **Table A** relate to multiple rows in **Table B**.

#### **Key Characteristics:**

- Implemented via a **junction table** with foreign keys from both tables.

#### **Use Case:**

Students enroll in many courses; courses have many students.

#### **PostgreSQL Example:**

```sql
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    title TEXT
);

CREATE TABLE student_course (
    student_id INT REFERENCES students(student_id) ON DELETE CASCADE,
    course_id INT REFERENCES courses(course_id) ON DELETE CASCADE,
    PRIMARY KEY (student_id, course_id)
);
```

#### **SQLAlchemy Example:**

```python
student_course = Table(
    'student_course', Base.metadata,
    Column('student_id', ForeignKey('students.student_id'), primary_key=True),
    Column('course_id', ForeignKey('courses.course_id'), primary_key=True)
)

class Student(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship('Course', secondary=student_course, back_populates='students')

class Course(Base):
    __tablename__ = 'courses'
    course_id = Column(Integer, primary_key=True)
    title = Column(String)
    students = relationship('Student', secondary=student_course, back_populates='courses')
```

<br>
<br>

## **How to Identify Relationship Types in Scenarios**

| Question                                                   | Interpretation |
| ---------------------------------------------------------- | -------------- |
| Does each entity instance relate to only one of the other? | One-to-One     |
| Does one entity relate to many of the other?               | One-to-Many    |
| Can many from both sides relate to each other?             | Many-to-Many   |

<br>
<br>

## **Visual Comparison Table**

| Type         | FK Placement      | Needs Junction Table | Uniqueness Constraint |
| ------------ | ----------------- | -------------------- | --------------------- |
| One-to-One   | Either table      | No                   | Yes (`UNIQUE`)        |
| One-to-Many  | "Many" side table | No                   | No                    |
| Many-to-Many | In junction table | Yes                  | No                    |

<br>
<br>

- **Relations** = tables in PostgreSQL
- **Foreign Keys** define relationships and enforce integrity
- Types of relationships:

  - One-to-One → FK with `UNIQUE`
  - One-to-Many → FK in the child table
  - Many-to-Many → Junction table

- **SQLAlchemy** uses `ForeignKey`, `relationship`, and `secondary` for ORM mappings

<br>
<br>

---

<br>
<br>

## **1. ForeignKey — Database-level link (physical relationship)**

**Definition:**
`ForeignKey` defines the **actual relationship constraint** at the **database level**.
It tells the database engine that one column refers to another column in a different table.

In your example:

```python
owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
```

### **What it does**

- Creates a **foreign key constraint** in the database between `posts.owner_id` and `users.id`.
- Ensures **referential integrity**, meaning:

  - You cannot insert a post with a `owner_id` that doesn’t exist in `users.id`.
  - If a user is deleted (and `ondelete="CASCADE"` is used), all their posts are automatically deleted.

### **Think of it as**

> The _"wire"_ connecting one table’s column to another table’s column inside the database.

<br>
<br>

## **2. relationship — Python-level link (object relationship)**

**Definition:**
`relationship()` is **not stored in the database**.
It’s purely a **Python-side construct** that tells SQLAlchemy how two tables’ ORM classes are related — enabling you to easily navigate between objects in code.

In your example:

```python
owner = relationship("User")
```

### **What it does**

- Enables you to access the **related `User` object** directly from a `Post` instance:

  ```python
  post = db.query(Post).first()
  print(post.owner.email)  # ← Works because of relationship
  ```

- Automatically performs joins behind the scenes when you access related objects.
- Lets you define **bidirectional relationships** (using `back_populates` or `backref`).

### **Think of it as**

> The _"shortcut"_ in Python that lets you move between related ORM objects without manually writing joins.

<br>
<br>

## **3. Analogy**

| Concept          | Acts On    | What It Does                                       | Example                      |
| ---------------- | ---------- | -------------------------------------------------- | ---------------------------- |
| **ForeignKey**   | Database   | Creates actual link/constraint between two tables  | `posts.owner_id → users.id`  |
| **relationship** | Python ORM | Creates object-level connection between two models | `post.owner → User instance` |

<br>
<br>

## **4. How They Work Together**

They usually come **in pairs**:

- The **`ForeignKey`** defines the relationship in the database schema.
- The **`relationship`** defines the relationship in your Python ORM model.

So in your example:

```python
owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
owner = relationship("User")
```

They work together like this:

- `owner_id` stores the **user’s id** (integer value).
- `owner` gives you direct access to the **actual `User` object** linked to that id.

<br>
<br>

## **5. Bonus Example: Bidirectional Relationship**

If you add this in your `User` model:

```python
posts = relationship("Post", back_populates="owner")
```

And update `Post` as:

```python
owner = relationship("User", back_populates="posts")
```

Then:

```python
user.posts     # gives all posts by that user
post.owner     # gives the user who owns the post
```

Now both sides know about each other — that’s a complete ORM relationship.

<br>
<br>

✅ **Summary Table**

| Feature             | `ForeignKey`                  | `relationship()`              |
| ------------------- | ----------------------------- | ----------------------------- |
| Level               | Database schema               | Python ORM                    |
| Purpose             | Enforce referential integrity | Provide object navigation     |
| Stored in DB?       | ✅ Yes                        | ❌ No                         |
| Required for joins? | Yes (underlying link)         | No (automates joining in ORM) |
| Type                | Column constraint             | ORM mapping helper            |
| Example             | `ForeignKey("users.id")`      | `relationship("User")`        |

<br>
<br>

---

<br>
<br>

## **1. What Are Query Parameters?**

**Definition:**
Query parameters are **key-value pairs** that you add to the **end of a URL** after a `?`.
They are mainly used to **filter, search, sort, or paginate** data in GET requests — without changing the URL path.

They look like this:

```
/posts?limit=10&skip=5&search=iphone
```

Here:

- `limit`, `skip`, and `search` are **query parameters**.
- They are part of the **URL**, not the request body.

<br>
<br>

## **2. How FastAPI Handles Query Parameters**

In your example:

```python
@router.get("/", response_model=List[schemas.postResponse])
async def get_posts(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(oauth2.get_current_user),
    limit: int = 10,
    skip: int = 0,
    search: Optional[str] = ""
):
```

### **Here’s what happens:**

- FastAPI automatically detects that `limit`, `skip`, and `search` are **query parameters**.
- It reads them from the URL if they’re provided.
- If they’re **not provided**, it uses the **default values** (`limit=10`, `skip=0`, `search=""`).

<br>
<br>

## **3. Example in Action**

If you call:

```
GET /posts?limit=5&skip=10&search=phone
```

Then inside your function:

```python
limit = 5
skip = 10
search = "phone"
```

Your query will run:

```python
posts = db.query(models.Post).filter(
    models.Post.title.contains("phone")
).limit(5).offset(10).all()
```

That means:

- Only posts whose **title contains “phone”** will be fetched.
- Return **5 posts** (limit).
- **Skip the first 10 posts** (offset = pagination).

<br>
<br>

## **4. Why Use Query Parameters**

Query parameters are perfect for:

| Use Case       | Example                                       |
| -------------- | --------------------------------------------- |
| **Pagination** | `/posts?limit=10&skip=20` → fetch posts 21–30 |
| **Filtering**  | `/posts?published=true`                       |
| **Searching**  | `/posts?search=iphone`                        |
| **Sorting**    | `/posts?sort_by=date`                         |

They’re flexible and lightweight — ideal for **GET requests** where you only need to retrieve data with conditions.

<br>
<br>

## **5. Difference Between Query Parameters and Path Parameters**

| Type                | Example URL                | Used For                         | Declared As                                     |
| ------------------- | -------------------------- | -------------------------------- | ----------------------------------------------- |
| **Path Parameter**  | `/posts/{id}` → `/posts/5` | Identifying a specific resource  | `def get_post(id: int)`                         |
| **Query Parameter** | `/posts?limit=10&skip=0`   | Filtering, searching, pagination | `def get_posts(limit: int = 10, skip: int = 0)` |

✅ **Path parameters** are **part of the URL structure**,
✅ **Query parameters** are **additional modifiers**.

<br>
<br>

## **6. In Your Example**

```python
posts = db.query(models.Post).filter(
    models.Post.title.contains(search)
).limit(limit).offset(skip).all()
```

So:

- `search` filters posts by title,
- `limit` restricts how many posts to return,
- `skip` helps paginate (skip some records).

Example API call:

```
GET /posts?limit=3&skip=2&search=Samsung
```

→ This returns **3 posts** (after skipping first 2) where the title contains “Samsung”.

<br>
<br>

✅ **Summary:**

| Parameter | Type        | Purpose                         | Default |
| --------- | ----------- | ------------------------------- | ------- |
| `limit`   | Query param | Limit number of posts           | `10`    |
| `skip`    | Query param | Skip first N posts (pagination) | `0`     |
| `search`  | Query param | Filter posts by title keyword   | `""`    |

<br>
<br>

- `Optional[str]` means the parameter **can be a string or None**.
- If you already give a **default value** (like `""`), then it’s **never None**, so `Optional` isn’t required.
- Developers sometimes still use `Optional` just to make it **clear the parameter is not required**.
- The best practice is:

  ```python
  search: Optional[str] = None
  ```

  and then check:

  ```python
  if search:
      query = query.filter(Post.title.contains(search))
  ```

→ This clearly means the user **may or may not** provide the `search` parameter.

<br>
<br>

---

<br>
<br>

## **What Are Environment Variables?**

Environment variables are **key-value pairs** used to store configuration data **outside** your source code.
They are commonly used for things like:

- Database credentials (`DB_USER`, `DB_PASSWORD`, etc.)
- API keys and secrets (`SECRET_KEY`)
- Environment-specific settings (like debug mode or port numbers)

The goal:
✅ **Avoid hardcoding secrets** in your code.
✅ **Easily switch configurations** between development and production.
✅ **Prevent leaks of sensitive information** (e.g., if your repo is public).

<br>
<br>

## **How Pydantic Handles Environment Variables**

You’re already using `BaseSettings` from `pydantic_settings` — that’s the **correct** approach.
Let’s revisit your example step by step.

### **1. Your Settings Class**

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"   # automatically loads environment variables from a .env file

settings = Settings()
```

✅ **How it works:**

- Pydantic will **first look** for variables in the actual system environment (`os.environ`).
- If not found, it will **fall back** to the `.env` file specified in `Config.env_file`.
- `.env` is just a text file with key-value pairs, e.g.:

```bash
# .env file
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=postgress@123
DB_NAME=mydatabase
SECRET_KEY=mysecret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

✅ **Usage in your code:**

```python
print(settings.DB_USER)  # prints 'postgres'
print(settings.DB_PASSWORD)  # prints 'postgress@123'
```

<br>
<br>

## **How to Deal with Environment Variables in Development**

During **development**, you usually:

- Keep a local `.env` file (like the example above).
- Add it to `.gitignore` so it’s **never pushed** to GitHub.

```bash
# .gitignore
.env
```

- Pydantic automatically loads it when you run your FastAPI app locally.
- If you need different settings for dev vs test, you can have multiple `.env` files like:

  - `.env.development`
  - `.env.testing`
  - `.env.production`

Then, modify your class to dynamically load one:

```python
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ...
    class Config:
        env_file = f".env.{os.getenv('FASTAPI_ENV', 'development')}"
```

Then set:

```bash
FASTAPI_ENV=production
```

<br>
<br>

## **How to Handle Environment Variables in Production**

In **production**, you usually **don’t keep a `.env` file** on the server.
Instead, you configure environment variables directly in your **server or container environment**, e.g.:

### **1. On Linux Server**

When deploying (e.g., on EC2, Ubuntu, etc.):

```bash
export DB_HOST=my-prod-db-url
export DB_USER=admin
export DB_PASSWORD='very_secure_password'
export SECRET_KEY='prod_secret'
```

Then run your FastAPI app:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Pydantic will automatically read them from the system environment.

<br>
<br>

### **2. In Docker**

You can define environment variables in your `Dockerfile` or `docker-compose.yml`:

**docker-compose.yml**

```yaml
version: "3"
services:
  web:
    build: .
    environment:
      - DB_HOST=db
      - DB_USER=admin
      - DB_PASSWORD=${DB_PASSWORD}
      - SECRET_KEY=${SECRET_KEY}
    env_file:
      - .env.production
    ports:
      - "8000:8000"
```

<br>
<br>

### **3. On Cloud (e.g., AWS, Render, Railway, etc.)**

Every platform has an **“Environment Variables”** section where you can add them directly in the dashboard.
This is the safest method since the variables are encrypted and hidden from your code.

<br>
<br>

## **Summary Table**

| Environment             | How to Store Vars             | Example                      | Notes                       |
| ----------------------- | ----------------------------- | ---------------------------- | --------------------------- |
| **Development**         | `.env` file                   | `.env` in project root       | Add to `.gitignore`         |
| **Production (Server)** | `export VAR=value`            | `export DB_HOST=db-prod.com` | Use system environment      |
| **Docker**              | `env_file:` or `environment:` | in `docker-compose.yml`      | Keep `.env.production`      |
| **Cloud Platforms**     | Dashboard config              | AWS, Render, Vercel          | Most secure and recommended |

<br>
<br>

## ✅ **Best Practices**

1. **Never commit** `.env` files.
2. Use **different env files** for dev and production.
3. Validate your settings early — e.g.:

   ```python
   print(settings.dict())  # quickly check what’s being loaded
   ```

4. For secrets like API keys, prefer **platform-level env vars** (not files).
5. Keep consistent variable names (e.g., `DB_` prefix for all database settings).

<br>
<br>

- **why `settings` has values even though you never set them manually in code**.

<br>
<br>

## **1. The Key Idea**

When you create:

```python
settings = Settings()
```

you’re creating an instance of your `Settings` class (a subclass of `BaseSettings`).

Now — `BaseSettings` in Pydantic has a **special behavior**:
When the object is created, it automatically **loads values from external sources** — not from assignments in code.

<br>
<br>

## **2. What Happens Internally**

Let’s go step-by-step:

1. You define your class:

   ```python
   class Settings(BaseSettings):
       DB_HOST: str
       DB_USER: str
       DB_PASSWORD: str

       class Config:
           env_file = ".env"
   ```

2. You create an object:

   ```python
   settings = Settings()
   ```

3. When `Settings()` runs, Pydantic’s `BaseSettings` constructor automatically does this internally:

   - Look for each field name (`DB_HOST`, `DB_USER`, etc.) in:

     1. **System environment variables** (`os.environ`)
     2. **`.env` file**, if `Config.env_file` is defined

   - If found, assign the value to the attribute.
   - If not found, raise an error (unless you provided a default).

So when you do:

```python
print(settings.DB_USER)
```

You’re not accessing a manually set property — you’re accessing a value that was automatically pulled from the environment or `.env`.

<br>
<br>

## **3. Why It Works in Both Dev and Production**

- **In development:**
  `.env` file exists → `BaseSettings` reads from `.env`.

- **In production:**
  `.env` file is missing → it skips `.env` and reads from the **system environment** (`os.environ`), which your server/Docker/cloud injects.

Thus, `settings.DB_USER` works in both cases — same code, different data source.

<br>
<br>

## **4. Summary (one line)**

`BaseSettings` automatically populates the attributes of your `Settings` object from environment variables (system or `.env`) — so you never need to assign them manually.

<br>
<br>

Perfect — let’s go deep into **what it means when we say “Pydantic automatically reads from the system environment”**, especially in **production**.

<br>
<br>

---

<br>
<br>

## **Understanding What “System Environment” Means**

When you run any program (like your FastAPI app) on a machine — whether it’s your laptop, a server, or a container — that machine has an **environment**.
This environment includes a **set of key-value pairs** available to all processes, called **environment variables**.

You can see them by running:

```bash
printenv
```

or

```bash
echo $DB_HOST
```

These are stored **in the system memory**, not in a file.

So when we say “Pydantic reads from the system environment,” it means:

> It looks into the process’s environment (like `os.environ`) for variables that match the field names in your `Settings` class.

<br>
<br>

## **Example: How It Works Internally**

Let’s say your production server has this environment:

```bash
export DB_HOST=prod-db.company.com
export DB_USER=admin
export DB_PASSWORD=supersecurepass
export DB_NAME=main_db
export SECRET_KEY=prodsecret
```

Now when you run your FastAPI app:

```bash
uvicorn app.main:app
```

And your `settings.py` looks like this:

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    SECRET_KEY: str

settings = Settings()
```

What happens step-by-step:

1. Pydantic checks each field (e.g., `DB_HOST`, `DB_USER`, etc.).
2. For each field, it calls:

   ```python
   os.getenv("DB_HOST")
   ```

3. If the variable is found in the environment, Pydantic assigns it automatically to that field.
4. If it’s **not found** and there’s **no default value**, Pydantic raises a **ValidationError** (so you’ll know something is missing).

So, when your code runs:

```python
print(settings.DB_HOST)
```

You’ll get:

```
prod-db.company.com
```

— even though there’s **no `.env` file** in production.

That’s the key idea — Pydantic reads directly from **the environment of the process**, not just from a file.

<br>
<br>

## **Why You Don’t Need `.env` in Production**

In production:

- `.env` files can be a **security risk** if someone gets access to the server or container image.
- Instead, the hosting environment (like AWS, Docker, or Railway) manages those environment variables securely.

For example:

- **AWS EC2 / Linux server:**

  ```bash
  export SECRET_KEY="your_prod_secret"
  export DB_PASSWORD="your_prod_password"
  ```

- **Docker container:**

  ```yaml
  environment:
    - SECRET_KEY=your_prod_secret
    - DB_PASSWORD=your_prod_password
  ```

- **Render / Railway / Vercel / AWS ECS:**
  You add these variables in the **Environment Variables panel** in the dashboard.

All these platforms automatically inject these values into the container’s or system’s **environment memory**.
When your FastAPI app starts, `BaseSettings` reads them just like it would read from `.env`.

<br>
<br>

## **What Happens If Both Are Present (.env + system vars)**

If you **accidentally have both**, Pydantic uses this priority order:

1. **System environment variables**
2. **`.env` file variables**
3. **Default values defined in the class**

So, production system vars always **override** `.env` file values.
This ensures your production credentials always take priority.

<br>
<br>

## **Verifying It’s Working**

You can test that Pydantic is indeed reading from the system:

```python
import os
print(os.environ.get("DB_HOST"))     # Directly from environment
print(settings.DB_HOST)              # Pydantic reads from same source
```

Both will print the same value in production.

<br>
<br>

## **In Summary**

| Step | Where It Reads From               | Description                                             |
| ---- | --------------------------------- | ------------------------------------------------------- |
| 1    | System Environment (`os.environ`) | Variables set via `export`, Docker, or cloud dashboards |
| 2    | `.env` file (if configured)       | Only used in dev or if system vars are missing          |
| 3    | Default values in class           | Fallback when no env var found                          |

**So in production, you don’t need `.env` — just make sure your deployment environment has the variables set.**
Once your app starts, Pydantic automatically picks them up without you doing anything extra.

<br>
<br>

In short: nothing breaks.

If you define this:

```python
class Config:
    env_file = ".env"
```

Pydantic will **try** to load `.env` — but if it doesn’t exist (like in production), it just **skips it silently** and continues reading from the **system environment**.

✅ So in production:

- `.env` is ignored (if missing).
- Pydantic still loads variables from `os.environ` (system).
  No error, no crash.

<br>
<br>

---

<br>
<br>

## **What is a Composite Key?**

A **composite key** (also called a **composite primary key**) is a **primary key made up of two or more columns** that together uniquely identify a record in a table.

- Individually, none of those columns can uniquely identify a row.
- But **their combination** can.

<br>
<br>

## **Why Composite Keys Are Needed**

They’re useful when:

1. **No single column is unique enough** to act as a primary key.
2. You want to **enforce uniqueness across a combination of relationships**.

For example, in a table recording user votes on posts:

- A user can vote on **many posts**.
- A post can receive votes from **many users**.
- But **a single user should not be able to vote on the same post twice**.

So we combine `user_id` + `post_id` to make them **jointly unique** — that’s the composite key.

<br>
<br>

## **When to Use Composite Keys**

You use composite keys typically in **many-to-many relationship tables**, often called **association tables** or **junction tables**.
Examples:

- `student_course` (student_id + course_id)
- `author_book` (author_id + book_id)
- `vote` (user_id + post_id)

These tables don’t need their own `id` column because the combination of the foreign keys uniquely identifies each record.

<br>
<br>

## **Example Explained (Your Code)**

```python
class Vote(Base):
    __tablename__ = "votes"

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
```

### **How It Works**

- Both `user_id` and `post_id` are marked as `primary_key=True`.
- Together, they form a **composite primary key** `(user_id, post_id)`.
- This ensures:

  - A user cannot vote on the same post twice.
  - But the same user can vote on different posts.
  - And multiple users can vote on the same post.

### **Behavior in PostgreSQL**

PostgreSQL internally enforces uniqueness on the combination `(user_id, post_id)` via a **composite unique index** automatically created for the composite primary key.

<br>
<br>

## **Example in SQL**

The equivalent PostgreSQL table would be:

```sql
CREATE TABLE votes (
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    post_id INTEGER REFERENCES posts(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, post_id)
);
```

This tells PostgreSQL:

> The pair `(user_id, post_id)` must be unique and non-null across the table.

<br>
<br>

✅ **In short:**

- A composite key = primary key made of multiple columns.
- It’s needed when **only the combination of columns uniquely identifies a row**.
- Commonly used in **many-to-many relationship tables** (like votes, enrollments, likes, etc.).

<br>
<br>

---

<br>
<br>

## **What is a Junction (or Association) Table?**

A **junction table** (also called an **association table** or **bridge table**) is an **intermediate table** that connects **two tables in a many-to-many relationship**.

It doesn’t usually have its own standalone meaning — its purpose is purely to **link records** from two other tables.

<br>
<br>

## **Why It’s Needed**

Relational databases (like PostgreSQL) **don’t allow direct many-to-many relationships** between two tables.
Instead, you must break that relationship into **two one-to-many relationships** using a third table (the junction table).

So the logic is:

- **Table A** ↔ **Junction Table** ↔ **Table B**

This middle table stores **foreign keys** from both sides to record the connection.

<br>
<br>

## **Real Example**

Let’s use your **vote system** example again:

- One **user** can vote on many **posts**.
- One **post** can receive votes from many **users**.

That’s a **many-to-many** relationship.

We can’t directly link `users` and `posts` because each side can have multiple associations with the other.
So, we create a **junction table** called `votes`.

<br>
<br>

### **Diagram (Conceptually)**

```
users              votes              posts
-------             -------            -------
id (PK)  ──┐     user_id (FK)  ─┐   id (PK)
name        │                   │     title
...          │                   │     ...
             └───────────────────┘
                 post_id (FK)
```

<br>
<br>

## **SQL Example**

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL
);

CREATE TABLE votes (
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    post_id INTEGER REFERENCES posts(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, post_id)
);
```

Here, the **`votes`** table acts as the junction:

- `user_id` links to `users.id`
- `post_id` links to `posts.id`
- `(user_id, post_id)` as **composite key** ensures each user can vote only once per post.

<br>
<br>

## **In SQLAlchemy (ORM Example)**

You already have:

```python
class Vote(Base):
    __tablename__ = "votes"

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
```

Now you can define relationships in your models:

```python
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)

    voted_posts = relationship("Post", secondary="votes", back_populates="voters")


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    voters = relationship("User", secondary="votes", back_populates="voted_posts")
```

### **What Happens Here**

- The `secondary="votes"` tells SQLAlchemy to use the `votes` table as a **link table**.
- The `back_populates` enables you to navigate both ways:

  - `user.voted_posts` → list of posts that the user voted on.
  - `post.voters` → list of users who voted on that post.

<br>
<br>

## **Key Properties of Junction Tables**

| Property                       | Description                                                                     |
| ------------------------------ | ------------------------------------------------------------------------------- |
| **Has two foreign keys**       | Each linking to one side of the relationship.                                   |
| **Often uses a composite key** | `(foreign_key_1, foreign_key_2)` ensures uniqueness.                            |
| **No extra columns (usually)** | But you _can_ add others (e.g., `created_at` to record when the vote occurred). |
| **Used for many-to-many**      | Converts the relationship into two one-to-many relationships internally.        |

<br>
<br>

## **Optional: Enriched Junction Table**

Sometimes, you need to **add metadata** to the relationship — for example, to record when the vote was made or its type (upvote/downvote).
Then it becomes an **association object** instead of just a table.

Example:

```python
class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id"), primary_key=True)
    vote_type = Column(String, default="upvote")
    created_at = Column(DateTime, default=func.now())
```

This adds meaning to the relationship.

<br>
<br>

✅ **Summary**

| Concept            | Explanation                                                                   |
| ------------------ | ----------------------------------------------------------------------------- |
| **Junction Table** | A linking table used to represent a many-to-many relationship.                |
| **Contains**       | Foreign keys from both related tables (and optionally other attributes).      |
| **Composite Key**  | Usually `(fk1, fk2)` to ensure each pair is unique.                           |
| **Used When**      | Two entities have a many-to-many relationship (like users ↔ posts via votes). |
| **Example Tables** | `votes`, `student_courses`, `author_books`, `followers`, etc.                 |

<br>
<br>

---

<br>
<br>

## **How to Identify When You Need a Junction (Association) Table**

You should think in terms of **relationships between entities** — specifically, how many instances of one entity can relate to another.

That’s the **cardinality** of the relationship.

<br>
<br>

## **Step 1: Identify the Relationship Type**

Every relationship between two entities (tables) can be one of the following:

| Relationship Type      | Meaning                                                         | Example                                                         | Implementation                         |
| ---------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | -------------------------------------- |
| **One-to-One (1:1)**   | One record in table A relates to only one record in table B     | Each user has one profile                                       | Add a foreign key in one of the tables |
| **One-to-Many (1:N)**  | One record in table A can be related to many records in table B | A user has many posts                                           | Add a foreign key in the “many” side   |
| **Many-to-Many (M:N)** | Many records in table A relate to many records in table B       | Users can like many posts, and posts can be liked by many users | **Use a junction (association) table** |

So, **junction tables are used _only_ for Many-to-Many (M:N) relationships**.

<br>
<br>

## **Step 2: Recognize the Many-to-Many Pattern**

Ask yourself these two questions:

1. Can one record in **Table A** be associated with multiple records in **Table B**?
2. Can one record in **Table B** be associated with multiple records in **Table A**?

If **both answers are YES**, → you need a **junction table**.

<br>
<br>

### **Example Scenarios**

| Scenario                      | Relationship                                                                      | Why Junction Table?                  |
| ----------------------------- | --------------------------------------------------------------------------------- | ------------------------------------ |
| Users vote on posts           | Many users can vote on many posts                                                 | Yes — use a `votes` table            |
| Students enroll in courses    | Many students can join many courses                                               | Yes — use an `enrollments` table     |
| Products belong to categories | A product can have multiple categories, and a category can have multiple products | Yes — use a `product_category` table |
| Authors write books           | A book can have multiple authors, and an author can write multiple books          | Yes — use an `author_book` table     |

<br>
<br>

## **Step 3: Understand Why Foreign Keys Alone Don’t Work**

If you try to model a many-to-many relationship without a junction table, you run into redundancy or data integrity issues.

### Example — Wrong Way:

```sql
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title TEXT,
  user_ids INTEGER[]  -- list of users who liked the post ❌
);
```

Problems:

- Arrays violate normalization.
- Hard to query (e.g., can’t easily join on user_id).
- No way to enforce foreign key constraints for each user_id.

Hence, relational databases require a **normalized approach** using a junction table.

<br>
<br>

## **Step 4: Visualize the “Bridge” Pattern**

You can visualize it like this:

```
Users (A)
   ↓ 1:N
Votes (junction)
   ↑ N:1
Posts (B)
```

- Each user can have multiple votes → One-to-Many from Users → Votes
- Each post can have multiple votes → One-to-Many from Posts → Votes
- Together, this makes Users ↔ Posts a Many-to-Many relationship through Votes.

<br>
<br>

## **Step 5: When You Don’t Need a Junction Table**

You **don’t** need a junction table if:

- Only one side is “many” (e.g., a user has many posts, but a post belongs to one user).
  → Then, just add `user_id` as a foreign key in `posts`.
- There’s a strict one-to-one relationship (e.g., each user has one profile).
  → Then, link directly with a foreign key and unique constraint.

<br>
<br>

## **Step 6: Optional — When to Use an Association Table with Extra Data**

If you later realize your “link” needs its own attributes (like timestamp, rating, or status), it’s still a junction table — but now it becomes an **association table** with meaning.

Example:

```python
class Enrollment(Base):
    __tablename__ = "enrollments"
    student_id = Column(Integer, ForeignKey("students.id"), primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.id"), primary_key=True)
    enrolled_on = Column(DateTime, default=func.now())  # extra attribute
    grade = Column(String)
```

Now, you’re not just linking students and courses — you’re describing _how_ they’re linked (when they enrolled, what grade they got).

<br>
<br>

## ✅ **In Summary:**

| Checkpoint | Ask Yourself                                            | Decision                            |
| ---------- | ------------------------------------------------------- | ----------------------------------- |
| 1️⃣         | Can one record in A relate to many in B?                | → Maybe One-to-Many                 |
| 2️⃣         | Can one record in B relate to many in A?                | → If yes to both → **Many-to-Many** |
| 3️⃣         | Are both “many”?                                        | → Use a **Junction Table**          |
| 4️⃣         | Does the link need extra data (like timestamp or type)? | → Make it an **Association Table**  |

<br>
<br>

---

<br>
<br>

## **Joins in PostgreSQL**

- A JOIN combines rows from two (or more) tables using a related column between them. Joins let you answer questions like “which posts does each user have?”, “which users have no posts?”, or “show posts even when the author is missing”.

- Think of joins as a way to **combine two or more lists (tables) into one new, combined list** based on a shared piece of information (a "matching key").

Imagine you have two separate lists:

1.  A list of all **Users** on your website.
2.  A list of all **Posts** written on your website.

The `Users` list has a unique `UserID`. The `Posts` list has a `UserID` to show _who_ wrote it. A JOIN lets you create a new list that shows the `Username` and the `Post Content` side-by-side, by matching the `UserID` from both lists.

<br>
<br>

## The Example Tables

For all our examples (except the last one), we will use these two simple tables: `users` and `posts`.

**Table: `users`**
This table lists all registered users.

| id  | username |
| :-- | :------- |
| 1   | Alice    |
| 2   | Bob      |
| 3   | Charlie  |

**Table: `posts`**
This table lists all posts. The `user_id` column links to the `id` in the `users` table.

| id  | content          | user_id |
| :-- | :--------------- | :------ |
| 101 | 'Hello world\!'  | 1       |
| 102 | 'My first post.' | 1       |
| 103 | 'SQL is fun.'    | 2       |
| 104 | 'Orphan post.'   | 5       |

**Important Notes:**

- **Alice (id=1)** has two posts.
- **Bob (id=2)** has one post.
- **Charlie (id=3)** has **no posts**.
- **'Orphan post.' (id=104)** has `user_id=5`, but there is **no user with id=5**.

Let's explore how different joins handle this data.

<br>
<br>

## `INNER JOIN`

- **What it is:** The `INNER JOIN` is the "perfect matches only" join. It combines rows from two tables **only if** the matching key exists in **both** tables. If a user has no posts, they won't be in the result. If a post has no matching user, it won't be in the result.

- **Use Case:** Use this when you _only_ want to see data that has a complete relationship.

- **Real-World Scenario:** "Show me all posts _and_ the name of the user who wrote them. I don't care about users who haven't posted, and I don't care about posts that are broken (orphaned)."

### SQL Query

```sql
SELECT u.username, p.content
FROM users u
INNER JOIN posts p ON u.id = p.user_id;
```

### SQLAlchemy Query

```python
# ORM (Object Relational Mapper) style
# Assumes you have User and Post models
query = db.session.query(User.username, Post.content).join(Post, User.id == Post.user_id)

# Core (Table objects) style
# Assumes you have 'users' and 'posts' table objects
query = db.select(users.c.username, posts.c.content).join(posts, users.c.id == posts.c.user_id)
```

### Resulting Table

| username | content          |
| :------- | :--------------- |
| Alice    | 'Hello world\!'  |
| Alice    | 'My first post.' |
| Bob      | 'SQL is fun.'    |

**Explanation:**

- **Alice** and **Bob** are included because their `id` (1, 2) matches a `user_id` in the `posts` table.
- **Charlie** is **gone** because his `id` (3) is not in the `posts` table.
- The **'Orphan post.'** is **gone** because its `user_id` (5) is not in the `users` table.

<br>
<br>

## `LEFT OUTER JOIN` (or just `LEFT JOIN`)

- **What it is:** The `LEFT JOIN` is the "left side is king" join. It gets **everything** from the **left** table (the one after `FROM`) and then brings in matching data from the right table. If there's no match on the right, it just fills in the right-side columns with `NULL` (empty).

- **Use Case:** Use this when you want all items from one list, regardless of whether they have a match in the second list.

- **Real-World Scenario:** "Show me **all** users, and _if_ they have any posts, show those too. I must see every user, even if they've never posted."

### SQL Query

```sql
SELECT u.username, p.content
FROM users u
LEFT JOIN posts p ON u.id = p.user_id;
```

### SQLAlchemy Query

```python
# ORM style
query = db.session.query(User.username, Post.content).outerjoin(Post, User.id == Post.user_id)

# Core style
query = db.select(users.c.username, posts.c.content).join(posts, users.c.id == posts.c.user_id, isouter=True)
```

### Resulting Table

| username | content          |
| :------- | :--------------- |
| Alice    | 'Hello world\!'  |
| Alice    | 'My first post.' |
| Bob      | 'SQL is fun.'    |
| Charlie  | `NULL`           |

**Explanation:**

- This query starts with the `users` table (the "left" table).
- It finds matches for **Alice** and **Bob**.
- It gets to **Charlie**, looks for posts with `user_id=3`, finds none, but **still keeps Charlie** in the list. It puts `NULL` in the `content` column for him.
- The **'Orphan post.'** is still gone because it has no match in the `users` table, which is the "left" table we started with.

<br>
<br>

## `RIGHT OUTER JOIN` (or just `RIGHT JOIN`)

- **What it is:** The `RIGHT JOIN` is the "right side is king" join. It's the exact opposite of a `LEFT JOIN`. It gets **everything** from the **right** table (the one after `JOIN`) and brings in matching data from the left. If there's no match on the left, it fills in the left-side columns with `NULL`.

- **Use Case:** This is less common, but useful for data cleanup or when the "right" table is your main focus.

- **Real-World Scenario:** "Show me **all** posts, and _if_ they have a valid author, show the author's name. I need to see every post, even if the author has been deleted." This helps you find orphan data.

### SQL Query

```sql
SELECT u.username, p.content
FROM users u
RIGHT JOIN posts p ON u.id = p.user_id;
```

### SQLAlchemy Query

```python
# There's no direct `.right_outerjoin()` in SQLAlchemy's ORM.
# You achieve it by swapping the tables and using a LEFT JOIN.

# ORM style (by changing the "from" entity)
query = db.session.query(User.username, Post.content).select_from(Post).outerjoin(User, Post.user_id == User.id)

# Core style (swapping order)
query = db.select(users.c.username, posts.c.content).select_from(posts).join(users, users.c.id == posts.c.user_id, isouter=True)
```

### Resulting Table

| username | content          |
| :------- | :--------------- |
| Alice    | 'Hello world\!'  |
| Alice    | 'My first post.' |
| Bob      | 'SQL is fun.'    |
| `NULL`   | 'Orphan post.'   |

**Explanation:**

- This query starts with the `posts` table (the "right" table).
- It finds matches for the first three posts.
- It gets to the **'Orphan post.'**, looks for a user with `id=5`, finds none, but **still keeps the post** in the list. It puts `NULL` in the `username` column for it.
- **Charlie** is **gone** because he had no posts, so he wasn't in the "right" table to begin with.

<br>
<br>

## `FULL OUTER JOIN` (or just `FULL JOIN`)

- **What it is:** The `FULL JOIN` is the "get everything from everyone" join. It combines a `LEFT JOIN` and a `RIGHT JOIN`. It returns **all** rows from **both** tables. If there's a match, the rows are combined. If there's no match, the missing side is filled with `NULL`.

- **Use Case:** Use this when you need a complete, comprehensive view of all data from both tables, including all relationships and all non-relationships.

- **Real-World Scenario:** "I need a complete audit. Show me every user and their posts, _and_ show me any users who have no posts, _and_ show me any posts that have no user."

### SQL Query

```sql
SELECT u.username, p.content
FROM users u
FULL OUTER JOIN posts p ON u.id = p.user_id;
```

### SQLAlchemy Query

```python
# ORM style
query = db.session.query(User.username, Post.content).outerjoin(Post, User.id == Post.user_id, full=True)

# Core style
query = db.select(users.c.username, posts.c.content).join(posts, users.c.id == posts.c.user_id, full=True)
```

### Resulting Table

| username | content          |
| :------- | :--------------- |
| Alice    | 'Hello world\!'  |
| Alice    | 'My first post.' |
| Bob      | 'SQL is fun.'    |
| Charlie  | `NULL`           |
| `NULL`   | 'Orphan post.'   |

**Explanation:**
This result gives you the full picture:

- **Matches:** Alice and Bob with their posts.
- **Left-only:** Charlie, the user with no posts (content is `NULL`).
- **Right-only:** The 'Orphan post.', the post with no user (username is `NULL`).

<br>
<br>

## A Note: `OUTER JOIN` vs. `LEFT INNER JOIN`

You mentioned a few terms that can be confusing:

- **`OUTER JOIN`:** This isn't a command by itself. It's the _category_ of joins that include non-matching rows. `LEFT OUTER JOIN`, `RIGHT OUTER JOIN`, and `FULL OUTER JOIN` are the three types. Most people just write `LEFT JOIN` because the `OUTER` part is implied.
- **`LEFT INNER JOIN` and `RIGHT INNER JOIN`:** These are **not valid SQL commands**. This is a common point of confusion. You are mixing two opposite ideas.
  - **`INNER`** means "matches only."
  - **`LEFT`** (or `RIGHT`) means "include non-matches from this side."
  - You can't have both. It's either an `INNER JOIN` (matches only) or an `OUTER JOIN` (like `LEFT JOIN`, which includes non-matches).

<br>
<br>

## `SELF JOIN`

- **What it is:** A `SELF JOIN` isn't a new _type_ of join. It's a regular `INNER JOIN` or `LEFT JOIN`, but you are joining a table **to itself**. This sounds weird, but it's very useful when a table has a relationship with its own data.

- **Use Case:** Use this when a table references itself. The classic example is an "employees" table where one column is `manager_id`, and the manager is also an employee in the same table.

- **Real-World Scenario:** "For every employee, show me their name and their manager's name."

Let's use a new table for this one, as `users`/`posts` doesn't fit.

**Table: `employees`**

| id  | name       | manager_id |
| :-- | :--------- | :--------- |
| 1   | 'Big Boss' | `NULL`     |
| 2   | 'Alice'    | 1          |
| 3   | 'Bob'      | 2          |
| 4   | 'Charlie'  | 2          |

### SQL Query

To do this, we have to _pretend_ the `employees` table is two separate tables by giving it two different "aliases" (nicknames): `e` (for the employee) and `m` (for the manager).

```sql
SELECT
    e.name AS employee_name,
    m.name AS manager_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

_(I use a `LEFT JOIN` so the 'Big Boss', who has no manager, is still included in the list)._

### SQLAlchemy Query

```python
# This requires aliasing the table/model
from sqlalchemy.orm import aliased

# ORM style
Manager = aliased(Employee) # Create the alias
query = db.session.query(
    Employee.name.label('employee_name'),
    Manager.name.label('manager_name')
).outerjoin(Manager, Employee.manager_id == Manager.id)

# Core style
e = employees.alias('e') # Alias 1
m = employees.alias('m') # Alias 2
query = db.select(
    e.c.name.label('employee_name'),
    m.c.name.label('manager_name')
).select_from(e.outerjoin(m, e.c.manager_id == m.c.id))
```

### Resulting Table

| employee_name | manager_name |
| :------------ | :----------- |
| 'Big Boss'    | `NULL`       |
| 'Alice'       | 'Big Boss'   |
| 'Bob'         | 'Alice'      |
| 'Charlie'     | 'Alice'      |

**Explanation:**
We "joined" the table to itself. For each row `e`, we looked up the row `m` where `e.manager_id` (e.g., Alice's `manager_id` of 1) matched `m.id` (the 'Big Boss' row's `id` of 1). This lets us pull the manager's `name` and the employee's `name` into the same row.

<br>
<br>

## `NATURAL JOIN`

- **What it is:** A `NATURAL JOIN` is a special type of `INNER JOIN`. Instead of you telling it which columns to join `ON` (like `ON u.id = p.user_id`), it **automatically** looks for **all columns in both tables that have the exact same name** and joins on them.

- **Why it's Dangerous:** This is extremely risky\! ☢️

  1.  It's implicit. Someone reading your query might not know which columns are being joined.
  2.  If someone adds a new column with the same name to both tables later (like an `updated_at` column), your query's logic will **silently change** and either break or produce wrong data.
  3.  It often doesn't join on the columns you _think_ it will.

- **Use Case:** (This is more of a _warning_ than a use case). You should only use this if you are 100% certain that the _only_ columns with matching names are the keys you want to join on. Most developers avoid it entirely in production code.

- **Real-World Scenario:** "I'm working on a quick, one-time analysis and my two tables (`orders` and `order_details`) _only_ share the `order_id` column and no other names. I'll use `NATURAL JOIN` to save 10 seconds of typing."

Let's see what happens when we try to `NATURAL JOIN` our `users` and `posts` tables.

- `users` has columns: `id`, `username`
- `posts` has columns: `id`, `content`, `user_id`

The _only_ column name they share is `id`. Therefore, PostgreSQL will try to run this query:
`... FROM users INNER JOIN posts ON users.id = posts.id;`

This is **not** what we want\! We want to join on `users.id = posts.user_id`.

### SQL Query

```sql
SELECT u.username, p.content
FROM users u
NATURAL JOIN posts p;
```

### SQLAlchemy Query

SQLAlchemy's ORM and Core **do not provide a simple `.natural_join()` method** because it is considered an anti-pattern. You would have to write it as raw text, which signals that you're doing something unusual.

```python
# You must use raw text, as SQLAlchemy intentionally discourages this.
from sqlalchemy import text

query = db.session.execute(
    text("SELECT users.username, posts.content FROM users NATURAL JOIN posts")
)
```

### Resulting Table

(The query `... ON users.id = posts.id` is executed)

| username | content |
| :------- | :------ |
|          |         |

**Explanation:**
The query returned an **empty table\!** Why?
Because it tried to match `users.id` (which has values 1, 2, 3) with `posts.id` (which has values 101, 102, 103, 104).
There were **no matches**, so the `INNER JOIN` logic returned nothing.

This perfectly illustrates the danger of `NATURAL JOIN`. It did something, but it was completely wrong, and it failed silently.

<br>
<br>

## `CROSS JOIN` (Cartesian Join)

- **What it is:** The `CROSS JOIN` is the "combine everything" join. It takes **every single row from the first table** and pairs it with **every single row from the second table**. It does not use an `ON` clause or any matching keys.

- If `users` has 3 rows and `posts` has 4 rows, the `CROSS JOIN` will produce $3 \times 4 = 12$ rows. This can get huge, fast\! (A 1,000-row table joined to a 1,000-row table creates 1,000,000 rows).

- **Use Case:** You use this when you need to generate a "matrix" or a complete set of all possible combinations between two lists.

- **Real-World Scenario:** "I have a `TShirts` table (Small, Medium, Large) and a `Colors` table (Red, Green, Blue). I need to generate a master list of all possible products I can sell (Small Red, Small Green, Small Blue, Medium Red, etc.)."

Let's apply this to our `users` and `posts`. The (somewhat strange) scenario would be: "I want to show every user a list of every post on the site."

### SQL Query

```sql
SELECT u.username, p.content
FROM users u
CROSS JOIN posts p;

-- An older (and sometimes confusing) syntax also does this:
-- SELECT u.username, p.content FROM users u, posts p;
```

### SQLAlchemy Query

```python
# ORM style
query = db.session.query(User.username, Post.content).cross_join(Post)

# Core style
query = db.select(users.c.username, posts.c.content).select_from(
    users.cross_join(posts)
)
```

### Resulting Table

(Total rows: 3 users $\times$ 4 posts = 12 rows)

| username | content          |
| :------- | :--------------- |
| Alice    | 'Hello world\!'  |
| Alice    | 'My first post.' |
| Alice    | 'SQL is fun.'    |
| Alice    | 'Orphan post.'   |
| Bob      | 'Hello world\!'  |
| Bob      | 'My first post.' |
| Bob      | 'SQL is fun.'    |
| Bob      | 'Orphan post.'   |
| Charlie  | 'Hello world\!'  |
| Charlie  | 'My first post.' |
| Charlie  | 'SQL is fun.'    |
| Charlie  | 'Orphan post.'   |

**Explanation:**
As you can see, the result is a simple "brute force" combination. Alice is paired with all 4 posts, Bob is paired with all 4 posts, and Charlie is paired with all 4 posts. The `user_id` on the post is completely ignored, as is the `id` of the user. We just get all possible pairs.

<br>
<br>

---

<br>
<br>

**In PostgreSQL (and all SQL):**

When you use GROUP BY, every column in your SELECT list must either:

- Appear in the GROUP BY clause, or

- Be inside an aggregate function (COUNT(), SUM(), MAX(), MIN(), AVG(), etc.)

- In PostgreSQL when you group by a primary key (or any unique key), you can safely reference all columns from that table — because that key uniquely identifies every other column in that table.

- let’s unpack exactly **why** `SELECT user.*` sometimes works in PostgreSQL _even though not all fields are in the GROUP BY_.

<br>
<br>

## ⚙️ What’s actually happening behind the scenes

PostgreSQL is **a bit more flexible than other databases (like MySQL in strict mode or SQL Server)** because of something called **“functional dependency inference.”**

In short:

> If PostgreSQL can logically deduce that one column’s value is **uniquely determined** by a column in the GROUP BY clause, it allows you to select that column **without explicitly adding it to GROUP BY.**

<br>
<br>

## 🧠 The functional dependency rule

Let’s say you write:

```sql
SELECT users.*, COUNT(posts.id)
FROM users
LEFT JOIN posts ON users.id = posts.user_id
GROUP BY users.id;
```

Even though you didn’t explicitly `GROUP BY users.username` or `users.email`, **PostgreSQL allows it** because:

- `users.id` is the **PRIMARY KEY** (unique for each user).
- Therefore, `users.id → users.username`, `users.id → users.email`, etc.
  (We say “username is _functionally dependent_ on id.”)

PostgreSQL says:

> “Since all other columns in this table are uniquely determined by `users.id`, I can safely return them — they’ll always have the same value within each group.”

✅ So this query is perfectly legal **in PostgreSQL** (and produces deterministic results).

<br>
<br>

## 🚫 Why this doesn’t work in other databases

Try the same query in **MySQL (with ONLY_FULL_GROUP_BY)** or **SQL Server** — it will throw an error like:

> Column 'users.username' is invalid in the select list because it is not contained in either an aggregate function or the GROUP BY clause.

That’s because those databases don’t automatically reason about **functional dependency**.

<br>
<br>

## 🧩 A simpler analogy

Imagine grouping students by their unique `roll_number`:

```sql
SELECT roll_number, student_name
FROM students
GROUP BY roll_number;
```

✅ Works fine in PostgreSQL — because each roll number uniquely identifies a student name.
There’s no ambiguity: one roll number = one name.

But if you grouped by `class_name` instead:

```sql
SELECT class_name, student_name
FROM students
GROUP BY class_name;
```

❌ PostgreSQL will throw an error — because each class has **many students**, and it can’t decide which student name to show per class.

<br>
<br>

## ⚠️ Important: When it will **NOT** work

If the column you group by is **not unique**, PostgreSQL will **not** allow `SELECT *` unless you aggregate the rest.

Example:

```sql
SELECT users.*, COUNT(posts.id)
FROM users
JOIN posts ON users.id = posts.user_id
GROUP BY users.username;
```

❌ Error:

> column "users.id" must appear in the GROUP BY clause or be used in an aggregate function.

Because `username` is **not guaranteed unique** — multiple users could share the same username (unless you defined it as UNIQUE in your schema).

<br>
<br>

## ✅ Summary

| Situation                                 | Works?                           | Why                                          |
| ----------------------------------------- | -------------------------------- | -------------------------------------------- |
| `GROUP BY` includes **primary key**       | ✅ Yes                           | All other columns are functionally dependent |
| `GROUP BY` includes **unique column**     | ✅ Yes                           | Unique key ensures dependency                |
| `GROUP BY` includes **non-unique column** | ❌ No                            | Ambiguity — multiple rows may differ         |
| Using `SELECT *`                          | ✅ Only if grouped by unique key |                                              |
| Other databases                           | ❌ Often fail                    | They don’t infer dependencies                |

<br>
<br>

## 🧩 Key idea to remember

> PostgreSQL allows `SELECT *` with GROUP BY **only when it can prove there’s no ambiguity** — typically when grouping by a unique or primary key.

So in your case,
`user.*` worked because you grouped by `user.id`, and `id` is the **primary key**, which **functionally determines** all other fields of that user.

<br>
<br>

---

<br>
<br>

## **What is Database Migration?**

**Database migration** means **transferring or changing a database’s structure, schema, or data** — usually from one state to another.

It typically refers to:

1. **Schema Migration** → Changing the *structure* of the database (tables, columns, constraints, relationships, etc.)
   Example: Adding a new column `price` to a `products` table.

2. **Data Migration** → Moving *actual data* between databases or formats.
   Example: Moving data from a MySQL database to PostgreSQL.

<br>
<br>

## **Why We Need Database Migration**

Migrations are essential for maintaining a **consistent and version-controlled database** as an application evolves.

### **1. Evolving Application Requirements**

When your application changes — like adding new features — your database schema must change too.
Example: If you add a new feature for “user profiles,” you might need a new `profiles` table.

### **2. Version Control for Database Schema**

Just like source code is tracked in Git, migrations help track database changes (who changed what and when).

### **3. Team Collaboration**

In a team environment, everyone’s local and production databases must stay synchronized with the same structure.

### **4. Continuous Deployment**

During CI/CD, migrations allow databases to automatically update to the correct version during deployment.

### **5. Portability / Database Switch**

When moving from one database to another (e.g., SQLite → PostgreSQL), migrations help automate the transformation.

<br>
<br>

## **What Are Database Migration Tools?**

**Migration tools** help automate, track, and manage database schema or data changes.
They prevent manual SQL errors and ensure smooth upgrades/downgrades.

<br>
<br>

### **Common Database Migration Tools**

| **Tool**                             | **Description / Usage**                                                              |
| ------------------------------------ | ------------------------------------------------------------------------------------ |
| **Alembic (Python)**                 | Used with SQLAlchemy & FastAPI/Django; handles schema migrations in Python projects. |
| **Flyway**                           | Java-based, supports many databases; migrations defined via SQL or Java code.        |
| **Liquibase**                        | XML/JSON/YAML-based migration tool for enterprise-level projects.                    |
| **Django Migrations**                | Built into Django ORM; automatically generates migration scripts for schema changes. |
| **Knex.js Migrations**               | For Node.js apps using Knex; migrations are JavaScript files.                        |
| **FluentMigrator (.NET)**            | Used in .NET ecosystem; migrations are written in C#.                                |
| **Liquibase / Flyway (Spring Boot)** | Integrated in Java projects for managing schema versions.                            |
| **Prisma Migrate**                   | Used with Prisma ORM (Node.js); easy declarative migration tool.                     |

<br>
<br>

---

<br>
<br>


## **What is Alembic?**

**Alembic** is a **database migration tool** built specifically to work with **SQLAlchemy**.
It helps you **track, version, and apply changes** to your database schema — just like Git does for your code.

Think of Alembic as a **"version control system for your database structure."**

<br>
<br>

## **Why Do We Need Alembic If We Already Have SQLAlchemy?**

Let’s compare their roles:

| **Feature**                  | **SQLAlchemy**                                                    | **Alembic**                                                           |
| ---------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------- |
| **Purpose**                  | ORM for defining database models (tables, relationships, etc.)    | Tool for managing and version-controlling schema changes (migrations) |
| **Focus**                    | Runtime interaction — query, insert, update, delete data          | Schema evolution — alter tables, add/remove columns, track versions   |
| **Automatic Schema Updates** | ❌ Does *not* automatically update the database when models change | ✅ Automatically generates migration scripts based on model changes    |
| **Used For**                 | Mapping Python classes → database tables                          | Updating database structure when models evolve                        |
| **Analogy**                  | Code that defines the current structure                           | Git that tracks all structural changes over time                      |

<br>
<br>

## **Why Alembic Became Necessary**

Let’s look at a real example 👇

### **Without Alembic**

You define models in SQLAlchemy:

```python
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
```

Then, suppose later you modify it:

```python
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)  # new field added
```

Now, your Python model has changed, but your **database table** still does **not have an `email` column**.
SQLAlchemy **does not** automatically detect and apply this change to the actual database.

You’d have to manually write:

```sql
ALTER TABLE users ADD COLUMN email VARCHAR;
```

This is risky, especially in production — you could break things or lose data.

<br>
<br>

### **With Alembic**

You just run:

```bash
alembic revision --autogenerate -m "Add email column to users"
alembic upgrade head
```

✅ Alembic **detects** that `email` was added
✅ Generates a **migration file** describing how to apply this change
✅ Applies it safely to your database

Now your **models** and **database schema** are perfectly in sync.

<br>
<br>

## **Key Benefits of Alembic**

1. **Automatic detection of schema changes** (`--autogenerate`).
2. **Version-controlled migrations** (each migration file is tracked).
3. **Rollback support** — you can downgrade if something breaks.
4. **Team collaboration** — same migrations work across environments.
5. **CI/CD ready** — integrates into deployment pipelines easily.

<br>
<br>

---

<br>
<br>

## **Complete, practical, step-by-step guide to set up, configure, and use Alembic**

### **Prerequisites**

* Python project with virtualenv/venv.
* SQLAlchemy models already defined (or plan to create them).
* A database (Postgres, MySQL, SQLite, etc.) and connection URL.
* `pip install alembic` (and `asyncpg` / DB driver if using async).

<br>
<br>

### **Project layout (example)**

```
myproject/
├─ app/
│  ├─ db.py            # SQLAlchemy engine/session
│  ├─ models.py        # SQLAlchemy ORM models (Base metadata)
│  └─ __init__.py
├─ alembic.ini
├─ alembic/            # created by `alembic init`
│  ├─ env.py
│  ├─ script.py.mako
│  └─ versions/
└─ pyproject.toml / requirements.txt
```

<br>
<br>

### **1) Install Alembic**

`pip install alembic`
(If using async Postgres): `pip install asyncpg`
Explanation: Alembic itself is pure Python and integrates with SQLAlchemy; DB drivers are needed to actually connect.

<br>
<br>

### **2) Initialize Alembic in your project**

From project root:

```
alembic init alembic
```

What this creates:

* `alembic.ini` — main config file (DB URL, logging).
* `alembic/` dir with `env.py`, `script.py.mako`, `versions/` folder for migration files.

<br>
<br>

### **3) Configure alembic.ini**

Open `alembic.ini` and set your SQLAlchemy URL or leave it out and supply it in `env.py`. Example:

```
[alembic]
script_location = alembic
sqlalchemy.url = postgresql+psycopg2://user:pass@localhost/dbname
```

Recommendation: For security and environment flexibility, do NOT hardcode creds in `alembic.ini`. Instead, load URL from environment variables inside `env.py`.

<br>
<br>

### **4) Point Alembic to your models (target_metadata)**

Alembic needs your `MetaData` to autogenerate migrations. In `alembic/env.py` you need to import the `Base.metadata` from your models and set `target_metadata`.

Example `app/models.py`:

```python
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
```

Then in `alembic/env.py` (short):

```python
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.models import Base   # import your Base
target_metadata = Base.metadata
```

Explanation: `target_metadata` is what Alembic compares with the live DB schema to autogenerate diffs.

<br>
<br>

### **5) Best practice: naming_convention for constraints**

To make migrations stable (especially for SQLite and autogenerate), define a naming convention in your `MetaData`:

```python
from sqlalchemy import MetaData
naming_convention = {
  "ix": "ix_%(column_0_label)s",
  "uq": "uq_%(table_name)s_%(column_0_name)s",
  "ck": "ck_%(table_name)s_%(constraint_name)s",
  "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
  "pk": "pk_%(table_name)s"
}
Base = declarative_base(metadata=MetaData(naming_convention=naming_convention))
```

Why: Alembic can predict constraint names instead of creating random names which cause noisy migrations.

<br>
<br>

### **6) Using Alembic with synchronous SQLAlchemy (classic)**

Typical `env.py` portions (sync):

```python
from sqlalchemy import engine_from_config, pool
from alembic import context
config = context.config

# load target_metadata as above
target_metadata = Base.metadata

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata, compare_type=True)
        with context.begin_transaction():
            context.run_migrations()
```

`compare_type=True` tells Alembic to detect type changes (e.g. Integer->BigInteger).

<br>
<br>

### **7) Using Alembic with async SQLAlchemy (FastAPI pattern)**

If you use `sqlalchemy.ext.asyncio.create_async_engine`, your `env.py` must use `run_sync` to run migrations synchronously via a sync context. Example `env.py` (async-ready):

```python
from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context
import asyncio, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.models import Base

config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata

def run_migrations_offline():
    url = os.getenv("DATABASE_URL")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection: Connection):
    context.configure(connection=connection, target_metadata=target_metadata, compare_type=True)
    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online():
    connectable = create_async_engine(os.getenv("DATABASE_URL"))
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()

if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
```

Explanation: Alembic itself expects a synchronous DB connection for migration operations; `run_sync` runs the sync migration code inside the async engine connection.

<br>
<br>

### **8) Autogenerate a migration**

After getting `target_metadata` set:

```
alembic revision --autogenerate -m "add email to users"
```

What happens:

* Alembic inspects `target_metadata` vs DB schema and writes a script in `alembic/versions/` with `upgrade()` and `downgrade()` functions and `op` operations (e.g., `op.add_column()`).
  Important: ALWAYS read and verify the generated migration file before applying it — autogenerate can be imperfect (esp. with enums, server defaults, or complex constraints).

<br>
<br>

### **9) Apply (upgrade) migrations**

```
alembic upgrade head
```

This applies pending migrations up to the most recent (head). You can also upgrade to a specific revision id.

<br>
<br>

### **10) Downgrade (rollback)**

```
alembic downgrade -1        # revert the last revision
alembic downgrade <rev_id>  # revert to a specific revision
```

Caution: Downgrades may be irreversible if they drop data-bearing columns. Write explicit downgrade logic carefully (or avoid destructive operations automatically).

<br>
<br>

### **11) Stamp (mark DB at a revision without running migrations)**

Useful when you want the DB to be considered up-to-date (e.g., you created schema by other means):

```
alembic stamp head
```

<br>
<br>

### **12) Example generated migration file**

`alembic/versions/20251022_add_email.py`

```python
"""add email column to users

Revision ID: 20251022_add_email
Revises: some_prev_rev
Create Date: 2025-10-22 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = '20251022_add_email'
down_revision = 'some_prev_rev'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=True))

def downgrade():
    op.drop_column('users', 'email')
```

Explanation: `op` module performs schema ops; `upgrade()` applies changes; `downgrade()` reverts them.

<br>
<br>

### **13) Data migrations (migrating values)**

Migrations can include data modifications. Use `op.get_bind()` to get a connection:

```python
from alembic import op
import sqlalchemy as sa
def upgrade():
    conn = op.get_bind()
    conn.execute(sa.text("UPDATE users SET email = name || '@example.com' WHERE email IS NULL"))
```

Caution: keep data migrations idempotent and small; test on staging first.

<br>
<br>

### **14) Handling SQLite quirks: batch mode**

SQLite has limited ALTER support. Use `batch_alter_table` inside migrations:

```python
with op.batch_alter_table('users') as batch_op:
    batch_op.add_column(sa.Column('email', sa.String))
```

Alembic supports generating batch-mode code when autogenerating for SQLite.

<br>
<br>

### **15) Enums / Type changes**

* For DB enums (Postgres `ENUM`), autogenerate may not always fully capture changes; you may need to write `sa.Enum(...).create()` / `.drop()` manually.
* For column type changes, `compare_type=True` helps, but test carefully.

<br>
<br>

### **16) Multiple databases / multiple metadata**

If your project has multiple `MetaData` objects or multiple DBs, you must supply the correct `target_metadata` to `env.py` and potentially maintain separate alembic environments or logic to route migrations.

<br>
<br>

### **17) Branching, heads, and conflicts**

When multiple developers create migrations (different heads), Alembic can show multiple heads. Resolve by creating **merge revisions**:

```
alembic merge -m "merge heads" head1 head2
```

This creates a revision that depends on both heads.

<br>
<br>

### **18) CI/CD integration**

Common patterns:

* Run `alembic upgrade head` as part of deployment after the code is deployed (so migration runs against the deployed DB).
* Alternatively, perform migrations before switching traffic (blue/green).
* Use DB backups and migrations inside a transaction when supported.

<br>
<br>

### **19) Common pitfalls & tips**

* **Always** review `--autogenerate` output. It can miss complex changes.
* Use `naming_convention` to avoid random constraint names.
* Avoid destructive automatic downgrades; explicitly code downgrades where necessary.
* When changing column nullability or types that require data fixes, do it in 2 steps: first backfill data, then alter constraint.
* Test migrations on a copy of production data when possible.
* Keep migrations small and focused (one logical change per migration).

<br>
<br>

### **20) Useful Alembic commands (cheat sheet)**

* `alembic init alembic` — initialize
* `alembic revision -m "msg" --autogenerate` — create migration from models
* `alembic upgrade head` — apply all migrations
* `alembic downgrade -1` — revert last migration
* `alembic history --verbose` — view history
* `alembic current` — show current revision in DB
* `alembic heads` — show head revisions
* `alembic stamp head` — mark DB as up-to-date without running migrations
* `alembic merge -m "msg" <rev1> <rev2>` — merge branches

<br>
<br>

### **21) Example: Full minimal async-ready env.py**

```python
# alembic/env.py (async-ready)
from logging.config import fileConfig
import asyncio, os, sys
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.models import Base  # your declarative Base

config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata

def do_run_migrations(connection: Connection):
    context.configure(connection=connection, target_metadata=target_metadata, compare_type=True)
    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online():
    DATABASE_URL = os.getenv("DATABASE_URL")  # example: postgresql+asyncpg://user:pass@host/db
    connectable = create_async_engine(DATABASE_URL)
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()

if context.is_offline_mode():
    context.configure(url=os.getenv("DATABASE_URL"), target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()
else:
    asyncio.run(run_migrations_online())
```

<br>
<br>

### **22) Workflow example (FastAPI dev flow)**

1. Add or change model in `app/models.py`.
2. `alembic revision --autogenerate -m "add email to users"` → review file.
3. `alembic upgrade head` → apply to dev DB.
4. Run tests, manual checks.
5. Commit migration file to VCS. Peers pull migrations and run `alembic upgrade head`.
6. In production pipeline, run `alembic upgrade head` as part of deploy job (or run it from a migration job).

<br>
<br>

### **23) When Alembic is not enough**

* For complex data transforms across large datasets, consider separate data migration scripts (one-off ETL jobs) rather than cramming everything into a migration.
* For multi-tenant systems, plan migrations carefully to avoid locking too many rows or long transactions.

<br>
<br>

### **24) Final best practices**

* Keep migrations in VCS.
* Keep migrations small & reversible when possible.
* Use `compare_type=True` and naming conventions.
* Review autogenerate output.
* Test on staging/backup.
* Backup DB before running destructive migrations in prod.

<br>
<br>

---

<br>
<br>


## 🧠 What is CORS (Cross-Origin Resource Sharing)?

**CORS** stands for **Cross-Origin Resource Sharing**.
It’s a **browser security mechanism** that controls whether a web page from one domain is allowed to request data from another domain.

<br>
<br>

### **Example to Understand CORS**

Let’s say:

* Your **frontend** runs on `http://localhost:3000`
* Your **backend API** runs on `http://localhost:8000`

Now, your frontend makes a call like this:

```javascript
fetch("http://localhost:8000/api/products")
```

Even though both are on localhost, they’re **different origins** because:

* One runs on port 3000
* The other on port 8000

So the browser blocks this request by default for security reasons.

You’ll see an error like:

```
Access to fetch at 'http://localhost:8000/api/products' from origin 'http://localhost:3000' has been blocked by CORS policy
```

<br>
<br>

## 🔒 Why Browsers Enforce CORS

Without CORS, any website could send requests to your backend using a user’s cookies — which could lead to **data theft, CSRF, and security breaches**.

CORS is basically the browser saying:

> “Hey server, this site (`http://localhost:3000`) wants to talk to you. Do you trust it?”

If the server replies with proper **CORS headers**, the browser allows the request.

<br>
<br>

## ⚙️ How CORS Works Internally

When your frontend sends a request to another origin, the browser first sends a **preflight request** (an `OPTIONS` request).
This request checks if the target server allows the origin.

If the backend responds with:

```http
Access-Control-Allow-Origin: http://localhost:3000
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
```

Then the browser proceeds with the actual request.
If not, the browser blocks it.

<br>
<br>

## 🚀 Configuring CORS in FastAPI

FastAPI makes this super easy using `CORSMiddleware`.

### **Step 1: Import the middleware**

```python
from fastapi.middleware.cors import CORSMiddleware
```

<br>
<br>

### **Step 2: Add CORS middleware in your main.py**

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allowed origins (frontend domains)
origins = [
    "http://localhost:3000",  # React/Next.js frontend
    "https://yourfrontend.com"  # production frontend
]

# Add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # list of allowed origins
    allow_credentials=True,         # allow cookies/auth
    allow_methods=["*"],            # allow all HTTP methods
    allow_headers=["*"],            # allow all headers
)
```

<br>
<br>

### **Step 3: Test it**

Now, if your React app on `http://localhost:3000` calls:

```javascript
fetch("http://localhost:8000/api/products")
```

Your backend will automatically respond with:

```http
Access-Control-Allow-Origin: http://localhost:3000
Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS
```

and the browser will allow it.

<br>
<br>

## ⚡ Common CORS Configuration Mistakes

| Mistake                       | Description                               | Fix                                                    |
| ----------------------------- | ----------------------------------------- | ------------------------------------------------------ |
| Forgetting CORS middleware    | Requests blocked by browser               | Add `CORSMiddleware`                                   |
| Using `*` with credentials    | Not allowed by browsers                   | Either remove credentials or specify origin explicitly |
| Wrong port or protocol        | Origin mismatch (`http://` vs `https://`) | Use exact URL                                          |
| Configuring CORS only for `/` | Middleware must be global                 | Apply at `app` level                                   |

<br>
<br>

---

<br>
<br>

## **Deployment Checklist**

<br>
<br>

## 🧩 **Step 1 — Prepare Environment Variables (.env)**

In development, we often keep credentials and configuration directly in code, but in deployment that’s a **big security risk**.
So we move all sensitive values to a **`.env` file** that is never pushed to GitHub.

### **1️⃣ Create a `.env` file in your project root**

```
project/
│
├── app/
│   ├── main.py
│   └── ...
├── .env
└── requirements.txt
```

### **2️⃣ Add environment variables**


<br>
<br>

## 🧩 **Step 2 — Generate `requirements.txt`**

This file lists all Python packages (and their versions) used in your project — it’s essential for deployment.

### **1️⃣ Activate your virtual environment**

If you’re using venv:

```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### **2️⃣ Freeze your dependencies**

```bash
pip freeze > requirements.txt
```

This will create a file like:

```
fastapi==0.115.0
uvicorn==0.30.1
pydantic==2.8.2
SQLAlchemy==2.0.31
alembic==1.13.2
psycopg2==2.9.9
python-dotenv==1.0.1
```

### **3️⃣ Verify the file**

Open it and make sure all required packages are listed — especially:

* `fastapi`
* `uvicorn`
* `sqlalchemy`
* `alembic`
* `psycopg2`
* `pydantic`
* `python-dotenv` or `pydantic-settings`

<br>
<br>


## 🧩 **Step 3 — Create GitHub Repository & Configure Local Git**

<br>
<br>

### **1️⃣ Create a new repository on GitHub**

1. Go to [https://github.com/new](https://github.com/new)
2. Enter:

   * **Repository name**: e.g. `fastapi-bargain-bot`
   * **Description**: optional (e.g. *FastAPI backend for bargaining chatbot project*)
   * **Visibility**: Choose **Public** or **Private**
   * ✅ **Do not** initialize with README, .gitignore, or license (we’ll do it locally)
3. Click **Create repository**

You’ll now see a page with Git setup commands like:

```
…or create a new repository on the command line
```

Keep that open — we’ll use it soon.

<br>
<br>

### **2️⃣ Initialize Git in your local project**

Open your terminal inside your project folder (root):

```bash
git init
```

This creates a local `.git` directory to track version history.

<br>
<br>

### **3️⃣ Create a `.gitignore` file**

We must exclude environment files and cache folders from version control.

Create a file `.gitignore` in your project root and add:

```
# Environment files
.env
venv/

# Python cache
__pycache__/
*.pyc

# IDE settings
.vscode/
.idea/

# Alembic versions (optional if generated dynamically)
alembic/__pycache__/
```

This ensures secrets and unnecessary files aren’t uploaded to GitHub.

<br>
<br>

### **4️⃣ Stage and commit your project**

Now tell Git which files to track and make your first commit:

```bash
git add .
git commit -m "Initial project setup with FastAPI and Alembic"
```

<br>
<br>

### **5️⃣ Connect your local repo with GitHub**

Copy the commands from GitHub (the same page where you created your repo), usually like:

```bash
git remote add origin https://github.com/<your-username>/<repo-name>.git
git branch -M main
git push -u origin main
```


<br>
<br>

### **6️⃣ Verify your repository**

Go back to GitHub → refresh the repository page.
✅ You should now see your project files uploaded.

<br>
<br>

## ⚡ Summary

| Step | Action                    | Purpose                             |
| ---- | ------------------------- | ----------------------------------- |
| 1️⃣  | Create GitHub repo        | Host your code remotely             |
| 2️⃣  | `git init`                | Initialize version control          |
| 3️⃣  | `.gitignore`              | Exclude sensitive/unnecessary files |
| 4️⃣  | `git add . && git commit` | Track and save project snapshot     |
| 5️⃣  | `git push`                | Upload code to GitHub               |
| 6️⃣  | Verify                    | Ensure everything is synced         |

<br>
<br>