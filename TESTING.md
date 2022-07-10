# Testing

Most testing was carried out via Google Chrome browser and Chrome Dev Tools for responsivity and checking to see if the JavaScript/Python code was working as expected, throughout the process of building the project. Microsoft Edge and Firefox was also used for testing overall performance and responsivity. I also tested the site on an iPhone 12 for responsivity, this included Google Chrome and Safari browsers.

## User Story Testing

| User Story | Description | Testing |
| ------- | ----------- | --------- |
| 1 | "As a first time visitor, I want to understand what the site's purpose is so that I know whether or not I want to explore further." | Upon entering the site, the user is directed straight to the landing page where a clear explanation of the app's purpose with both text and imagery. |

![Landing Page](/documentation/images/features/landing.jpg)

| User Story | Description | Testing |
| ------- | ----------- | --------- |
| 2 | "As a first time visitor, I want to know as much information as possible about the memberships so I know which is right for me." | Users can view all memberships or choose to filter a search to show a specific category. Users can see which days each class is available on, along with price and parking facilities. |

![Memberships](/documentation/images/features/memberships.jpg)

| User Story | Description | Testing |
| ------- | ----------- | --------- |
| 3 | "As a first time visitor, I want to be able to easily register so I can keep track of memberships that I have purchased." | Registration is quick and simple, requiring the user to provide a valid username, email-address and password. Users are then able to view their order history/memberships they have purchased. |

![Registration](/documentation/images/features/sign-up.jpg)

![My Memberships](/documentation/images/features/my-memberships.jpg)

| User Story | Description | Testing |
| ------- | ----------- | --------- |
| 4 | "As a first time visitor, I would like to be able to contact the owner easily if I have any queries." | Users are able to fill out a contact form that is sent to the site owners' inbox. *(Not live)* |

![Contact Form](/documentation/images/features/contact-form.jpg)

| User Story | Description | Testing |
| ------- | ----------- | --------- |
| 5 | "As a returning user, I want to be able to purchase my chosen membership/s with just a few clicks." | Users can add a chosen membership to their cart, they are then given the option to view their shopping cart via a button in the *Successful toast message*. Users can then update their cart or go straight to checkout, fill out billing information and are able to purchase their membership securely and safely via Stripe payments. |

![Go To Checkout](/documentation/images/testing/purchase1.jpg)

| User Story | Description | Testing |
| ------- | ----------- | --------- |
| 6 | "As a returning user, I want to be able to log into my account easily to view and manage my membership/s." | Users can log in securely and go to the *My Memberships* page to view their order history. |

![Log In](/documentation/images/features/sign-in.jpg)

![My Memberships](/documentation/images/features/my-memberships.jpg)

| User Story | Description | Testing |
| ------- | ----------- | --------- |
| 7 | "As a frequent user, I want to be able to follow the company's social media platforms so that I can follow them and share my fitness journey, as well as keeping up-to-date with any new activities or offers." | Users can find the social media links a in the footer which will direct them to the company's social platforms. |

![Social Media Links](/documentation/images/features/footer.jpg)

| User Story | Description | Testing |
| ------- | ----------- | --------- |
| 8 | "As a frequent user, I want to be able to view the gym's timetable to keep track of class' times and days that they are running." | Users can view the gym's timetable in the footer which shows class names, days and times. |

![Timetable](/documentation/images/features/footer.jpg)

| User Story | Description | Testing |
| ------- | ----------- | --------- |
| 9 | "As a frequent user, I want to be able to access and manage my profile and memberships." | Users can update their billing details. |

![Manage Profile](/documentation/images/features/my-memberships.jpg)

| User Story | Description | Testing |
| ------- | ----------- | --------- |
| 10 | "As a site owner, I want to advertise the memberships I have to offer to clients with a clean and organised look." | The membership info is displayed in a card element with styling that compliments the theme of the website. The site owner can add/edit/delete memberships with the CRUD functionality |

![Add Membership](/documentation/images/features/add-membership.jpg)
![Admin Access Buttons](/documentation/images/testing/admin-access.jpg)

| User Story | Description | Testing |
| ------- | ----------- | --------- |
| 11 | "As a site owner, I need to provide a safe and secure payment system for my clients." | Users are able to purchase memberships via the Stripe online payment system. |

