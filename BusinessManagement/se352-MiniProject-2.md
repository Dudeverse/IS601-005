<table><tr><td> <em>Assignment: </em> IS601 Mini Project 2  Business Management</td></tr>
<tr><td> <em>Student: </em> Surya Teja Ethalapaka (se352)</td></tr>
<tr><td> <em>Generated: </em> 12/5/2022 7:15:40 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-2-business-management/grade/se352" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>checkout dev and pull any latest changes</li><li>Create a branch called MiniProject-2</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li>Immediate add/commit/push to github</li><li>Open a pull request and keep it open until you're done adding the submission file</li><li>&nbsp;(optional) updated the deploy dev yml file and add MiniProject-2 so you can deploy to dev without needing to merge into dev</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item)<br></li><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 5</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together</li><li>Ensure all screenshots are properly captioned in the deliverable section</li></ol><li>You may save your progress when filling out this submission as often as you want</li><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from dev to prod and merge it</li><li>Navigate to the submission file under the BusinessManagement folder</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F22-MiniProject-2">https://github.com/MattToegel/IS601/tree/F22-MiniProject-2</a></div><div>May want to download branch as a zip, then copy/paste the files into your repo</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205585519-6b9e4cdb-012c-41a8-ae87-7bea678cf89c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DIAR-mt85 is visible. URL is visible and is from heroku dev. Brought to<br>you by...&quot; message  is updated to have my first name, ucid and<br>section.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/204824667-9b4baff8-182f-4f52-87e8-b1341f900c22.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>IS601_MP2_Companies table is visible. UCID / DB name is also visible.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/204824612-3c3421a7-fbfd-456d-adbe-3fcc0595f5f2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>IS601_MP2_Employees table is visible. UCID / DB name is also visible.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205371195-7fa8b5b4-f224-42de-9238-83d57b678108.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code checks if the file is a .csv file otherwise it will reject<br>with a flash message.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205371604-a960c5a2-9233-4e22-9f99-15ee7cc21159.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>CSV file is read from the provided stream as a dictionary and the<br>Extracted employee data is appended as a dictionary to the employee list .<br>Extracted company data should be appended as a dictionary to the company list.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205377332-22778c66-ddba-4d79-a584-582038e3a81a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After each query a flash message is generated noting how many records were<br>processed. If a particular list was empty a flash message  notes that<br>the particular list wasn&#39;t loaded or was empty.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205366667-71e04c95-6b4a-4aee-a1a0-838be21618d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing the proper success message and the proper count messages<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205363276-677e189a-f28d-435f-8f10-61af712f8d0a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows the error message when the file is not a .csv file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205369438-8d1648d8-3502-4758-a95b-26ae08b10814.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the error message when the form was submitted without a file attached.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205369223-0aa84c51-690f-46c1-b80d-e51cc56f9760.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing some employee data was uploaded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205369126-51342b4b-1d6c-47c5-98c6-6740be97c1d4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing some company data was uploaded<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205590383-07fd58bb-1279-46ec-baf0-560b3d288c93.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code retrieves first_name, last_name, company (id), email. Code flashes proper error messages <br>and user-friendly message when raised. Proper Insert query is visible. <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205592778-1d922346-0d14-491b-ad7c-ed760e934b9a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing filled in valid data prior to submission.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205592958-b574c20a-6f17-48da-aa93-252ed4bdeb1a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205608138-7d9f80b6-35ad-44d5-8683-93b068483626.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows first_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205608336-77cd2936-d275-48da-9186-ea492683f1cb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows last_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205608497-bd326b71-b32b-4a13-b5d6-37ee10e05e1e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show email error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205593371-cc39d9ca-08ee-470a-88aa-5d5d98299683.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Latest entry is in DB, in the last row. that is the added<br>employee record.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205594502-94a5606d-898e-473d-aa60-fffdc560f803.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>SELECT query should be filled in properly to pull employ id, first_name, last_name,<br>email, company_id, company_name via a LEFT JOIN and also checks request args for<br>fn, ln, email, company, column, order, limit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205594671-24e8e65b-fd8a-4786-849f-f50ded7dedc3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>appended filters for first name, last name , email company id and sort<br>and filter column too. appended limit filter too. Provides a proper error message<br>if number is out of bounds. Except bloacks also displays message. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205594795-eebec6a8-e7ea-45e9-a6bf-e49973eb792d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code snippet executes our dynamically created sql query.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205598028-51e2527f-a2a6-4386-bcf8-b0602079c75a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with first name filter. searching for names containing &quot;p&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205598284-95dfa670-4f76-40c6-b388-8f23c148acd6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with last name filter. searching for names containing &quot;B&quot; <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205598451-e5026f1b-296b-4bbb-8b43-d818c0ea4da0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with email filter. searching for email ids containing the word &quot;mail&quot; AND<br>ALSO last name containing letter &quot;B&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205599049-a8b39fc6-c4c4-4b08-8ca7-394922d811ee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with company name Benton, John B Jr<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205597329-08602c08-6583-4ad6-b1e9-b3b2b73eb14d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Applied asc order filter based on the column company &quot;name&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205597472-36238f60-d3f7-4acc-a1e9-5f8f60eeb39e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Applied desc order filter based on the column company &quot;name&quot;<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205600366-4fd21e9c-4f5e-4df6-97ad-e6f841e0bf3a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code retrieves id (from request args) first_name, last_name, company (id), email from form.<br>Also flashes proper error messages wherever required.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205600387-29c228aa-4be1-4ba9-99fb-28e69734e92b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper UPDATE and SELECT Query is visible. Employee data is passed to the<br>render_template.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205601730-3fd1a357-553e-444f-a230-a60950438eff.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>James&#39;s record before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205601906-8a3d290f-582c-4efe-98a3-52c74a633113.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>James&#39;s edit employee page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205602111-f1ed02d6-d622-4da9-bdec-fc748736cdd9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>updating james&#39;s email id<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205602400-d52062d7-0984-4b2e-b5bf-fce8c6b15273.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>update success flash message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205602348-de9476f5-b659-4596-9d59-c203ab84eef3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>james&#39;s updated email id is now visible<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205602876-da3181d1-01fd-493d-94ea-236e5343a85e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>James&#39;s email id before updating<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205603120-1639fba6-bf24-45ac-9835-b87c7670b22b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>James&#39;s email id after updating<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205609545-42de90a7-6bd4-4288-a250-283ec5052359.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code retrieves form data for name, address, city, state, country, zip, website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205609866-b7a58fc8-d453-4aa4-b1fa-74be8b0995eb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing proper flash messages.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205610210-701ceb8c-ec23-4393-b839-833e63cd10c2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Implementing insert query and handling exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205610900-f68dab5d-8f4a-450a-8fdd-db65f52595c2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing data before submitting.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205610918-78ddf5c2-3da7-4cef-a470-e05b7e2b99ff.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205611304-c66cab3c-7325-4984-89a5-9caeec5e65f2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205611534-2728c2b8-8c72-4fd3-846a-bb1b10c05d96.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show address error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205611798-b13e22f7-3562-4c30-ba08-4ebca3f94d1b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows city error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205612296-71de68bd-d735-4aa9-bb5d-dc09204a4490.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show state error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205613516-6bedeeb7-2496-443c-bd5a-716226f60d49.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot includes the valid company data shown previously<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205615104-132deeb9-139e-4a48-9c04-ce8fa02e407c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot the code that Appends filters and checks requests for args. The SELECT<br>QUERY is visible and fetches id, name, address, city, country, state, zip, website,<br>employee count for the company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205615561-73f6281f-8d0f-4630-8fd4-c33385bcf2db.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the snippet that appends limit filter and implements the above written<br>query dynamically based on filters applied.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205618170-dcb38136-6c95-4548-a954-1cee245079c1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing results with name filter applied when name contains &quot;FE&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205618698-dc4b54ef-8284-40c4-8058-b1d81d5fbff4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing results with country filter applied when country is United Kingdom (GB)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205618967-18fae4a1-a03f-4b37-8d73-f83ec34f99b5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing results with state filter applied when state is Andhra Pradesh in India<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205620562-be258150-c9a5-4974-9417-f2091a78481d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code retrieves id (from request args) name, address, city, state, country, zip, website<br>from form. All flash messages are properly defined. Proper UPDATE and SELECT Query<br>is visible. company data is passed to the render_template.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205621205-738e047b-498c-4b79-ab46-5496bdef7137.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>sherlock holmes company data before edit.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205621955-04059711-dbfa-40be-87cb-d97825e99d0d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>say, sherlock holmes company updated their company name.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205622277-832907a4-2aae-4c37-aa79-a7836ce45d59.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>page showing company data before editing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205618698-dc4b54ef-8284-40c4-8058-b1d81d5fbff4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>page showing company data after editing<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205624315-7b137cf6-8ef3-4ccd-8c08-a4532f3947b5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Previously the name of the company is used to be Private Investigator as<br>shown in the above picture.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205624301-1fe3e930-0052-4bcf-9a6f-4f4dba2a79d9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After editing the record, name changed to Investigative Agency. For more evidence, observe<br>the modified timestamp of sherlock record at the bottom of the table. <br><br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205625244-60bd8744-3381-4876-b1fa-1eeaf0a875a4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The Snippet above deletes the employee record based on it&#39;s id. After deleting<br>it redirects to employee search. All request args (minus id) are passed to<br>the redirect route. Success message flashes if record is deleted.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205625763-3bb0bb47-5a0c-4400-a060-fd1bbeb98b87.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting James Watson<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205626009-fbba377f-9d7a-4811-b811-89800a231f7e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deleting James Watson<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/205634743-2965dae1-dabf-4eb0-8276-535fcdac5db2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search tests were mostly failures and I was not able to prevent edit<br>employee failure. The rest of tests were successes.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p><font size="3"><b><i>Learnings:</i></b></font><div><ol><li><font size="3"><i style="font-weight: bold;">Flask packages:&nbsp; &nbsp;</i>I learnt about different packages in flask<br>that are helpful for implementing a navigation system for a website. the packages<br>url_for, redirect are very helpful to move around the webpages easily.&nbsp;</font></li><li><font size="3"><i style="font-weight:<br>bold;">Jinja Templating: </i>An interesting thing I learnt and like about this templating technique<br>is the flexibility of it and it&#39;s ease of use. Instead of writing<br>multiple values in a drop down menu we can just use Jinja templates<br>to loop over however many dropdown menu options we want. Not only dropdown<br>menus but can also be used to implement dropup, dropleft, dropright menus too.&nbsp;</font></li><li>&lt;font<br>size=&quot;3&quot;&gt;<i style="font-weight: bold;">url route methods(Blueprints): </i>I learnt how blueprints can help in keeping<br>the functionality of a website organised. In this MiniProject, Each task related to<br>an enitity in the database has been given a blue print and within<br>it, their functionality has been implemented. Each entity like employee, company have their<br>own methods which are further helpful in <b style="font-style: italic;">Creating a record(ex: add<br>employee), Search/reading records (ex:search_employee), updating a record (ex: add company), and finally deleting<br>a record . </b>Basically the entire functionality of these CRUD OPERATIONS have been<br>implmented in these blueprints.</font></li><li><font size="3"><b><i>Beautifulsoup testing:&nbsp;</i>&nbsp;</b>I learnt that beautifulsoup package can be used<br>to parse html and basically track the tags and ids of a html<br>page/file. With this it is advantageous to dissect html the way we want<br>to to implement test cases.</font></li><li><b style="font-style: italic;"><font size="3">Bootstrap</font></b><font size="3" style=""><i>&nbsp;</i><b style="font-style: italic;">basics like<br>flash messages:&nbsp;</b>I learnt how to write flash messages and give different types of<br>alerts to the user like &quot;warning&quot;(yellow color), &quot;danger &quot; (red color). success (green<br>color) etc.</font></li></ol><blockquote><font size="5"><b>Most Important Learning: Debugging.&nbsp;</b></font></blockquote><blockquote><b style=""><font size="3">The way this assignment and almost<br>all the other assignments that are designed have have put me in a<br>role of &quot;troubleshooter&quot;. Constantly using the console to print out what values exist<br>in what variables and how they changes between files and within the files<br>is what I learnt most.</font></b></blockquote><div><font size="3">Issues:</font></div></div><div><font size="3">&nbsp;1. I was not able to run<br>many of the test cases at the end of the project. some methods<br>worked fine and some methods have failed tests. I have deployed the website<br>onto heroku by temporarily bypassing the test cases. I have to work on<br>that. There was really very less time to implement all the methods but<br>I tried my best to minimize those failures.</font></div><div><font size="3"><br></font></div><div><font size="3">Main issues noteworthy of<br>this assignment:</font></div><div><font size="3">The continuous discussions on discord and constant updates about latest changes<br>in code kept me going with the flow. Sometimes the code worked with<br>older test cases and with new test cases it didn&#39;t. Nonetheless, it was<br>riveting till the end.</font></div><div><font size="3"><br></font></div><div><font size="3"><br></font></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-2-business-management/grade/se352" target="_blank">Grading</a></td></tr></table>