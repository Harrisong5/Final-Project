# Beet:

Beet is a forum website where users can post and comment, and join different communities to discuss topics with like-minded others. Posts can be combined through various feeds depending on what the user wants to see.

The live application can be viewed here:

https://beet-3a5123bf2df1.herokuapp.com/

This document will give insight into the creation process.

## Purpose and Target Audience:

### Problem Statement: 
Traditional forums offer little flexibility in what a user can view at once. Going to individual groups and finding specific threads is often at burden for the user.

### Purpose: 
Beet aims to make posts easy to find and joining communities easy. It also aims to make it easy for a user to combine their interests in a clear feed of posts that are delivered straight to them with little effort.

### Target Audience: 
The primary target audience are existing users of online forums, each with their own set of interests and topics, as well as non-forum users who are currently avoidant of them because it is not presented in a clean and user-friendly way.

### Persona and User Stories:
The test user has used forums in the past, and prefers the system of commenting, however uses them much less and especially finds the user experience on mobile devices off-putting.

#### User Stories:
- As a new user, I want to create an account so that I can participate in the forum.
- As a registered user, I want to create a new post so that I can start a discussion.
- As a registered user or site visitor, I want to be able to view posts by other users and clearly read them.
- As a registered user, I want to receive notification when I have altered details relating to my profile/posts.

## Wireframe & Initial Design:

Initial, minimal wireframes were created first to plan what pages might be needed. A second, more high fidelity set after more design considerations were also made after.  
### Home Page:
![Alt text](/README%20assets/v1/home.png){width=500px}

### Log in page
![Alt text](/README%20assets/v1/login.png){width=500px}

### Register page
![Alt text](/README%20assets/v1/register.png){width=500px}
### Create a post
![Alt text](/README%20assets/v1/create%20post.png){width=500px}
### Group page
![Alt text](/README%20assets/v1/group%20view.png){width=500px}
### Home (Mobile view)
![Alt text](/README%20assets/v1/home%20(mobile).png){height=400px}

After considering some design, some colours and branding were implemented:

### Home 
![Alt text](/README%20assets/v1.1/home.png){width=500px}
### Dashboard 
![Alt text](/README%20assets/v1.1/dashboard.png){width=500px}
### Mobile 
![Alt text](/README%20assets/v1.1/mobile.png){width=500px}

## Agile:
Using Agile principles, I created a projectboard and user stories. Taking into consideration a user's needs and tracking various criteria was a very valuable way to plan and structure my development time. This enabled me to be more efficient with my efforts and ensure progress was tracked and the deadline met. I was able to test and review features at multiple stages, iterating over my processes and able to improve the project each time until reaching a minimal viable product (MVP). I will be able to continue this process in the future in order to add more features and improve my project even further.

Below is my project board upon reaching my MVP.

![project board](/README%20assets/project%20board.png)

## Design Choices:

Beet is inspired by beetroots, where digging up a post within a forum can feel like pulling out a fresh vegetable from the ground!

### Mock logo
A simplistic Beetroot icon was chosen

![Logo](/README%20assets/beetroot%20logo.png)

### Colour scheme:
Themed around Beetroots vibrant colours as well as earthy contrasting colours, I used Coolers.co to help see some colour combinations together: https://coolors.co/7b1f4d-ac3448-ae5985-2f3702-a5c77d



![Hex Color Preview](/README%20assets/colours/7B1F4D.png) #7B1F4D - Main theming colour of background

![Hex Color Preview](/README%20assets/colours/AE5985.png) #AE5985 - Secondary colour mainly used for bulk text and buttons background

![Hex Color Preview](/README%20assets/colours/AC3448.png) #AC3448 - Tertiary colour for less important text such as post dates

![Hex Color Preview](/README%20assets/colours/A5C77D.png) #A5C77D - Contrasting colour used to make usernames stand out

![Hex Color Preview](/README%20assets/colours/2F3702.png) #2F3702 - Darker earthy colour for footer and borders

![Hex Color Preview](/README%20assets/colours/FFFFFF.png) #FFFFFF - white for headings and button text


### Font

**"Dosis"** from Google Fonts

A consistent font was chosen for the website that was clear to read whilst offering a softer, more nature-like look without hard edges. 
![Font sample](/README%20assets/font-dosis.png)


## Features:

### Navbar & branding:
A view of the navbar when no user is currently logged in.

