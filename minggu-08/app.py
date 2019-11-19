from flask import flask
import os

app = Flask(__name__)

@app.router("/")
def hello();
  return "Shafira Latihan membuat aplikasi menggunakan python+flask"


if __name__== "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
