# Harmonia Hall

<!-- Table of Contents -->
<details>
  <summary>Index</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#overview">Overview</a></li>
        <li><a href="#rationale">Rationale</a></li>
        <li><a href="#mvp-features">MVP Features</a></li>
        <li><a href="#desktop-appearance">Desktop Appearance</a></li>
        <li><a href="#tablet-appearance">Tablet Appearance</a></li>
        <li><a href="#mobile-appearance">Mobile Appearance</a></li>
      </ul>
    </li>
    <li>
      <a href="#ux-design">UX Design</a>
      <ul>
        <li><a href="#wireframes">Wireframes</a></li>
        <li><a href="#database-structure-erd">Database Structure (ERD)</a></li>
      </ul>
    </li>
    <li>
      <a href="#user-stories">User Stories</a>
      <ul>
        <li><a href="#must-haves">Must Have's</a></li>
        <li><a href="#should-haves">Should Have's</a></li>
        <li><a href="#could-haves">Could Have's</a></li>
        <li><a href="#wont-haves">Won't Have's</a></li>
        <li><a href="#project-board">Project Board</a></li>
        <li><a href="#outcomes">Outcomes</a></li>
      </ul>
    </li>
    <li><a href="#features">Features</a></li>
    <li><a href="#bugs">Bugs</a></li>
    <li><a href="#testing">Testing</a></li>
      <ul>
        <li><a href="#manual-testing">Manual Testing</a></li>
        <li><a href="#user-stories-testing">User Stories Testing</a></li>
        <li><a href="#lighthouse-testing">Lighthouse Testing</a></li>
        <li><a href="#responsive-testing">Responsive Testing</a></li>
        <li><a href="#validator-testing">Validator Testing</a></li>
      </ul>
    </li>
    <li><a href="#use-of-ai">Use of AI</a></li>
    <li><a href="#deployment">Deployment</a></li>
    <li><a href="#future-development">Future Development</a></li>
    <li><a href="#credits">Credits</a></li>
  </ol>
</details>

<!-- About the Project -->
## About the Project

![Am I Responsive](/images/responsive.png)
*Harmonia Hall site on multiple device sizes, using the 'Am I Responsive?' tool*
<!-- Overview of project -->
### Overview
This project is a full-stack web application built using the Django framework. It uses Python, HTML and CSS to create a dynamic and responsive site for a fictious concert venue called Harmonia Hall. The application allows users to view upcoming events, book tickets, and manage their bookings. It also includes user authentication features, enabling users to create accounts, log in, and log out securely.

