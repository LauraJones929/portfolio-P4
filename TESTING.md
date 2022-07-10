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
| 002 | Memberships link | Directs user to Memberships page | Opens Membership page | PASS | PASS | PASS |
| 003 | Contact Us link | Directs user to Contact Us page | Opens the Contact Form | PASS | PASS | PASS |
| 004 | Memberships link on mobile nav | Directs user to Memberships page | Opens Membership page | PASS | PASS | PASS |
| 005 | Contact Us link on mobile nav | Directs user to Contact Us page | Opens the Contact Form | PASS | PASS | PASS |
| 006 | Sign-In link | Directs user to sign-in page | Opens Sign-In page | PASS | PASS | PASS |
| 007 | Sign-Up redirect link on Sign-In page | Directs user to Sign-Up page | Opens Sign-Up page | PASS | PASS | PASS |
| 008 | Sign-Up link | Directs user to Sign-Up page | Opens Sign-Up page | PASS | PASS | PASS |
| 009 | Sign-In redirect link on Sign-Up page | Directs user to Sign-In page | Opens Sign-In page | PASS | PASS | PASS |
| 010 | Forgot Password link | Directs user to Password Reset page | Opens Password Reset page | PASS | PASS | PASS |
| 011 | Shopping Cart link | Directs user to the Shopping Cart page | Opens Shopping Cart page | PASS | PASS | PASS |

### Sign-Up/Sign-In Testing

Testing the registration process for new users and the log-in process for returning users. The app should provide feedback to the user in cases where incorrect inputs are provided.

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 012 | Username input | Feedback when requirements not met | User is unable to progress further until requirements are met | PASS | PASS | PASS |
| 013 | Password input | Feedback when requirements not met | Input box turns red and tooltip provides feedback | PASS | PASS | PASS |
| 014 | Email confirmation | Feedback when email addresses do not match | User is unable to progress further until requirements are met | PASS | PASS | PASS |
| 015 | Password confirmation | Feedback when passwords do not match | User is unable to progress further until requirements are met | PASS | PASS | PASS |
| 016 | Email address already has account | Lets user know that the email address entered has already created an account | User is unable to progress further until requirements are met | PASS | PASS | PASS |
| 017 | Incorrect username | Inform user of a incorrect username OR password | Message letting user know that either an incorrect username or password has been entered | PASS | PASS | PASS |
| 018 | Incorrect password | Inform user of a incorrect username OR password | Message letting user know that either an incorrect username or password has been entered | PASS | PASS | PASS |

![Incorrect Username/Password](/documentation/images/testing/incorrect-pass.jpg)

![Requirements not met](/documentation/images/testing/feedback.jpg)

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 019 | Sign-In/Sign-In successful | User directed to Home page | Home page is loaded, displaying a successful toast message. | PASS | PASS | PASS |

![Toast Sign-in](/documentation/images/testing/sign-in-success.jpg)

### Memberships Filter & View (READ)

Testing the ability to view the memberships/products and filter by category. Clicking the 'Join Now' button should also direct the user to the Membership Details page which gives the user the option to add the membership to their cart.

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 020 | Navigate to Memberships page, viewing all memberships (navbar) | Direct user to Memberships page, showing all memberships | The Memberships page is loaded, displaying all membership cards. | PASS | PASS | PASS |
| 021 | Navigate to Memberships page, filtering 'HIIT Fitness' memberships (navbar) | Direct user to Memberships page, displaying memberships for 'HIIT Fitness' | The Memberships page is loaded, displaying 'HIIT Fitness' membership cards. | PASS | PASS | PASS |
| 022 | Navigate to Memberships page, filtering 'Strength & Conditioning' memberships (navbar) | Direct user to Memberships page, displaying memberships for 'Strength & Conditioning' | The Memberships page is loaded, displaying 'Strength & Conditioning' membership cards. | PASS | PASS | PASS |
| 023 | Navigate to Memberships page, filtering 'Boxing' memberships (navbar) | Direct user to Memberships page, displaying memberships for 'Boxing' | The Memberships page is loaded, displaying 'Boxing' membership cards. | PASS | PASS | PASS |
| 024 | Categories and Memberships organised & displayed | Memberships are organised by category | Memberships are displayed in order of category | PASS | PASS | PASS |

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
| 032 | Edit button | Direct user to Edit Membership form | Edit Edit Membership form is loaded | PASS | PASS | PASS |
| 033 | Existing data renders | Display existing membership data from the database onto the form | All of the existing data is loaded into the form fields | PASS | PASS | PASS |
| 034 | Edit Category name | Category name can be edited | Admin user can edit the category name | PASS | PASS | PASS |
| 035 | Edit Membership name | Membership name can be edited | Admin user can edit and delete the membership name | PASS | PASS | PASS |
| 036 | Edit Description | Description can be edited | Admin user can edit and delete the description | PASS | PASS | PASS |
| 037 | Edit Price | Price can be edited | Admin user can edit the membership price | PASS | PASS | PASS |
| 038 | 'Update Membership' button | Admin user is redirected to the Membership Details page | Upon completing the edit form and submitting, the admin user is successfully redirect to the specificied Membership Details page | PASS | PASS | PASS |
| 039 | Data Written to Django Admin | Confirm membership data is edited and written to Django Admin | Edited memberships appear in the Django Admin displaying their updated fields | PASS | PASS | PASS |
| 040 | Memberships page updated | Edited membership successfully renders on Memberships page | The edited membership renders as intended on the Memberships page | PASS | PASS | PASS |

