from flask import Flask, render_template, request
import main

app = Flask(__name__)

main.init()

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    msg = ""
    key = ""

    if request.method == "POST":
        msg = request.form.get("msg", "")
        key = request.form.get("key", "0")

        try:
            key = int(key)
            if 0 <= key <= 17575:
                result = main.swap(msg.lower(), key)
            else:
                result = "Key must be between 0 and 17575"
        except ValueError:
            result = "Invalid key"

    return render_template(
        "index.html",
        msg=msg,
        key=key,
        result=result
    )

if __name__ == "__main__":
    app.run("0.0.0.0",port=5000)
