from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db, bcrypt, jwt
from controllers.auth_controller import auth_blueprint

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)
CORS(app)

# Register blueprints
app.register_blueprint(auth_blueprint, url_prefix='/auth')

# Initialize database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)