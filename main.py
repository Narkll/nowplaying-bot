from flask import Flask, request

app = Flask(__name__)
last_message = "🎵 Ainda não foi recebida nenhuma música"

@app.route("/", methods=["GET"])
def home():
    return last_message

@app.route("/update", methods=["POST"])
def update():
    global last_message
    last_message = request.data.decode("utf-8")
    print("Atualizado:", last_message)
    return "OK"

app.run(host="0.0.0.0", port=5000)


