from flask import Blueprint, render_template, request, flash

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", author = "toto")



@views.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html", text ="testing")



@views.route('/signup', methods=['GET','POST'])
def signup():

    # data = request.form
    # print(data)

    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('email must be greater than 4 characters', category='error')
        elif len(firstname) < 2:
            flash('firstname must be greater than 2 characters', category='error')
        elif password1 != password2:
            flash('password don\'t match', category='error')
        elif len(password1) < 7 :
            flash('password must be greater than 7 characters', category='error')
        else : 
            #add user to DB
            flash('Account Created', category='success')

    return render_template("signup.html")



@views.route('/graph', methods=['GET','POST'])
def graph():

    data = [
        ("01-01-2020", 1594),
        ("02-01-2020", 1679),
        ("03-01-2020", 1613),
        ("04-01-2020", 1651),
        ("05-01-2020", 1600),
        ("05-01-2120", 1600)
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]


    return render_template("graph.html", labels = labels, values = values)