### ADMIN ACCESS ONLY - Delete Membership (UPDATE)

Testing the ability to delete the diet memberships from the database.

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 041 | Delete Button | Deletes membership | Admin user can successfully delete a membership from the web app and the database | PASS | PASS | PASS |
| 042 | Redirect | Admin user is redirected to the Memberships page | Upon deleting the membership, the admin user is successfully redirected to the Memberships page, where the deleted membership is no longer displayed | PASS | PASS | PASS |

### Purchase a Membership

Testing the ability to purchase a membership by adding to the shopping cart and making a secure online payment via Stripe.

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 043 | 'Join Now' button | Directs user to the Membership Detils page of chosen membership | User is successfully directed to the Membership Detail | PASS | PASS | PASS |
| 044 | Quantity increment/decrement | Increases or decreases the quantity of the membership | Quantity is successfully increased/decreased and shows in the grand total once added to cart | PASS | PASS | PASS |
| 045 | 'Add To Cart' button | Adds membership/s to shopping cart and lets user know with a toast message | Membership/s is successfully added to shopping cart, displaying a 'success' toast message to let the user know | PASS | PASS | PASS |
| 046 | 'Go To Secure Checkout' button | Toast message displays button that directs user to the Shopping Cart | Upon clicking the button in the success toast message, the user is successfully directed to the Shopping Cart | PASS | PASS | PASS |
| 047 | Quantity increment/decrement (Shopping Cart) | Increases or decreases the quantity of the membership and changes grand total price | Quantity and price are successfully increased/decreased | PASS | PASS | PASS |
| 048 | 'Secure Checkout' button | Directs user to the Checkout page | User is successfully directed to the Checkout page | PASS | PASS | PASS |
| 049 | Checkout Form Fields | All mandatory fields display feedback messages if no value is entered | Feedback message is displayed to let the user know that they must enter a value | PASS | PASS | PASS |
| 050 | 'Complete Payment' button | If payment functionality is successful, user is directed to the Confirmation page | User is successfully directed to the Confirmation page, displaying order details and a message letting the user know that a confirmation email has been sent | PASS | PASS | PASS |
| 051 | Stripe validation | Order is passed from checkout app to stripe | Stripe receives the order and payment request | PASS | PASS | PASS |

### Other Links

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 052 | Social Media Links | Social Media icons to perform as a link that directs user to the company's social media platforms | User is directed to the social media platform when relevant icon is clicked | PASS | PASS | PASS |

## Appearance Testing

The following tables show the appearance testing to check for any differences across different web browsers. This web app was developed on a Google Chrome browser, on a Windows Laptop. The app has also been regularly tested on Firefox and Microsoft Edge.

| Page | Google Chrome | Edge | Firefox |
| ---- | ------------- | ---- | ------- |
| Landing Page | No visible difference | No visible difference | No visible difference |
| Sign-Up Page | No visible difference | No visible difference | No visible difference |
| Sign-In Page | No visible difference | No visible difference | No visible difference |
| My Memberships Page | No visible difference | No visible difference | No visible difference |
| Memberships Page | No visible difference | No visible difference | No visible difference |
| Contact Us Page | No visible difference | No visible difference | No visible difference |
| Membership Details Page | No visible difference | No visible difference | No visible difference |
| Shopping Cart Page | No visible difference | No visible difference | No visible difference |
| Checkout Page | No visible difference | No visible difference | No visible difference |
| Gym Management Page | No visible difference | No visible difference | No visible difference |

