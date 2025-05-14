from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db, bcrypt, jwt
from controllers.auth_controller import auth_blueprint
<<<<<<< HEAD
from controllers.transaction_controller import transaction_blueprint
from controllers.dashboard_controller import dashboard_blueprint
=======
# from controllers.dashboard_controller import dashboard_blueprint
>>>>>>> 0750c18b4b0907cf2afa02a5a9b613d31544b5c9

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
app.register_blueprint(transaction_blueprint, url_prefix='/transaction')
app.register_blueprint(dashboard_blueprint, url_prefix='/api')

# Initialize database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)