![Make Payment](/documentation/images/testing/payment.jpg)
![Stripe Webhook](/documentation/images/testing/webhook.jpg)

## Functionality Testing (Manual)

The following tables show the functionality testing performed on the web-app to ensure it works as desired. I have tested on a Windows device on the listed browsers.

### Navigation Testing

Tests the navbar selections and various anchor links provided to assist users navigating between pages.

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 001 | Home/logo link | Directs user to homepage | Opens homepage | PASS | PASS | PASS |
| 003 | Memberships link | Directs user to Memberships page | Opens Membership page | PASS | PASS | PASS |
| 004 | Contact Us link | Directs user to Contact Us page | Opens the Contact Form | PASS | PASS | PASS |
| 003 | Memberships link on mobile nav | Directs user to Memberships page | Opens Membership page | PASS | PASS | PASS |
| 004 | Contact Us link on mobile nav | Directs user to Contact Us page | Opens the Contact Form | PASS | PASS | PASS |
| 005 | Sign-In link | Directs user to sign-in page | Opens Sign-In page | PASS | PASS | PASS |
| 006 | Sign-Up redirect link on Sign-In page | Directs user to Sign-Up page | Opens Sign-Up page | PASS | PASS | PASS |
| 007 | Sign-Up link | Directs user to Sign-Up page | Opens Sign-Up page | PASS | PASS | PASS |
| 009 | Sign-In redirect link on Sign-Up page | Directs user to Sign-In page | Opens Sign-In page | PASS | PASS | PASS |
| 010 | Forgot Password link | Directs user to Password Reset page | Opens Password Reset page | PASS | PASS | PASS |
| 010 | Shopping Cart link | Directs user to the Shopping Cart page | Opens Shopping Cart page | PASS | PASS | PASS |

### Sign-Up/Sign-In Testing

Testing the registration process for new users and the log-in process for returning users. The app should provide feedback to the user in cases where incorrect inputs are provided.

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 011 | Username input | Feedback when requirements not met | User is unable to progress further until requirements are met | PASS | PASS | PASS |
| 012 | Password input | Feedback when requirements not met | Input box turns red and tooltip provides feedback | PASS | PASS | PASS |
| 013 | Email confirmation | Feedback when email addresses do not match | User is unable to progress further until requirements are met | PASS | PASS | PASS |
| 013 | Password confirmation | Feedback when passwords do not match | User is unable to progress further until requirements are met | PASS | PASS | PASS |
| 014 | Email address already has account | Lets user know that the email address entered has already created an account | User is unable to progress further until requirements are met | PASS | PASS | PASS |
| 016 | Incorrect username | Inform user of a incorrect username OR password | Message letting user know that either an incorrect username or password has been entered | PASS | PASS | PASS |
| 017 | Incorrect password | Inform user of a incorrect username OR password | Message letting user know that either an incorrect username or password has been entered | PASS | PASS | PASS |

![Incorrect Username/Password](/documentation/images/testing/incorrect-pass.jpg)

![Requirements not met](/documentation/images/testing/feedback.jpg)

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 018 | Sign-In/Sign-In successful | User directed to Home page | Home page is loaded, displaying a successful toast message. | PASS | PASS | PASS |

![Toast Sign-in](/documentation/images/testing/sign-in-success.jpg)

### Memberships Filter & View (READ)

Testing the ability to view the memberships/products and filter by category. Clicking the 'Join Now' button should also direct the user to the Membership Details page which gives the user the option to add the membership to their cart.

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 020 | Navigate to Memberships page, viewing all memberships (navbar) | Direct user to Memberships page, showing all memberships | The Memberships page is loaded, displaying all membership cards. | PASS | PASS | PASS |
| 021 | Navigate to Memberships page, filtering 'HIIT Fitness' memberships (navbar) | Direct user to Memberships page, displaying memberships for 'HIIT Fitness' | The Memberships page is loaded, displaying 'HIIT Fitness' membership cards. | PASS | PASS | PASS |
| 021 | Navigate to Memberships page, filtering 'Strength & Conditioning' memberships (navbar) | Direct user to Memberships page, displaying memberships for 'Strength & Conditioning' | The Memberships page is loaded, displaying 'Strength & Conditioning' membership cards. | PASS | PASS | PASS |
| 021 | Navigate to Memberships page, filtering 'Boxing' memberships (navbar) | Direct user to Memberships page, displaying memberships for 'Boxing' | The Memberships page is loaded, displaying 'Boxing' membership cards. | PASS | PASS | PASS |
| 022 | Categories and Memberships organised & displayed | Memberships are organised by category | Memberships are displayed in order of category | PASS | PASS | PASS |

