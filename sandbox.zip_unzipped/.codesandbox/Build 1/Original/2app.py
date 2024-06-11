from flask import Flask
from models import Bank, Admin
from general.routes import general_bp
from admin.routes import admin_bp
from user.routes import user_bp

app = Flask(__name__)

# Initialize global objects
bank = Bank("Example Bank")
admin = Admin()
current_user = None

# Register blueprints
app.register_blueprint(general_bp)
app.register_blueprint(admin_bp, url_prefix="/admin")
app.register_blueprint(user_bp, url_prefix="/user")

if __name__ == "__main__":
    app.run(debug=True)
