from src import app

if __name__ == "__main__":
    app.run(debug=True) 
 # app = Flask(__name__) δες __init__.py αρχείο

#τρέχει τοπικά στην πόρτα 5000 (γιατί γράφει στο Terminal: Running on http://127.0.0.1:5000) (localhost = 127.0.0.1)
# ΠΡΟΣΟΧΗ: σ'αυτή την εντολή μπορώ να δηλώσω εγώ πόρτα π.χ. app.run(host='127.0.0.1', port=81), στην συνέχεια πηγαίνω στην εφαρμογή μου στην Angular, στις μεταβλητές που έχω φτιάξει μέσα στον φάκελο environments, συγκεκριμένα στο environments.development.ts και εκεί δηλώνω την πόρτα που έχω βάλει εδώ => ΕΤΣΙ ΓΙΝΕΤΑΙ Η ΣΥΝΔΕΣΗ ΜΕΤΑΞΥ ΤΟΥ BACKEND ΚΑΙ ΤΟΥ FRONTEND δηλ έτσι συνδέω το Frontend με το ΣΥΓΚΕΚΡΙΜΕΝΟ Backend !


