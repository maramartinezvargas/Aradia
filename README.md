# **Aradia – Juego de Adivinación con IA**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-Framework-000000?logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Jinja2-Templates-B41717?logo=jinja&logoColor=white" />
  <img src="https://img.shields.io/badge/HTML5-Frontend-E34F26?logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS3-Estilos-1572B6?logo=css3&logoColor=white" />
  <img src="https://img.shields.io/badge/JSON-Structured Data-000000?logo=json&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenRouter-API-FF4F00?logo=openai&logoColor=white" />
</p>

Aradia es una pequeña aplicación web creada con Flask que simula un pequeño juego de adivinación: inspirándome en la clásica web de Akinator ("el genio que lee la mente"), la IA intenta averiguar en qué personaje está pensando el usuario haciendo preguntas sencillas.
La conversación aparece en formato chat, con burbujas de estilo mensajería.

La IA responde siempre en formato JSON y sigue un conjunto de reglas diseñado para mantener la conversación fluida, divertida y coherente.

Se trata tan solo de una prueba de concepto más que un proyecto completo, pero me sirvió para entender cómo funcionan las peticiones, los endpoints y el flujo entre backend y modelo.

---

## **Características**

* Conversación estilo chat con burbujas (HTML + CSS).
* La IA inicia el juego automáticamente.
* Persistencia de la conversación.
* Interfaz ligera construida con Flask y Jinja2.
* Respuestas en JSON estrictas, interpretadas por la app.
* Llamadas a modelos de OpenRouter (cualquier modelo compatible).
* Soporte para humor ligero, ironía y preguntas cerradas.

---

## **Requisitos**

Python 3.10+
Dependencias listadas en `requirements.txt`:

```
Flask
requests
python-dotenv
```

(Se instalarán automáticamente en el siguiente paso).

---

## **Instalación**

1. Clona el repositorio:

```
git clone git@github.com:TU_USUARIO/TU_REPO.git
cd TU_REPO
```

2. Crea y activa un entorno virtual:

```
python3 -m venv venv
source venv/bin/activate
```

3. Instala dependencias:

```
pip install -r requirements.txt
```

4. Crea un archivo **.env** (por buenas prácticas, no se incluye en este repositorio):

```
OPENROUTER_API_KEY=tu_api_key
MODEL=tu_modelo_de_openrouter
FLASK_SECRET_KEY=cualquier_string
```

---

## **Ejecución**

Lanza la aplicación:

```
python3 app.py
```

Abre en el navegador:

```
http://127.0.0.1:5000
```

---

## **Estructura del proyecto**

```
Aradia/
│
├── app.py
├── requirements.txt
├── .gitignore
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   ├── ai.svg
│   └── user.svg
└── README.md
```

---

## **Licencia**

Este proyecto es libre. Lo he creado únicamente con fines experimentales y didacticos. Puedes modificarlo, extenderlo o usarlo como base para tus propios experimentos con IA.

---
