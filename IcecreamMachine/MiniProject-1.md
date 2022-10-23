<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - IceCream</td></tr>
<tr><td> <em>Student: </em> Surya Teja Ethalapaka (se352)</td></tr>
<tr><td> <em>Generated: </em> 10/23/2022 6:00:45 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-1-icecream/grade/se352" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216">https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder IcecreamMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/197411216-d4d4396d-46e4-4e01-b026-95eb1256a1f9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows the method of calculate cost, with my approach stated in<br>the comments. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/197412656-eed68a95-e785-4c3b-9ada-c00d8b7ad846.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The lines 294-295 show how the currency formatting was handled. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/197413938-6de10c85-7e39-4b22-8bd0-8a4e48727eb6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output showing that the currency format is handled and displays 2.00$ instead of<br>2.0. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/197414521-532475a4-a958-44aa-a19f-107334a0a329.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows how the input captured from the user is compared to<br>the actual cost in handle_pay() method<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <div><b><font size="4">Sub Task-2 answer:</font></b></div><div><br></div><div><b style="font-size: medium;">Implementing the calculation part:</b><br><ol><li>The inprogress_icecream array is continuously<br>appended with choices as the user gives their inputs. Each object in that<br>list is a class object.</li><li>Each of that class object has an instance attribute<br>called "cost".</li><li>I have assumed the inprogress_icecream to be a list called "x"(for the<br>sake of easiness).</li><li>I have a made a new empty list called "y".</li><li>By running<br>a for loop on x, I was able to grab cost of each<br>object in x and append it to y.</li><li>The summation of all costs in<br>y is the total cost of the ice cream.</li><li>The summation value is stored<br>in a new a variable "z" in float format.</li></ol></div><div><font size="3">Handling the currency formatting:</font></div><div><ol><li>The<br>value of z/expected is of float type.</li><li>Using {variable:.2f} can be used to format.</li><li>{expected:.2f}<br>is actually a string type. I stored this variable "currency"<br></li><li>I had to change<br>it to string format temporarily to make it look like "##.##" format.<br></li><li>The currency<br>variable stores the formatted float value as a string.&nbsp;</li><li>I used this variable to<br>display the correct format in the input message(line 295)</li><li>The output screenshot shows an<br>example run, with correct currency format.</li><li>In the handle_pay() method the variable total takes<br>in a string value from console. I changed it float in this method<br>to smoothly compare the values of same type.</li></ol></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/196834240-8e875d6c-54d6-48a1-b240-09b0378236b2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot-1 Caption: The OutOfStockException is raised in the use() method in class Usable.<br>Because this is where the calculation of number of remaining items happens.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/196835636-aa3db96c-4078-4b40-ab24-8ff88fcf276f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot -2 Caption: The OutOfStockException is handled in the run() method, for the<br>stage of Container selection.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/196836355-7b3f40d2-0410-407d-8afe-3cb036d1ea64.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot -3 Caption: The OutOfStockException is handled in the run() method, for the<br>stage of Flavor selection.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/196836488-270d9b1e-29c2-4d5b-bcbe-bfdb3991ea19.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot -4 Caption: The OutOfStockException is handled in the run() method, for the<br>stage of Toppings selection.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/196837909-5b7d1fe6-e729-48e0-8f2e-8459c9e943a0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot -5 : The NeedsCleaningException is raised in pick_flavor() method. See line number<br>89.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/197414870-3bc4c504-700f-4621-84a3-bd72f1080637.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot -6 :The NeedsCleaningException is handled in run() method, in the Flavor stage<br>section. It is handled by adding an input to its except block that<br>takes user input to decide whether the ice-cream machine should be cleaned or<br>not.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/196840215-cc5da8fa-7a25-4df0-98da-a95ab8fb8cb0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot -7 : InvalidChoiceException is raised in pick_container() method.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/196840604-829c1646-a661-49fa-a18c-6f7c69274f30.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot -8 : The exception is handled by prompting the user to enter<br>the available options.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/196841120-3d06228b-f88c-478d-be7b-9b5da628b787.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot -9 : Another InvalidChoiceException is raised in pick_flavor() method. See line number<br>99.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/196841539-ed6a3996-a3c8-4b2d-b585-8cc900fc79c7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot -10: This InvalidChoiceException is handled in run method during the flavor selection<br>stage.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/196841770-c249ad9a-8009-4d80-a5b1-278a021caea2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot -11: Another InvalidChoiceException is raised during the pick_toppings() method. See line number<br>110.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/197415451-dbda1927-fe9a-4e6b-a001-12eabe579284.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot -12: This InvalidChoiceException is handled in run method during the toppings selection<br>stage.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/196842612-1d898997-989a-417d-bee6-216f1131cceb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot -13 : An ExceededRemainingChoicesException is raised in pick_flavor() method. See line number<br>91.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/196842988-4cf7a8f9-4438-4c86-9981-52a6b566659c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot -14 : That ExceededRemainingChoicesException is handled in run() method during flavor selection<br>stage.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/196843463-700f5fa3-f0cc-4698-9976-72cbd01acfb5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot -15 : An ExceededRemainingChoicesException is raised in pick_toppings() method. See line number<br>103.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/196843570-954916fb-00be-4cfc-9d16-6d4694d9e6de.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot -16 : That ExceededRemainingChoicesException is handled in run() method during toppings selection<br>stage.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/197415651-b44ffa57-b4dc-4384-a858-a929ae21d7ff.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot -17: The InvalidPaymentException is raised when an invalid payment amount is entered<br>and handle_pay() raises it.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/197416115-d0b927bf-8203-4c0d-87c5-40984d84e632.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot -18: The InvalidPaymentException is handled in STAGE.Pay section, returning to the same<br>stage until correct payment is entered.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <div><font size="4"><b>How I handled each of the following exceptions:</b></font></div><div><br></div><div><i><b>OutOfStockException(Screenshots 1 to 4):</b></i> <br>When<br>these type of exceptions are raised, they are handled by prompting the user<br>to choose from available options. When no option is available(in case of container)<br>the program exits. In case of flavors and toppings being out of stock,<br>the user is prompted to quit because they are not allowed to choose<br>flavors or toppings without selecting the container first. The exception handles on a<br>case-by-case basis:<br><ol><li>One (or) more type of Container(s) is out of stock: The exception<br>prompts the user to select from remaining available containers. If no container is<br>available then the program exits like mentioned above.&nbsp;</li><li>One (or) more type of Flavor(s)<br>is out of stock: The exception prompts the user to select from remaining<br>available flavors.<br>If no flavor is left it takes user to toppings section.</li><li>One (or)<br>more type of Topping(s) is out of stock: The exception prompts user to<br>select from available toppings.If no topping is left it takes user to payment<br>section.</li></ol><i style="font-weight: bold;">NeedsCleaningException(Screenshots 5 and 6):</i><br>This exception is raised when the Ice cream<br>Machine needs cleaning, meaning when remaining uses has reached 0. This is handled<br>by prompting the user to input yes or no to clean the machine.<br>Cleaning machine resets the number of remaining uses. If the user enter "yes"<br>the machine gets cleaned. If they enter "no" the program prompts until the<br>user enter "yes".</div><div><br></div><div><b><i>InvalidChoiceException(Screenshots 7-12):<br></i></b>When these type of exceptions are raised, the are handled<br>by prompting user to enter a valid option from the choices they are<br>given during that stage. Not as a new input but the program redirects<br>the user to the same stage again so they can enter a valid<br>choice. This is raised when the user enters a choice that is not<br>in the given list of options or enter some garbage value.<br>This is raised<br>on case-by-case basis too.<br><br><ol><li>When user enters invalid container: program prompts user to enter<br>valid container choice; keeps prompting until a valid container choice is selected.</li><li>When user<br>enters invalid Flavor: program prompts user to enter valid&nbsp; flavor choice; keeps prompting<br>until a valid flavor choice is selected.</li><li>When user enters invalid Toppings: program prompts<br>user to enter valid toppings choice; keeps prompting until a valid toppings choice<br>is selected.</li></ol><br><i style="font-weight: bold;">ExceededRemainingChoicesException(Screenshots 13-16):&nbsp;<br></i>This exception is raised on case-by-case basis. Depending on<br>the exceeding choices in the flavor stage or toppings stage. When the remaining<br>scoops or remaining toppings reaches 0, this exception is raised.<br><ol><li>When user selects more<br>than MAX_scoops: The program prompts the user that the flavor was not added<br>and that they have reached the max limit of scoops, Prompts them to<br>enter "next"</li><li>When user selects more than Max_Toppings: The program prompts the user that<br>the flavor was not added and that they have reached the max limit<br>of toppings, Prompts them to enter&nbsp;"done"</li></ol><b><i>InvalidPaymentExcept(Screenshots 17 and&nbsp; 18):<br></i></b>This exception is raised when<br>user enters an invalid amount of payment. This exception redirects them back to<br>payment stage and asks them to try again until the correct payment amount<br>is entered.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/ff0000/000000?text=Incomplete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <p>(missing)</p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Dudeverse/IS601-005/pull/5">https://github.com/Dudeverse/IS601-005/pull/5</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p><font size="4">Issues:</font><br><ol><li><font size="3">Deliverable - 1:<br>While calculating the cost, had to understand what type<br>of objects are stored in self.inprogress_icecream array. simple debugging clarified it. While handling<br>the currency format, the formatting technique {float variable:.2f} returned a string. I thought<br>it would give a float value but no. Had to utilize this only<br>while displaying the input but not during the calculation. That helped.</font></li><li><font size="3">Deliverable -<br>2: Didn&#39;t know how to handle exceptions until I took this course. While<br>handling the NeedsCleaningException I had written the program to exit when the user<br>entered &quot;no&quot;. Fixed it with a small while loop.</font></li><li><font size="3">Deliverable - 3: Understood<br>that I have to do Integration Testing but I didn&#39;t know how to<br>use fixtures and parametrization and assert statements. I know how they act and<br>behave but I didn&#39;t know the correct syntax to implement the test cases.&nbsp;</font></li></ol>&lt;font<br>size=&quot;4&quot;&gt;Difficulties:</font><br><ol><li><font size="3">Deliverable - 1: No difficulties. Pretty smooth. Needed to understand how inheritance<br>works within a script.</font></li><li><font size="3">Deliverable - 2: No difficulties. Got a good grasp<br>on using try-except blocks to handle raised exceptions.</font></li><li><font size="3">Deliverable - 3: Understood the<br>philosophy of pytest, or in general testing of the code. Found it difficult<br>to access other module&#39;s classes and using them to create fixtures and marks<br>and parametrization. I was in the wrong mindset, meaning that I was still<br>in programming/handling-error mindset. Have to work on this and come back and must<br>re-visit this mini-project.</font></li></ol><font size="4">Learnings:</font><br><ol><li><font size="3">Deliverable - 1: Learnt how derived classes and inheritance<br>works. Learnt to handle formatting strings.</font></li><li><font size="3">Deliverable - 2: Learnt how to raise<br>exceptions and how to use try-except. Learnt how to keep the program flowing.</font></li><li>&lt;font<br>size=&quot;3&quot;&gt;Deliverable - 3:&nbsp;Understood the core concept and reason behind testing applications; to understand<br>how the code/app behaves if it is in the hands of a user/layman<br>instead of a dev. It feels like this testing of code is useful<br>in the business side of things, say when a new app is launched<br>and it must be tested several number of times before they can beta-test<br>it with real users. Learnt that there is something called &quot;Inversion of control&quot;<br>when we test programs, and I failed to have that mindset. Nonetheless, I<br>personally feel testing is really really REALLY handy. Looking at the big picture,<br>I am starting to see how this relates to Web systems development. Easy,<br>(Integration) testing can be used when our program/app requires a database and needs<br>to run on those database values. Also useful when working on flask applications,<br>or any other framework for that matter. Learnt that testing is basically running<br>a simulation of our program on test cases, against some test data to<br>observe the behavior of the program.<br>Have to work on this and come back<br>and must re-visit this mini-project.<br></font></li></ol><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/197418639-50502949-2e0a-40cd-8dd2-42f60eada749.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>A normal execution of the program without raising any exceptions.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/197418743-dcf5f8eb-c354-4925-9370-0d117210fcd4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>A case where ExceededRemainingChoicesException and InvalidPaymentException are raised and handled with continued program<br>flow<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/107896500/197418862-e6eff282-7682-47ba-b285-cf8cc231ff99.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>A case where InvalidchoiceException is raised and handled with continued program flow.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-1-icecream/grade/se352" target="_blank">Grading</a></td></tr></table>