![navbar logged out](/README%20assets/snaps/navbar1.png)

A view on a wider screen of the navbar with a user logged in.

![navbar logged in](/README%20assets/snaps/navbar2.png)

A view on a mobile sized screen. The nav menu toggles to show the menu items to avoid taking up uneccesary screen space.

![navbar mobile](/README%20assets/snaps/navbar%20toggled%20mobile.png)

#### "New Post"
Allows user to see that they can create their own post and contribute immediately once they have registered. Redirects to login page if not signed in.

![create post](/README%20assets/snaps/create%20post%20form.png)

#### "Create an account" 
Ability to sign up by picking a username, password and providing an email address. Not visible if a user is logged in.

![register](/README%20assets/snaps/register%20form.png)


#### "Login" 
Existing users can login here, they are redirected to their dashboard and the navbar menu will change and display their username. The form is styled very similarly to the register forms but with only a username and password input field.


### Sidebar:
The sidebar is a way to navigate different post feeds. It will be more personalised and show different communities a user follows. This makes it easy to find desired posts and is present in the base html file so is always accessible.

![sidebar](/README%20assets/snaps/sidebar.png)


### Home/default feed:
The home page reflects the branding and theme instantly, using a navbar with clear items that a user can easily see where they can register, login and be able to create their own post. The sidebar provides better navigation of posts specifically, offering more personalised views when logged in. The default feed delivers posts automatically so the user can instantly see content without having to input upon entering the website. Posts are fed individually showing what community they are from, with username, title, content and comments. Results paginated by default in order to see footer more easily.
Below is a view of it on mobile, the post list can be easily scrolled down.

![navbar logged in](/README%20assets/snaps/feed%20mobile.png)

#### Post view
When a post title is clicked on, the post can be viewed in more detail on its own page with the comments expanded by default.

![post view](/README%20assets/snaps/post%20view.png)

### Dashboard
The dashboard is the what the user sees when they log in. It can also be accessed via "My account" on the navbar. It displays info such as their associated email address and a list of their posts, split into published and awaiting approval sections. When they do not have any "No posts" is displayed instead of the post list. The biography section is a future feature to be implemented.

![dashboard](/README%20assets/snaps/dashboard.png)

The dashboard post list if a user does have previous posts. They can edit and delete the post and are taken to a confirmation screen before finalising.

![dashboard with posts](/README%20assets/snaps/dashboard%20post%20list.png)

#### "Change password"
Takes user to a form where a user can change their password linked to their account. It is also styled in the same way as other forms with input fields for "old password", "new passowrd" and "confirm password".

### Confirmation/system notification message
When the user makes a successful action or would alter information on the database permenentley, such as deleting a post, a system messaged will be shown. Below is an example of one confirming post deletion.

![system message](/README%20assets/snaps/delete%20warning.png) 

### Footer:
Minimal footer with other social media links and other details. Is easily accessibly by user as it is fixed at the bottom but takes up minimal screen space.

![footer](/README%20assets/snaps/footer.png)

### Future Features:

#### User profiles
Access to a personalised bio and other user's pages with chosen information displayed such as post/comment history and ability to upload a profile picture. A bio section has already been implemented on the dashboard.
#### Commenting
Ability to chain comments onto on another in replies and user's have more access to the current comments model.
#### Votes
Implement a simple upvote system, which can influence what is prioritised to be displayed on certain pages, based on an algorithm. This has been considered in the model but has not been made fully functional in terms of it's display.
#### Search function
A user can input text and search posts by content/title/author and sort by date or search for other users and profiles.
#### Video/image links
Attach videos and images into posts and have them embeded within the post cards for easy viewing. Fields have already been included in the Post model for this.

## Database Schema:

I used an Entity Relationship Diagram to plan out what models I would need for my database and what components and keys they should have. I used a flowchart to visualise each one's relationship to each other.

The initial basic draft was changed in another iteration in order to incorporate features more efficiently and reduce unnecessary coding.

![schema1](/README%20assets/schema1.png)
![schema2](/README%20assets/schema%202.png)


### Data Models:

|User| 
|----|
**username**    VARCHAR     [Primary key]|
**email**       VARCHAR
**password**	VARCHAR
**community**	VARCHAR		[Foreign key]

