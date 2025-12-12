# KARTS - BACKEND

Backend del proyecto Karts desarrollado con **FastAPI** y **MySQL**.  
El frontend está en el repo: [web-karts](https://github.com/ldvelasco/web-karts).

## 📦 Tech Stack

- **Framework: FastAPI (Python)**
- **Database: MySQL (v8.0)**
- **ORM/Queries: SQLAlchemy + PyMySQL (async)**
- **Contenedores: Docker + Docker Compose**
- **Frontend integrado: Soporte para React/Vite (en repo separado)**

## 🛠️ Setup & Installation
###  Requisitos
- **Docker Desktop** (Windows) o **Docker** (Linux) instalado y corriendo.  
  Descarga: https://www.docker.com/products/docker-desktop/

### Instalación
    1. En la misma carpeta clona ambos repositorios
        ```sh
        git clone https://github.com/ldvelasco/backend-karts.git
        git clone https://github.com/ldvelasco/web-karts.git
        cd backend-karts
        ```
    2. Configura las variables de entorno
        Copia el ejemplo
        `cp .env.example .env`    # Linux/Mac
        o en Windows:
        `copy .env.example .env`
        
        - Contenido de ejemplo
        ```sh
        # -----------------------------------------------------------------------------
        # Database (MySQL)
        # -----------------------------------------------------------------------------
        MYSQL_ROOT_PASSWORD=root123
        MYSQL_DATABASE=karts_db
        MYSQL_USER=karts
        MYSQL_PASSWORD=karts123
        DATABASE_URL=mysql+pymysql://karts:karts123@db:3306/karts_db
        ```
    3. Levanta todo (MySQL + Backend + Frontend):
        `docker-compose up -d --build`
    4. Abre en el navegador
        - Backend
        `http://localhost:8000/`
        - Frontend
        `http://localhost:3000/`