### ADMIN ONLY - Add Membership (CREATE)

Testing the ability to add a new product/membership to the database.

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 025 | Navbar link (Gym Management) | Direct admin user to the 'Add a Membership form' page | The Gym Management page loads and displays the 'Add a Membership form' | PASS | PASS | PASS |
| 026 | Mob nav link (Gym Management) | Direct admin user to the 'Add a Membership form' page | The Gym Management page loads and displays the 'Add a Membership form' | PASS | PASS | PASS |
| 027 | Category name | Admin user can select the category that the membership will be added to | Category name successfully added | PASS | PASS | PASS |
| 028 | Add Membership name | Field is required | Admin user is able to add a membership name and feedback is provided when this field does not have a value | PASS | PASS | PASS |
| 029 | Add description | Field is required | Admin user is able to add a membership description and feedback is provided when this field does not have a value | PASS | PASS | PASS |
| 030 | Add price | Field is required | Admin user is able to add a membership price and feedback is provided when this field does not have a value | PASS | PASS | PASS |
| 031 | New membership adds to Memberships page | New membership is displayed in the Memberships page in category order | Users can view the newly added membership | PASS | PASS | PASS |

### ADMIN ACCESS ONLY - Edit Membership (UPDATE)

Testing the ability to retrieve a previously uploaded membership from the database and edit any of the data previously supplied.

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 037 | Edit button | Direct user to Edit Membership form | Edit Edit Membership form is loaded | PASS | PASS | PASS |
| 039 | Existing data renders | Display existing membership data from the database onto the form | All of the existing data is loaded into the form fields | PASS | PASS | PASS |
| 041 | Edit Category name | Category name can be edited | Admin user can edit the category name | PASS | PASS | PASS |
| 042 | Edit Membership name | Membership name can be edited | Admin user can edit and delete the membership name | PASS | PASS | PASS |
| 043 | Edit Description | Description can be edited | Admin user can edit and delete the description | PASS | PASS | PASS |
| 044 | Edit Price | Price can be edited | Admin user can edit the membership price | PASS | PASS | PASS |
| 044 | 'Update Membership' button | Admin user is redirected to the Membership Details page | Upon completing the edit form and submitting, the admin user is successfully redirect to the specificied Membership Details page | PASS | PASS | PASS |
| 049 | Data Written to Django Admin | Confirm membership data is edited and written to Django Admin | Edited memberships appear in the Django Admin displaying their updated fields | PASS | PASS | PASS |
| 050 | Memberships page updated | Edited membership successfully renders on Memberships page | The edited membership renders as intended on the Memberships page | PASS | PASS | PASS |

### ADMIN ACCESS ONLY - Delete Membership (UPDATE)

Testing the ability to delete the diet memberships from the database.

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 055 | Delete Button | Deletes membership | Admin user can successfully delete a membership from the web app and the database | PASS | PASS | PASS |
| 044 | Redirect | Admin user is redirected to the Memberships page | Upon deleting the membership, the admin user is successfully redirected to the Memberships page, where the deleted membership is no longer displayed | PASS | PASS | PASS |

### Purchase a Membership

