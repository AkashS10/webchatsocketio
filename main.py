from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("message")
def handleMessages(message):
    print(f"Recieved message: {message}")
    if message != "User Connected!":
        send(message, broadcast=True)

@app.route("/")
def index():
    return render_template("chat.html")

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=80)
