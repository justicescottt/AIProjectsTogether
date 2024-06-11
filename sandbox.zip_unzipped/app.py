from flask import Flask
from blueprints.general import general_bp
from blueprints.admin import admin_bp
from blueprints.user import user_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(general_bp, url_prefix="/")
app.register_blueprint(admin_bp, url_prefix="/admin")
app.register_blueprint(user_bp, url_prefix="/user")

if __name__ == "__main__":
    app.run(debug=True)
