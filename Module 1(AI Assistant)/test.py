


from flask import Flask
import main

app = Flask(__name__)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
    return "Well Done"

    
