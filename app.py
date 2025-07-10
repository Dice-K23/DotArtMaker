from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# キャンバスサイズ
CANVAS_WIDTH = 26
CANVAS_HEIGHT = 30

# 初期化用の空キャンバス
EMPTY_CANVAS = [["#FFFFFF" for _ in range(CANVAS_WIDTH)] for _ in range(CANVAS_HEIGHT)]

@app.route("/")
def index():
    return render_template("index.html", width=CANVAS_WIDTH, height=CANVAS_HEIGHT, canvas=EMPTY_CANVAS)

@app.route("/update", methods=["POST"])
def update():
    data = request.get_json()
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True) 