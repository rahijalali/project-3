# project-3

bookkeeping records : this website is developed using Django Framework as part of Portfolio Project 3 for my Full Stack Software Development at Code Institute.

Record keeping can help you to find the information you need. It promotes the creation of full and accurate records in the first place. It also involves storing and managing records appropriately so that the information will be available to you when you need it. very simple and easy to use for everyone specifically for the users requested. Welcome to Grandma's Money Manager, a user-friendly and straightforward system designed with simplicity in mind. the database which I used to store my data is Squlight.

You can view the live site here:

## Overview

Managing finances can be overwhelming, so I've created this easy-to-use money bookkeeping system to help user to keep track and record their financial transactions. The system is designed to be user-friendly, allowing users to easily add new transactions and view their financial history.

## Features

- **User-Friendly Interface:** No need to worry about complicated technology. system is designed with buttons and clear fonts, making navigation a breeze.

- **Quick Data Entry:** Add the name and add the debit and credit.. No confusing forms or jargon.

- **Clear Categories:** Everything is neatly organized, so you can easily see where your money is going.

## User Experience - UX

# Site Aims

The primary objectives or aims of bookkeeping include:

. Recording Transactions: Documenting all financial transactions, including debit and credit

. Classification: Categorizing transactions into appropriate accounts to facilitate analysis and reporting.

. Accuracy: Ensuring that recorded information is precise and error-free to produce reliable financial statements.

. Compliance: Adhering to accounting principles and standards to meet legal and regulatory requirements.

. Financial Analysis: Providing a basis for financial analysis, budgeting, and decision-making within the organization.

. Facilitating Reporting: Generating financial statements, such as the income statement, balance sheet, and cash flow statement, to communicate the financial position of the business.

In summary, the aim of bookkeeping is to maintain a systematic and accurate record of financial transactions, which in turn supports informed decision-making and financial analysis for businesses.

## Agile Methodology

The Agile Methodology was used to plan this project. This was implemented through Github and the Project Board. Through the use of the Kanban board in the projects view in Github, the project was divided into a few different sections:

To Do- (All the User stories were initially entered in the 'To Do' column)
In Progress- (then during development story they were moved into the 'In Progress' column)
Done- (and then finally they get moved into 'Done' once the development completes)
Please find my Kanban Board with my user stories here:

<img alt="kanban.png" src=./assets/img/kanban.png>

## Related user Stories

. as a user I can easly add credit and debit transaction
. as a user I can add new costumers
. as a user I can check the costumers transaction

## Tasks

The tasks for the website development process was closely followed as mentioned in CI's Django module "I Think Therefore I Blog" walkthrough project. The task is generally the developers step towards preparing the app. The tasks that I have followed during the development phase were carried out in this order.

Before Project Inception

. Design ERD and Data
. Create Repository in GitHub
. Create Project, User Stories and prepare Kanban Board

## Creation of Project in GitPod

. Create the django project.
. Create Database Models
. Set up models.py file in "blog" directory
. Build Admin site
. Set up Templates
. Create base.html
. Create index.html, view and style
. Set up template file features with views.py and urls.py
. Install Allauth for sign in, sign up and sign out templates with- pip3 install django-allauth

## Database Diagram

Smart Draw was used to create a database schema to visualise the types of custom models the project requires. This schema was used as a guide to what needed to be added to each model. Below is the Database structure that this project is based on. The relationship between Entities Post, Author, Destination are shown in this diagram.

<img alt="ERD.jpg" src=./assets/img/ERD.jpg>

## Features

# Pages

In total it will be 2 pages: customer and transaction
for example:

- https://rahiwallet-1dd88e63e8bf.herokuapp.com/wallet/1/

- https://rahiwallet-1dd88e63e8bf.herokuapp.com/wallet/

## Admin Panel/Superuser

- Admin accesses the project via logging into Django admin panel with a superuser id and password. The page appears as shown;

<img alt="admin-page.png" src=./assets/img/admin-page.png>

- A superuser "admin" was created for this project to manage the admin panel.
- On the Admin Panel, as an admin I have full access to CRUD functionality so I can view, Create, Read, Update, and Delete the following ones:

## Admin login

this is where admin can sign in with username and password.

<img alt= " signin.png" src= ./assets/img/signin.png>

---

## Technologies Used

### Languages Used

- [HTML 5](https://en.wikipedia.org/wiki/HTML/)- Used to structure all the templates on the site
- [CSS 3](https://en.wikipedia.org/wiki/CSS)- to provide extra styling to the site
- [JavaScript](https://www.javascript.com/)- Minimum javascript was used to fade out alerts after a few seconds.
- [Python](https://www.python.org/)- To provide the functionality to the site. Packages used in the project can be found in requirements.txt

### Django Packages

- [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)- For authentication, registration, account management.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)- To style the forms.

### Frameworks - Libraries - Programs Used

- [Django](https://www.djangoproject.com/) was used as the framework for the back-end logic of the project. Django enables rapid and secure development.
- [Bootstrap](https://getbootstrap.com/)- Used to style the website, add responsiveness and interactivity.
- [Git](https://git-scm.com/)- Used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.
- [GitHub](https://github.com/)- Used to store the project's code after being pushed from Git.
- [PostgreSQL](https://www.postgresql.org/)- Database used through ORM.
- [Google Fonts:](https://fonts.google.com/) used for the Kurale, serif font
- [Font Awesome:](https://fontawesome.com/) was used to add icons for DJANGO and UX purposes.

---

## Testing

### Validation

I used the following validation tools to validate CSS. Below the link of TESTING.md file, which includes all validation results.

- HTML using [validator w3]
  <img alt="w3-validator.jpg" scr=./assets/img/w3-validator.jpg>

### Manual Testing

Testing has taken place continuously throughout the development of the project. Each view was tested regularly.

<img alt= "transaction-page.jpg" scr=./assets/img/transaction-page.jpg>

<img alt= "customer-page.jpg" scr=./assets/img/customer-page.jpg>
