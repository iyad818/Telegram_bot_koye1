import os
import threading
import time
import subprocess
from flask import Flask, jsonify

app = Flask(__name__)

bot_running = False
bot_process = None

def start_bot():
    global bot_running, bot_process
    if not bot_running:
        bot_process = subprocess.Popen(["python3", "bot.py"])
        bot_running = True

def check_bot_status():
    global bot_running
    if bot_process and bot_process.poll() is not None:
        bot_running = False

@app.route('/')
def home():
    check_bot_status()
    return jsonify({"bot_status": "Running" if bot_running else "Stopped"})

def run_flask():
    app.run(host='0.0.0.0', port=8000)

flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

start_bot()

while True:
    check_bot_status()
    if not bot_running:
        print("⚠️ البوت توقف! إعادة تشغيله...")
        start_bot()
    time.sleep(10)