|Post|
|----|
**id**		    INT		    [Primary key]
**community**	VARCHAR		[Foreign key]
**title**		VARCHAR		
**content**		TEXT	
**img_link**	VARCHAR
**author**		VARCHAR		[Foreign key]
**date**		DATETIME	
**vote**		VARCHAR		[Foreign key]	(Many-to-many)
**status**		BOOLEAN	

|Community|
|----|
**title**		VARCHAR		[Primary key]
**user**		VARCHAR 	[Foreign key]	
**url**		    VARCHAR	
**img_link**    VARCHAR
**description** TEXT	
**date**		DATETIME
**post**		INT		    [Foreign key]

|Comment|
|----|
**id**		    INT		    [Primary key]
**post**		INT		    [Foreign key]
**username**	VARCHAR 	[Foreign key]
**body**		TEXT	
**date**		DATETIME
**vote**		VARCHAR		[Foreign key]	(Many-to-many)	

## Validation
 
### HTML
The W3C HTML validator was used on all my html templates
https://validator.w3.org/#validate_by_input

The initial validation pulled up a few errors across all my html files. Below is a summary of the reoccuring ones.
| Error   | Notes |
| -------- | ------- |
'Bad value' referencing curly braces {} |Django's syntax for its html templates, these are not used in this way for pure HTML, but were necessary for function and design, so these could be ignored
Button elements descendents of a elements|Present in my forms, this did not effect functionality
H5 elements descendents of button elements|Present in my forms, this also did not effect functionality but was needed for stylings to work
Doctype not seen before start tag|Due to templating this only needed to be present on my base.html
Missing head elements and child element title|Due to templating this was flagged with my forms, the required elements are present on my base html.
Warning: lang attribute|Templates did not include this as the base html 

In this example below I validate my base.html file, the issues were corrected and re-validated until the only errors were related to Django's templates.

![basehtmlvalid](/README%20assets/testing%20and%20validation/base%20html%20validate.png)

### CSS
The W3C CSS validator was used for my style.css file
https://jigsaw.w3.org/css-validator/validator

As I had already tidied up my CSS code before this step, it returned no errors.

![cssvalid](/README%20assets/testing%20and%20validation/css%20validate.png)

### Python 

I used The Code Institute's Python Linter https://pep8ci.herokuapp.com/ to validate my .py files.

I used it to especially check my larger, more core python files such as settings.py, forms.py and models,py.

![settings.py](/README%20assets/testing%20and%20validation/settings%20py%20validate.png)

![forms.py](/README%20assets/testing%20and%20validation/python%20validator.png)

![models.py](/README%20assets/testing%20and%20validation/models%20py%20validate.png)

#### The errors found were indentations, line lengths, line spacing and whitespace. These were easily fixed until they passed validation.

![python validated](/README%20assets/testing%20and%20validation/python%20pass.png)

## Testing

### Java
I mainly used manual tests for my Javascript such as on my homepage. A simple script was used to be able to toggle comments from being visible for each post. 
I viewed the console while I toggled the button multiple times to test functionality, and confirmed the class was changing with input from the user.

![javatest](/README%20assets/testing%20and%20validation/java%20test.png)

### Python
For Python, as well as continously doing manual tests with my models, forms and views on the live database I did some automated testing using Django. The test checked for each datafield having invalid input attempts.

Here is a test I ran for the create user form.

![python auto test](/README%20assets/testing%20and%20validation/createuser.png)

The error did not effect functionality as it was looking for the notification to be in double quotes but instead was in single quotes, as generated by Django's form.

### Testing user experience
Below is an example of a user navigating the website, testing various components and functions, as the project was at an earlier date. Several changes have been made after this video, including logout success notifaction and various form stylings.

<video width="1280" height="720" controls>
  <source src="README assets/beet user test muted.mp4" type="video/mp4">
</video>

| Feature |Passed?|Notes|
| -------- | ------- | ------- |
Home view| Y |Post fonts appear to be of appropriate size
Comments toggle|Y|Comments hidden be default
Pagination|-|Posts appear paginated and next button functions as intended, but does not have a "previous" button on page 2
Nav bar links|Y|Each link is active and directs to it's intended page
Create account|-|Form functions correctly, but no success message
Login|Y|Form functions and directs to dashboard
Create post|-|Post appears in dashboard but is not automatically public, but no success message
Edit post|-|Post can be edited and will reset status to not public, no success message
Change Password|-|Password change updates database User model correctly, no success message
Logout|Y|A success message could be added

