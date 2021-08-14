from __future__ import with_statement
from flask import Flask, render_template
import routes

app = Flask(__name__)
app.register_blueprint(routes.companies,url_prefix = "")
app.register_blueprint(routes.mcc_codes,url_prefix = "")
app.register_blueprint(routes.iab_codes,url_prefix = "")

@app.route("/")
def home():

    return render_template("home.html")

    #response tipi (json-html-csv) belirt
    #kodu düzenle

if __name__ == "__main__":
    app.run(debug=True)
