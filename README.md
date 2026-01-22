# Harmonia Hall

<!-- TABLE OF CONTENTS (to be modified for this project) -->
<details>
  <summary>Index</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#overview">Overview</a></li>
        <li><a href="#rationale">Rationale</a></li>
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
      <ul>
        <li><a href="#home-page">Home Page</a></li>
        <li><a href="#about-page">About Page</a></li>
        <li><a href="#contact-page">Contact Page</a></li>
        <li><a href="#bookings-page">Bookings Page</a></li>
        <li><a href="#navigation-bar">Navigation Bar</a></li>
        <li><a href="#footer">Footer</a></li>
        <li><a href="#sign-in">Sign In</a></li>
        <li><a href="#sign-out">Sign Out</a></li>
        <li><a href="#admin">Admin</a></li>
      </ul>
    </li>
    <li><a href="#bugs">Bugs</a></li>
      <ul>
        <li><a href="#bug-1">Bug 1</a></li>
        <li><a href="#bug-2">Bug 2</a></li>
        <li><a href="#bug-3">Bug 3</a></li>
      </ul>
    </li>
    <li><a href="#testing">Testing</a></li>
      <ul>
        <li><a href="#manual-testing">Manual Testing</a></li>
        <li><a href="#lighthouse-testing">Lighthouse Testing</a></li>
        <li><a href="#responsive-testing">Responsive Testing</a></li>
        <li><a href="#validator-testing">Validator Testing</a></li>
      </ul>
    </li>
    <li><a href="#use-of-ai">Use of AI</a></li>
    <li><a href="#deployment">Deployment</a></li>
    <li><a href="#credits">Credits</a></li>
  </ol>
</details>

## About the Project
<!-- Overview of project -->
![Am I Responsive](/images/responsive.png)
*Am I Responsive showing the Harmonia Hall site on multiple device sizes*

### Overview
This project is a full-stack web application built using the Django framework. It uses Python, HTML and CSS to create a dynamic and responsive site for a fictious concert venue called Harmonia Hall. The application allows users to view upcoming events, book tickets, and manage their bookings. It also includes user authentication features, enabling users to create accounts, log in, and log out securely.

