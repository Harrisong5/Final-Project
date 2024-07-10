Beet:
pic (1)

Beet is a forum website where users can post and comment, and join different communities to discuss topics with like-minded others. Posts can be combined through various feeds depending on what the user wants to see.

The live application can be viewed here :

https:// .herokuapp.com/

Purpose and Target Audience:

Problem Statement: Traditional forums offer little flexibility in what a user can view at once. Going to individual groups and finding specific threads is often at burden for the user.

Purpose: Beet aims to make posts easy to find and joining communities easy. It also aims to make it easy for a user to combine their interests in a clear feed of posts that are delivered straight to them with little effort.

Target Audience: The primary target audience are existing users of online forums, each with their own set of interests and topics, as well as non-forum users who are currently avoidant of them because it is not presented in a clean and user-friendly way.

Persona and User Stories:
The test user has used forums in the past, and prefers the system of commenting, however uses them much less and especially finds the user experience on mobile devices off-putting.

User Stories:
As a new user, I want to create an account so that I can participate in the forum.
As a registered user, I want to create a new post so that I can start a discussion.
As a registered user, I want to comment on posts so that I can participate in discussions.
As a registered user, I want to receive notifications when someone replies to my post so that I can stay engaged in the discussion.

Wireframe & Initial Design:

Home Page


Log in page


Register page

Create a post

Group page

Home (Mobile view)


Agile:
Using Agile principles, I created a projectboard and user stories. Taking into consideration a user's needs and tracking various criteria was a very valuable way to plan and structure my development time. This enabled me to be more efficient with my efforts and ensure progress was tracked and the deadline met.

project board

Design Choices:

Beet is inspired by beetroots, where digging up a post within a forum can feel like pulling out a fresh vegetable from the ground!

Logo
A simplistic Beetroot icon was chosen
https://cdn-icons-png.freepik.com/512/5668/5668408.png

Colour scheme:
Themed around Beetroots vibrant colours as well as earthy contrasting colours

#7B1F4D - Main theming colour of background

#AE5985 - Secondary colour mainly used for bulk text and buttons background

#AC3448 - Tertiary colour for less important text such as post dates

#A5C77D - Contrasting colour used to make usernames stand out

#2F3702 - Darker earthy colour for footer and borders

#FFF - white for headings and button text


Font

"Dosis"

A consistent font was chosen for the website that was clear to read whilst offering a softer, more nature-like look without hard edges.


Features:

Navbar & branding:
Sidebar:
Home/default feed:

The home page reflects the branding and theme instantly, using a navbar with clear items that a user can easily see where they can register, login and be able to create their own post. The sidebar provides better navigation of posts specifically, offering more personalised views when logged in. The default feed delivers posts automatically so the user can instantly see content without having to input upon entering the website.

"New Post" - allows user to see that they can create their own post and contribute immediately once they have registered. Redirects to login page if not signed in.

"Create an account" - ability to sign up by picking a username, password and providing an email address. Not visible if a user is logged in.

"Login" - existing users can login here, they are redirected to their dashboard and the navbar menu will change and display their username.


Side bar nav items will change what is content is fed to the main section 

Feed - posts are fed individually showing what community they are from, with username, title, content and comments. Results paginated by default in order to see footer more easily.

Dashboard

"Change password" - taken to a form where a user can change their password linked to their account 

Post list - lists posts by logged in user, split into published and ones awaiting approval.

Footer:
Minimal footer with other social media links and other details.

Future Features:

User profiles - access to a personalised bio and other user's pages with chosen information displayed such as post/comment history
Commenting - ability to chain comments onto on another in replies
Votes - implement a simple upvote system, which can influence what is prioritised to be displayed on certain pages, based on an algorithm 
Search function - a user can input text and search posts by content/title/author and sort by date or search for other users and profiles




Database Schema:

I used an Entity Relationship Diagram to plan out what models I would need for my database and what components and keys they should have. I used a flowchart to visualise each one's relationship to each other.

The initial draft was changed in another iteration in order to incorporate features more efficiently and reduce unnecessary coding.


Data Models:

User
username	VARCHAR 	[Primary key]
email		VARCHAR
password	VARCHAR
community	VARCHAR		[Foreign key]

Post
id		INT		[Primary key]
community	VARCHAR		[Foreign key]
title		VARCHAR		
content		TEXT	
img_link	VARCHAR
author		VARCHAR		[Foreign key]
date		DATETIME	
vote		VARCHAR		[Foreign key]	(Many-to-many)
status		BOOLEAN	

Community
title		VARCHAR		[Primary key]
user		VARCHAR 	[Foreign key]	
url		VARCHAR	
img_link	VARCHAR
description	TEXT	
date		DATETIME
post		INT		[Foreign key]

Comment
id		INT		[Primary key]
post		INT		[Foreign key]
username	VARCHAR 	[Foreign key]
body		TEXT	
date		DATETIME
vote		VARCHAR		[Foreign key]	(Many-to-many)	


*********
Validation
HTML
Page	W3C URL	Screenshot	Notes
Home	W3C	home page validate	Pass: button is a descendant of a tag
Books	W3C	Validate Books page	Pass: No Errors
Add a Book	W3C	validate adda book page	Pass: No Errors
Sign In	W3C	validate sign in	Pass: No Errors
Register	W3C	validate sign up	unclosed elements main and div
CSS
I have used the recommended CSS Jigsaw Validator to validate my CSS file.

