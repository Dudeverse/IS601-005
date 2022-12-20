import traceback
from flask import Blueprint, request, flash, render_template, redirect, url_for, request
from werkzeug.datastructures import MultiDict
from shop.forms import ItemForm, CheckoutForm
from sql.db import DB
from roles.permissions import admin_permission
from flask_login import login_required, current_user
shop = Blueprint('shop', __name__, url_prefix='/',template_folder='templates')

@shop.route("/item_details", methods=["GET","POST"])
@login_required
def item_details():
    form = ItemForm()
    id = request.args.get("id", form.id.data or None)
    if id:
        try:
            result = DB.selectOne("SELECT id, name, description, category, stock, unit_price, image, visibility FROM IS601_S_Products WHERE id = %s", id)
            if result.status and result.row:
                    form.process(MultiDict(result.row))
        except Exception as e:
            print("Error fetching item", e)
            flash("Item not found", "danger")
    return render_template("prod_details.html", form=form)



@shop.route("/admin/item", methods=["GET","POST"])
@admin_permission.require(http_exception=403)
def item():
    form = ItemForm()
    id = request.args.get("id", form.id.data or None)
    type = "Edit" if id else "Create"
    if form.validate_on_submit():
        if form.id.data: # it's an update
            try:
                result = DB.update("UPDATE IS601_S_Products set name = %s, description = %s, category = %s, stock = %s, unit_price = %s, image=%s, visibility=%s WHERE id = %s",
                form.name.data, form.description.data, form.category.data, form.stock.data, form.unit_price.data, form.image.data, 1 if form.visibility.data else 0, form.id.data)
                if result.status:
                    flash(f"Updated {form.name.data}", "success")
            except Exception as e:
                print("Error updating item", e)
                flash(f"Error updating item {form.name.data}", "danger")
        else: # it's a create
            try:
                result = DB.update("""INSERT INTO IS601_S_Products (name, description, category, stock, unit_price, image, visibility) 
                VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                form.name.data, form.description.data, form.category.data, form.stock.data, form.unit_price.data, form.image.data, 1 if form.visibility.data else 0)
                if result.status:
                    flash(f"Created {form.name.data}", "success")
                    form = ItemForm() # clear form
            except Exception as e:
                print("Error creating item", e)
                flash(f"Error creating item {form.name.data}", "danger")
    if id:
        try:
            result = DB.selectOne("SELECT id, name, description, category, stock, unit_price, image, visibility FROM IS601_S_Products WHERE id = %s", id)
            if result.status and result.row:
                    form.process(MultiDict(result.row))
        except Exception as e:
            print("Error fetching item", e)
            flash("Item not found", "danger")
    return render_template("item.html", form=form, type=type)

@shop.route("/admin/items/delete", methods=["GET"])
@admin_permission.require(http_exception=403)
def delete():
    id = request.args.get("id")
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_S_Products WHERE id = %s", id)
            if result.status:
                flash("Deleted item", "success")
        except Exception as e:
            print("Error deleting item",e)
            flash("Error deleting item", "danger")
    return redirect(url_for("shop.items"))

@shop.route("/admin/items", methods=["GET","POST"])
@admin_permission.require(http_exception=403)
def items():
    rows = []
    try:
        result = DB.selectAll("SELECT id, name, description, category, stock, unit_price, image, visibility FROM IS601_S_Products LIMIT 25",)
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error fetching items", e)
        flash("There was a problem loading items", "danger")
    return render_template("items.html", rows=rows)

@shop.route("/shop", methods=["GET","POST"]) #se352 dec 17 8:42 pm 2022
@login_required
def shop_list():
    rows = []
    query = "SELECT id, name, description, category, stock, unit_price, image, visibility FROM IS601_S_Products WHERE stock > 0 AND visibility = TRUE AND 1=1"
    args = []
    allowed_columns = ["category","unit_price"]
    field_columns = zip(allowed_columns, allowed_columns)
    name = request.args.get("name")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)

    if name:
        query += " AND name like %s"
        args.append(f"%{name}%")

    if column and order:
        
        if column in allowed_columns \
            and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"

    try:
        if limit and int(limit) > 0 and int(limit) <= 100:
            query += " LIMIT %s"
            args.append(int(limit))
        elif int(limit) >100 or int(limit)<0:
            pass
            flash("limit out of bounds", "danger")

    except ValueError:
        flash("enter a valid value", "warning")

    try:
        result = DB.selectAll(query, *args)
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error fetching items", e)
        flash("There was a problem loading items", "danger")
    return render_template("shop.html", rows=rows, allowed_columns=field_columns)



#se352 18 dec 20222
@shop.route("/cart", methods=["GET","POST"])
@login_required
def cart():
    product_id = request.form.get("product_id")
    id = request.form.get("id", product_id)
    print("id", id)
    quantity = request.form.get("quantity", 1, type=int)
    user_id = current_user.get_id()
    if id and user_id:
        if quantity > 0:
            try:
                result = DB.selectOne("SELECT unit_price,name from IS601_S_Products WHERE id = %s", id)
                print("result", result)
                if result.status and result.row:
                    unit_price = result.row["unit_price"]
                    name = result.row["name"]
                    if product_id: # update from cart
                        result = DB.insertOne("""
                        UPDATE IS601_S_Cart SET
                        quantity = %(quantity)s,
                        unit_price = %(unit_price)s
                        WHERE product_id = %(id)s and user_id = %(user_id)s
                        """,{
                            "id":id,
                            "quantity": quantity,
                            "unit_price":unit_price,
                            "user_id":user_id
                        })
                        if result.status:
                            flash(f"Updated quantity for {name} to {quantity}", "success")
                    else: #add from shop
                        result = DB.insertOne("""
                        INSERT INTO IS601_S_Cart (product_id, quantity, unit_price, user_id)
                        VALUES(%(id)s, %(quantity)s, %(unit_price)s, %(user_id)s)
                        ON DUPLICATE KEY UPDATE
                        quantity = quantity + %(quantity)s,
                        unit_price = %(unit_price)s
                        """,{
                            "id":id,
                            "quantity": quantity,
                            "unit_price":unit_price,
                            "user_id":user_id
                        })
                        
                        if result.status:
                            flash(f"Added {quantity} of {name} to cart", "success")
            except Exception as e:
                print("Error updating cart" ,e)
                flash("Error updating cart", "danger")
        else:
            # assuming delete
            try:
                print(product_id)
                result = DB.delete("DELETE FROM IS601_S_Cart where product_id = %s and user_id = %s", id, user_id)
                if result.status:
                    flash("Deleted item from cart", "success")
            except Exception as e:
                print("Error deleting item", e)
                flash("Error deleting item from cart", "danger")
    rows = []
    try:
        result = DB.selectAll("""SELECT c.id, product_id, name, c.quantity, (c.quantity * c.unit_price) as subtotal 
        FROM IS601_S_Cart c JOIN IS601_S_Products i on c.product_id = i.id
        WHERE c.user_id = %s
        """, current_user.get_id())
        if result and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error getting cart", e)
        flash("Error fetching cart", "danger")
    return render_template("cart.html", rows=rows)



#se352 18 dec 20222
@shop.route("/cart_empty", methods=["GET","POST"])
@login_required
def cart_empty():
    user_id = current_user.get_id()
    if user_id:
        try:
            result = DB.delete("DELETE FROM IS601_S_Cart where user_id = %s", user_id)
            if result.status:
                    flash("Emptied your cart", "success")
        except Exception as e:
            print("Error deleting cart", e)
            flash("Error deleting cart", "danger")
    return redirect(url_for("shop.cart"))

@shop.route("/purchase", methods=["GET","POST"])
@login_required
def purchase():
    cart = []
    total = 0
    quantity = 0
    order = {}
    try:
        DB.getDB().autocommit = True # make a transaction

        # get cart to verify
        
        result = DB.selectAll("""SELECT c.id, product_id, name, c.quantity, i.stock, c.unit_price as cart_unit_price, i.unit_price as item_unit_price, (c.quantity * c.unit_price) as subtotal 
        FROM IS601_S_Cart c JOIN IS601_S_Products i on c.product_id = i.id
        WHERE c.user_id = %s
        """, current_user.get_id())
        if result.status and result.rows:
            cart = result.rows
        # verify cart # se352 dec19  2022
        has_error = False
        for item in cart:
            if item["quantity"] > item["stock"]:
                flash(f"Sorry! Item {item['name']} doesn't have enough stock left", "warning")
                flash(f"Remaining stock quantity for {item['name']} is {item['stock']}. Feel free to update your cart!", "success")
                result = DB.delete("DELETE FROM IS601_S_Orders WHERE total_price IS NULL AND user_id = %s", current_user.get_id())
                has_error = True
            if item["cart_unit_price"] != item["item_unit_price"]:
                x = item["cart_unit_price"]
                y = item["item_unit_price"]
                if x < y:
                    percent_increase = ((y-x)/x)*100
                    hiked_price = x + ((percent_increase*x)/100)
                    flash(f"Item {item['name']}'s price has gone up by {percent_increase}%. Hiked price is {hiked_price}. Please refresh cart. To refresh, click on update button.", "warning")
                    result = DB.delete("DELETE FROM IS601_S_Orders WHERE total_price IS NULL AND user_id = %s", current_user.get_id())
                    has_error = True
                if x > y:
                    percent_decrease = ((x-y)/x)*100
                    discounted_price = x - ((percent_decrease*x)/100)
                    flash(f"Item {item['name']}'s price has gone down by {percent_decrease}%. Discounted price is {discounted_price}! Please refresh cart. To refresh, click on update button.", "success")
                    result = DB.delete("DELETE FROM IS601_S_Orders WHERE total_price IS NULL AND user_id = %s", current_user.get_id())
                    has_error = True
            total += int(item["subtotal"] or 0)
            quantity += int(item["quantity"])

        print("quantity check passed")
        # check can afford # se352 dec19  2022
        if not has_error:
            result = DB.selectOne("SELECT MAX(id) as m FROM IS601_S_Orders WHERE user_id = %s", current_user.get_id())
            order_id = result.row["m"]
            result = DB.delete("DELETE FROM IS601_S_Orders WHERE first_name IS NULL AND user_id = %s", current_user.get_id())

            result = DB.selectOne("SELECT money_received as p FROM IS601_S_Orders WHERE id = %s", order_id)
            
            if result.row["p"]<total:
                flash("You can't afford to make this purchase", "danger")
                result = DB.selectOne("SELECT MAX(id) as m FROM IS601_S_Orders WHERE user_id = %s", current_user.get_id())
                order_id = result.row["m"]
                result = DB.delete("DELETE FROM IS601_S_Orders WHERE id = %s", order_id)
                has_error = True
            if result.row["p"]>total:
                flash("You have entered invalid amount, please enter the right amount in checkout form.", "danger")
                result = DB.selectOne("SELECT MAX(id) as m FROM IS601_S_Orders WHERE user_id = %s", current_user.get_id())
                order_id = result.row["m"]
                result = DB.delete("DELETE FROM IS601_S_Orders WHERE id = %s", order_id)
                has_error = True
        print("affordability check passed")
        # create order data
        
        # se352 dec19  2022
        
        if not has_error:
            result = DB.selectOne("SELECT MAX(id) as m FROM IS601_S_Orders WHERE user_id = %s", current_user.get_id())
            order_id = result.row["m"]
            result = DB.update("UPDATE IS601_S_Orders SET total_price = %s, number_of_items = %s, user_id =%s WHERE id =%s", total, quantity, current_user.get_id(), order_id)


            

            result = DB.selectOne("SELECT MAX(id) as m FROM IS601_S_Orders WHERE user_id = %s", current_user.get_id())
            if not result.status:
                flash("Error generating order", "danger")
                DB.getDB().rollback()
                has_error = True
            else:
                order_id = result.row["m"]
                order["order_id"] = order_id
                order["total"] = total
                order["quantity"] = quantity
                result = DB.selectOne("SELECT money_received as p, payment_method as pm, address as a FROM IS601_S_Orders WHERE id = %s", order_id)
                money_received = result.row["p"]
                order["money_received"] = money_received
                payment_method = result.row["pm"]
                order["payment_method"] = payment_method
                address = result.row["a"]
                order["address"] = address
                
                print("order id is", order_id)
        print("created order data")
        # record order history
        result = DB.selectOne("SELECT MAX(id) as m FROM IS601_S_Orders WHERE user_id = %s", current_user.get_id())
        order_id = result.row["m"]
        if order_id > -1 and not has_error:
            # Note: Not really an insert 1, it'll copy data from Table B into Table A
            print("code has cometh")
            result = DB.insertOne("""INSERT INTO IS601_S_OrderItems (quantity, unit_price, order_id, product_id, user_id)
            SELECT quantity, unit_price, %s, product_id, user_id FROM IS601_S_Cart c WHERE c.user_id = %s""",
            order_id, current_user.get_id())
            
            if not result.status:
                flash("Error recording order history", "danger")
                has_error = True
                DB.getDB().rollback()
        # update stock based on cart data
        if not has_error:
            result = DB.update("""
            UPDATE IS601_S_Products 
                set stock = stock - (select IFNULL(quantity, 0) FROM IS601_S_Cart WHERE product_id = IS601_S_Products.id and user_id = %(uid)s) 
                WHERE id in (SELECT product_id from IS601_S_Cart where user_id = %(uid)s)
            """, {"uid":current_user.get_id()} )
            if not result.status:
                flash("Error updating stock", "danger")
                has_error = True
                DB.getDB().rollback()

        
        #empty the cart
        if not has_error:
            result = DB.delete("DELETE FROM IS601_S_Cart WHERE user_id = %s", current_user.get_id())
        else:
            return redirect(url_for("shop.cart"))
    except Exception as e:
        print("Transaction exception", e)
        flash("Something went wrong", "danger")
        traceback.print_exc()
    # TODO route to thank you / summary page
    # TODO add link from cart page to this route
    return render_template("order_summary.html", rows=cart, order=order)

@shop.route("/orders", methods=["GET"])
@login_required
def orders():
    rows = []
    try:
        result = DB.selectAll("""
        SELECT id, total_price, number_of_items, created FROM IS601_S_Orders WHERE user_id = %s
        """, current_user.get_id())
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error getting orders", e)
        flash("Error fetching orders", "danger")
    return render_template("orders.html", rows=rows)

# se352 dec19  2022

@shop.route("/order", methods=["GET"])
@login_required
def order():
    rows = []
    total = 0
    id = request.args.get("id")
    if not id:
        flash("Invalid order", "danger")
        return redirect(url_for("shop.orders"))
    try:
        # locking query to order_id and user_id so the user can see only their orders
        result = DB.selectAll("""
        SELECT name, oi.unit_price, oi.quantity, (oi.unit_price*oi.quantity) as subtotal FROM IS601_S_OrderItems oi JOIN IS601_S_Products i on oi.product_id = i.id WHERE order_id = %s ANd user_id = %s
        """, id, current_user.get_id())
        if result.status and result.rows:
            rows = result.rows
            total = sum(int(row["subtotal"]) for row in rows)
            print(total)
    except Exception as e:
        print("Error getting order", e)
        flash("Error fetching order", "danger")
    return render_template("order.html", rows=rows, total=total)


# se352 dec19  2022
@shop.route("/place_order", methods=["GET","POST"])
@login_required
def place_order():
    form = CheckoutForm()
    user_id = current_user.get_id()
    if user_id:
        try:
            print("code entered here")
            result = DB.insertOne("""INSERT INTO IS601_S_Orders (first_name, last_name, payment_method, money_received, address, user_id) VALUES (%s, %s, %s, %s, %s,%s) """, form.first_name.data, form.last_name.data, form.payment_method.data, form.money_received.data, form.address.data, current_user.get_id())
            if result.status and result.row:
                    flash("Filled form", "success")
        except Exception as e:
            print("Error fetching page", e)
            flash("page not found", "danger")
    return render_template("place_order.html", form=form)

# se352 dec19  2022
@shop.route("/admin/orders", methods=["GET"])
@admin_permission.require(http_exception=403)
def admin_orders():
    rows = []
    try:
        result = DB.selectAll("""
        SELECT o.id, o.total_price, o.number_of_items, o.created, u.username FROM IS601_S_Orders as o JOIN IS601_Users as u ON o.user_id=u.id""")
        if result.status and result.rows:
            rows = result.rows
            print(result.rows)
    except Exception as e:
        print("Error getting orders", e)
        flash("Error fetching orders", "danger")
    return render_template("admin_orders.html", rows=rows)

# se352 dec19  2022
@shop.route("/admin/order", methods=["GET"])
@login_required
def admin_order():
    rows = []
    total = 0
    id = request.args.get("id")
    if not id:
        flash("Invalid order", "danger")
        return redirect(url_for("shop.admin_orders"))
    try:
        # locking query to order_id and user_id so the user can see only their orders
        result = DB.selectAll("""
        SELECT name, oi.unit_price, oi.quantity, (oi.unit_price*oi.quantity) as subtotal FROM IS601_S_OrderItems oi JOIN IS601_S_Products i on oi.product_id = i.id WHERE order_id = %s AND oi.user_id > -1""", id)
        if result.status and result.rows:
            rows = result.rows
            total = sum(int(row["subtotal"]) for row in rows)
    except Exception as e:
        print("Error getting order", e)
        flash("Error fetching order", "danger")
    return render_template("admin_order.html", rows=rows, total=total)