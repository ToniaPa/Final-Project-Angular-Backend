import mongoengine as me
from werkzeug.security import generate_password_hash


class User(me.Document): #Η κλάση είναι me.Document δηλ είναι εγγραφή της MongoDB (me από πιο πάνω: import mongoengine as me)
    # τα πεδία της κλάσης (είναι τα πεδία του Collection στην MongoDB):
    givenName = me.StringField(required=True)
    surName = me.StringField(required=True)
    email = me.StringField(required=True, unique=True)
    password = me.StringField(required=True)
    meta = {"collection": "users", "db_alias": "angular"} #METADATA, δεν είναι πεδίο
    # meta = {"collection": "users", "db_alias": "codingfactory"} # εδώ είναι του καθηγητή

# εδώ του λέει να φτιάξει έναν hash code για το password του User που κάνουμε register (δηλ του User που δημιουργούμε στo user-registration component => το password φυλάσσεται στην MongoDB Atlas βάση μου σε hash μορφή (για security)):
# ΠΡΟΣΟΧΗ: η function save είναι ΜΕΣΑ στην class User
# def save = Save the ~mongoengine.Document to the database. If the document already exists, it will be updated, otherwise it will be created. Returns the saved object instance.
    def save(self, *args, **kwargs):
        self.password = generate_password_hash(self.password) #την generate_password_hash την κάνει import στην αρχή
        super(User, self).save(*args, **kwargs)
        # *args = unpacking των args που είναι list (οι λίστες της python δηλώνονται μέσα σε [] π.χ. mylist = ["apple", "banana", "cherry"] το ένα αστεράκι είναι python syntax και δηλώνει το list unpacking)
        # **kwargs = unpacking των keyword args που είναι dictionary δηλ είναι εγγραφές τύπου key: value (τα dictionaries της python είναι τα αντίστοιχα maps της java και δηλώνονται μέσα σε {} 
        # π.χ. thisdict = {
        #                    "brand": "Ford",
        #                    "model": "Mustang",
        #                    "year": 1964
        #                  }
        # τα δύο αστεράκια είναι python syntax και δηλώνει το dictionary unpacking)
