# Portfolio Project 4 - Full Stack Frameworks with Django

## LJ Fitness - Live Site

[View Live Site]()

## Business Objectives

As a gym goer myself, I decided to design and create a website that allows users to access the website in order to locate and purchase the wide range of monthly memberships that the gym has to offer, as well as signing up to create their own account to manage memberships. The site also allows the owner/business to advertise their brand and keep their membership offers up to date.

The primary focus for this website is to provide a database for the user so that they can view and purchase their own chosen memberships with just a few clicks. Users will also be able to add and delete memberships as they please. 
The owner of the site can update and delete memberships too, in order to advertise their current passes available.

The application is designed to be responsive to all screen sizes and accessible to all users, so that navigation is easy for everyone, no matter what device is being used. My goal is to achieve this with a visually appealing, interactive UX, which encourages users to:
- view a wide range of memberships that they are able to purchase in order to join LJ Fitness.
- purchase as many monthly memberships as they would like.
- create their own account so they can easily view which memberships they are currently signed up to.
- share the website with friends and family to encourage them to sign up.
- follow the company's social media platforms to keep up-to-date with the gym's latest offers and recent activities.
- contact the owner of the site if they wish to.

The owner of the site will be able to:
- inform visitors of new memberships or classes.
- promote the wide range of memberships they have to offer.
- edit or delete memberships.
- communicate with visitors who have reached out via email.

## Homepage Mockup

![]()

## User Experience (UX)
### User Stories
**First Time Visitor Goals**

1. As a first time visitor, I want to understand what the site's purpose is so that I know whether or not I want to explore further.

2. As a first time visitor, I want to know as much information as possible about the memberships so I know which is right for me.

3. As a first time visitor, I want to be able to easily register so I can keep track of memberships that I have purchased.

4. As a first time visitor, I would like to be able to contact the owner easily if I have any queries.

**Returning Visitor Goals**

5. As a returning user, I want to be able to purchase my chosen membership/s with just a few clicks.

6. As a returning user, I want to be able to log into my account easily to view and manage my membership/s.

**Frequent Visitor Goals**

7. As a frequent user, I want to be able to follow the company's social media platforms so that I can follow them and share my fitness journey, as well as keeping up-to-date with any new activities or offers.

8. As a frequent user, I want to be able to access and manage my profile and memberships.

**Site Owner Goals**

9. As a site owner, I want to advertise the memberships I have to offer to clients with a clean and organised look.

10. As a site owner, I need to enforce some basic access control when a user is editing or deleting data in order to prevent unauthorised editing or deletion of user uploaded data.

11. As a site owner, I need to provide a safe and secure payment system for my clients.

12. As a site owner, I want to receive email enquiries from clients directly into my inbox.

## Design
### Colour Scheme
Colour contrast checks were made throughout the process of building the project to save going back and re-doing colours that did not work together.

The main colour scheme is clean and sharp, using shades of *dark-grey*, *light-grey*, *off-white* and *orange*. The look and feel I wanted to go for was the same first impression you want when you first walk into a gym - sharp, confident and bold.

There are some photographic images throughout, to tie in well with the theme of the site. These images are used on the landing page, and the *Membership Details* page. The images I chose were selected to inspire potential clients into signing up for the gym.

The text throughout the site is either off-white against the dark-grey background, or orange against a grey background, in order to keep the sharp contrast throughout the site.

![Landing Imagery](documentation/images/features/landing.jpg)

### Typography