File	Jigsaw URL	Screenshot	Notes
style.css	Jigsaw	validate css	Pass: No Errors
Python
I have used the recommended PEP8 CI Python Linter to validate all of my Python files.

File	CI URL	Screenshot	Notes
forms.py	PEP8 CI	![screenshot]forms py	
Pass: No Errors			
settings.py	PEP8 CI	![screenshot]settings py	
Pass: No Errors			
Book views.py	PEP8 CI	![screenshot]views py	
Pass: No Errors			
Book urls.py	PEP8 CI	![screenshot]urls py	
Pass: No Errors			
models.py	PEP8 CI	![screenshot]models py	
Pass: No Errors			
Responsiveness:
Development tools were used to test responsiveness on varying sized devices including laptop, mobile and tablet size.

Full testing was performed on the following devices:

Laptops:

Macbook Air 2018 13.3-inch screen
Lenovo Thinkpad 14" screen
Mobile Devices:

Google Pixel 4a

Browser Compatibility:

I have tested the site using the following browsers:

Google Chrome
chrome

Microsoft Edge
microsoft edge

I can confirm that the site is responsive and looks as expected good on different screen sizes.

Mobile devices:

Screenshot_20231207-234024

Screenshot_20231207-234033

Screenshot_20231207-234013

0

Screenshot_20231207-234117 (1)

Screenshot_20231208-000014

Tablet Devices:

homepage

signup tablet

sign in tablet

books tablet

tabletadd

bookdetails tablet
*********
Testing:
Lighthouse Audit:
I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

On a laptop:
Home

homeaudit

Books

auditbooks

Add a book audit add book

On a mobile device:

Home audit home mobile 

Books auditbooks

Add a book audit addbookmobile

Links
Link	Expected Outcome	Grade
Logo	Navigates to the home page when clicked	Fail
Home	Navigates to the home page when clicked	Pass
Books	Navigates to a book list page when clicked	Pass
Add a Book	Navigates to a form to add a book when clicked	Pass
Register	Navigates to a registration form when clicked	Pass
Log in	Navigates to a screen where users can log in when clicked	Pass
Logout	Navigates to a page confirming for the user to log out	Pass
Testing
Feature	Expected Outcome	Grade	Screenshots
Modal	A message will appear informing the user of a successful action	Pass	modal sign out 
User logged in	Text displays the user logged in with their username	Pass	modal sign in name
View books	Users can see available books which have been added	Pass	testing books
Add a book	Add a book to the book collection that will be available to borrow	Pass	addbook
Admin has access to crud functionality of all additions	Admin can edit or delete any book addition	Pass	admin testing
Edit a book	A user can edit the details on the book that they have addded. It will update their addition on the books page	Pass	edit book 
Delete a book	A user who added a book OR an admin can delete a book. It will then be deleted from the DB	Pass	delete book
Registration	New users can access a registration form from the "Register" link	Pass	testing sign up
Log in	Users can log in using a form after clicking "Log in"	Pass	sign in testing 
Log out	Users get logged out after clicking "Log out"	Pass	testing sign out
Grid display	A CSS grid will display the books in a clear, responsive format	Pass	N/A
Functional buttons	Edit, delete, create buttons will be functional throughout the site	Pass	edit delete buttons
Footer	A footer displays social information	Pass	footer
Social links work	The social links will navigate to a new page when they're clicked. They will open in a new tab	Pass	footer
Tools and Technologies Used:
The technologies implemented in this application included HTML5, CSS, Bootstrap, Python and Django.

Python used as the back-end programming language.

Git used for version control. (git add, git commit, git push)

GitHub used for secure online code storage.

GitHub Pages used for hosting the deployed front-end site.

Gitpod used as a cloud-based IDE for development.

Bootstrap used as the front-end CSS framework for modern responsiveness and pre-built components.

ElephantSQL used as the Postgres database.

Heroku used for hosting the deployed back-end site.

Cloudinary used for online static file storage.

Canva Utilized for collaborative design and prototyping(wireframes).

Google and Stack Overflow utilized for general research or solving a bug, information gathering, and various online tools.

Languages Used:
HTML5
CSS
Python
Deployment :
I used the steps used when deploying our django blog to deploy this application. The instructions for this mainly came from the follow along videos and text-steps provided on the code institute LMS.

Bugs
All the bugs that occured during the creation of this application have been resolved. There is a section of the application which allows you to reset your password that needs to be implemented, however they were not within the scope of this particular project and will be addressed in the near future along with the other future features.

Credit:
Although I used the django blog resources provided on the LMS, I also received alot of additional clarification by following along with django projects on YouTube. One of the vidoes I found especially helpful was : https://youtu.be/JzDBCZTgVyw?si=w3BBwJswUjBTm1xw

Stack Overflow was used to solve any smaller bugs and further clarification on errors I was receiving in the terminal.

I used this site to generate a persona and created user stories: https://founderpal.ai/user-persona-generator

A special thanks to all the other indivudals in our cohort for their continuous support throughout the course.

The added book covers and details were taken from the Waterstones Website.

Font Awesome was used for icons and the fonts used were derived from Google Fonts.

Wireframes, logo and flowcharts were created using Canva.