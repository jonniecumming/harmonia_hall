# Harmonia Hall

<!-- TABLE OF CONTENTS (to be modified for this project) -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#desktop-appearance">Desktop Appearance</a></li>
        <li><a href="#tablet-appearance">Tablet Appearance</a></li>
        <li><a href="#mobile-appearance">Mobile Appearance</a></li>
      </ul>
    </li>
    <li>
      <a href="#ux-design">UX Design</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#wireframes">Wireframes</a></li>
      </ul>
    </li>
    <li><a href="#user-stores">User Stories</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#bugs">Bugs</a></li>
    <li><a href="#testing">License</a></li>
    <li><a href="#use-of-ai">Use of AI</a></li>
    <li><a href="#deployment">Deployment</a></li>
    <li><a href="#credits">Credits</a></li>
  </ol>
</details>

## About the Project
<!-- Overview of project -->
The aim of this project is to create a small concert venue bookings site, where visitors can browse the upcoming concerts/events at the ficticious venue, 'Harmonia Hall' and book tickets for a desired event.

Users should be able to create an account and then be able to book an event. Once this has happend, they can view their bookings, modify the number of tickets or delete the event.

Design...

<!-- Deployed homepage screenshot examples of site -->
### Desktop Appearance
- Deployed Desktop view screenshot
### Tablet Appearance
- Deployed Tablet view screenshot
### Mobile Appearance
- Deployed Mobile view screenshot

<!-- Overview of UX Design of project -->
## UX Design
- Icons, Fonts, e.g. [**Font Awesome**](https://fontawesome.com)
- colour palette
- Wireframes (by page, not device, e.g. 3 device home, 3 device, about... etc.)

### Wireframes
Wireframes were created for different viewports (mobile, tablet and desktop) to help visualise how the site would look on different devices.

I used the software _Balsamiq_, to create these diagrams.

![Home page wireframe](/images/wireframe-home.png)
![What's on page wireframe](/images/wireframe-whats-on.png)
![Sign in page wireframe](/images/wireframe-sign-in.png)
![Bookings page wireframe](/images/wireframe-bookings.png)
![about page wireframe](/images/wireframe-about.png)
![Contact page wireframe](/images/wireframe-contact.png)

<!-- Overview of User Stories project -->
## User Stories
### ADD Screenshot of project board here !

### Must Have:
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
### Should Have:
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

### Could Have:
#### User Story: Contact Us
As a **site visitor**, I can **find relevant contact information, including a contact form** so that **I can get in touch about more specific queries relating to the events**.
Acceptance criteria:
- A user can easily navigate to a contact page.
- The contact page includes relevant contact information.
- The contact page has a contact form that can be filled out by the site visitor.
#### User Story: View Event Bookings
As a **site admin**, I can **view all bookings for a concert** so that **I can monitor attendance and capacity**.
Acceptance criteria:
- The site allows admins to view bookings for an event, including the total number of bookings per event.

### Won't Have:
#### User Story: Search for Events
As a **site user**, I can **search for events with keywords** so that **I can find the events I am looking for**.
Acceptance criteria:
- A user is able to easily navigate to a search bar.
- Entering keywords into the search will bring up corresponding/relevant events.

<!-- Overview of features of the project -->
## Features
- Home page (with screenshot): what does it offer to a user?
- About page (with screenshot): what does it offer to a user?
- contact...
- bookings...
- Navigation bar (with screenshot): what does it offer to a user?
- Footer...
- Sign in...
- Sign out...
- Admin...
- Entity Relationship Diagram

<!-- Overview of bugs and solutions -->
## Bugs

<!-- Overview of testing done -->
## Testing
- Manual Testing (various browsers)
- Lighthouse
- Responsive Testing
- Validator Testing (W3C HTML, CSS, Python PEP8, JS (-JS hint?) )

<!-- Overview of AI use within project -->
## Use of AI
- How has this been used in the project (bugs, code, planning, etc.)
- commit messages skeleton

<!-- Overview of How the project was deployed -->
## Deployment
- How the site was deployed (Steps, see Mark B's Blog for example)
- Live link

<!-- Credits for project -->
## Credits

### Content

### Media

`This is an example of how to write command line text`