You can visit the deployed site at: [Harmonia Hall](https://harmonia-hall-b317b69502c7.herokuapp.com/)

### Rationale
The aim of this project is to provide a solution to the following problem faced by the venue, Harmonia Hall, and its event attendees:

"Harmonia Hall and its event attendees currently lack an efficient, centralised platform to manage event bookings and capacity. The venue struggles to prevent overbooking, track event capacity accurately, and manage multiple bookings, while attendees face difficulties in discovering upcoming events, making reservations, and managing their bookings effectively. This fragmented and manual process results in capacity management issues, double bookings, missed events, and a poor user experience for both venue operators and customers seeking to attend live music events."

This web application addresses these challenges by providing a comprehensive, user-friendly booking platform that streamlines the entire event management process. The platform enables attendees to easily discover upcoming events, view real-time availability, and securely reserve tickets with capacity tracking to prevent overbooking. Built-in booking management features allow users to view, modify, or cancel their reservations at any time, while administrators benefit from a robust backend system to create, manage, and monitor events and bookings. By implementing real-time capacity validation, enforcing one booking per user per event, and providing clear error messaging and confirmation feedback, the application eliminates double bookings, ensures accurate capacity management, and delivers a seamless, trustworthy booking experience for both venue operators and customers.

With this in mind, this application has been designed for two primary user groups. First, it serves music enthusiasts and event-goers who seek a convenient, reliable platform to discover upcoming live music and other events, browse event details, and securely book tickets without the fear of overbooking or capacity conflicts. Second, it caters to venue administrators and staff at Harmonia Hall, who require efficient tools to create and manage events, track real-time capacity and bookings, and maintain accurate event listings. Whether its users are looking to attend their next favorite concert or manage a busy event venue, this application provides an intuitive, reliable solution that enhances the overall event experience for both attendees and venue operators alike.

### MVP Features
The MVP (minimum viable product) for this project includes the following core features:
- User Registration and Authentication: Allow users to create accounts, log in, and log out securely.
- Event Listings: Display a list of upcoming events with details such as date, time, location, and availability.
- Event Details: Provide detailed information about each event, including descriptions, images, and current capacity.
- Booking System: Enable logged-in users to create, view, update, and cancel bookings for events, with real-time capacity validation to prevent overbooking.


<!-- Deployed homepage screenshot examples of site -->
### Below are screenshots of the deployed site on different devices:
### Desktop Appearance
![Desktop Appearance](/images/desktop.png)
*screenshot of deployed site on Desktop*
### Tablet Appearance
![Tablet Appearance](/images/tablet.png)
*screenshot of deployed site on Tablet*
### Mobile Appearance
![Mobile Appearance](/images/mobile.png)
*screenshot of deployed site on Mobile*

<!-- Overview of UX Design of project -->
## UX Design
For the social media icons, I used [**Font Awesome**](https://fontawesome.com).

For the colour scheme, I used [**Colormind**](http://colormind.io) to generate a palette based on images of concert venues and music events.
![Colormind](/images/colormind-palette.png)
*screenshot of colour palette generated by Colormind*

For the fonts, I used Google Fonts 'Lato' font, and Bootstrap's default fonts, with Lato being used specifically for the footer.

### Wireframes
The following wireframes were created for different sized devices (mobile, tablet and desktop) to help visualise how the site would look on different devices.

I used [**Balsamiq**](https://balsamiq.com) to create the following wireframe diagrams.

<details>
<summary><strong>Wireframe Diagrams</strong></summary>

#### Home Page
![Home page wireframe](/images/wireframe-home.png)
*Home page with featured upcoming events*

#### What's On Page
![What's on page wireframe](/images/wireframe-whats-on.png)
*What's On page with events listings*

#### Sign In Page
![Sign in page wireframe](/images/wireframe-sign-in.png)
*User sign in with authentication*

#### Bookings Page
![Bookings page wireframe](/images/wireframe-bookings.png)
*User's event bookings management*

#### About Page
![about page wireframe](/images/wireframe-about.png)
*Venue information and details*

#### Contact Page
![Contact page wireframe](/images/wireframe-contact.png)
*Contact page for information and inquiries*

</details>

### Database Structure (ERD)
The database structure for this project is based around three main models: Event, Booking, and User (using Django's built-in User model).The main entities and their relationships are as follows:
- Event: Represents an event at the concert venue, with attributes such as title, date, time, venue, price, capacity, and description.
- Booking: Represents a booking made by a user for a specific event, with attributes such as user (foreign key to User), event (foreign key to Event), number of tickets, and booking date.
- User: Represents a user of the site, with attributes such as username, email, and password (handled by Django's Allauth authentication system).

This is illustrated in the Entity Relationship Diagram (ERD) below, created using [**dbdiagram.io**](https://dbdiagram.io).

![ERD](/images/erd.png)
*Entity Relationship Diagram (ERD) from [dbdiagram.io](https://dbdiagram.io) showing database structure*

The ERD shows the relationships between the models:
- A User can have multiple Bookings (one-to-many relationship).
- An Event can have multiple Bookings (one-to-many relationship).
- A Booking is associated with one User and one Event (many-to-one relationship).

<!-- Overview of User Stories project -->
## User Stories

<details id="must-haves">
<summary><strong>Must Have's</strong></summary>

#### User Story: User Registration
As a **site visitor**, I am able to **create an account**, so that I can **book tickets for events**.
Acceptance criteria:
- Visitors are able to register an account with valid details, which creates a new account upon successful registration.
- The site redirects the user after a successful registration.
- When invalid details are used, the system prevents the account from being created.
#### User Story: User Log in/Log out
As a **site user**, I can **log in and out securely**, so that I can **access my bookings/personal details, and keep them secure on shared devices**.
Acceptance criteria:
- The site authenticates users with their valid credentials.
- Access is denied when invalid login details are used.
- The site correctly logs out a user from their account following a logout.
- Users are redirected accordingly after a successful log in and log out.
#### User Story: View Upcoming Events
As a **site visitor** I can **view a list of upcoming events**, so that I can **see what events are available**.
Acceptance criteria:
- The site displays a list of upcoming events, including dates and times.
- The site will hide past events from the list of upcoming events.
#### User Story: View Event Details
As a **site visitor**, I can **view event details** so that I can **decide wether or not I want to attend**.
Acceptance criteria:
- The site displays full details for a selected event.
- The site shows the current availability for the event.
#### User Story: Create Booking
As a **site user**, I can **reserve a ticket for an event** so that I can **secure my place at it**.
Acceptance criteria:
- The site allows logged-in users to create a booking, which is then assigned to the authenticated user.
- The booking is confirmed when capacity is available.
- The site updates the available capacity after booking.
#### User Story: View My Bookings
As a **site user**, I can **view all of my bookings** so that I can **keep track of upcoming events I am attending**.
Acceptance criteria:
- The site displays only the authenticated user's bookings.
- The site shows the booking details and status.
#### User Story: Update Bookings
As a **site user**, I can **update an existing booking** so that I can **change the number of tickets if needed**.
Acceptance criteria:
- Users are able to update existing bookings.
- The site validates the updated booking details.
- Capacity limits are enforced when updating bookings.
#### User Story: Cancel Bookings
As a **site user**, I can **delete a booking** so that I can **free up tickets I no longer need**.
Acceptance criteria:
- Users are able to successfully cancel their bookings and updates the status/removes the booking.
- The capacity limits for the event are updated after the cancellation.
#### User Story: Prevent Booking
As a **site user**, I want **the system to prevent overbooking of events**, so that **I can trust that my reservation is valid**.
Acceptance criteria:
- The site prevents bookings that exceed event capacity.
- The site displays an error message when the capacity is exceeded.
#### User Story: Data Privacy
As a **site user**, I want **my bookings to be associated only with my account** so that **I can be confident my data is private**.
Acceptance criteria:
- The site restricts booking access to the booking owner, blocking others from access to the booking data.
#### User Story: Repsonsive Design
As a **site user** the site **adapts to work well on a range of different devices** so that **I can navigate the site quickly and comfortably on all of my devices**.
Acceptance criteria:
- The site is responsive and adapts automatically to the different media screen sizes using break points and media queries.
#### User Story: Accessibility
As a **disabled site user** I can **fully access the site using accessibility features** so that **I can use it effectively**.
Acceptance criteria:
- The site meets the WCAG standards for colour contrast, text size and keyboard navigation.
- Form fields have suitable aria labels.
- Error messages are clear and descriptive.

</details>

<details id="should-haves">
<summary><strong>Should Have's</strong></summary>

#### User Story: Profile Management
As a **site user**, I can **view my profile information** so that **I can confirm my details are correct**.
Acceptance criteria:
- Users are able to view their profile information.
- Users are not able to view other user's profiles and information.
#### User Story: Edit Profile
As a **site user**, I can **edit my profile details** so that **I can make changes to keep my account information up to date**.
Acceptance criteria:
- The site allows users to edit their profile details.
- The site validates updated profile information and saves the validated information successfully.
#### User Story: Manage Events
As a **site admin**, I can **create and manage events** so that **I can keep the event listings accurate and up to date**.
Acceptance criteria:
- Administrators are able to create, view, update and delete events.
#### User Story: Password Reset
As a **site user** I want to be able to **reset my password** so that I can**regain access if I forget my credentials**.
Acceptance criteria:
- Users are allowed to request a password reset using their email, which sends reset instructions to this email.
- Following these instructions, users are able to assign a new password successfully.
#### User Story: About Page
As a **site visitor**, I want to **be able find out information about the venue and site** so that **I can be confident in booking a ticket for an event held here**.
Acceptance criteria:
- A user is able to find out suitable information and pictures of the venue that match what would be expected.
#### User Story: View Event Bookings
As a **site admin**, I can **view all bookings for a concert** so that **I can monitor attendance and capacity**.
Acceptance criteria:
- The site allows admins to view bookings for an event, including the total number of bookings per event.
</details>

<details id="could-haves">
<summary><strong>Could Have's</strong></summary>

#### User Story: Contact Us
As a **site visitor**, I can **find relevant contact information, including a contact form** so that **I can get in touch about more specific queries relating to the events**.
Acceptance criteria:
- A user can easily navigate to a contact page.
- The contact page includes relevant contact information.
- The contact page has a contact form that can be filled out by the site visitor.
#### User Story: Search for Events
As a **site user**, I can **search for events with keywords** so that **I can find the events I am looking for**.
Acceptance criteria:
- A user is able to easily navigate to a search bar.
- Entering keywords into the search will bring up corresponding/relevant events.
</details>

<details id="wont-haves">
<summary><strong>Won't Have's</strong></summary>

There were no "won't have" user stories for this project.

</details>

### Project Board
![GitHub Project board](/images/project-board.png)
*Screenshot of the project board on GitHub*
The project board for this project can be found here: https://github.com/users/jonniecumming/projects/12/views/1


### Outcomes
- Must Haves: All completed successfully, with thorough testing to ensure functionality and usability, reaching the MVP.
- Should Haves: The Manage Events and About Page user stories were completed successfully. The Profile Management and Edit Profile user stories were not implemented due to time constraints.
- Could Haves and Won't Haves: These user stories were not implemented as the should haves were prioritised, and were not fully completed.

<!-- Overview of features of the project -->
## Features

<details>
<summary><strong>Feature Details</strong></summary>

### Home Page
![home page](/images/home.png)
*screenshot of the home page*

The home page displays a welcome message to Harmonia Hall, along with a carousel of featured upcoming events and a call-to-action button that directs users to explore all upcoming events via the What's On page.
### What's On Page
![what's on page](/images/whats-on.png)
*screenshot of the what's on page*

The What's On page displays a list of upcoming events in a card layout, with pagination controls to navigate between pages of 6 events at a time. Each event card includes an image, title, date, time, venue, price, and a link to view more details about the event.
### About Page
![about page](/images/about.png)
*screenshot of the about page*

The About page provides information about Harmonia Hall, including its history, mission, and facilities. It also includes images of the venue to give users a visual representation of the space.
### Event Detail Page
![event detail page](/images/event-detail.png)
*screenshot of the event detail page*

The Event Detail page displays comprehensive information about a specific event, including its title, date, time, venue, price, capacity, description, and an event image. It also shows the current availability for the event and provides a booking form for logged-in users to reserve tickets, or a prompt to log in/register for non-authenticated users.
### Sign In
![sign in page](/images/sign-in.png)
*screenshot of the sign in page*

The sign in page allows users to log in to their accounts using their credentials. It includes fields for username/email and password, along with a submit button to authenticate the user.
### Sign Out
![sign out page](/images/sign-out.png)
*screenshot of the sign out page*

The sign out page allows the user to sign out of their account, and notifies the user they have been successfully logged out of their account following a logout.
### Booking Form Page
![booking form page](/images/booking-form.png)
*screenshot of the booking form page*

The booking form page allows logged-in users to create a booking for a specific event. It includes fields for the number of tickets to book, along with a submit button to confirm the booking.
### View Bookings Page
![View bookings page](/images/view-bookings.png)
*screenshot of the view bookings page*

The bookings page displays a list of the authenticated user's bookings, including details such as event title, date, time, number of tickets, and booking status. It also provides options to edit or cancel each booking.
### Edit Booking Page
![edit booking page](/images/edit-booking.png)
*screenshot of the edit booking page*

The edit booking page allows users to modify the details of an existing booking, such as the number of tickets. It includes fields pre-populated with the current booking information and a submit button to save changes.
### Navigation Bar
![navigation bar](/images/navbar.png)
*screenshot of the navigation bar*

The navigation bar is fixed at the top of the page that provides links to the main sections of the site, including Home, What's On, About, Register, Login/Logout, and Bookings. It also includes the site logo and is responsive to different screen sizes, with a burger menu for mobile devices.

### Footer
![footer](/images/footer.png)
*screenshot of the footer*

The footer includes social media icons that link to various social media platforms. It also contains copyright information and is styled to match the overall design of the site.
### Django Admin Login
![Django admin login](/images/django-admin-login.png)
*Admin login page screenshot*

The Django admin login page allows administrators to log in to the backend of the site using their admin credentials.
### Django Admin
![Django admin](/images/django-admin.png)
*Django admin dashboard screenshot*

The Django admin dashboard provides administrators with an overview of the site's data, including events, bookings, and users. It allows admins to manage and monitor the site's content and user activity.
### Django Admin Event Management
![Django admin event management](/images/django-admin-events.png)
*Django admin event management screenshot*

The Django admin event management page allows administrators to create, view, update, and delete events. It provides a user-friendly interface for managing event details, including title, date, time, venue, price, capacity, and description.

### Differences Between Wireframes and End Product

The main differences between the end product and the wireframes are within the home page, What's On page and the lack of a contact page.
I decided to simplify the Home page by removing the featured events as a grid, and instead using a carousel to highlight upcoming events. This was to create a cleaner look and feel, and to make it easier for users to get an overview of the events available. Linking to this change, I implemented the card layout featured on the Home page wireframe, into the What's On page. This allowed for a more visual representation of the events, making it easier for users to browse and select events of interest. I would like to make the date element more prominent in future iterations, as I feel this is an important piece of information for users when browsing events.
Finally, I decided not to prioritise the contact page, as I felt that the About page provided sufficient information about the venue. However, this is something that I would liked to be added in the future to enhance the user experience further. I have included a section in the Future Development part of this README to outline more features and functionality I would like to add.

</details>

<!-- Overview of bugs and solutions -->
## Bugs

<details>
<summary><strong>Bug Details</strong></summary>

### iPhone Footer Issue 
![edit booking page](/images/iphone-footer.png)
*screenshot of iPhone 11 Pro footer issue*

When viewing pages on an iPhone 11 Pro, the footer bar was not displaying correctly, and was floating above the bottom of the viewport, with white space below it. To try to fix this issue, I asked other developers and copilot for help after changing some CSS properties. The suggestions were similar, such as adding various CSS properties to the footer element. After testing different combinations, I looked online for similar issues, and found that it was likley due to an ios Safari webkit bug. I decided to compromise and add CSS to minus the footer height from the bottom of the body element, which fixed the issue to some extent. However, there was still a small amount of white space below the footer. Because of this, the issue is not fully resolved, but it was much improved.

### Notification Messages Issue
![notification messages issue](/images/notifications-bug.png)
*screenshot of notification messages issue*

When logging in and out, specifically on the admin pannel, the notficiations were cumlative and stacking ontop of each other. This was due to the way the messages framework in Django works, where messages are stored in the session and displayed on the next page load. To fix this issue, I asked Claude to help me, which suggested I added code to the base.html template to clear the messages after they have been displayed. This ensured that only one message is shown at a time, and prevents them from stacking up.

### Slug Issue
![slug issue](/images/slug-bug.png)
*screenshot of slug issue*

I added some code to automatically generate slugs for events based on their titles. However, I found that when submitting the event form in the admin pannel, the slug field was not being populated correctly, resulting in an error when trying to save the event. To fix this issue, I asked Claude to look at my event model and suggest a solution. Claude pointed out I had missed some asterisks in the save method when calling the super() function. After correcting this, the slug field was populated correctly when saving events.


</details>

<!-- Overview of testing done -->
## Testing


<details id="manual-testing">
<summary><strong>Manual Testing</strong></summary>

### Manual Testing
I completed manual testing throughout the development process, ensuring that all features and functionality worked as intended. I tested the navigation bar links, forms, and booking system to ensure that they were functioning correctly. I also tested the site on an iPhone 11 Pro, using Safari, to ensure that the site was responsive and worked well on mobile devices.

Navigation bar testing:
| Test | Expected Result | Pass/Fail |
|--- |--- |--- |
| 'Home' page link | link redirects to Home page | Pass |
| 'Home' page link (title image) | link redirects to Home page | Pass |
| 'What's On' page link | link redirects to What's On page | Pass |
| 'About' page link | link redirects to About page | Pass |
| 'Register' page link | link redirects to Register page | Pass |
| 'Login' page link | link redirects to Login page | Pass |
| 'Logout' page link | link redirects to Logout page | Pass |
| 'Bookings' page link | link redirects to Bookings page | Pass |

Footer testing:
| Test | Expected Result | Pass/Fail |
|--- |--- |--- |
| Facebook icon link | link redirects to Facebook page | Pass |
| Twitter (X) icon link | link redirects to Twitter page | Pass |
| Instagram icon link | link redirects to Instagram page | Pass |
| Youtube icon link | link redirects to Youtube page | Pass |

Page testing:
| Test | Expected Result | Pass/Fail |
|--- |--- |--- |
| Home Page | Page loads | Pass |
| What's On Page | Page loads | Pass |
| About Page | Page loads | Pass |
| Register Page | Page loads | Pass |
| Login Page | Page loads | Pass |
| Logout Page | Page loads | Pass |
| Bookings Page | Page loads | Pass |
| Event Detail Page | Page loads | Pass |
| Booking Form Page | Page loads | Pass |
| Edit Booking Page | Page loads | Pass |


</details>

<details id="user-stories-testing">
<summary><strong>User Stories Testing</strong></summary>

### User Stories Testing
I tested each user story to ensure that the acceptance criteria were met. This included testing user registration, login/logout, viewing upcoming events, viewing event details, creating bookings, viewing bookings, updating bookings and canceling bookings. I also tested the capacity validation to ensure that overbooking was prevented.

| User Story | Expected Result | Pass/Fail |
|--- |--- |--- |
| User Registration | Account created with valid details, redirected, error message for invalid details | Pass
| User Log in/Log out | Authenticated with valid credentials, access denied for invalid details, redirected after log in/out | Pass |
| View Upcoming Events | List of upcoming events displayed, past events hidden | Pass |
| View Event Details | Full details for selected event displayed, current availability shown | Pass |
| Create Booking | Booking created for logged-in users, confirmed when capacity available, capacity updated | | Pass |
| View My Bookings | Only authenticated user's bookings displayed, booking details and status shown | Pass |
| Update Bookings | Existing bookings updated, validated, capacity limits enforced | Pass |
| Cancel Bookings | Bookings successfully cancelled, capacity limits updated | Pass |
| Prevent Booking | Bookings exceeding event capacity prevented, error message displayed | Pass |
| Data Privacy | Booking access restricted to booking owner | Pass |
| Repsonsive Design | Site responsive and adapts to different screen sizes | Pass |
| Accessibility | Meets WCAG standards, form fields have aria labels, clear error messages | Pass |
| Manage Events | Admins can create, view, update and delete events | Pass |
| About Page | Venue information and pictures displayed | Pass |
| View Event Bookings | Admins can view bookings for an event, including total number of bookings per event | Pass |

</details>
</details>

<details id="lighthouse-testing">
<summary><strong>Lighthouse Testing</strong></summary>

### Lighthouse Testing
![Lighthouse Report](/images/lighthouse-report.png)
*Screenshot of Lighthouse report showing scores for performance, accessibility, best practices, and SEO*
![Cloudinary Cookies](/images/cloudinary-cookies.png)
*Screenshot showing 3rd party cookies issues due to Cloudinary in Lighthouse report*

</details>

<details id="responsive-testing">
<summary><strong>Responsive Testing</strong></summary>

### Responsive Testing
I tested the responsiveness of the site constantly throughout the development process, using both browser developer tools and real devices such as my iPhone and iPad. I ensured that the layout and functionality of the site adapted correctly to different screen sizes and orientations. When there were issues, I made sure to address them promptly, using media queries and Bootstrap to ensure a consistent user experience across all devices.

</details>

<details id="validator-testing">
<summary><strong>Validator Testing</strong></summary>

### Validator Testing
![W3C HTML Validation](/images/w3c-html-validation.png)
*Screenshot of passing W3C HTML validation*

The HTML code for the site was validated using the W3C Markup Validation Service. Minor errors such as heading issues, were addressed and corrected to ensure compliance with HTML standards.
#### W3C CSS Validation

![W3C CSS Validation](/images/w3c-css-validation.png)
*Screenshot of passing W3C CSS validation*

The CSS code for the site was validated using the W3C CSS Validation Service. No errors were found during this validation process.

#### CI Linter PEP8 Validation
![CI Linter PEP8 Validation](/images/ci-linter-validation.png)
*Screenshot of passing CI Linter PEP8 validation*

On validating my Python code using PEP8 standards, I realised that I had issues with my line lengths exceeding the recommended 79 characters. This was due to my linter being set to a different line length limit. I addressed this by adjusting my linter settings to match PEP8 standards, then subsequently, refactoring my code to ensure compliance with the 79 character limit. This involved breaking up longer lines of code into multiple lines, and ensuring that my code was properly indented and formatted.

I did not use any custom JavaScript in this project, so I felt there was no need to validate any JavaScript code.

</details>

<!-- Overview of AI use within project -->
## Use of AI

During this project, AI was utilised in a few ways. Initially, I wanted to use AI to help me plan out certain aspects of the project, such as the user stories and features. I found this to be a useful starting point, as it helped me to think about what I wanted to achieve with the project, and how I could break it down into manageable parts. However, I made sure that I changed and refined the suggestions so that they fit my specific project needs, rather than just accepting them as they were.

For code generation, I picked Claude as my preferred AI tool. From what I understand and have experienced so far, I found Claude to be particularly good at understanding the context of my project, and providing the most relevant suggestions.

I used it to suggest how it could help with certain functions and methods. I wanted to make sure that for every use of AI, I reviewed the code thoroughly to ensure it made sense to me, and that it was keeping what I wanted to achieve in mind. 

I also used Claude to help with debugging certain issues I was having. When doing this, I made sure to understand what the suggestions were doing, and why they would help solve the issue. I would also make sure to challenge the suggestions if I felt they were not correct, which on a number of occasions they were not, despite my careful and descriptive prompting. One particular area that Claude helped in this way, was with booking capacity validation, which was a tricky area to get right. As I primarily used Claude as my client, I created a claude.md file in the root of my project to follow Django best practices. This helped to ensure that the suggestions I received about the Django framework were in line with best practices.

I also used AI to help with writing content for the site, such as the About page text. Again, I made sure to review and edit the content to ensure it fit my specific needs, and that it was accurate and relevant to the project. Seperately, I used AI to generate the logo for the site, based on my description of what I wanted it to look like, what the site was about, and various style preferences I wantd it to match.

<!-- Overview of How the project was deployed -->
## Deployment
The site was deployed to Heroku from the main branch of my GitHub repository. Below are the steps I took to deploy the site:

1. I navigated to my Heroku account and created a new app.
2. I gave the app an appropriate and unique name and selected the region closest to me (Europe).
3. In the "Deploy" tab, I connected my GitHub repository to Heroku by searching for the repository name and clicking "Connect".
4. I then went to the "Settings" tab and clicked on "Reveal Config Vars".
5. I added the necessary config vars, such as my `SECRET_KEY`, `DATABASE_URL`, `CLOUDINARY_URL`, as these environment variables are required for the app to run correctly.
6. Next, I went back to the "Deploy" tab, selected the main branch, and deployed the app by clicking on "Deploy Branch".
7. Once the deployment was complete, I navigated to the "Overview" tab and clicked on "Open App" to view my live site.
![Heroku Application Information](/images/heroku-app-info.png)
*Screenshot of Heroku application information page*
![Heroku Deployment](/images/heroku-deployment.png)
*Screenshot of successful Heroku deployment page*

Here is the link to the deployed site: [Harmonia Hall on Heroku](https://harmonia-hall-b317b69502c7.herokuapp.com/)

<!-- Future development -->
## Future Development
Some features that could be added in the future to enhance the functionality and user experience of the web application include:

- Add more Booking options, e.g for children/over 65’s/disability spaces
- Interactive JavaScript seat selection for relevant concerts
- Add 'How to Find Us/Plan your visit' page with map integration
- Add more descriptive data to each event, i.e. genre, to allow for filtering functionality on What’s On page
- Add News/Updates page for venue announcements, with newsletter sign-up
- Add site search feature for easier event discovery
- Add Calendar view to What’s On page
- Add Shopping Cart to allow for subtotals, multiple bookings at once
- Implement user profile management (view/edit profile)
- Implement admin profile management (view/edit profile)
- Add user reviews/ratings for events
- Add social media sharing functionality for events
- Implement email notifications for booking confirmations and reminders
- Integrate payment functionality

<!-- Credits for project -->
## Credits

### Code

For this project, I used the following libraries and frameworks:
- Django: Python framework for building web applications.
- Bootstrap: A front-end framework for building responsive, mobile-first websites using HTML, CSS, and JavaScript.
- Font Awesome: A library of icons and social logos for use in web projects.
- Cloudinary: A cloud-based service for managing images and videos, used here for storing and serving event image files.
- Django Allauth: An integrated set of Django applications addressing authentication, registration and account management.
- Psycopg2: Used for connecting Django to a PostgreSQL database, hosted by Code Institute.
- GitHub: For code repository hosting and project board management.
- Heroku: Cloud platform for deploying and hosting the web application.

### Content
- Text content on the website is a mixture of original writing, variations on existing content from similar sites and AI-assisted text generation.

### Media
The media used in this project were in two distinct categories: the About page images (including interior and exterior shots of a concert venue) These images were sourced from:
- Image sources: Unsplash, and are free to use under the Unsplash license.
- Event images: These were all images taken from various event listing sites. As this is a demo site, and the events are fictitious, I felt this was acceptable for the purposes of demonstrating the functionality of the site. I wanted to ensure that the images used gave a good representation of the type of events that would be held at a concert venue like Harmonia Hall.

### Acknowledgements
I would like to thank Code Institute for providing the resources and support needed to complete this project, including the Django framework and deployment guidance. This project was partly based on the CI CodeStar Blog, which provided a solid foundation for building the web application.
