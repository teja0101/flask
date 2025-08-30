from flask import Flask
from extensions import db
from config import Config

# Blueprints
from hr.routes import hr_bp
from students.routes import student_bp

app = Flask(__name__)
app.config.from_object(Config)

# Init database
db.init_app(app)

# Register Blueprints
app.register_blueprint(hr_bp)
app.register_blueprint(student_bp)

@app.route("/")
def home():
    return "Welcome to Future Forbes HR + Student Portal"

if __name__ == "__main__":
    app.run(debug=True)
