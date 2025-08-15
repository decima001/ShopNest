# ShopNest
ShopNest is a Django-based RESTful API for managing products in an e-commerce platform. It supports CRUD operations for products and users, product search, filtering, and authentication using JWT. This project is designed for learning purposes, focusing on backend development with Django and Django REST Framework.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Product Management**: Create, read, update, and delete products with attributes like name, description, price, category, stock quantity, and image URL.
- **User Management**: CRUD operations for users with authentication to manage products.
- **Product Search**: Search products by name or category with partial matches.
- **Filtering & Pagination**: Filter products by category, price range, or stock availability with paginated results.
- **Authentication**: Secure endpoints using JWT (JSON Web Tokens).
- **Future Enhancements**: Product reviews, wishlists, and stock management (planned).

## Tech Stack
- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: Django Authentication, Simple JWT
- **Deployment**: Heroku (planned)
- **Other Tools**: django-filter, python-decouple

## Setup Instructions

### Prerequisites
- Python 3.8+
- PostgreSQL
- Git
- Virtualenv (recommended)

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ShopNest.git
   cd ShopNest
