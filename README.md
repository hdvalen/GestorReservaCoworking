# 🏢 Gestor de Reservas de Salas

## 📖 Descripción

API REST desarrollada con **FastAPI** para la gestión de reservas de salas de coworking. El sistema permite registro de usuarios, autenticación JWT, gestión de salas.

## 🎯 Objetivo

Construir una API REST robusta que permita:
- ✅ Registro e inicio de sesión de usuarios (roles: `user` y `admin`)
- ✅ Gestión completa de salas de coworking
- ✅ Sistema de reservas con validaciones de horarios
- ✅ Reportes simples para administradores
- ✅ Autenticación segura con JWT + Auth0

## 🛠️ Tecnologías

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Python** | 3.12.6 | Lenguaje de programación |
| **FastAPI** | Latest | Framework web moderno y rápido |
| **MySQL** | 8.0+ | Base de datos relacional |
| **SQLAlchemy** | Latest | ORM para Python |
| **JWT** | Latest | Autenticación y autorización |
| **Auth0** | Latest | Servicio de autenticación |
| **Uvicorn** | Latest | Servidor ASGI |

## 📂 Estructura del Proyecto

```
nameProject/
│── .venv/
│── requirements.txt
│── README.md
│── app/
│   │── main.py
│   │── auth/
│   │   └── model.py
│   │   └── router.py
│   │   └── Auth.py
│   │── models/
│   │   └── room_model.py
│   │   └── reservation_model.py
│   │
│   │── controllers/
│   │   └── room_controller.py
│   │   └── reservation_controller.py
│   │
│   │── routes/
│   │   └── room_outes.py
│   │   └── reservation_routes.py
│   │
│   │── config/
│   │   └── databseb.py         # conexión a MySQL
│   │   
│   │── data/
│       └── docsFlowEstructura.sqlite   # creación tablas

```

## 🚀 Instalación y Configuración

### 📋 Prerrequisitos

- Python 3.12.6 instalado
- MySQL 8.0+ ejecutándose
- Git instalado

### 🔧 Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd nameProject
   ```

2. **Crear y activar entorno virtual**
   ```bash
   # Crear entorno virtual
   python -m venv .venv
   
   # Activar entorno virtual
   # En Windows:
   .venv\Scripts\activate
   
   # En macOS/Linux:
   source .venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

5. **Ejecutar Proyecto**
   ```bash
    uvicorn app.main:app --reload 
   ```

### ⚙️ Variables de Entorno (.env)

```env

# JWT Configuration
JWT_SECRET_KEY=tu_clave_secreta_muy_segura
JWT_ALGORITHM=HS256

```

## 🏃‍♂️ Ejecutar el Proyecto

### 🌐 Acceso a la Aplicación

- **API**: http://localhost:8000
- **Documentación Swagger**: http://localhost:8000/docs

## 🧰 Endpoints de la API

### 👤 Autenticación
| Método | Endpoint | Descripción | Permisos |
|--------|----------|-------------|----------|
| POST | `/auth/register` | Registro de nuevos usuarios | Público |
| POST | `/auth/login` | Inicio de sesión | Público |

### 👥 Usuarios
| Método | Endpoint | Descripción | Permisos |
|--------|----------|-------------|----------|
| GET | `/users/me` | Obtener perfil del usuario actual | Autenticado |
| GET | `/users/` | Listar todos los usuarios | Admin |
| DELETE | `/users/{id}` | Eliminar usuario | Admin |

### 🏢 Salas
| Método | Endpoint | Descripción | Permisos |
|--------|----------|-------------|----------|
| GET | `/rooms` | Listar todas las salas | Autenticado |
| POST | `/rooms` | Crear nueva sala | Admin |
| PUT | `/rooms/{id}` | Actualizar sala | Admin |
| DELETE | `/rooms/{id}` | Eliminar sala | Admin |

### 📅 Reservas
| Método | Endpoint | Descripción | Permisos |
|--------|----------|-------------|----------|
| POST | `/reservations` | Crear nueva reserva | Autenticado |
| GET | `/reservations/me` | Mis reservas | Autenticado |
| GET | `/reservations/room/{room_id}` | Reservas por sala | Autenticado |
| GET | `/reservations/date/{yyyy-mm-dd}` | Reservas por fecha | Autenticado |
| DELETE | `/reservations/{id}` | Cancelar reserva | Propietario/Admin |