Testing the ability to purchase a membership by adding to the shopping cart and making a secure online payment via Stripe.

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 055 | 'Join Now' button | Directs user to the Membership Detils page of chosen membership | User is successfully directed to the Membership Detail | PASS | PASS | PASS |
| 044 | Quantity increment/decrement | Increases or decreases the quantity of the membership | Quantity is successfully increased/decreased and shows in the grand total once added to cart | PASS | PASS | PASS |
| 044 | 'Add To Cart' button | Adds membership/s to shopping cart and lets user know with a toast message | Membership/s is successfully added to shopping cart, displaying a 'success' toast message to let the user know | PASS | PASS | PASS |
| 044 | 'Go To Secure Checkout' button | Toast message displays button that directs user to the Shopping Cart | Upon clicking the button in the success toast message, the user is successfully directed to the Shopping Cart | PASS | PASS | PASS |
| 044 | Quantity increment/decrement (Shopping Cart) | Increases or decreases the quantity of the membership and changes grand total price | Quantity and price are successfully increased/decreased | PASS | PASS | PASS |
| 044 | 'Secure Checkout' button | Directs user to the Checkout page | User is successfully directed to the Checkout page | PASS | PASS | PASS |
| 044 | Checkout Form Fields | All mandatory fields display feedback messages if no value is entered | Feedback message is displayed to let the user know that they must enter a value | PASS | PASS | PASS |
| 044 | 'Complete Payment' button | If payment functionality is successful, user is directed to the Confirmation page | User is successfully directed to the Confirmation page, displaying order details and a message letting the user know that a confirmation email has been sent | PASS | PASS | PASS |
| 044 | Stripe validation | Order is passed from checkout app to stripe | Stripe receives the order and payment request | PASS | PASS | PASS |

### Other Links

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 059 | Social Media Links | Social Media icons to perform as a link that directs user to the company's social media platforms | User is directed to the social media platform when relevant icon is clicked | PASS | PASS | PASS |

## Appearance Testing

The following tables show the appearance testing to check for any differences across different web browsers. This web app was developed on a Google Chrome browser, on a Windows Laptop. The app has also been regularly tested on Firefox and Microsoft Edge.

| Page | Google Chrome | Edge | Firefox |
| ---- | ------------- | ---- | ------- |
| Landing Page | No visible difference | No visible difference | h1 heading is less bold |
| Registration Page | No visible difference | No visible difference | No visible difference |
| Log-In Page | No visible difference | No visible difference | No visible difference |
| Profile Page | No visible difference | No visible difference | No visible difference |
| My Recipes Page | No visible difference | No visible difference | Placeholder text is lighter than other browsers. Recipes text is bolder
| Add a Recipe Page | No visible difference | No visible difference | No visible difference |
| Edit Recipe Page | No visible difference | No visible difference | Input text appears to be darker/bolder but less sharp
| Manage Categories Page | No visible difference | No visible difference | No visible difference |
| Edit Category Page | No visible difference | No visible difference | No visible difference |
| Add Category Page | No visible difference | No visible difference | No visible difference |

## Code Quality and Validation

Online tools have been used to validate the HTML, CSS, Python and JavaScript files to ensure they are free from errors, and comply with the latest standards. The results for these tests are shown below.

| Test | Process | Result | Image URL | Comment |
| ---- | ------- | ------ | --------- | ------- |
| HTML Validation | Copy page URI into W3C validator | 1 Warning - Section lacks headers | [HTML W3C Validator Results](/documentation/images/testing/htmlvalid.jpg) | The page has a heading. This is not a conventional website page layout of multiple headed sections |
| CSS Validation | Copy page URI into W3C validator | 7 Warnings - Related to Materialize CSS | [CSS W3C Validator Results](/documentation/images/testing/cssvalid.jpg) | The errors that have shown are related to the Materialize CSS that I have used. Layout or functionality of the app is not affected |
| Python Validation | Copy Python code into PEP8 validator | No issues | [Pep8 Validator Results](/documentation/images/testing/pep8.jpg)
| JavaScript Validation | Copy JavaScript code into JShint | Warnings | [JShint Validator Results](/documentation/images/testing/jshint.jpg) | Warning related to Materialize CSS code and ES6 versions. Web app not affected |

## Responsivity Testing

I have carried out continuous responsiveness testing, throughout building the project, to ensure the website functions on different devices and in both portrait and landscape orientation, using Google Devtools. The website was built and tested on a Windows 11 Lenovo Laptop. Other devices that the website has been tested on:

- Attached Dell monitor
- iPhone 12

![Mobile Responsivity](/documentation/images/testing/responsive1.jpg)

![Tablet Responsivity](/documentation/images/testing/responsive2.jpg)

![Mobile Responsivity](/documentation/images/testing/responsive3.jpg)

