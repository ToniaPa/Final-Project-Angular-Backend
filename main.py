from src import app

if __name__ == "__main__":
    app.run(debug=True) 
 # app = Flask(__name__) δες __init__.py αρχείο

#  τρέχω το παρόν όντας στο φάκελο
#  (venv) C:\Users\papad\CodingFactory - ασκήσεις\CF5\Angular-Fragoudakis\angular-introduction-python-backend> και γράφοντας την εντολή py main.py
# βλέπω ότι τρέχει τοπικά στην πόρτα 5000 (γιατί γράφει στο Terminal: Running on http://127.0.0.1:5000) (localhost = 127.0.0.1)
# ΠΡΟΣΟΧΗ: σ'αυτή την εντολή μπορώ να δηλώσω εγώ πόρτα π.χ. app.run(host='127.0.0.1', port=81), στην συνέχεια πηγαίνω στην εφαρμογή μου στην Angular, στις μεταβλητές που έχω φτιάξει μέσα στον φάκελο environments, συγκεκριμένα στο environments.development.ts και εκεί δηλώνω την πόρτα που έχω βάλει εδώ => ΕΤΣΙ ΓΙΝΕΤΑΙ Η ΣΥΝΔΕΣΗ ΜΕΤΑΞΥ ΤΟΥ BACKEND ΚΑΙ ΤΟΥ FRONTEND δηλ έτσι συνδέω το Frontend με το ΣΥΓΚΕΚΡΙΜΕΝΟ Backend !

# για να βγω στο (venv) που είναι virtual environment στον φάκελό μου και σημαίνει ότι τρέχω την Python αποκλειστικά σε αυτόν τον φάκελο δημιουργώντας εικονικό περιβάλλον (ΕΤΣΙ ΠΡΕΠΕΙ ΝΑ ΓΙΝΕΤΑΙ ΜΕ ΤΗΝ Python! καθε εφφαρμογή ΠΡΕΠΕΙ να τρέχει σε ΔΙΚΟ ΤΗΣ (αυτόνομο) περιβάλλον), γράφω στον φάκελο C:\Users\papad\CodingFactory - ασκήσεις\CF5\Angular-Fragoudakis\angular-introduction-python-backend> την εντολή venv\Scripts\activate
#βέβαια θα πρέπει προηγουμένως να έχει δημιουργηθεί το venv, αυτό γίνεται με την εντολή: python -m venv venv
