#create branch QA

Still in progress? This project implements a profile management microservice developed in Python using Flask. 
The service provides functionality for querying user profiles, 
both clients and organizers, connecting to multiple MySQL databases.

## Technologies Used

### Main Framework
- **Flask 3.1.1**: Lightweight web framework for Python that provides the foundation for the REST API

### Database
- **MySQL Connector Python 9.3.0**: Official MySQL driver for Python that allows connection to MySQL databases

### Authentication and Security
- **Flask-JWT-Extended 4.7.1**: Extension for handling JSON Web Tokens (JWT) in Flask
- **PyJWT 2.10.1**: Library for encoding and decoding JWT tokens

### Configuration and Environment Variables
- **python-dotenv 1.1.1**: Library for loading environment variables from .env files

### CORS and Communication
- **flask-cors 6.0.1**: Extension to enable Cross-Origin Resource Sharing (CORS)

## Implemented Design Patterns

### 1. Factory Method Pattern
- Implemented in `config.py` with the `DBConnections` class, which provides static methods for creating connections to different databases.

### 2. MVC (Model-View-Controller) Pattern
- **Model**: `app/models.py` - Handles data access logic and database queries.
- **Controller**: `app/profile_controller.py` - Processes HTTP requests and coordinates between the view and the model.
- **View**: `app/routes.py` - Defines API endpoints and handles JSON responses.

### 3. Blueprint Pattern
- Used in Flask to organize routes into separate modules (`profile_bp`).

### 4. Singleton Pattern (Implicit)
- Database connections are managed centrally through the `DBConnections` class.

## Communication Protocols

### 1. HTTP/HTTPS
- Main protocol for REST communication
- Supported HTTP methods: GET, POST

### 2. REST API
- RESTful endpoints for CRUD operations
- JSON-formatted responses
- Standard HTTP status codes

### 3. JWT (JSON Web Tokens)
- Token-based authentication protocol
- Stateless session handling

### 4. CORS (Cross-Origin Resource Sharing)
- Protocol for allowing requests from different domains