from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from mongoengine import connect
from src.user_blueprint import user
from src.worker_blueprint import worker
from src.client_blueprint import client
from src.timesheet_blueprint import timesheet

# Flask, είναι WEB Framework
app = Flask(__name__)

# JWT cookies, κάνουν το authentication του user
jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = "super secret and difficult to guess key"

# Connect to the database specified by the 'db' argument.
connect(
    host="mongodb+srv://anguser:IpapWJtzkCCN2DcA@cluster0.f2t2trg.mongodb.net/",
    db="angular-fp",
    alias="angular-fp",
)

# cross origin policy
cors = CORS(
    app,
    resources={
        r"*": {"origins": ["http://localhost:4200"]}
    },  # στην port 4200 τρέχει η angular, εδώ του λέμε να επιτρέπεται ό,τι τρέχει τοπικά σε Angular
)

# flask Blueprints
app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(worker, url_prefix="/workers")
app.register_blueprint(client, url_prefix="/clients")
app.register_blueprint(timesheet, url_prefix="/timesheets")
