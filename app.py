from flask import Flask, render_template, request, redirect, url_for, session
from forms import CalculationForm
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'

############################################

        # SQL DATABASE AND MODELS

##########################################
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
# Migrate(app,db)

@app.route("/", methods=['GET', 'POST'])
def index():
    form = CalculationForm()
    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():
        # Grab the data from the breed on the form.
        session['item1'] = form.item1.data
        session['item2'] = form.item2.data
        session['quantity1'] = form.quantity1.data
        session['quantity2'] = 5

        return redirect(url_for("result"))

    return render_template("index.html", form=form)

@app.route("/methodology")
def methodology():
    return render_template("methodology.html")


@app.route("/result")
def result():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)