## Code Quality and Validation

Online tools have been used to validate the HTML, CSS, Python and JavaScript files to ensure they are free from errors, and comply with the latest standards. The results for these tests are shown below.

| Test | Process | Result | Image URL | Comment |
| ---- | ------- | ------ | --------- | ------- |
| HTML Validation | Copy page URI into W3C validator | 1 Error - 2 Warnings - Section lacks headers | [HTML W3C Validator Results](/documentation/images/testing/html-check.jpg) | After changing the ID to a Class, this returned more errors as the aria-labelledby tag would not register the class attribute. I have left this error as it is, as it does not seem to have effected the layout or structure of the page. |
| CSS Validation | Copy page URI into W3C validator | No Errors or Warnings detected | [CSS W3C Validator Results](/documentation/images/testing/css-check.jpg) |  |
| Python Validation | Copy Python code into PEP8 validator | Some Errors |  [Pep8 Validator Website](http://pep8online.com/) | Some issues relating to lines being too long however some of these were best left alone as they created further issues when breaking up lines which effected the functionality |
| JavaScript Validation | Copy JavaScript code into JShint | Warnings | [JShint Validator Results](/documentation/images/testing/jshint.jpg) | Warning related to ES6 versions. Web app not affected |

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

![Performance Testing](/documentation/images/testing/lighthouse/landing.jpg)

| Page | Performance | Accessibility | Best Practices | SEO |
| ---- | ----------- | ------------- | -------------- | --- |
| Landing Page | 98% | 80% | 92% | 78% |
| Sign-Up Page | 98% | 83% | 92% | 89% |
| Sign-In Page | 99% | 83% | 92% | 89% |
| Memberships Page | 99% | 80% | 92% | 78% |
| Contact Us Page | 99% | 83% | 92% | 78% |
| Gym Management Page | 98% | 75% | 92% | 78% |
| My Memberships Page | 93% | 85% | 92% | 78% |
| Membership Details Page | 96% | 75% | 92% | 80% |
| Shopping Cart Page | 98% | 68% | 92% | 78% |
| Checkout Page | 93% | 87% | 92% | 78% |

- Google Lighthouse (Mobile)

| Page | Performance | Accessibility | Best Practices | SEO |
| ---- | ----------- | ------------- | -------------- | --- |
| Landing Page | 81% | 82% | 92% | 82% |
| Sign-Up Page | 88% | 83% | 92% | 91% |
| Sign-In Page | 88% | 83% | 92% | 91% |
| Memberships Page | 83% | 82% | 92% | 91% |
| Contact Us Page | 87% | 83% | 92% | 91% |
| Gym Management Page | 84% | 75% | 92% | 82% |
| My Memberships Page | 82% | 85% | 92% | 82% |
| Membership Details Page | 84% | 75% | 92% | 82% |
| Shopping Cart Page | 82% | 68% | 92% | 72% |
| Checkout Page | 76% | 87% | 92% | 82% |

## Security Testing

Testing security measures that are in place to improve user experience and confidentiality.

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 060 | Username Duplication | No username duplication allowed | Registration will check for username duplication. A flash message will warn the user if the username already exists | PASS | PASS | PASS |
| 062 | Password confirmation | Checks for password match | When the password confirmation input matches the first password input, feedback validation is given and the user can register successfully | PASS | PASS | PASS |
| 064 | Admin access | Only the admin user can add, edit or delete memberships | The *Gym Management* link in the navbar is only visible to admin users | PASS | PASS | PASS |

## Additional Testing

I used the a11y Contrast Checker to test all colours throughout the project. As you can see there were no issues detected.

![Colour Contrast Checker](/documentation/images/testing/colour-checker1.jpg)
![Colour Contrast Checker](/documentation/images/testing/colour-checker2.jpg)

# Known Bugs & Fixes

| Issue # | Bug | Description | Solution |
| ------- | --- | ----------- | -------- |
| 1 |  |  |
| 2 |  |  |

[Back to README.md file](README.md)