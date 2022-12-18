<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Surya Teja Ethalapaka (se352)</td></tr>
<tr><td> <em>Generated: </em> 12/18/2022 5:08:58 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone-2-shop-project/grade/se352" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208311490-9d700256-dc15-48cc-b778-572d20a104a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing valid data filled in.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208311540-f9a041ea-de48-4fbc-8f15-2e3324c53a13.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Columns: (id, name, description, category, stock, created, modified, unit_price, visibility [true, false]) are<br>all visible in the table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <p>Step 1: When a product is created, it is registered in this Create<br>Item form, which inly admin can view/operate.<div>Step2 : After the details of the<br>product are given and the form is submitted, the shop.item method in shop.py<br>file comes into play.</div><div>Step 3: The logic of shop.item method is, it first<br>checks for the id, if there is none, then it goes into create<br>mode.</div><div>Step 4: The create mode of this method is simple, taking the data<br>from the form and then it is provided to a query which stores<br>the details of the product in a particular order.</div><div>Step 5: The DB query<br>is a simple INSERT query which inserts the data from the form into<br>IS601_S_Products table.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Dudeverse/IS601-005/pull/36">https://github.com/Dudeverse/IS601-005/pull/36</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-se352-prod3.herokuapp.com/admin/item">https://is601-se352-prod3.herokuapp.com/admin/item</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208311613-7db23857-fb8f-417e-b348-7df16f6ac4bf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ADMIN VIEW : screenshot of the Shop page showing 10 items without filters/sorting<br>applied. It is displaying 10 sample items.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208312020-e5c7e5a6-1139-4c03-b42b-668da304a3b9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>USER(CUSTOMER) VIEW : screenshot of the Shop page showing 10 items without filters/sorting<br>applied. It is displaying 10 sample items.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208311737-80af2c50-d3cd-4bc4-abf2-ddc558fbe0a5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The filter is &quot;e&quot;. So it fetches the products that contain the letter<br>e. And the sorting is set to &quot;category&quot;, in ascending order (&quot;up&quot;). The<br>page displays the results shown above.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208275503-0852bd28-b386-4b6e-9e14-5d4d54646bfb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot of entire shop.shop route in shop.py and it contains the logic<br>for sort/filter in the if conditions below the data retrieval.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <p>Step 1 : Basically the entire Shop page is just one method, namely<br>shop.shop method in shop.py file.<br>Step 2: For this implementation, on the front- end,<br>I have used the Jinja template code provided in the BusinessManagement MiniProject, where<br>there&#39;s a sort/filter applied.<br>Step 3: For the back-end, I have implemented the query<br>that dynamically changes itself based on the filter applied, just like Business Management<br>Miniproject.&nbsp;<div>Step 4: The query is just a simple query in the beginning, retrieving<br>required values and in the end has WHERE 1=1. This can be used<br>to concatenate query filters, as these are additive.</div><div>Step 5: I implemented the sort/filter<br>for category and price and they can be sorted in ascending or descending<br>order.<br>Step 6: For the search fitler, it does partial matches because of LIKE<br>%s% in the query.&nbsp;<br><div><br></div></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Dudeverse/IS601-005/pull/36">https://github.com/Dudeverse/IS601-005/pull/36</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-se352-prod3.herokuapp.com/shop">https://is601-se352-prod3.herokuapp.com/shop</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208311859-10383da2-ad70-4aee-98c1-89ddcee81aae.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows non-visible products too. This is from an admin page (admin in<br>the url) not the shop page.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <p>Step 1: For this Product List page I have just changed the shop.items(plural)<br>method to accommodate the visibility status.<div>Step 2: The Product list is only visible<br>to the users that have admin role.</div><div>Step 3: The db query logic is<br>simple, we just select all the items from the products table and display<br>them here.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Dudeverse/IS601-005/pull/36">https://github.com/Dudeverse/IS601-005/pull/36</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-se352-prod3.herokuapp.com/admin/items">https://is601-se352-prod3.herokuapp.com/admin/items</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208312090-f792eae1-ad29-4dc5-916e-3108ef4e72f4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit button is visible on every product card under the view button. This<br>is from the public shop page.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208312192-d672d350-b639-4485-96ff-b262e5b5941a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This edit button is in the bottom of product details page. The selected<br>product name is Eggs.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208311859-10383da2-ad70-4aee-98c1-89ddcee81aae.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The edit button is visible on every row in the table at the<br>rightmost corner. This is from admin product list page(not the shop page)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208312380-388d9727-d6fd-4ab3-bf40-bd28341ac078.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>I searched for chicken in the shop page. Notice the search filter. The<br>record says Stock: 4 and price is 8 USD. I am going to<br>change this to Stock 9 and Price : 7 USD. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208312526-a19bb6f4-0c13-478f-8ad3-5081663ff452.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>On the edit item page, editing the stock and price values.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208312560-6d442e4b-90c1-4b20-bf96-d12846077ae5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After editing the item, again I searched for the item &quot;chicken&quot; and the<br>record is now edited.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>Step 1: The Edit button was initially given in the Product List page.<br>The job is to make new buttons in Shop page and Product Details<br>Page and redirect those buttons to Edit Item page.<br>Step 2: The Edit button<br>in the Product List page is from a template. So I tried to<br>implement the same in the Shop page, in shop.html where there is +Add<br>button. I have added the Edit Button under the Add Button.&nbsp;<br>Step 3: Coming<br>to the backend part, all I had to do was to reroute this<br>newly created button to Edit Item page. This was possible by using url_for<br>and also to pre-fill the data, I have used the row[&quot;id&quot;] to specify<br>the id of the item we are about to edit.<div>Step 4:&nbsp; This step<br>was taken to ensure that the values will be prefilled when the admin<br>wants to edit. Also on the side note, this Edit button is only<br>visible to users that have admin role.</div><div>Step 5: The next Edit button was<br>supposed to be in Product Details page. For this I have tried to<br>redirect it to Edit item button, but I had trouble figuring out how<br>to pre-fill the data.</div><div>Step 6: I have succeeded in taking the admin to<br>Edit Item page but failed to pre-fill the values in the fields.<br>Step 7:<br>Possible roadblock for this sub-feature is because of lack of understanding of Jinja<br>templates. Sometime these templates are easy to figure out and can be exploited,<br>but sometimes it&#39;s hard, this was one of those times.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Dudeverse/IS601-005/pull/37">https://github.com/Dudeverse/IS601-005/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-se352-prod3.herokuapp.com/admin/item?id=4">https://is601-se352-prod3.herokuapp.com/admin/item?id=4</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208312751-3d389b17-1d97-4f83-8508-c9877571380f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the button (clickable item) that directs the user to the Product<br>Details Page. Notice that every card has a view button on it.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208312804-b46eb221-d05b-43a2-9dcf-26f0e6a20a2c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>When I click the first result in the shop page, the above page<br>is displayed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>Step 1: This implementation was quite simple. I have created a new route<br>in shop.py which takes users/admins to a new page called Product Details. This<br>method is named item_details.<br>Step 2: This method is similar to edit method where<br>the values are prefilled. I have utilized the pre-filling part to create this<br>method.<br>Step 3: This method retrieves data from the database (via a simple select<br>query) and fills the values in the fields.<div>Step 4: The user may try<br>to change the values but it doesn&#39;t change anything. There is no submit<br>button.</div><div>Step 5: For this, I have created a separate html file called prod_details.HTML<br>which is same as Create/ Edit item, but with added permissions. Only Admin<br>can see the visibility option and the Edit button.</div><div>Step 6: It is also<br>implemented on the cart page, and user can see more details of the<br>product by clicking the view button.&nbsp;</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Dudeverse/IS601-005/pull/37">https://github.com/Dudeverse/IS601-005/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-se352-prod3.herokuapp.com/item_details?id=4">https://is601-se352-prod3.herokuapp.com/item_details?id=4</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208313052-179a44df-02ee-4f2d-b022-53036852e5c1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the success message of adding to cart. Added 5 number of<br>Eggs product.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208313141-4ffc5a80-f3b6-4a41-ad42-38dc1124200c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the error message of adding to cart (i.e., when not logged<br>in)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208313242-97be01e1-77da-49e0-9b66-a4a8c497457d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Cart table with data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p>I have decided to go with 1 cart per user method. This seemed<br>simple to implement and it felt minimalistic.<br><br>Every user has a cart, and it<br>is basically identified by the user_id. This cart can be used to add<br>products, remove products, update the quantity of the products you want and can<br>also be emptied when you decide not to use it anymore.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <p>Step 1: User first visits the shop page and then clicks on add<br>button. This takes the user to cart page.<div>Step 2: I have implemented a<br>&quot;My Cart&quot; button in the navigation bar so the user can see the<br>stuff in their cart at any time during shopping and not only when<br>they add stuff to it.<br>Step 3: When the user press add button in<br>the shop page, The front-end checks for the quantity and sends the data<br>to shop.cart method.</div><div>Step 4: Based on the quantity selected by the user the<br>cart gets updated.</div><div>Step 5: When quantity is greater than 0, it checks for<br>id, if there is one then its update via cart and if there<br>is non then it is from shop page.&nbsp;</div><div>Step 6: SQL side: If there&#39;s<br>no id, it takes the item and stores it, based on the quantity<br>selected by the user.If there is a duplicate key then it simply increases<br>the quantity that the user selected. Here INSERT query is used</div><div>Step 7: SQL<br>side: Else it is taken as an update from the cart and is<br>updated in the Cart Table accordingly. A simple UPDATE query is used here<br>to update quantity.</div><div>Step 8: Since the items can be added to cart from<br>two ways, from cart page and shop page, both cases are handled accordingly<br>and the updates are stored in the Cart table.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Dudeverse/IS601-005/pull/38">https://github.com/Dudeverse/IS601-005/pull/38</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208313353-958628f4-f80d-4add-b52e-5f76b7716d9b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Cart View. The cart total adds up properly. Each row<br>has its own view button to view product details. It has few different<br>products as examples.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <p>Step 1: The cart is another table that gets updated when a user<br>decides to select an item for purchase.<br>Step 2: When an item is added<br>a row gets added into the cart table, which includes the product quantity<br>and product price(subtotal). Product&#39;s unit_price times quantity is the subtotal of the row.<div>Step<br>3: When the item&#39;s quantity is updated the&nbsp; subtotal changes based on the<br>increase or decrease in quantity.</div><div>Step 4: Th subtotals of each row are then<br>added and is displayed on the last row. This is implemented on the<br>front-end itself using namespace feature in Jinja. Since the scope is not like<br>python, we can update or manipulate variables in Jinja because the scope is<br>different.</div><div>Step 5: The total value is simply the sum of the subtotal value,<br>it increases as the user adds items or updates the items to a<br>higher number in quantity.</div><div>Step 6: The total is then displayed in the bottom<br>row on the right.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Dudeverse/IS601-005/pull/38">https://github.com/Dudeverse/IS601-005/pull/38</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-se352-prod3.herokuapp.com/cart">https://is601-se352-prod3.herokuapp.com/cart</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208313353-958628f4-f80d-4add-b52e-5f76b7716d9b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot before any updates. Now let&#39;s update number of blenders to 3.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208313557-7f1b90bc-ebac-4999-aa74-a6871cc627fa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot after updating number of blenders to 3. Notice that the price has<br>increased.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208313641-b06a39b0-9b2a-4fc2-beca-00493d2eeddb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before setting quantity of item say, Australian lamb chop, to 0<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208313759-5c7c309f-a83d-4cdd-8088-618f5b245780.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot Australian lamb chop&#39;s quantity set to 0.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208313789-5b5b34d8-6a6e-404b-8b51-2fdd2a1ab735.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot after setting the quantity of Australian lamb chop to 0.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208313863-c92a7191-4577-424f-a4a5-62910365d795.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>In the screenshot the Milk 1L quantity is set to -1. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208313916-0c94be3b-6616-4308-80b0-fbdf5961afe1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Upon clicking update, it gets deleted.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <p>Step 1: When the quantity of an item is set to 0 or<br>any negative value, in the cart page, then that item gets deleted from<br>the cart.&nbsp;<div>Step 2: This is because we only have items in the cart<br>when quantity is greater than zero.<br>Step 3: If the quantity goes below zero<br>or becomes zero, the shop.cart method then uses the conditional else branch and<br>goes onto delete the record.<br>Step 4: When the quantity becomes less than zero<br>or equals to zero, the id and user_id is then used to delete<br>that particular item from the user&#39;s cart. This is the logic on the<br>SQL side.&nbsp;<br><div><br></div></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Dudeverse/IS601-005/pull/38">https://github.com/Dudeverse/IS601-005/pull/38</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208314021-95df1078-acfd-4a3c-bf1d-6077382ec3ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting poland springs water. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208314040-d80676cb-e138-41e7-9ff4-d6594f76cf54.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deleting poland spring water. The item is deleted from the cart.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208314091-3ef9c20a-8937-40ca-86bb-e63f96d6f6e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before clearing the cart.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/208314105-fe2db84c-7012-4018-b0d5-97f37e152491.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After clicking the Empty Cart button at at the bottom of your cart,<br>the cart items get deleted and the message &quot;Emptied your cart&quot; displays.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <div>Step 1: If the quantity goes below zero or becomes zero, the shop.cart<br>method then uses the conditional else branch and goes onto delete the record.<br></div><div>Step<br>2: The product's quantity can be set to 0 to delete the record.<br>Or it can be set to any negative value.<br>Step 3: Another way to<br>delete an item is to press the X button on the item's row<br>in the cart.</div>Step 3: When the quantity becomes less than zero or equals<br>to zero, the id and user_id is then used to delete that particular<br>item from the user's cart.&nbsp;<div>Step 4: This is the logic on the SQL<br>side.&nbsp; However this is only for deleting a single item.&nbsp;<br><br>For deleting the entire<br>cart, I had to take an alternate approach.<br>Step 1: For this I have<br>created an Empty cart button in the bottom row of the cart.<br>Step 2:<br>When the user clicks on this button, the shop.cart_empty method in shop.py gets<br>called. This a new method I wrote.<br>Step 3: What this method does is<br>delete the cart items based on the user id only. Because for emptying<br>the cart we need only user id, and product id's are unnecessary.<br>Step 4:<br>Using this user_id we can delete the records of the cart table that<br>belong to the user.<br>Step 5: This method ensures no user can delete items<br>or empty other users' cart.<br>Step 6: This method, after deleting the cart items<br>of the user, redirects them to the cart page, with a message saying<br>Cart is emptied.<br><br><br></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Dudeverse/IS601-005/pull/38">https://github.com/Dudeverse/IS601-005/pull/38</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>I&#39;ll classify my learnings as revisited and new approaches.<br><br>New learnings:<br>1. I have learnt<br>how to write new methods to add new functionality to pages and different<br>actions.<br>2. I have learnt to manipulate and exploit templates to fit into my<br>approach on page display.<br>3. I have learnt about helper files to make new<br>html forms.<br>4. I have understood how to apply css to an element of<br>my choice.<br>5. Learnt how to understand the features in project proposal.<br>6. I have<br>learnt to use different PRs for working on different features. This prevents hassles<br>during debugging.<br><br>Revisited learnings:<br>1) For the many of the above deliverables, I have just<br>updated the table that has been provided and changed the queries to accommodate<br>the new methods.<br>2) For the sort/filter deliverable I had reused the code provided<br>in BusinessManagement MiniProject and changed it support the features in this project.<br>3) For<br>Edit deliverable, I have reused the Edit button code in the project multiple<br>times to the same effect (this attempt failed in product details page but<br>succeeded in Shop page)<br>4) Understood the importance of roles while using some features.<br>Just like in the previous milestone, some functionality is restricted to admin only.<br>5)Code<br>can be reused many times and we just have to know where this<br>reusability can work. The DRY principle.<br><br>Issues:<br>1. I tried to place an edit button<br>in the Product Details page but I wasn&#39;t able to. Have to understand<br>Jinja templates better. However I tried to put the edit button there(though it<br>doesn&#39;t work). This edit button is only visible for admins.<br><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-se352-prod3.herokuapp.com/login">https://is601-se352-prod3.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone-2-shop-project/grade/se352" target="_blank">Grading</a></td></tr></table>