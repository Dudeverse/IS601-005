<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Surya Teja Ethalapaka (se352)</td></tr>
<tr><td> <em>Generated: </em> 12/12/2022 7:01:08 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone1-deliverable/grade/se352" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206937466-f7e33e57-784a-4722-b77a-83e9ad032488.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing invalid email validation <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206937875-dd5708ea-508a-4202-a179-efe6fad74343.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing invlaid password validation insufficent length<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206937986-5a41953e-9575-4e03-a8e6-4e42dcce2817.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing passwords not match validation. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206938103-522db6ec-581b-4f32-a155-3757bbb911f2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the email not available validation.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206938178-d3ab89d1-4b93-4bac-b786-6196eab31400.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing showing username not available validation.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206938302-69f2aed5-6f97-483c-8538-a73aa999cbb4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing filled in valid data before submission.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206938417-15eb229a-0f31-4ee2-b5dc-04035edb6038.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing that the user &quot;testing1&quot; is registered. Their details are in the<br>last record of the database above.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Dudeverse/IS601-005/pull/28">https://github.com/Dudeverse/IS601-005/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;">Basically, the register route in auth.py gets its data from form.data,<br>i.e., the data that is provided by the user in the form in<br>the register form. the form gets email, username, and password in this way.&nbsp;<br>Next the the entered field values, username and email and password are validated<br>by other files in the auth folder, i.e., the forms.py file.&nbsp; The forms.py<br>file has validators packages imported and it verifies the field values like username,<br>email and password entered. this is the backed validation logic. In the frontend<br>the corresponding html files take care of the validation part. It will check<br>for the errors in the front end and display the appropriate message, for<br>example the minimum number of characters required for creating a new password. The<br>password is handled by another backend file called forms.py and auth.py. The auth.py<br>checks for logical errors in the password validation and&nbsp; human errors in the<br>password validation are handled by form.py validators package imported from wtforms. Finally the<br>DB utilized in this way, the registered user&#39;s info is entered into DB<br>by this query in the auth.py form&nbsp;</span><span style="font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace;<br>font-size: 12px; white-space: pre; color: rgb(206, 145, 120);">&quot;INSERT INTO IS601_Users (email, username, password)<br>VALUES (</span><span style="font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size: 12px; white-space: pre; color:<br>rgb(86, 156, 214);">%s</span><span style="font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size: 12px; white-space: pre;<br>color: rgb(206, 145, 120);">, </span><span style="font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size: 12px;<br>white-space: pre; color: rgb(86, 156, 214);">%s</span><span style="font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size:<br>12px; white-space: pre; color: rgb(206, 145, 120);">, </span><span style="font-family: Menlo, Monaco, &quot;Courier New&quot;,<br>monospace; font-size: 12px; white-space: pre; color: rgb(86, 156, 214);">%s</span><span style="font-family: Menlo, Monaco, &quot;Courier<br>New&quot;, monospace; font-size: 12px; white-space: pre; color: rgb(206, 145, 120);">)&quot;</span><span style="background-color: rgb(30, 30,<br>30); color: rgb(212, 212, 212); font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size: 12px;<br>white-space: pre;">, </span><span style="font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size: 12px; white-space: pre;<br>color: rgb(156, 220, 254);">email</span><span style="background-color: rgb(30, 30, 30); color: rgb(212, 212, 212); font-family:<br>Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size: 12px; white-space: pre;">, </span><span style="font-family: Menlo, Monaco,<br>&quot;Courier New&quot;, monospace; font-size: 12px; white-space: pre; color: rgb(156, 220, 254);">username</span><span style="background-color: rgb(30,<br>30, 30); color: rgb(212, 212, 212); font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size:<br>12px; white-space: pre;">, </span><span style="font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size: 12px; white-space:<br>pre; color: rgb(156, 220, 254);">hash</span><span style="background-color: rgb(30, 30, 30); color: rgb(212, 212, 212);<br>font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size: 12px; white-space: pre;">)</span><span style="font-size: 13px;">.This query<br>actually inserts the form data into the users table. It inserts the email<br>id, username and password into the table.&nbsp; This is how the DB table<br>is utilized.&nbsp;</span><br><div><span style="font-size: 13px;"><br></span><div><span style="font-size: 13px;">&nbsp;<br></span><div><br></div></div><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;"><br></span></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206938724-79cf88ef-4236-4a7d-8253-fff650ae2a32.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing password mismtach. Displays a flash message saying invalid passowrd<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206938860-0b317f90-151a-4a1b-a325-688835b351e4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing validation based on non-existing user. Shows &quot;invalid user&quot; flash message.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206938949-e44589e6-9af7-42a3-9dd0-7d74420f4b2e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of successful login page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Dudeverse/IS601-005/pull/28">https://github.com/Dudeverse/IS601-005/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;">The form data is handled by the GET request that gets<br>the email and password form the user. The validation happens in this way:<br>If the user enters their username and password the login page takes them<br>to landing page. There&#39;s also another way, if the user enters their email<br>and password, then also the site takes them to the landing page. if<br>the user just registered with his email id and password, the site takes<br>his username as the value that is before the @ in their email<br>id and accepts their login info. this is code logic in the backend.<br>The DB is utilized in this way:&nbsp; The username and email are searched<br>in the Users table and selected from it.&nbsp; If login is successful the<br>user identity will change and hence they are taken to the landing page.The<br>DB is utilized only to check whether the user exists or not, and<br>if they do exist the which role they have and if they do<br>successfully login what role do they possess.</span><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206939693-eaaecf54-540f-4c5b-8818-0be8afcd2823.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showimg message about successfully being logged out<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206939938-863b5cf1-ecc5-42ef-a9e7-fd6797c20051.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of landing page when user is not logged in. It displays the<br>Unauthorized message and explains possible reasons for the URL being inaccessible.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Dudeverse/IS601-005/pull/28">https://github.com/Dudeverse/IS601-005/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>Basically session is like a global variable that keeps track of the user<br>that is being logged in. If the user logs in to the site<br>their status changes with many of the other flags associated to them. So<br>for log out logic basically their user identity is changed from known logged<br>in user to anonymous as soon as they logs out. It also removes<br>any keys set by the user when they logs in into his session.<br>Those keys are automatically removed when they&#39;re logged out.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206940780-6a3437cf-0607-494e-ac3c-6b6eced45577.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of landing page when user is not logged in. It displays the<br>Unauthorized message and explains possible reasons for the URL being inaccessible.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206940964-a9cdc4b1-d5bd-426f-a02b-fb7f85016031.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The 403 error page is being displayed in the screenshot. We have defined<br>this exception in main.py, in case the user accesses a role-protected page.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206941997-be098b9c-2046-45f2-9b7d-bb868f265290.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing available roles. This includes Admin role and Cookies role. <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206942436-bdfa47c5-5fb4-4333-839b-d7a7eaeb1458.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The record with user_id = 5 is my admin user. Their role_id is<br>-1 hence they are the admin.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Dudeverse/IS601-005/pull/29 ">https://github.com/Dudeverse/IS601-005/pull/29 </a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>When the user tries to access role-protected page, a custom made 404 error<br>pops up saying &quot;Page not found&quot;. This is loaded from 404.html file and<br>it is invoke from main.py. When a user logs in, their session class<br>object values are set and especially the is_authenticated value is set to true<br>and when they log out this value is set to false. When this<br>&quot;false&quot;-set user tries to access login protected page, the error page pops up.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>When the user tries to access role-protected page, a custom made 403 error<br>pops up saying &quot;Permission denied&quot;. This is loaded from 403.html file and it<br>is invoke from main.py. When a user logs in, their session class object<br>values are set and especially the is_authenticated value is set to true and<br>when they log out this value is set to false. When this &quot;false&quot;-set<br>user tries to access login protected page, the error page pops up.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206958094-f6d8d61f-d74c-4f79-b56d-3de5efae195f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data output is clean that is, table rows and table columns are neat.<br><br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206958068-0c65758b-5b8a-4dc1-b530-1cd68d5d6465.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Navigation and Forms are styled. It is my design choice temporarily. <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Dudeverse/IS601-005/pull/31">https://github.com/Dudeverse/IS601-005/pull/31</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>The basic styling for the site has been applied in the layout.html file<br>for all the forms. This is temporary design choice and it may vary<br>based on future decisions. The styling I chose for form labels is text<br>shadow and color. For the nav.html I have chosen different colors for the<br>nav bar and for the table rows and table columns in the Roles_list.html<br>for listing the roles. As I mentioned, this is temporary, and based on<br>the additions made in the future, the css and styling for majority of<br>the forms and nav bars may change. I have learnt how to manipulate<br>css for individual html elements and this wiil help me in styling each<br>and every element in the long run.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206938103-522db6ec-581b-4f32-a155-3757bbb911f2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the email not available validation.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206938178-d3ab89d1-4b93-4bac-b786-6196eab31400.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the username not available validation.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206948122-46f9dac0-dbc3-4fd6-a3c8-99859f5c891a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing user-friendly error message for invalid username format.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Dudeverse/IS601-005/pull/30">https://github.com/Dudeverse/IS601-005/pull/30</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>For making the technical errors more user friendly, the suggested method was to<br>define new functions to handle error messages, The handled error messages are used<br>in a very well-defined manner ,based on the error&#39;s raised. The check duplicate<br>error method, for example uses, regex to find out any duplicate values in<br>the DB and then inform the user about the existing username&nbsp; or email.<br>Defining new functions for unexpected users certainly makes our life easier when it<br>comes to handling error messages.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206944562-9ffded84-c826-40f4-ae0f-73491cde1e7e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows that the email and username are pre-filled properly<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Dudeverse/IS601-005/pull/31">https://github.com/Dudeverse/IS601-005/pull/31</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>The data is retrieved from database via a select query and is loaded<br>into a User class object. Then this class object&#39;s fields&#39; data is passed<br>into the form. This form data is displayed in the profile section via<br>profile.html. After the form data is loaded, the session is updated for the<br>updated email and username.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206944922-20d0213d-27df-47da-8457-e0d5df06b2ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot Showing email/username already in use message.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206945103-87ca227d-8290-49af-8881-9e588589dd1c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot Showing email validation message.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206945484-7b95a586-8ced-47b5-9fe1-108a9a499ec3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing username validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206946145-a79663ad-e6b4-45a9-9b03-16a9d8a91a33.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing password mismatch message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206946589-65b19c02-02fe-42c6-ba74-d522a38bdaf5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows invalid password message. It also shows saved profile because it&#39;s<br>triggered even if username and email are not changed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206946931-57e13896-1a71-4fc2-ac25-34079cf3e519.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing user &quot;test2&quot; and his username is &quot;test2&quot; before editing.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/206947332-50d39fed-a133-41eb-8f28-a7d8d9e7127e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the username is changed from &quot;test2&quot; to &quot;test2name&quot;. Also email is<br>changed from &quot;<a href="mailto:&#116;&#101;&#x73;&#116;&#x32;&#x40;&#x74;&#101;&#115;&#116;&#x2e;&#x63;&#111;&#x6d;">&#116;&#101;&#x73;&#116;&#x32;&#x40;&#x74;&#101;&#115;&#116;&#x2e;&#x63;&#111;&#x6d;</a>&quot; to &quot;<a href="mailto:&#116;&#101;&#x73;&#x74;&#50;&#110;&#x61;&#x6d;&#x65;&#64;&#116;&#101;&#115;&#x74;&#x2e;&#x63;&#111;&#109;">&#116;&#101;&#x73;&#x74;&#50;&#110;&#x61;&#x6d;&#x65;&#64;&#116;&#101;&#115;&#x74;&#x2e;&#x63;&#111;&#109;</a>&quot; <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Dudeverse/IS601-005/pull/31">https://github.com/Dudeverse/IS601-005/pull/31</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p>After the user updates their info, the data is then updated in the<br>database based on the user_id. The username and email updating are quite simple<br>and they are also updated based on their user_id. password also is updated<br>in the same way, on the basis of user_id, get matching hash value<br>and update it. For validation part, the forms.py handles the password validation, email<br>validation, username validation, password mismatch aspects using wtforms.validators. The password change only happens<br>when the user enters their current password and types in the new password<br>twice.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <ol><li>Learnt how to implement a basic authentication module.</li><li>Learnt how to validate emails</li><li>Learnt how<br>to validate passwords</li><li>Learnt how to validate username</li><li>Learnt how to update css for tables<br>using bootstrap</li><li>Learnt how to utilize the utils.py to set flags to various roles<br>and statuses.</li><li>Learnt how to Match passwords&nbsp;</li><li>Learnt how to Handle error messages in a<br>user-friendly way so that a fully-technical user has no idea where it went<br>wrong and and first time user knows what basically went wrong.</li><li>Learnt how to<br>implement a profile editing module</li><li>Learnt how to map users to their respective roles<br>as an admin.</li></ol><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-se352-prod3.herokuapp.com/login">https://is601-se352-prod3.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone1-deliverable/grade/se352" target="_blank">Grading</a></td></tr></table>