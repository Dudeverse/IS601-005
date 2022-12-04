import io
from flask import Blueprint, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from sql.db import DB
import traceback
import csv

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route("/import", methods=["GET","POST"])
def importCSV():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.

        if file.filename == '':
            flash('No selected file', "warning")
            return redirect(request.url)
        # TODO importcsv-1 check that it's a .csv file, return a proper flash message if it's not|se352--Nov 30 2022|
        if len(file.filename) < 4 or file.filename[len(file.filename)-4:] != ".csv":
            flash("Not a csv", "danger")
            return redirect(request.url)
        if file and secure_filename(file.filename):
            companies = []
            employees = []
            company_query = """
            INSERT INTO IS601_MP2_Companies (name, address, city, country, state, zip, website)
                        VALUES (%(name)s, %(address)s, %(city)s, %(country)s, %(state)s, %(zip)s, %(website)s)
                        ON DUPLICATE KEY UPDATE address = %(address)s, city = %(city)s, country=%(country)s, state=%(state)s, zip=%(zip)s, website=%(website)s 
            """
            employee_query = """
            INSERT INTO IS601_MP2_Employees (first_name, last_name, email, company_id)
                        VALUES (%(first_name)s, %(last_name)s, %(email)s, (SELECT id FROM IS601_MP2_Companies WHERE name = %(company_name)s LIMIT 1))
                        ON DUPLICATE KEY UPDATE first_name=%(first_name)s, last_name = %(last_name)s, email = %(email)s, company_id = (SELECT id FROM IS601_MP2_Companies WHERE name = %(company_name)s LIMIT 1)
            """
            # Note: this reads the file as a stream instead of requiring us to save it
            stream = io.TextIOWrapper(file.stream._file, "UTF8", newline=None)
            # TODO importcsv-2 read the csv file stream as a dict|se352--Nov 30 2022|
            companies_keys = {"company_name","address","city","country","state","zip","web"}
            employees_keys = {"first_name","last_name","email" }
            csv_reader = csv.DictReader(stream)
            for row in csv_reader:
                employee_data = {}
                company_data = {}
                for key in row.keys():
                    if key in companies_keys:
                        if key == "company_name":
                            company_data["name"] = row[key]
                            employee_data[key] = row[key]
                        elif key == "web":
                            company_data["website"] = row[key]
                        else:
                            company_data[key] = row[key]
                    elif key in employees_keys:
                        employee_data[key] = row[key]
            # TODO importcsv-3 extract company data and append to company list as a dict only with company data
                companies.append(company_data)
            # TODO importcsv-4 extract employee data and append to employee list as a dict only with employee data 
                employees.append(employee_data)


            print(len(companies))
            print(len(employees))

            if len(companies) > 0:
                print(f"Inserting or updating {len(companies)} companies")
                try:
                    result = DB.insertMany(company_query, companies)
                    # TODO importcsv-5 display flash message about number of companies inserted|se352--Nov 30 2022|
                    num_companies = len(companies)
                    flash(f"{num_companies} companies inserted", "success")
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error loading in the csv data", "danger")
            else:
                # TODO importcsv-6 display flash message (info) that no companies were loaded|se352--Nov 30 2022|
                flash("No companies were added", "info")
                pass
            if len(employees) > 0:
                print(f"Inserting or updating {len(employees)} employees")
                try:
                    result = DB.insertMany(employee_query, employees)
                    # TODO importcsv-7 display flash message about number of employees loaded|se352--Nov 30 2022|
                    num_employees = len(employees)
                    flash(f"{num_employees} employees loaded", "success")
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error loading in the csv data", "danger")
            else:
                # TODO importcsv-8 display flash message (info) that no employees were loaded|se352--Nov 30 2022|
                flash("No employeess were loaded", "info")
                pass
    return render_template("upload.html")