You can visit the deplyed site at: [Harmonia Hall](https://harmonia-hall-b317b69502c7.herokuapp.com/)

### Rationale
The aim of this project is to provide a solution to the following problem faced by the venue, Harmonia Hall, and its event attendees:

"Harmonia Hall and its event attendees currently lack an efficient, centralised platform to manage event bookings and capacity. The venue struggles to prevent overbooking, track event capacity accurately, and manage multiple bookings, while attendees face difficulties in discovering upcoming events, making reservations, and managing their bookings effectively. This fragmented and manual process results in capacity management issues, double bookings, missed events, and a poor user experience for both venue operators and customers seeking to attend live music events."

This web application addresses these challenges by providing a comprehensive, user-friendly booking platform that streamlines the entire event management process. The platform enables attendees to easily discover upcoming events, view real-time availability, and securely reserve tickets with capacity tracking to prevent overbooking. Built-in booking management features allow users to view, modify, or cancel their reservations at any time, while administrators benefit from a robust backend system to create, manage, and monitor events and bookings. By implementing real-time capacity validation, enforcing one booking per user per event, and providing clear error messaging and confirmation feedback, the application eliminates double bookings, ensures accurate capacity management, and delivers a seamless, trustworthy booking experience for both venue operators and customers.

With this in mind, this application is designed for two primary user groups. First, it serves music enthusiasts and event-goers who seek a convenient, reliable platform to discover upcoming live music and other events, browse event details, and securely book tickets without the fear of overbooking or capacity conflicts. Second, it caters to venue administrators and staff at Harmonia Hall, who require efficient tools to create and manage events, track real-time capacity and bookings, and maintain accurate event listings. Whether its users are looking to attend their next favorite concert or manage a busy event venue, this application provides an intuitive, reliable solution that enhances the overall event experience for both attendees and venue operators alike.

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
For the icons, I used [**Font Awesome**](https://fontawesome.com)

For the colour scheme, I used [**Colormind**](http://colormind.io) to generate a palette based on images of concert venues and music events.
![Colormind](/images/colormind-palette.png)
*screenshot of colour palette generated by Colormind*


### Wireframes
Wireframes were created for different viewports (mobile, tablet and desktop) to help visualise how the site would look on different devices.

I used the software _Balsamiq_, to create the following wireframe diagrams.

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
The database structure for this project is based around three main models: Event, Booking, and User (using Django's built-in User model). This is illustrated in the Entity Relationship Diagram (ERD) below.

![ERD](/images/erd.png)
*Entity Relationship Diagram (ERD) showing database structure*

<!-- Overview of User Stories project -->
## User Stories
### ADD Screenshot of project board here !

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
- Interactive elements are accessible via keyboard shortcuts and screen readers.

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
- Must Haves: All completed successfully.
- Should Haves: ...
- Could Haves: ...
- Won't Haves: ...

<!-- Overview of features of the project -->
## Features
- Home page (with screenshot): what does it offer to a user?
- About page (with screenshot): what does it offer to a user?
- bookings... (with screenshot): what does it offer to a user?
- Sign in... etc.
- Sign out...
- Navigation bar
- Footer...
- Admin...

<!-- Overview of bugs and solutions -->
## Bugs
- iPhone footer bug - iPhone safari specific problem (Still an issue?)
- 

- Bug 1: description...
- How it was fixed.
- Bug 2: description...
- How it was fixed.
- Bug 3: description...
- How it was fixed.
<!-- Overview of testing done -->
## Testing

<details>
<summary><strong>Testing Details</strong></summary>

### Manual Testing
- Description of manual testing done, e.g., functionality, links, forms, etc.

| Test | Expected Result | Pass/Fail |
|--- |--- |--- |
| Home Page | Page loads with carousel | Pass |
| Login Form | User logged in | Pass |
| Carousel | Next event displays | Pass |
| Responsivity | Layout adjusts | Pass |
| Home page link (nav bar) | success | success |
| Home page link (title) | success | success |
| About page link | success | success |
| Log in link | success | success |

### Lighthouse Testing
- Description of Lighthouse testing done, e.g., performance, accessibility, best practices, SEO.
![Lighthouse Report](/images/lighthouse-report.png)
*Screenshot of Lighthouse report showing scores for performance, accessibility, best practices, and SEO*

### Responsive Testing
- Description of responsive testing done, e.g., different devices, screen sizes, etc.

### Validator Testing

#### W3C HTML Validation
![W3C HTML Validation](/images/w3c-html-validation.png)
*Screenshot of passing W3C HTML validation*

#### W3C CSS Validation
![W3C CSS Validation](/images/w3c-css-validation.png)
*Screenshot of passing W3C CSS validation*

- Description of validator testing done, e.g., W3C HTML, CSS, Python PEP8, JS (-JS hint? ).

</details>

<!-- Overview of AI use within project -->
## Use of AI

During this project, AI was utilised in a few ways. Initially, I wanted to use AI to help me plan out certain aspects of the project, such as the user stories and features. I found this to be a useful starting point, as it helped me to think about what I wanted to achieve with the project, and how I could break it down into manageable parts. However, I made sure that I changed and refined the suggestions so that they fit my specific project needs, rather than just accepting them as they were.

For code generation, I picked Claude as my preferred AI tool. From what I understand and have experienced so far, I found Claude to be particularly good at understanding the context of my project, and providing the most relevant suggestions.

I used it to suggest how it could help with certain functions and methods. I wanted to make sure that for every use of AI, I reviewed the code thoroughly to ensure it made sense to me, and that it was keeping what I wanted to achieve in mind. 

I also used Claude to help with debugging certain issues I was having. When doing this, I made sure to understand what the suggestions were doing, and why they would help solve the issue. I would also make sure to challenge the suggestions if I felt they were not correct, which on a number of occasions they were not, despite my careful and descriptive prompting. One particular area that Claude helped in this way, was with booking capacity validation, which was a tricky area to get right. As I primarily used Claude as my client, I created a claude.md file in the root of my project to follow Django best practices. This helped to ensure that the suggestions I received about the Django framework were in line with best practices.


- Which AI tools were used (e.g., ChatGPT, DALL·E 2, etc.)
- Purpose of use (e.g., code generation, image creation, etc.)
- How has this been used in the project (bugs, code, planning, etc.)
- commit messages skeleton

<!-- Overview of How the project was deployed -->
## Deployment 
The site was deployed to Heroku from the main branch of my GitHub repository. Bewlow are the steps I took to deploy the site:

1. I navigated to my Heroku account and create a new app
2. I gave the app an appropriate and unique name and selected the region closest to me (Europe).
3. In the "Deploy" tab, I connected my GitHub repository to Heroku by searching for the repository name and clicking "Connect".
4. I then went to the "Settings" tab and clicked on "Reveal Config Vars"
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
- Booking options for children/over 65’s/disability spaces
- Interactive JS seat selection for relevant concerts
- New Page: How to find us/Plan your visit
- Add more descriptive data to each event, i.e. genre, to allow for filtering functionality on What’s on page
- Add News/updates page
- Add site search feature
- Calendar view for what’s on page
- Add Shopping Cart to allow for subtotals, multiple bookings at once.
- Integrate real payment functionality
- Option to select venue, to allow for expansion into concerts in other performance spaces within concert venue
<!-- ========================================
     CREDITS
     ======================================== --><!-- Credits for project -->
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
- Text content sources: e.g., Wikipedia, blogs, articles, etc.

### Media
- Image sources: Unsplash, iStock
### Acknowledgements
- Mentors, tutors, peers, etc.


- Am I Responsive: for responsive design image
- Colormind: for colour palette generation
- Balsamiq: for wireframe creation