After reviewing these tests, the fixes were made (notifation of more user actions and pageination controls improved) and are updated in the live link. Several other features were also tested and updated where needed, such as social media links on the footer.

## Responsiveness and browser compatability

To test responsiveness for different screen sizes I used the developer tools within my browser to view my website at various different sizes and aspect ratios, as well as changing the size dynamically to see how the different components scaled and test any breakpoints. I tested different pages on each screen size, especially checking for body text and form size was appropriate for each. Below are example screenshots of each size.

### Screen size 375 x 667 px 16:9, portrait mode (iPhone SE)
The navbar is collapsed in this screenshot to show post size, especially body text.

![iphone](/README%20assets/screen%20sizes/iphone%20se%20375.png)

### Screen size 768 x 1024 px 4:3, portrait mode (iPad Mini)
The navbar is expanded in this example to show that the links are large and clear.

![ipad](/README%20assets/screen%20sizes/ipad%20mini%20768.png)

### Screen size 1024 x 600 px (Nest Hub)
This was used to test when a device is orientated a different way to see how the site is viewed landscape.

![nest hub](/README%20assets/screen%20sizes/nest%20hub%201024.png)

### Screen size 1280 x 800 px 16:10
A test on a larger screen with wider aspect ratio, showing a form.

![nest hub](/README%20assets/screen%20sizes/1280%20x%20800.png)

### Screen size 1920 x 1080 px 16:9
This tested it on more modern resolutions as well as desktop computer sizes.

![1080p](/README%20assets/screen%20sizes/1080p.png)

### Screen size 3840 x 2160 px 16:9 (4K)
Final testing was done to consider larger desktop resolutions and multi-monitor set-ups, although it is likely many users using these setups would not neccesarily view it at full resolution.

![4k](/README%20assets/screen%20sizes/4k.png)

### Browser Compatibility:

The previous screnshots were all taken using Google Chrome. I also tested in Microsoft Edge and Mozilla Firefox.

Microsoft Edge

![edge](/README%20assets/snaps/MS%20edge.png)

Mozilla Firefox

![firefox](/README%20assets/snaps/firefox.png)


## Deploying

The app was created on Heroku, initially using settings of "DISABLE_COLLECTSTATIC" to test before setting up my static files. 
After installing gunicorn and creating a Procfile for my project, adding access for heroku url in my settings.py file and setting DEBUG to False, I was able to link my project from github and manually deploy. 
After setting up my databse and static files, I changed the config vars on heroku to include the database url and secret key, which enabled me to have it hidden from commits on github for security.

*****
## Technical toolkit and resources

||||
| -------- | ------- | ------- |
|HTML5, CSS, Javascript| Used as a basis of front-end coding, providing the website structure and appearance 
|Bootstrap|CSS framework to speed design up, providing a basis of pre-made styling options
|Python|Language used for back-end logic and communicating to database
|Postgres Database server|Provided by Code Institute, allowed me to manage data using SQL
|Django|Framework for Python which made it easy to combine front-end components and back-end components together
|Github|For storage and version control over my project code
|Gitpod|IDE used during development
|Balsamiq|Program used to create wireframes
|Heroku|Used to deploy and host site
|ChatGBT|Used to gain a better understanding of concepts and suggest issues
|Google|Used for research and finding various other tools
|Code Institute LMS|Providing inital concept teaching and process walkthroughs

### Bugs and issues

Continuous testing as described in the "Testing" section of this document as well as attention to process allowed to continually solve any errors or issues I encountered on all stages of this project, with the help of varous resources and tools.

### Other credit

#### General project guide

I used several video tutorials to provide a general idea and a look into different approches to achieve smiliar projects in Django.

- https://www.youtube.com/@aiocallinonecode6506

- https://www.youtube.com/@DjangoWorld

- https://www.youtube.com/@Codemycom


#### Design

Logo chosen from free image website https://www.freepik.com/

Colour palette chosen using the help of https://coolors.co/

Google fonts used to find and choose design font https://fonts.google.com/


#### Users

I was helped by several friends and housemates as they were able to test various features of my project and different stages, as users, and provide feedback.

#### Other online resources

- https://randomkeygen.com/ was used to generate a secret database key

- https://www.w3schools.com/ provided extra learning support and code validation
