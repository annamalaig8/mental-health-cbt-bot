from flask import Flask, render_template, request
import joblib
import re
from cbt_responses import get_response

app = Flask(__name__)

# Load model
model = joblib.load("mental_state_model.pkl")

# Conversation state
last_label = None
stage_index = 0
STAGES = ["reflect", "explore", "reframe", "checkin"]

# Chat history (server-side, demo purpose)
chat_history = []

GREETINGS = ["hi", "hello", "hey"]
DECLINE_WORDS = ["no", "nah", "stop", "not now"]

def normalize(text):
    text = text.lower()
    text = re.sub(r"\bim\b", "i am", text)
    text = re.sub(r"\bi'm\b", "i am", text)
    return text

def is_short_reply(text):
    return text.strip() in ["yes", "yeah", "ok", "okay", "idk", "hmm"]

def is_greeting(text):
    return text.strip() in GREETINGS

def is_decline(text):
    return text.strip() in DECLINE_WORDS

@app.route("/", methods=["GET", "POST"])
def chat():
    global last_label, stage_index, chat_history

    if request.method == "POST":
        user_input = request.form["message"]
        clean = normalize(user_input)

        # Save user message
        chat_history.append(("user", user_input))

        if is_greeting(clean):
            bot_reply = "Hi 🙂 Take your time. I’m here."
            last_label = None
            stage_index = 0

        elif is_decline(clean):
            bot_reply = "That’s okay. We can pause. I’m here whenever you’re ready."
            last_label = None
            stage_index = 0

        elif is_short_reply(clean) and last_label:
            label = last_label
            stage = STAGES[min(stage_index, len(STAGES)-1)]
            bot_reply = get_response(label, stage)
            stage_index += 1

        else:
            label = model.predict([clean])[0]
            last_label = label
            stage_index = 0
            stage = STAGES[stage_index]
            bot_reply = get_response(label, stage)
            stage_index += 1

        # Save bot reply
        chat_history.append(("bot", bot_reply))

    return render_template("chat.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

