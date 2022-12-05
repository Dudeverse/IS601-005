from flask import Blueprint, render_template, request, flash, redirect, url_for
from sql.db import DB
company = Blueprint('company', __name__, url_prefix='/company')

@company.route("/search", methods=["GET"]) # se352 on Dec
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count for the company
    # don't do SELECT *
    query = "SELECT c.id, name, address, city, country, state, zip, website, count(e.id) as 'Employee Count ' FROM IS601_MP2_Companies c JOIN IS601_MP2_Employees e ON c.id = e.company_id or NULL WHERE 1=1"
    
    args = [] # <--- append values to replace %s placeholders
    allowed_columns = ["name", "city", "country", "state"]
    field_columns = zip(allowed_columns, allowed_columns)
    # TODO search-2 get name, country, state, column, order, limit request args
    name = request.args.get("name")
    country = request.args.get("country")
    state = request.args.get("state")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)
    # TODO search-3 append a LIKE filter for name if provided
    if name:
        query += " AND name like %s"
        args.append(f"%{name}%")
    # TODO search-4 append an equality filter for country if provided
    if country:
        query += " AND country = %s"
        args.append(f"{country}")
    # TODO search-5 append an equality filter for state if provided
    if state:
        query += " AND state = %s"
        args.append(f"{state}")
    # TODO search-6 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)    
    if column and order:
        
        if column in allowed_columns \
            and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"
    query += " GROUP BY c.id"

    
    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100
    try:
        if limit and int(limit) > 0 and int(limit) <= 100:
            query += " LIMIT %s"
            args.append(int(limit))
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds 
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
        # TODO search-9 make message user friendly
        flash(str(e), "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    return render_template("list_companies.html", rows=rows, allowed_columns=field_columns)

# se352 Dec-04-2022
@company.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        name = request.form.get("name", None)
        address = request.form.get("address", None)
        city = request.form.get("city", None)
        state = request.form.get("state", None)
        country = request.form.get("country", None)
        website = request.form.get("website", None)
        zipcode = request.form.get("zip", None)


        # TODO add-2 name is required (flash proper error message)
        if name == "":
            flash("Company name is required")
            return redirect(request.url)
        # TODO add-3 address is required (flash proper error message)
        if address == "":
            flash("Address is required")
            return redirect(request.url)
        # TODO add-4 city is required (flash proper error message)
        if city == "":
            flash("city is required")
            return redirect(request.url)
        # TODO add-5 state is required (flash proper error message)
        if state == "":
            flash("state is required")
            return redirect(request.url)
        # TODO add-6 country is required (flash proper error message)
        if country == "":
            flash("country is required")
            return redirect(request.url)
        # TODO add-7 website is not required
        if website == "":
            website = None
        # add-8 zipcode is required
        if zipcode == "":
            flash("Zip is required")
            return redirect(request.url)

        has_error = False # use this to control whether or not an insert occurs # se352 Dec-04-2022
        

        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP2_Companies (name, address, city, state, country, website, zip)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, name, address, city, state, country, website, zipcode 
                ) # <-- TODO add-8 add query and add arguments
                if result.status:
                    flash("Added Company", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                flash(str(e), "danger")
        
    return render_template("add_company.html")


# se352 Dec-04-2022

@company.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    id = request.args.get("id")
    row= None
    if id is None: # TODO update this for TODO edit-1
        flash("ID is missing", "danger")
        return redirect("employee.list")
    else:
        if request.method == "POST":
            # TODO edit-2 retrieve form data for name, address, city, state, country, zip, website
            name = request.form.get("name", None)
            address = request.form.get("address", None)
            city = request.form.get("city", None)
            state = request.form.get("state", None)
            country = request.form.get("country", None)
            zipcode = request.form.get("zip", None)
            website = request.form.get("website", None)
            # TODO edit-3 name is required (flash proper error message)
            if name == "":
                flash("Company name is required")
                return redirect(request.url)
            # TODO edit-4 address is required (flash proper error message)
            if address == "":
                flash("Address is required")
                return redirect(request.url)
            # TODO edit-5 city is required (flash proper error message)
            if city == "":
                flash("city is required")
                return redirect(request.url)
            # TODO edit-6 state is required (flash proper error message)
            if state == "":
                flash("state is required")
                return redirect(request.url)
            # TODO edit-7 country is required (flash proper error message)
            if country == "":
                flash("country is required")
                return redirect(request.url)
            if zipcode == "":
                flash("zip is required")
                return redirect(request.url)
            # TODO edit-8 website is not required
            if website == "":
                website = None
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            data = [name, address, city, state, country, zipcode, website]
            data.append(id)
            try:
                # TODO edit-9 fill in proper update query
                result = DB.update("""
                UPDATE IS601_MP2_Companies SET name = %s, address = %s, city = %s, state = %s, country = %s, zip = %s, website = %s WHERE id = %s""", *data)
                if result.status:
                    flash("Updated record", "success")
            except Exception as e:
                # TODO edit-10 make this user-friendly
                flash(str(e), "danger")
        try:
            # TODO edit-11 fetch the updated data
            result = DB.selectOne("SELECT name, address, city, state, country, zip , website FROM IS601_MP2_Companies as c WHERE c.id = %s", id)
            if result.status:
                row = result.row
                
        except Exception as e:
            # TODO edit-12 make this user-friendly
            flash(str(e), "danger")
    # TODO edit-13 pass the company data to the render template
    return render_template("edit_company.html", row=row)

# se352 Dec-04-2022
@company.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete company by id (unallocate any employees)
    id = request.args.get("id")
    args = {**request.args}
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_MP2_Employees WHERE id IN (SELECT id FROM IS601_MP2_Employees WHERE  company_id = %s) ", id)
            result2 = DB.delete("DELETE FROM IS601_MP2_Companies  WHERE id = %s", id)
            if result.status and result2.status:
                flash("Deleted record", "success")
        except Exception as e:
            # TODO make this user-friendly
            flash(e, "danger")
    # TODO delete-2 redirect to company search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
        del args["id"]
    return redirect(url_for("company.search", **args))