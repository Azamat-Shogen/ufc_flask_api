from src import create_app


app = create_app()

@app.route('/')
def hello():
    return "welcome to the flask tutorials"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