## Performance Testing

Further testing using the following tools:

- Google Lighthouse (Desktop)

![Performance Testing](/documentation/images/testing/performance.jpg)

| Page | Performance | Accessibility | Best Practices | SEO |
| ---- | ----------- | ------------- | -------------- | --- |
| Landing Page | 89% | 94% | 83% | 89% |
| Registration Page | 100% | 93% | 83% | 89% |
| Log-In Page | 100% | 93% | 83% | 89% |
| Profile Page | 100% | 90% | 83% | 89% |
| My Recipes Page | 95% | 85% | 83% | 80% |
| Add a Recipe Page | 100% | 84% | 83% | 89% |
| Edit Recipe Page | 100% | 84% | 83% | 89% |
| Manage Categories Page | 96% | 80% | 83% | 80% |
| Add a Category Page | 100% | 93% | 83% | 89% |
| Edit Category Page | 100% | 93% | 83% | 89% |

- Google Lighthouse (Mobile)

| Page | Performance | Accessibility | Best Practices | SEO |
| ---- | ----------- | ------------- | -------------- | --- |
| Landing Page | 73% | 90% | 83% | 91% |
| Registration Page | 97% | 93% | 83% | 91% |
| Log-In Page | 98% | 93% | 83% | 91% |
| Profile Page | 97% | 90% | 83% | 91% |
| My Recipes Page | 78% | 85% | 83% | 83% |
| Add a Recipe Page | 96% | 84% | 83% | 89% |
| Edit Recipe Page | 96% | 84% | 83% | 89% |
| Manage Categories Page | 73% | 80% | 80% | 83% |
| Add a Category Page | 97% | 93% | 83% | 91% |
| Edit Category Page | 96% | 93% | 83% | 91% |

## Security Testing

Testing security measures that are in place to improve user experience and confidentiality.

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 060 | Username Duplication | No username duplication allowed | Registration will check for username duplication. A flash message will warn the user if the username already exists | PASS | PASS | PASS |
| 061 | Password security | Password is hashed | The password is converted into a complicated string or an algorithm | PASS | PASS | PASS |
| 062 | Password confirmation | Checks for password match | When the password confirmation input matches the first password input, feedback validation is given and the user can register successfully | PASS | PASS | PASS |
| 063 | Restricted access | Users are only able to edit or delete their own recipe | The *edit* and *delete* buttons are only visible to the user who created the recipe | PASS | PASS | PASS |
| 064 | Admin access | Only the admin user can edit or delete categories | The *Manage Categories* link in the navbar is only visible to admin users | PASS | PASS | PASS |

## Additional Testing

I used the a11y Contrast Checker to test all colours throughout the project. As you can see there has been some problems detected regarding the grey/white contrast that runs throughout the website, as well as the pink/white that I used for the *Reset/Cancel* buttons. I am happy to leave these colours as they are as I want to create a soft, subtle look to the entire site. By changing this soft tone to something more contrasting and vibrant, I fear that the intended look will be lost. After further testing on different screens, I can confidently say that the grey text is easily read-able, and the buttons are highly visible, and are not at all lost in the  white background.

![Colour Contrast Checker](/documentation/images/testing/colour-contrast.jpg)

# Known Bugs & Fixes

| Issue # | Bug | Description | Solution |
| ------- | --- | ----------- | -------- |
| 1 | White-space in text areas | When clicking on the text area for the *Ingredients* and *Method* I noticed there was some white space, which affected the validation feedback when filling in the form. | I remembered seeing this on the Code Institute tutorials as this was an issue that came up during a walkthrough project. I was able to follow this advice and get rid of the whitespace by using the closing tag `</textarea>` on the same line of the last line of text.
| 2 | White-space on either side of Landing Page image (desktop only) | When viewing the web-app on a desktop, you can see there is a fair amount of white-space on either side of the image, as opposed to stretching across the entire screen. | No solution yet - I have researched on various forums and websites how to get rid of the unwanted white-space but have not yet found a solution that works as desired. I could inject the background image into the `<body>` element of the page,which will allow the image to fill the entire screen, however I don't want to use the background image across the entire site, only the landing page. |

[Back to README.md file](README.md)