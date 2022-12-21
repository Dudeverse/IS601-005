CREATE TABLE
    IF NOT EXISTS IS601_S_Orders(
        id int AUTO_INCREMENT PRIMARY KEY,
        total_price int,
        number_of_items int,
        user_id int,
        first_name VARCHAR(30),
        last_name VARCHAR(30),
        payment_method VARCHAR(30),
        money_received int,
        address VARCHAR(30),
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES IS601_Users(id)
    )