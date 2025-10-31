from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai
import os

app = FastAPI()

# CORS para permitir acceso desde Netlify
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configurar OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Simulación simple de base de datos en memoria
users = {}  # estructura: {ip: {"role": "demo", "used": 1}}

PLAN_LIMITS = {
    "demo": 3,
    "pago": 50,
    "premium": float("inf")
}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get("message", "")
    ip = request.client.host

    # Si el usuario no está en la base, lo agregamos como demo
    if ip not in users:
        users[ip] = {"role": "demo", "used": 0}

    role = users[ip]["role"]
    used = users[ip]["used"]
    limit = PLAN_LIMITS[role]

    if used >= limit:
        return {"status": "limit_reached", "message": "Has usado todos tus mensajes gratuitos. Desbloquea acceso para seguir usando el chat."}

    # Llamada a OpenAI (GPT personalizado si se desea)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un asistente culinario llamado Queso. Ayudas a planificar menús baratos y sabrosos."},
                {"role": "user", "content": message}
            ]
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"Error al contactar con el modelo: {str(e)}"

    # Actualizamos el contador
    users[ip]["used"] += 1

    return {"status": "ok", "reply": reply, "remaining": int(limit - users[ip]["used"])}

