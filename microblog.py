from flask import Flask

app = Flask("MicroBlog")

@app.route("/")
def index():
    return "Olá Mundo"

app.run()