<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 Shop Project</td></tr>
<tr><td> <em>Student: </em> Surya Teja Ethalapaka (se352)</td></tr>
<tr><td> <em>Generated: </em> 12/20/2022 11:32:15 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone-3-shop-project/grade/se352" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Orders will be able to be recorded </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Orders table with valid data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208767881-f6318bf4-4a97-463c-8efd-38081bfed76b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows the Orders Table in my db. It has the following<br>columns: id, user_id, created, total_price, address, payment_method, money_received, first_name, last_name. All data is<br>valid.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of OrderItems table with validate data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208768266-b170f267-aa7f-4eae-8dc9-ef0e3b7b80fe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot of OrderItems table from my db extensions. It has valid data<br>filled in it. Also, it refers to the table shown in previous deliverable,<br>check the order_id&#39;s.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the purchase form UI from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208769209-7950ca54-fc76-4cff-9d74-ac112fb2c63e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot of a purchase form from Heroku. It has valid data filled<br>in.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208769295-90eabbe5-3095-4a02-81bf-c77e9a42dd38.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot of above order going through.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot showing the items pending purchase from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208770612-a76b700e-b7e9-4938-a58d-a958c4055901.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>I have not implemented this page but I did implement the cart.price vs<br>product.price percentage change suing flash messages. The above screenshot captures that feature.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a screenshot showing the Order Process validations from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208770961-1420bfa5-ca5a-48fd-b247-c1cf9d24648e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot captures Verifying stock(shop) amount and quantity(customer) amount. It verifies the price<br>increase or decrease and displays it in percentages.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208771421-c053e125-05c6-4c1b-a28a-3b2a8a45d17a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The above snippet verifies the price entered by the user and total cost<br>of the purchase. If the entered amount is less, it displays &quot;you cannot<br>afford message&quot;, if more amount is entered the nit reverts back to cart<br>and displays to enter the right amount.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a screenshot showing the Order Process validations from the UI (Heroku)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208770612-a76b700e-b7e9-4938-a58d-a958c4055901.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing price difference<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208772035-663cc69f-e66c-43fb-a70c-b6e31fb9da06.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing unavailable stock message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208772198-6a8f6ba9-6bac-4cb2-a98b-22d27574e860.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows invalid &quot;Money Received&quot; message. This is when user enters amount that<br>is more than required.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208774159-3d397d52-f898-4e9d-8da9-8181bdc2b4f6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows invalid &quot;Money Received&quot; message. This is when user enters amount that<br>is less than required.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly describe the code flow/process of the purchase process</td></tr>
<tr><td> <em>Response:</em> <p>From user point of view:<br>Step 1 : I first add items to my<br>cart<br>Step 2: After adding enough items of my choice, I click on &quot;Place<br>order&quot; button.<br>Step 3: Now I&#39;m taken to a checkout form where I need<br>to fill in my first name, last name, payment method, Amount of money<br>I need to pay and my address.<br>Step 4: Click on save button. This<br>ensures that my form is submitted.<br>Step 5: Now I click on &quot;Buy now!&quot;<br>button below the save button.<br>Step 6: If I entered the amount correctly and<br>there&#39;s no change in product price after adding them to my cart, I&#39;ll<br>be redirected to an order confirmation page, knowing that my order is placed.<br><br>From<br>dev view-point:<br>1. When user adds items to their cart, the cart table gets<br>updated. However, in the meanwhile, if the store owner changes a product price<br>or if the item is out of stock, they wouldn&#39;t know until they<br>have clicked on the place order button.<br>2. When the user clicks on the<br>place order button, an entry/record would be made into the orders table. Here<br>the actual recording of the order starts.<br>3. When the user fills in valid<br>data in the form, the aforementioned record will get updated with the form<br>data. Submitting the form ensures the mapping of order id to user data(user<br>id)<br>4. After the user clicks on the Buy now button, another database table<br>called OrderItems gets updated. The table is a list of mappings from orders<br>and the users who placed the orders, along with items they purchased.<br>5. The<br>aforementioned summary page appears only if the user entered the amount correctly. Or<br>else they would be redirected to the cart.<br>6. If there&#39;s any error like<br>Invalid money, item-out-of-stock, item-price-change, the order doesn&#39;t go through. Meaning the records which<br>kept track of the order gets deleted. The user would have to update<br>their cart and then place an order again, this time with a new<br>order id.<br>&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Dudeverse/IS601-005/pull/48">https://github.com/Dudeverse/IS601-005/pull/48</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-se352-prod3.herokuapp.com/cart">https://is601-se352-prod3.herokuapp.com/cart</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Order Confirmation Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot showing the order details from the purchase form and the related items that were purchased with a thank you message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208769295-90eabbe5-3095-4a02-81bf-c77e9a42dd38.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot of order summary page. This includes Shippng info, payment method, cost<br>of each item, total cost, total money recieved, and balance. It also displays<br>Thank you message. My Project is a simple online grocery shop.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how this information is retrieved and displayed from a code logic perspective</td></tr>
<tr><td> <em>Response:</em> <p>This order-summary or Order confirmation page appears only if all these checks have<br>passed:<br>1. Quantity check: A check placed in order to verify the number of<br>items in the cart vs the number of items in stock. If everything<br>is ok, meaning the cart has items that are in stock, it goes<br>to next check.<br>2. Price change check: A check placed to verify if any<br>of the products have changed prices in the cart-purchase time window. In this<br>cart-purchase time window, anything could happen, like a product&#39;s price would have gone<br>up, or down. If this check fails, the app redirects the user to<br>their cart.<br>3. Money check: A final check that verifies the amount entered by<br>the user and the calculated total price of the cart items. If these<br>two don&#39;t match they get redirected to their cart. If the user enters<br>more amount, it goes back to cart page with a warning saying the<br>amount is invalid. If the user enters less amount, the same happens but<br>this time with a different warning saying they cannot afford the cart.<br><br>Once all<br>the above checks are passed, a record is created in the OrderItems table<br>and the backend query selects these details and calculates the subtotal and total<br>on the cart and displays them on the page. It displays the Order<br>Id, list of all items and their subtotals. The page also gathers the<br>form data the user has provided in a form prior to this page<br>and shows it as shipping info. It displays details like payment method, shipping<br>address, total cart cost, total amount received. It displays a thank you message.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Dudeverse/IS601-005/pull/49">https://github.com/Dudeverse/IS601-005/pull/49</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-se352-prod3.herokuapp.com/login">https://is601-se352-prod3.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> User will be able to see their Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history for a user</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208775918-b901518e-8fa2-476e-8dc5-19f3936c204c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The above screenshot shows the My orders page of a user. Each order<br>has a view button that can be clicked to see more details. <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208776253-1b9a5921-8085-49ce-992b-407fe43977da.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>For instance lets select the last row in the previous subtask&#39;s screenshot. Order<br>id 280. The above page is displayed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>The table_helper file and form_helper file handle the front end of it,<br>while the backend part is handled by shop.order and shop.orders methods in shop.py<br>file.<br>2. The shop.orders method selects the list of all the entries that are<br>associated with a single user_id and the related order id&#39;s from the Orders<br>table.<br>3. Each of these orders is displayed on the page along with a<br>view button next to them, in each line. A simple for loop iterates<br>this button and the links to their respective pages.<br>4. When the user presses<br>the view button on an order, another method called shop.order is called. This<br>is different from the previous method. This method utilizes both the Products table<br>and the OrderItems table and displays the product details in each order. This<br>is just like the cart page, but without the place order, delete order,<br>update order buttons.&nbsp;<br></li><br></ol><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Dudeverse/IS601-005/pull/50">https://github.com/Dudeverse/IS601-005/pull/50</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-se352-prod3.herokuapp.com/orders">https://is601-se352-prod3.herokuapp.com/orders</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Store Owner Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history from multiple users</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208776553-e5cfc7a0-6af8-4b86-82a0-b300d2f8c160.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshotshowing orders of all users. This is from admin&#39;s view. Each item has<br>a view button to click and see what they purchased. The username is<br>also displayed in the list.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208776808-da07770b-4b29-4c3f-a622-9a1c03a6b270.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The url captures the order_id and in the backend, it is locked with<br>user_id to display their purchase records. The above order is not from Store<br>owner/admin. It&#39;s from Mama bear in the previous subtask1 [order 272]. <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details (mostly how it differs from the user's purchase history feature)</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>For this I used the same approach like the previous deliverable, and<br>this time updated the permissions to admin only.&nbsp;<br>2. This feature lets the admin/store-owner<br>to look at the purchases they made, and also purchases made by users<br>other than them.<br>3. For this implementation, I have created two new methods and<br>two separate html files.&nbsp;<br>4. In shop.py file, I have created methods called admin.order<br>and admin.orders.<br>5. When the admin logs into his account, he can see a<br>separate column called &quot;All Orders&quot; which takes them to admin.orders.html page.<br>6. This page<br>utilizes the admin.orders method I mentioned above and this time it queries all<br>the order without the user_id being in the WHERE condition. With no WHERE<br>clause the query outputs every record.<br>7. Using this strategy I have retrieved the<br>records of all entries in the Orders Table and subsequently OrderItems table.<br>8. The<br>admin.order method strategy uses the same technique I mentioned in the previous subtask(Joining<br>the Products and OrderItems table),&nbsp; and displays the results based on which view<br>button the admin clicks.<br></li><br></ol><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Dudeverse/IS601-005/pull/51">https://github.com/Dudeverse/IS601-005/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-se352-dev3.herokuapp.com/admin/orders">https://is601-se352-dev3.herokuapp.com/admin/orders</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart page showing the button to place an order</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208775511-36649baf-60ee-4bf0-bff7-651805bafb94.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The Place order button is in the right bottom corner.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p><b><font size="3">Learnings:</font></b><div><ol><li>1. I have learnt how to write new route methods, create new<br>form templates using witforms, and learnt how to handle templates.</li><li>2. Understood how Jinja<br>automates HTML. I know this is not the most appropriate term, but to<br>me it seems like Jinja saves time, the time required to write HTML<br>code from scratch.&nbsp;</li><li>3. Learnt how Jinja templating technique can be used to create<br>templates and how the macros can be reused.</li><li>4. Learnt how to retrieve database<br>values and display them on the website. The main connection between front-end and<br>backend.</li><li>5. I also learnt how to write queries, although not most effective ones<br>but learnt how querying and route methods go hand-n-hand.</li><li>6. Learnt the basic working<br>of a shopping website, the functionality of a cart, and how a method<br>or an html page can be reused many times, wherever required, for e.g<br>edit and add item/product utilize the same method and form.</li><li>7. Learnt how Jinja&#39;s<br>scope is different from that of python&#39;s.&nbsp;</li></ol><br><b><font size="3">Issues:</font></b><br>1. I have not been able<br>to implement the pending purchase page in the first deliverable. The following issues<br>might be the reasons for my roadblock.<br><ul><li><b>No clear understanding of the sitemap: </b>I<br>wasn&#39;t sure why a pending purchase page is needed and I didn&#39;t even<br>start to visualize. Usually in shopping websites, as soon as you click on<br>place order, there&#39;s a form and upon filling the form and card details<br>the order is placed. I though this was the norm and went with<br>it. However this is just my understanding.<br></li><li><b>Not able to figure out writing templates<br>for forms and tables in time: </b>It took me a lot of time<br>and debugging to understand the woking of a template and this was very<br>experimental and time-consuming. Reading documentation and playing around with sample code has given<br>me enough idea to exploit existing templates and to use them to my<br>advantage, i.e., for adding other pages and features into the app.</li><li><b>pending purchase page<br>felt redundant:&nbsp;</b>&nbsp;Part of the problem was to understand the need for such a<br>page. Why would I need another page when price changes can be seen<br>through flash messages? it struck me later that such a page is necessary<br>because not all user immediately buy after adding items to their carts. Some<br>take days or even months, but they need to have a page other<br>than cart that keeps track of items in the cart and the changes<br>that happened to the items in the cart.</li><li><b>Not enough time to implement the<br>address form: </b>I have a very clear idea of how to implement the<br>address form(Checkout). But I didn&#39;t get enough time to work on it. It<br>felt a bit tedious and honestly, implementing the other features like cart and<br>purchase were more fun. That is why I went with a very simple<br>and primitive form, to save time and work on other features.&nbsp;<br></li></ul><div><b><font size="3">Solutions</font></b></div><ul><li><b>Using Flash<br>messages to alert user about price change:&nbsp;</b>&nbsp;I have flash messaging to implement the<br>price hike/discount feature. It seemed a good alternative, i.e., when the price is<br>a discounted price, we can use &quot;success&quot; message, which is a positive thing,<br>and for price hikes, I have used &quot;error&quot; attribute so it doesn&#39;t seem<br>very bad.<br></li><li><b>Possible approach for the address form page:</b> I can use the wtforms<br>to make a class for the address form, in fact that is what<br>i did for my simple form. I can use the country-state selector template<br>that has been used in BusinessManagement Miniproject, (Add company form). I could have<br>extended that into this project. I could have made the form look more<br>elegant with dropdowns and other validations, along with the pre-filled values feature.</li></ul></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone-3-shop-project/grade/se352" target="_blank">Grading</a></td></tr></table>
