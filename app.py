#!/usr/bin/env python3
from dotenv import load_dotenv
load_dotenv(".env")

from flask import Flask, render_template, request, session
import requests
import os
import json

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY", "dev_secret_key")
app.config["SESSION_PERMANENT"] = False

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("MODEL")

if not OPENROUTER_API_KEY:
    raise RuntimeError("Falta OPENROUTER_API_KEY en .env")
if not MODEL:
    raise RuntimeError("Falta MODEL en .env")

# ------------------------------------------
# PROMPT 
# ------------------------------------------
SYSTEM_PROMPT = """
Eres Aradia, una IA que juega a adivinar personajes mediante preguntas sencillas.
Normas:
- Eres directa, amable, un poco irónica y con humor.
- Si no hay historial, te presentas en una frase, explicas el juego y haces la primera pregunta cerrada.
- Respondes SIEMPRE con JSON puro: {"type":"question"|"guess","content":"texto"}.
- Permites al usuario responder libremente.
- Si el usuario no responde una pregunta, repites la última pregunta de forma diferente amablemente.
- Nada fuera del JSON.
- Puedes usar comentarios con humor e ironía, y puntualmente emojis, dentro de "content".
- No repites preguntas.
- Cuando creas tener la respuesta → type:"guess".
- Si fallas puedes pedir pista.
- Si aciertas, felicitas solo si fue difícil.
- Si el usuario pide otra cosa, le recuerdas que solo puedes jugar.
- Hablas por defecto en español, a no ser que el usuario use otro idioma.
- Nunca explicas tu razonamiento interno.
"""


# -------------------------------
# LLM
# -------------------------------
def ask_llm(history):
    payload = {
        "model": MODEL,
        "max_tokens": 200,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            *history
        ]
    }

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    r = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        json=payload,
        headers=headers
    )

    data = r.json()

    if "choices" not in data:
        return {"type": "error", "content": str(data)}

    raw = data["choices"][0]["message"]["content"]

    # Intento 1
    try:
        return json.loads(raw)
    except:
        # Intento 2: limpiar posibles restos
        try:
            cleaned = raw[raw.index("{"): raw.rindex("}") + 1]
            return json.loads(cleaned)
        except:
            return {"type": "error", "content": raw}


# -------------------------------
# RUTA PRINCIPAL
# -------------------------------

@app.route("/", methods=["GET", "POST"])
def index():

    # PRIMERA VEZ: crear historial y hacer que Aradia empiece
    if "history" not in session:
        session["history"] = []

        first = ask_llm([])  # historial vacío → se presenta

        session["history"].append({
            "role": "assistant",
            "content": first["content"]
        })
        session.modified = True

        return render_template("index.html",
                               history=session["history"],
                               typing=False)

    # POST → mensaje del usuario
    if request.method == "POST":

        user_reply = request.form.get("reply", "")

        session["history"].append({
            "role": "user",
            "content": user_reply
        })

        response = ask_llm(session["history"])

        session["history"].append({
            "role": "assistant",
            "content": response["content"]
        })

        session.modified = True

        return render_template("index.html",
                               history=session["history"],
                               typing=False)

    # GET posteriores → mantiene el chat
    return render_template("index.html",
                           history=session["history"],
                           typing=False)


if __name__ == "__main__":
    app.run(debug=True)
