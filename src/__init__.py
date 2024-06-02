from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from mongoengine import connect
from src.user_blueprint import user
from src.customer_blueprint import customer

# Flask is a BACKEND micro-framework written in Python for the rapid development process. It is famous for its simplicity and independence. It does not need any external library for work, which makes it beginner-friendly, and many people choose this framework. Flask is generally used for building a REST API.

app = Flask(
    __name__
)  # η library Flask είναι WEB Framework, it is used for developing web applications using python (δες σχόλια επάνω)
jwt = JWTManager(
    app
)  # εδώ είναι τα JWT που είναι cookies (είναι jwt cookies, που είναι διαφορετικά από τα session cookies) και κάνουν το authentication του client που συνδέετεται με την ΒΔ (εν προκειμένω, στην εφαρμογή μας)
app.config["JWT_SECRET_KEY"] = "super secret and difficult to guess key"

connect(  # =Connect to the database specified by the 'db' argument.
    #   Τα παρακάτω είναι του καθηγητή (= Χριστόδουλος Φραγκουδάκης)
    # host="mongodb+srv://coding-factory:ufTXpw9bAEejrXfb@cluster0.okry00y.mongodb.net",
    # db="Coding-Factory",
    # alias="coding-factory",
    # Δικά μου στοιχεία -> δική μου βάση στην MongoDB Atlas:
    # αν δεν βρει την db θα την φτιάξει (εδώ δεν την έχω, έχω μόνο την codingfactory βάση δεδομένων => θα την δημιουργήσει)
    # (τον cfuser ομως ΠΡΕΠΕΙ να τον βρει δηλ ΠΡΕΠΕΙ να τον έχω δημιουργήσει ήδη -> η ΒΔ που δημιουργείται εδώ ή που πηγαίνει σε αυτή οταν υπάρχει ήδη θα έχει αυτόν τον user (τον cfuser (όπως και την codingfactory ΒΔ) το φτιάξαμε στο μάθημα για την MongoDB με τον Καραμπάτση Μάρκο))
    # INFO: Η ΒΔ είναι στο backend, πως την βλέπω?
    # την βλέπουμε στο http://localhost:5000 τι σημαίνει αυτό? δες παρακάτω
    # η 5000 είναι δίαυλος για την ΒΔ δηλ είναι ο δίαυλος επικοινωνίας της angular με την ΒΔ μου που είναι η MongoDB Atlas => πρέπει να τρέχει για να είναι ανοιχτός ο δίαυλος επικοινωνίας και να μπορούμε να στείλουμε τις εντολές get, post, patch Κλπ
    # Database: codingfactory (αποτυχημένη πρώτη προσάθεια...)
    # host="mongodb+srv://cfuser:nGMoXpJzhr6cxCvvRTy5@cluster0.f2t2trg.mongodb.net/",
    # db="codingfactory",
    # alias="codingfactory",
    # Database: angular (= η δική μου ΒΔ στην Altas Mongo DB, εγώ την έφτιαξα, κι έχω πάρει από εκεί το connection string που στην συνέχεια έβαλα στο host παρακάτω)
    host="mongodb+srv://anguser:IpapWJtzkCCN2DcA@cluster0.f2t2trg.mongodb.net/",
    db="angular-fp",
    alias="angular-fp",
)

# το παρακάτω ΔΕΝ αφορά την σύνδεση με την ΒΔ, έχει να κάνει με το Cross origin policy (cors)
cors = CORS(
    app,
    resources={
        r"*": {"origins": ["http://localhost:4200"]}
    },  # στην port 4200 τρέχει η angular, εδώ του λέμε να επιτρέπεται ό,τι τρέχει τοπικά σε Angular
)

app.register_blueprint(
    user, url_prefix="/user"
)  # εδώ του λέμε ότι στο endpoint /user έχουμε πρόσβαση στο blueprint user το οποίο με την σειρά του έχει τα δικά του endpoints => κι έτσι θα έχουμε πρόσβαση στα endpoints του blueprint user 'χτυπώντας' τα: /user/register, /user/check_duplicate_email/<string:email> Κλπ
app.register_blueprint(customer, url_prefix="/customer")