Fonts are imported into the head of the base.html template via [Google Fonts.](https://fonts.google.com/)

To keep up with the boldness of the site, I chose to use a font that is easy to read, alongside heavy use of uppercase text.
I have chosen to use the font family of 'Open Sans', with a fallback font of 'san-serif', in the event of the preferred font failing to import. This font will hopefully create a positive user experience when first entering the site as it exudes a professional yet bold approach.

![Open Sans font](documentation/images/features/welcome-text.jpg)

### Imagery

Photographic imagery is used in some parts of the site, all images are sourced from [Pixabay](https://pixabay.com/photos/search/) and [Pexels.](https://www.pexels.com/)

The landing page consists of a header, a background image, a welcome message and a footer. The chosen background image was selected because of its subtle tones and lack of contrast against the other elements, as I did not want to distract the site user away from the text.

This image gives the user a good idea of what the site is about upon entering.

The *Membership Details* page contains information and the option to add the selected membership to the users' cart. Alongside the membership information is an image of a lady at the gym, I wanted this to inspire the site user to explore further and motivate them to purchase a membership pass.

![Lady at the gym](/documentation/images/features/membership-details.jpg)

## Wireframes
Wireframes for the original design concepts across all devices were created using [Balsamiq.](https://balsamiq.com/wireframes/)

**Landing Page**

The landing page explains the purpose of the site to new and returning users through imagery and subheadings. From here users are able to sign up/in, contact the site owner, view social media platforms and view the available memberships via a link.

![Landing Page Wireframe](/documentation/images/wireframe_imgs/landing.jpg)

**Sign-Up/Sign-In Page**

 Here users can create unique log-in credentials based on an alphanumeric Username and alphanumeric Password. Back-end logic tests for duplicate entries and password confirmation.

![Sign-Up/Sign-In Page Wireframe](/documentation/images/wireframe_imgs/sign-up.jpg)

**Memberships Page**

Whether a user has signed up or not, they are able to view all memberships that the gym has to offer. Memberships can be filtered down to a specific category, "HIIT Fitness", "Strength & Conditioning", "Boxing" and "View All".

![Memberships Page Wireframe](/documentation/images/wireframe_imgs/memberships.jpg)

**Membership Details Page**

Here the user is able to view information about the membership as well as being given the option to add the pass to their cart. Upon which they will see a pop up letting them know that they have successfully added the item to their cart. The pop up will contain a button that will direct the user to the checkout page.

![Membership Details Page Wireframe](/documentation/images/wireframe_imgs/membership-details.jpg)

**Checkout Page**

Users can view, update and delete their shopping cart contents before they proceed to the payment page.

![Checkout Page Wireframe](/documentation/images/wireframe_imgs/checkout.jpg)

**Payment Page**

Users are shown a summary of their order details. A form must be filled out containing users' billing details. The user will be given the option to save details in order to make a profile.

![Payment Page Wireframe](/documentation/images/wireframe_imgs/payment.jpg)

**My Memberships Page**

Users are able to view any membership passes that they have previously purchased. Users can view and update their default billing information also. *In the future I would like to add another feature to this page that allows the user to see when their pass expires.*

![My Memberships Page Wireframe](/documentation/images/wireframe_imgs/my-memberships.jpg)

## Database schema

I used Mongo DB Atlas, a non-relational database to store and retrieve all of the user input data, illustrated below:

![Database](/documentation/images/features/data.jpg)

- The *Users* collection stores user data, including a usernsame and password that they will input each time they are required to log in. The username is used to populate the *created by* field in the *Recipes* collection when a user uploads a new recipe.

- The *Recipes* collection is the largest in the database and stores all user input regarding each recipe, as well as data retrieved from other collections. I included all elements of a recipe that I thought were most relevant for each field.

- The *Categories* collection consists of user input regarding the diet type of that recipe. Which is then injected into the *Recipes* collection as the *diet_name*.

## Features
### Existing Features
| Feature | Description | Image URL |
| ------- | ----------- | --------- |
| Landing | Landing page to convey the purpose of the website to new and returning users. | [Landing Page](/static/images/newlanding.jpg) |
| Header | Logo and nav bar allow user to navigate through the site with ease. Burger icon displays on smaller devices. | [Header](/documentation/images/features/header.jpg) |
| Footer | Sign up option and social media icons direct the user to the company's social media platforms. | [Footer](/documentation/images/features/footer.jpg) |
| Register | Provides the opportunity for new users to sign-up quickly and efficiently. | [Registration Page](/documentation/images/features/register.jpg) |
| Log-In | Provides the opportunity for returning users to log-in quickly. | [Log-In Page](/documentation/images/features/log-in.jpg) |
| Profile Page | Users are directed to a welcome message displaying their username. | [Profile Page](/documentation/images/features/profile.jpg) |
| Recipes | Page where all users' recipes are displayed. | [Recipes Page](/documentation/images/features/recipes.jpg) |
| Recipe Search | Users can text search for a recipe using the recipe name or diet category. | [Recipe Search](/documentation/images/features/recipe-search.jpg) |
| Drop Down Recipes | Recipes are organised with dropdown select elements. Users select/drop the recipe they want to view. | [Dropdown Recipe](/documentation/images/features/dropdown.jpg) |
| Add Recipe | Users can create and upload a recipe to their database. | [Add Recipe](/documentation/images/features/add-recipe.jpg) |
| Edit Recipe | Enables users to modify all of the fields for any of the recipes they uploaded. Original data is uploaded from the database into the value fields until the user modifies. | [Edit Recipe](/documentation/images/features/edit-recipe.jpg) |
| Delete Recipe | Allows user to delete a recipe that they have uploaded. | [Delete Recipe](/documentation/images/features/delete.jpg) |
| Manage Categories | Admin access only. Admin has the ability to create, update or delete diet categories. | [Manage Categories Page](/documentation/images/features/manage-cat.jpg) |
| Log-Out | Logs user out and clears session | [Log Out](/documentation/images/features/logout.jpg) |

### Security Features

Although certain security features were not required for this project I have chosen to implement basic measures to provide some protection against unauthorised access to other users data.

| Feature | Description | Image URL |
| ------- | ----------- | --------- |
| User Log-In | A simple username and password is required for registration. Password gets hashed using Password Hash from the Werkzeug Library. | [Log-In Security](/documentation/images/features/login-security.jpg) |
| Session Cookie | Upon registering or logging in, a unique session cookie is generated for the duration of the users' session. Recipe uploads are saved in the database against the session cookie username. | [Session Cookie](/documentation/images/features/session.jpg) |
| Restricted Access | Users cannot edit or delete recipes that are not uploaded by them. Only admin users can manage categories. In the Image URL, you can see that only the username of *laurajones* will be able to edit or delete the recipe. | [Restricted Access](/documentation/images/features/access.jpg) | 
| Password Confirmation | When registering, a password confirmation input field is displayed to ensure the user signing up is genuine. | [Password Confirmation](/documentation/images/features/password-conf.jpg) |



### Features yet to implement

| Feature | Description |
| ------- | ----------- |
| Dropdown for all Recipes | At the moment, all recipe names are visible under their category, ready to be selected and dropped down for full visibility. For better organisation, I would like to hide all recipes until the user clicks a drop down button (on the chosen category card) that will reveal all recipes under that category. |
| Next/Previous button | Incase the *My Recipes* page becomes too crowded once a user has uploaded a lot of recipes, I would like to set a limited amount of recipes that are shown below the category cards, and when that number of recipes is exceeded there is a *next* button that allows the user to skip to the next lot of recipes. |
| Family accounts | Once I have built up the knowledge required to be able to take the web app further, I would like to provide the opportunity to hold family/household accounts where users of the same family can log into the same account but have their own individual profile that only they can manage. |
| Profile Management | I would like to add a management system for users to be able edit their profiles and populate elements such as, usernames, profile picture, favourite recipe/food. |
| Delete confirmation | On developing the website further I would like to add a modal that appears when a user attempts to delete a recipe or category. The modal will ask the user if they are sure that they want to delete, to prevent any accidental deletions.

## Technologies Used
### Languages
- HTML5
- CSS3
- Python
- JavaScript


### Libraries/Integrations

- Flask - Flask micro-framework, links with jinja to create the webpages.

- Jinja - The project uses the Jinja templating engine.

- Materialize CSS - Grid system as well as other elements used throughout the site.

- Hover.css - Used in the Footer to highlight when links are hovered over.

- Google Fonts - Imported via CSS.

- Font Awesome - Icons used for social media links as well.

- Balsamiq - Used to create wireframes for the project.

### Database Management System

- MongoDB Atlas

### Version Control, Storage & Hosting

- Chrome Dev Tools - Heavily used to fix any spacing issues as well as testing responsivity.

- Github - To store repositories and codes after being pushed on Gitpod.

- Git - Used for version control and tracking changes made to files.

- Gitpod - Used for the workspace for this project.

- Heroku - Deployment site.

- Multi Device Mockup Generator (techsini) - To create an image of what the project will look like on various devices. [TechSini.com](http://techsini.com/multi-mockup/index.php)

- WebAIM Contrast Checker - To test colours throughout the site for whether or not they will produce good user experience.

- W3C Markup Validator - Checks HTML code for errors and warnings.

- W3C CSS Validator - Checks CSS code for errors and warnings.

- JShint - Checks JavaScript code for errors and warnings.

- PEP8 Validator - Checks that the Python code is PEP8 compliant.

## Testing

All testing for this project can be found in the [TESTING.md file](TESTING.md).

## Creating the Database

The key features required for this app to function as designed are centred around CRUD interactions with a MongoDB Atlas cloud database management system:

- Create or upload a recipe into the database which can then be viewed by all other registered users.
- Read or view all of the recipes stored in the database.
- The list of recipes can be searched by recipe name or category name.
- Update any of their own recipes, to change any of the previously stored content, or add additional information.
- Delete recipes they themselves have uploaded. This provides restricted access.

This app is connected to a MongoDB Atlas Cluster. The following steps were used to create the MongoDB Project Database:

1. Register/log-in to MongoDB Atlas.
2. Create a new project.
3. Click 'Build a Database'.
4. Locate the free, 'Shared' database and click 'Create'.
5. Ensure that you have the 'AWS' Cloud Provider selected, and that you have selected the region closest to you. Ensure that the Cluster Tier is of M0 Sandbox, then click 'Create Cluster'. *See below*.

![Create Database](/documentation/images/testing/createdb.jpg)

6. Create your username and password and ensure that 'My Local Environment' is selected for the network connection.
7. Add IP Address and allow Access from Anywhere (Not recommended for full production apps).
8. Once the database is active, you can connect it to Git or whatever version control you are working from.
9. Click Collections to add a database and start adding documents to your database collections by providing a database name and adding a name for your first collection of documents.

## Deployment

This project was created using Gitpod, which enabled me to stage and commit the files via Git (version control). ll of the files necessary to run this website have been stored in a GitHub repository.

### Forking the GitHub repository

1. Select the repository you wish to fork.
2. In the top right corner of the page (under your account icon) there will be an option to Fork.
3. By selecting Fork you will now have a copy of the respository in your own Github account.

### Cloning the Github Repository:

1. Select the repository you wish to clone locally.
2. Above the files, locate the Code dropdown menu.
3. Select and copy the link appropriately (HTTPS, SSH, Github CLI).
4. Open the terminal and change the directory to where you want the cloned version to be located.
5. Type git clone and paste the copied link.
6. Press Enter to create local clone.

### Creating the Heroku App

As this is a full-stack website it has been deployed to Heroku.com using the following procedure:

1. Register/log-in to Heroku.
2. From the Dashboard, select the "New" button on the top-Right of the screen, then select "Create new app".
3. Choose your app name.
4. Select your region.
5. Click "Create App".

### Heroku Deployment

1. In the "Deployment Method" section, select Github. Locate the Connect to GitHub section below.
2. Your Github profile should be displayed, if not type in your GitHub username.
3. Select the corresponding repository, and click "Connect".

Configuration settings and secret keys are needed for this app, which Heroku requires in order for the website to function as desired. To do this you need to set the Config Vars within Heroku:

5. Under the "Settings" tab, in the Config Vars section select the "Reveal Config Vars" button.
6. This will reveal a form for inputting the key and value pairs necessary to connect to the app, as follows:

| KEY | VALUE |
| --- | ----- |
| IP | 0.0.0.0 |
| PORT | 5000 |
| SECRET KEY | Randomly Generated Fort Knox Key |
| MONGO_URI | Your unique MongoDB URI |
| MONGO_DBNAME | Your unique Mongo DB name |

You can find the above Mongo_URI value in the appropriate Mongo DB Project under Cluster by selecting "Connect".

7. Select "Clusters".
8. Select "Connect".
9. Select "Connect your application".
10. Choose your Driver and Version.
11. Copy your connection string.

***Remember to substitute in your own DBNAME and Password***

### Enabling Automatic Deployment

1. In Heroku, click the "Deploy" tab.
2. In the "Automatic deploys" section select the branch you wish to use.

***Since first deploying the application on Heroku, Heroku themselves have encountered a security problem and therefore have had to remove certain functionalities that would allow users to automatically deploy or update. All deployments are now carried out manually using the following procudure:***

1. In the terminal, run the command `heroku login -i` and login when prompted.
2. Run the following command: `heroku git:remote -a your_app_name_here` and replace `your_app_name_here` with the name of your Heroku app. This will link the app to your Gitpod terminal, and the Heroku app to the Gitpod workspace.
3. After linking your app to your workspace with one of the above steps, you can then deploy new versions of the app by running the command `git push heroku main` and the app will be deployed to Heroku.

## Credits

The content of this website was created by Laura Jones. Snippets of code have been copied from official documentation and other sources credited below. All pre-loaded recipes were taken from various Cookbooks and online recipe sites, which are also credited below.

### Code

Much of the structure of this site follows what was taught during the Backend Development - Task Manager walkthrough project provided by Code Institute, but has been modified to suit a recipe database site.

| Code Snippet | Description | Source |
| ------------- | ----------- | ------ |
| Navbar |  Navbar element sits on the right with a responsive burger icon on smaller devices | [Materalizecss.com](https://materializecss.com/navbar.html) |
| Footer | Footer content is spaced evenly using rows and columns, consisting of a *Sign-Up* section and social media links | [Materalizecss.com](https://materializecss.com/footer.html) |
| Forms | Rows and colums are used to make the forms look organised and evenly spaced (Register, Log-In, Add/Edit Recipe and Add/Edit Categories) | [Materlizecss.com](https://materializecss.com/text-inputs.html) |
| Cards | Cards are used in the Profile page (welcomes user), the Recipes page (each card stands for a different diet category and holds the relevant recipes), the Search bar and in the Manage Categories page | [Materializecss.com](https://materializecss.com/cards.html) |
| Collapsible Recipes | Recipes drop down when they are clicked to keep the page looking organised | [Materializecss.com](https://materializecss.com/collapsible.html) |
| Buttons | Buttons used throughout the site | [Materliazecss.com](https://materializecss.com/buttons.html) |
| Python functions | The backend functionality structure was taught via the Code Institute Task Manager Project | [CI Task Manager Walkthrough Project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/9e2f12f5584e48acb3c29e9b0d7cc4fe/054c3813e82e4195b5a4d8cd8a99ebaa/) |
| Form Validation for Dropdown Input Box | Ensures form validation on the dropdown input field when using Materliaze | [CI Task Manager Walkthrough Project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/9e2f12f5584e48acb3c29e9b0d7cc4fe/6449dcd23ca14016aa83dc7313d91a02/?child=first) |
| 404 Page | Renders 404 Page through Python & Flask | [GeeksForGeeks.org](https://www.geeksforgeeks.org/python-404-error-handling-in-flask/) |

| Imagery | Description | Source |
| ------------- | ----------- | ------ |
| Landing Page | Background Image | [Pixabay](https://pixabay.com/) |
| Recipes Page | Card Images | [Pixabay](https://pixabay.com/) |
| Manage Categories | Card Images | [Pixabay](https://pixabay.com/) |

## Acknowledgements

- Code Institute - for the video tutorials and providing the knowledge for Python, Flask and some of the different databases structures.

- Code Institute Tutors - Providing advice on how to run a loop more than once on the same page.

- Code Institute Mentor, Spencer Barriball - for the fantastic, professional advice on what makes a good web developer.

- Fellow Slack Members - for providing outstanding advice in times of need.