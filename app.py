from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


# Route for AI Tool Picker tab
@app.route("/ai-tool-picker")
def ai_tool_picker():
    return render_template("ai-tool-picker.html")