# CompactDisc REST API Application

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [Swagger Documentation](#swagger-documentation)
- [Logging](#logging)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction
The CompactDisc REST API application is a Spring Boot-based project that provides a CRUD API for managing a catalog of compact discs. It allows users to create, read, update, and delete compact disc records and their associated tracks.

---

## Features
- ✅ RESTful API for managing compact discs.
- ✅ Integration with MySQL for persistent data storage.
- ✅ Swagger UI for API documentation and testing.
- ✅ Logging using Log4j2.
- ✅ Frontend HTML pages for interacting with the API.
- ✅ Docker support for deployment.

---

## Technologies Used
- **Java 11**
- **Spring Boot 2.5.3**
- **Spring Data JPA**
- **MySQL**
- **Swagger 2**
- **Log4j2**
- **H2 Database (for testing)**
- **HTML, CSS, JavaScript, jQuery**

---

## Project Structure

```
src/ 
├── main/ 
│   ├── java/ 
│   │   └── com.example.compactdisc/ 
│   │       ├── controllers/ 
│   │       ├── entities/ 
│   │       ├── repositories/ 
│   │       └── services/ 
│   └── resources/ 
│       ├── application.properties 
│       └── static/ 
└── test/
```

---

## Setup and Installation

### Prerequisites
- Java 11 or higher
- Maven
- MySQL
- Docker (optional, for containerized deployment)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Set up the database:
   - Create a MySQL database named `compactdisc`.
   - Update the `application.properties` file with your database credentials.

3. Build the project:
   ```bash
   mvn clean install
   ```

4. Run the application:
   ```bash
   mvn spring-boot:run
   ```

---

## Running the Application
- Access the application at [http://localhost:8080](http://localhost:8080).

---

## API Endpoints

| Method | Endpoint                  | Description                                      |
|--------|---------------------------|--------------------------------------------------|
| GET    | `/api/compactdiscs`       | Get all compact discs.                          |
| GET    | `/api/compactdiscs/{id}`  | Get a compact disc by ID.                       |
| GET    | `/api/compactdiscs/404/{id}` | Get a compact disc by ID with 404 if not found. |
| POST   | `/api/compactdiscs`       | Add a new compact disc.                         |
| DELETE | `/api/compactdiscs/{id}`  | Delete a compact disc by ID.                    |
| DELETE | `/api/compactdiscs`       | Delete a compact disc by passing its details.   |

### Example JSON Payloads
#### POST `/api/compactdiscs`
```json
{
  "title": "Greatest Hits",
  "artist": "Artist Name",
  "price": 19.99,
  "tracks": 12
}
```

#### DELETE `/api/compactdiscs`
```json
{
  "id": 1,
  "title": "Greatest Hits",
  "artist": "Artist Name",
  "price": 19.99,
  "tracks": 12
}
```

---

## Database Schema

### Table: `compact_discs`

| Column   | Type         | Description          |
|----------|--------------|----------------------|
| `id`     | Primary Key  | Unique identifier    |
| `title`  | VARCHAR      | Title of the disc    |
| `artist` | VARCHAR      | Artist name          |
| `price`  | DOUBLE       | Price of the disc    |
| `tracks` | INTEGER      | Number of tracks     |

---

## Swagger Documentation
Swagger UI is available at: [http://localhost:8080/swagger-ui.html](http://localhost:8080/swagger-ui.html)

---

## Logging
Logs are managed using Log4j2. Configuration can be found in the `log4j2.properties` file.

---

## Contributing
Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

---

## License
This project is licensed under the MIT License.