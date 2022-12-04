from flask import Blueprint, render_template, request, flash, redirect, url_for
from sql.db import DB
import re

employee = Blueprint('employee', __name__, url_prefix='/employee')


@employee.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    query = "SELECT e.id , first_name, last_name, email, e.company_id, name  FROM IS601_MP2_Employees as e LEFT JOIN IS601_MP2_Companies as c ON e.company_id = c.id WHERE 1=1"
    args = [] # <--- append values to replace %s placeholders
    allowed_columns = ["first_name", "last_name", "email", "name"]
    field_columns = zip(allowed_columns, allowed_columns)
    print(allowed_columns)
    print(request.args)
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    fn = request.args.get("first_name")
    ln = request.args.get("last_name")
    email = request.args.get("email")
    company = request.args.get("company")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)
    
    # TODO search-3 append like filter for first_name if provided
    if fn:
        query += " AND first_name like %s"
        args.append(f"%{fn}%")
    # TODO search-4 append like filter for last_name if provided
    if ln:
        query += " AND last_name like %s"
        args.append(f"%{ln}%")
    # TODO search-5 append like filter for email if provided
    if email:
        query += " AND email like %s"
        args.append(f"%{email}%")
    # TODO search-6 append equality filter for company_id if provided
    if company:
        query += " AND e.company_id = %s"
        args.append(f"{company}")
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)    
    if column and order:
        
        if column in allowed_columns \
            and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"
    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    try:
        if limit and int(limit) > 0 and int(limit) <= 100:
            query += " LIMIT %s"
            args.append(int(limit))
    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds 
        elif int(limit) >100 or int(limit)<0:
            pass
            flash("limit out of bounds", "danger")

    except ValueError:
        flash("enter a valid value", "warning")


    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, *args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-10 make message user friendly
        flash(e, "error")
    # hint: use allowed_columns in template to generate sort dropdown
    return render_template("list_employees.html", rows=rows, allowed_columns=field_columns)

@employee.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for first_name, last_name, company, email 
        first_name = request.form.get("first_name", None)
        last_name = request.form.get("last_name", None)
        company = request.form.get("company", None)
        email = request.form.get("email", None)
        # TODO add-2 first_name is required (flash proper error message)
        if first_name == "":
            flash("First name is required")
            return redirect(request.url)
        # TODO add-3 last_name is required (flash proper error message)
        if last_name == "":
            flash("last name is required")
            return redirect(request.url)
        # TODO add-4 company (may be None)
        if company == "":
            company = None
        # TODO add-5 email is required (flash proper error message)
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
        if email == "":
            flash("email is required")
            return redirect(request.url)
        elif not re.search(regex, email):
            flash("email is not valid")
            return redirect(request.url)
        
        try:
            result = DB.insertOne("""
            INSERT INTO IS601_MP2_Employees (first_name, last_name, company_id, email)
                        VALUES (%s, %s, %s, %s)
            """,first_name,last_name,company,email
            ) # <-- TODO add-6 add query and add arguments
            if result.status:
                flash("Created Employee Record", "success")
        except Exception as e:
            # TODO add-7 make message user friendly
            flash(str(e), "danger")
    return render_template("add_employee.html")

@employee.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    id = request.args.get("id")
    row = None
    if id is None:
        flash("ID is missing", "danger")
        return redirect("employee.list")
    else: # TODO update this for TODO edit-1
        if request.method == "POST":
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")
            company = request.form.get("company")
            email = request.form.get("email")
            company_id = request.form.get("company_id")
            # TODO edit-2 first_name is required (flash proper error message)
            if first_name == "":
                flash("First name is required")
                return redirect(request.url)
            # TODO edit-3 last_name is required (flash proper error message)
            if last_name == "":
                flash("last name is required")
                return redirect(request.url)
            # TODO edit-4 company may be None
            if company == "":
                company = None
            # TODO edit-5 email is required (flash proper error message)
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
            if email == "":
                flash("email is required")
                return redirect(request.url)
            elif not re.search(regex, email):
                flash("email is not valid")
                return redirect(request.url)
            data = [first_name, last_name, company, email]
            data.append(id)
            try:
                # TODO edit-6 fill in proper update query
                result = DB.update("UPDATE IS601_MP2_Employees SET first_name = %s, last_name = %s, company_id = %s, email = %s  WHERE id = %s", *data)
                if result.status:
                    flash("Updated record", "success")
            except Exception as e:
                # TODO edit-7 make this user-friendly
                flash(e, "danger")
        try:
            # TODO edit-8 fetch the updated data (including company_name)
            # company_name should be 'N/A' if the employee isn't assigned to a company
            result = DB.selectOne("SELECT first_name, last_name, email, e.company_id, name FROM IS601_MP2_Employees as e LEFT JOIN IS601_MP2_Companies as c ON e.company_id = c.id WHERE e.id = %s AND 1=1", id)
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-9 make this user-friendly
            flash(str(e), "danger")
    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html", row=row)

@employee.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete employee by id
    id = request.args.get("id")
    args = {**request.args}
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_MP2_Employees WHERE id = %s", id)
            if result.status:
                flash("Deleted record", "success")
        except Exception as e:
            # TODO make this user-friendly
            flash(e, "danger")
    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
        del args["id"]
    return redirect(url_for("employee.search", **args))