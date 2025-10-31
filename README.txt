PROYECTO QUESO – BACKEND (FastAPI)

PASOS PARA SUBIR A RENDER:

1. Ve a https://render.com y entra a tu cuenta.
2. Haz clic en "New" > "Web Service".
3. Selecciona "Upload a .zip file".
4. Sube el archivo proyecto_queso_backend.zip.
5. Cuando te pida:
   - Runtime: Python 3.11
   - Build Command: pip install -r requirements.txt
   - Start Command: uvicorn main:app --host 0.0.0.0 --port 10000

6. Crea una variable de entorno:
   - Key: OPENAI_API_KEY
   - Value: tu clave secreta de OpenAI (formato sk-...)

7. Dale a "Create Web Service" y espera que despliegue.

Tu backend estará disponible en:
https://<tu-nombre>.onrender.com/chat

