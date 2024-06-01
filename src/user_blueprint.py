from flask import Blueprint, request, Response
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from src.user_model import User
import json
from mongoengine.errors import NotUniqueError
from werkzeug.security import check_password_hash

user = Blueprint("user", __name__) # flask Blueprint = της python, βιβλιοθήκη flask

# η παρακάτω εκτελείται στο onSubmit του user-registration.components.ts που με την σειρά του καλεί το this.userService.registerUser(user).subscribe({...}), η registerUser είναι στο shared->services->user.service.ts

@user.route("/register", methods=["POST"]) #user = Blueprint("user", __name__) δες παραπάνω
# εδώ του λέμε ότι το endpoint είναι το /user/register (δες σχόλια στο __init__.py)
def register():
    try:    
        data = request.get_json()        
        User(**data).save()  # ** = unpacking the data and saving it to the database (κάνει destructure των data -> τα βάζει στα πεδία του User, αναλύει τα data στα πεδία του User), 
        # τα διπλά αστεράκια δείχνουν (σημαίνουν) ότι τα data που θα γίνουν unpacking είναι dictionary data type, τα dictionaries είναι τα αντίστοιχα Map της Java δηλ είναι εγγραφές σε μορφή key-value, ενώ το μονό αστεράκι αντίστοιχα δείχνει ότι είναι list      
        return Response(json.dumps({"msg": "User registered (backend)"}), status=201)
    except NotUniqueError as e1: #from mongoengine.errors import NotUniqueError
        print(e1)
        return Response(json.dumps({"msg": str(e1)}), status=400)
    except Exception as e: 
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400)

# Η παρακάτω εκτελείται γιατί στο HTML του User registration (user-registration.component.html) έχουμε βάλει στο πεδίο email το: (blur)="check_duplicate_email()
@user.route("/check_duplicate_email/<string:email>", methods=["GET"])
def check_duplicate_email(email):
    try:
        if User.objects(email=email):
            return Response(json.dumps({"msg": "Email already in use (backend)"}), status=400)
        return Response(json.dumps({"msg": "Email available (backend)"}), status=200)
    except Exception as e:
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400)

# η παρακάτω εκτελείται στο onSubmit του user-login.components.ts που με την σειρά του καλεί το this.userService.loginUser(credentials).subscribe({...}), η loginUser είναι στο shared->services->user.service.ts
@user.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json() #μας έρχεται το credentials (από την loginUser στο user.service.ts), έχει μέσα το email και το password
        user = User.objects(email=data["email"]).first() #o User είναι στο user_model.py
        if user:
            if check_password_hash(user.password, data["password"]): #είναι function της security της python
                fullname = f"{user.givenName}  {user.surName}"
                identity = {"fullname": fullname, "email": user.email}
                access_token = create_access_token(identity=identity) #είναι function της utils της python
                return Response(
                    json.dumps( #dumps = Serialize obj to a JSON formatted str
                        {"msg": "Login successful (backend)", "access_token": access_token} #επιστρέφει το access_token μέσα στο response, στην συνέχεια το παίρνουμε στην onSubmit() της user-login.ts μέσα στο next: (response)
                    ),
                    status=200, #εμείς ορίζουμε ότι status = 200 δηλ οκ
                )
        return Response(json.dumps({"msg": "Invalid credentials (backend)"}), status=400) #αν identity!=identity δηλ ο user δεν βρέθηκε
    except Exception as e: #σε οποιαδήποτε άλλη περίπτωση εμφάνισε το error
        print(e)
        return Response(json.dumps({"msg": str(e)}), status=400)
