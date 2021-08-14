from flask import Blueprint, render_template
from db_conn import conn

companies = Blueprint("companies",__name__,template_folder="templates")

@companies.route("/companies")
def getCompanies():

    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM companies")
            companies = cur.fetchall()

    return render_template("companies.html",companies=companies)

iab_codes = Blueprint("iab_codes",__name__,template_folder="templates")

@iab_codes.route("/iab_codes")
def get_iab_codes():

    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM iab_codes")
            iab_codes = cur.fetchall()

    return render_template("iab_codes.html",iab_codes=iab_codes)

mcc_codes = Blueprint("mcc_codes",__name__,template_folder="templates")

@mcc_codes.route("/mcc_codes")
def get_mcc_codes():

    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM mcc_codes")
            mcc_codes = cur.fetchall()

    return render_template("mcc_codes.html",mcc_codes=mcc_codes)

