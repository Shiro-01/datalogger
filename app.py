from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

# Store all received messages
messages = []

@app.post("/flight-data")
async def receive_data(request: Request):
    body = await request.body()
    message = body.decode("utf-8")
    messages.append(message)
    print(f"Received: {message}")
    return {"status": "received"}

@app.get("/", response_class=HTMLResponse)
async def show_messages():
    html = "<h2>Received Data Log</h2><ul>"
    for msg in messages:
        html += f"<li>{msg}</li>"
    html += "</ul>"
    
    # Auto-refresh every 2 seconds
    html += """
        <script>
            setTimeout(() => { location.reload(); }, 2000);
        </script>
    """
    return html
