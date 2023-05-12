# Django DDD Service Template

This repository is an example Django project that follows the principles of Domain-Driven Design (DDD). The template is organized into three layers: Application, Domain, and Infrastructure.

## Application Layer

The Application layer contains the use cases of the application and acts as the input port.

## Domain Layer

The Domain layer contains the business logic of the application. The Domain layer is the core of the application and defines the application's behavior.

## Infrastructure Layer

The Infrastructure layer contains the input and output adapters of the application. It includes the API, DB, and Repositories sublayers.

### API Sublayer

The API sublayer contains everything related to the application's REST API. It includes the Django views that act as the input adapters and handle HTTP requests.

### DB Sublayer

The DB sublayer contains everything related to the application's output schema. It includes the Django models that act as the output adapters and represent the data in the database.

### Repositories Sublayer

The Repositories sublayer contains the implementation of the output ports defined in the Domain layer. It provides the necessary methods to store and retrieve data from the database.

## Configuration

The Configuration folder contains all the general Django configuration files, including settings, URLs, and middleware.

## Getting Started

To use this template, follow these steps:

1. Clone the repository
2. Create a virtual environment and activate it
3. Install the dependencies with `pip install -r requirements.txt`
4. Delete example code / use it as a guide for how to use the project structure

## Conclusion

This template provides a starting point for building a Django application that follows the principles of Domain-Driven Design. By separating the layers of the application, it is easier to maintain and test the code, and to make changes to the business logic without affecting the infrastructure.
