<div align=center>
<img src="./design/logo-card.png" height=200px>
</div>

# [Parsley PCs]()

![Python](https://img.shields.io/static/v1?label=python&message=3.11.2&color=blue) 
![Django](https://img.shields.io/static/v1?label=django&message=3.2&color=092E20&logo=django)

![GitHub repo size](https://img.shields.io/github/repo-size/Natte2110/CI-Milestone-04?color=orange) ![GitHub pull requests](https://img.shields.io/github/issues-pr/Natte2110/CI-Milestone-04)

This is a project for the Code Institute Milestone Project 4. Parsley PCs is an e-commerce site that enables users to purchase individual computer parts.

The users of this website will be able to create an account, browse current available products and offers, and interactively build a PC with parts of their choice that can be built and delivered to them.

The users will be able to create accounts and track their cart/orders, or simply browse and purchase items as a guest.

View the live project [Here!](https://parsleypcs-e697de04d1ce.herokuapp.com/)

---

## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Color Scheme**](#color-scheme)
        - [**Imagery**](#imagery)
        - [**Typography**](#typography)
    - [**Wireframes**](#wireframes)
    - [**Database Design**](#database-design)
2. [**Technologies Used**](#technologies-used)
    - [**Development Technologies**](#development-technologies)
    - [**Front-End Technologies**](#front-end-technologies)
    - [**Back-End Technologies**](#back-end-technologies)
    - [**Python Modules**](#python-modules)
    - [**Deployment Technologies**](#deployment-technologies)

---

## UX

### User Stories

I have decided to place the user inside a table for good structure.

The table depicts three groups:

- **Guest User** - Someone who has not yet created an account on the site.

- **Registered User** - Someone who has created an account and activated it using the email link.

- **Site Admin** - Someone who has control over the site with an admin log in, they are able to manage the site unlike the previous two groups.

| **ID** | **As** | **I want to be able to** | **In order to** |
|:---:|:---:|:---:|:---:|
| **1** | **Guest User** | View the site irrespective of the browser/device I am using | Be able to view all required information |
| **2** | **Guest User** | View the site's available products and their information | View the purchasable items |
| **3** | **Guest User** | Sort the site's shop by order of popularity | View the most popular items first |
| **4** | **Guest User** | Sort the items by their specific category | View the items I am most interested in buying |
| **5** | **Guest User** | Add items to my cart | Purchase my chosen items and view a running total spend |
| **6** | **Guest User** | Remove items from my cart | Cancel a purchase on a specific item |
| **7** | **Guest User** | Create an account | Have a personalised shopping experience and saved information |
| **8** | **Guest User** | View each product in detail | Gain more insight into a specific product before purchase |
| **9** | **Guest User** | Interactively build my own PC | Gain an idea as to what the final product would be |
| **10** | **Guest User** | View featured or reduced deals | Get the best deals available on the site |
| **11** | **Guest User** | Search for products on the site | Find a specific item |
| **12** | **Guest User** | View related products to the one I am looking at | Find potentially better deals or suitability and compare the results |
| **13** | **Guest User** | View my current search and how many results were returned | Gain an insight into the usefulness of the search |
| **14** | **Guest User** | Easily update the items/quantity in my shopping bag | Make changes to my purchases |
| **15** | **Guest User** | Input my payment details when confirming a purchase | Pay for the items in my shopping bag |
| **16** | **Guest User** | Receive a confirmation email after placing an order (with option to provide email address) | Have peace of mind that my order was received |
| **17** | **Registered User** | Manage my account, such as username, address or name | Be able to keep my information up to date |
| **18** | **Registered User** | Change or reset my password | Access my account if the password is forgotten or stolen |
| **19** | **Registered User** | Delete my account | Remove my personal information from the site |
| **20** | **Registered User** | Add a review to an item | Provide feedback for the store owner and for other shoppers |
| **21** | **Registered User** | Save my delivery address for further potential purchases | Have an easy experience if I return to the site |
| **22** | **Registered User** | Delete a review I have previously posted | Remove my opinion from the product |
| **23** | **Registered User** | Update or edit a review posted by myself | Change a potential mistake in my review |
| **24** | **Site Admin** | Add an item to the store along with a picture | Add fresh or updated products to the store |
| **25** | **Site Admin** | Update an items on the store | Change the price or add more information such as an updated picture |
| **26** | **Site Admin** | Remove or hide items from the store  | Control what is available on the store currently |
| **27** | **Site Admin** | Update the site's terms and conditions, or other information such as banners | Ensure customers are updated on potential issues or specific sales |
| **28** | **Site Admin** | Add/Remove/Update categories of items | Ensure that there is a category readily available and suitable for each product |
| **29** | **Site Admin** | View all orders along with their completion status | Manage each order and ensure they are completed correctly |
| **30** | **Site Admin** | Manage reviews posted by users | Moderate the content, such as removing hateful or discrimatory messages |
| **31** | **Site Admin** | Manage user accounts | Aid users that are having issues with their personal accounts |

### Design

This web application will be designed to have a professional feel to it, with hints of technology dotted around.

#### Color Scheme

To keep in line with the name and theme, the app will follow a colour scheme extracted from the following logo image.

<div align=center>
    <img src="./design/logo-card.png" height=200px>
</div>

*Palette*: **Extracted From Above Image**

| 1 | 2 | 3 | 4 | 5 | 
| :---: | :---: | :---: | :---: | :---: |
| ![#2B2A40](https://via.placeholder.com/15/2B2A40/2B2A40) | ![#435C73](https://via.placeholder.com/15/435C73/435C73) | ![#618C74](https://via.placeholder.com/15/618C74/618C74) | ![#94A69B](https://via.placeholder.com/15/94A69B/94A69B) | ![#6D8C3F](https://via.placeholder.com/15/6D8C3F/6D8C3F) |
| #2B2A40 | #435C73 | #618C74 | #94A69B | #6D8C3F |

The above table was extracted from the image using [Adobe Color](https://color.adobe.com/create/image) by uploading the image and selecting the colours extracted from the image.

These will be placed as *:root* variables within the base css file in order to be used across all necessary elements.

#### Imagery

Any imagery used on the website will be follow a technological theme in lieu with the site's products.

Registered users of the site will be able to upload their own image in order to have a personalised profile picture.

The images of the products will all follow the same theme and style to ensure consistency across the products pages.

#### Typography

The main font that will be seen across the site is [Oswald](https://fonts.google.com/specimen/Oswald).

A fall-back font of sans-serif will be used upon failure to load the main font style.

### Wireframes

#### Home Page

The home page will introduce a user to the site's main prupose, as well as providing easy navigation elements to all other pages within the site. Featured products will also be available on the home page to entice users to click on said products initially.

<div align=center>
    <img src="./design/wireframes/home-page.png" >
</div>

#### All Products Page

The all products page will have all products returned based on a filter. users can sort, filter and change which types of products show up on this page.

The products will be in their own individual cards and laid on the page using the bootstrap grid system.

<div align=center>
    <img src="./design/wireframes/all-products.png" >
</div>

#### Build Your Own Page

The 'Build Your Own' page will be the main focus of the site, and will allow users to interactively build their own PC. 

Users will be able to drag and drop products onto the PC in order of assembly. The products they chose will automatically update their cart so that they can purchase all of the required products, or pay a small fee at the end of building to have the PC built for them.

When chosing parts for the PC, only parts that are compatible with the previously selected components will be available.

<div align=center>
    <img src="./design/wireframes/build-you-own.png" >
</div>

### Database Design

This entity relationship diagram represents the relationships users, products and all additional information to be captured alongside them.

As different PC parts will require different technical paramaters, class inheritence was used in this diagram to represent fields that will be present for each product, as well as the specific required technical fields for each type of PC Component.

<div align=center>
    <img src="./design/database-erd.png" >
</div>

## Technologies Used

### Development Technologies

- ![Balsamiq Wireframes](https://img.shields.io/static/v1?label=Balsamiq&message=4.7.4&color=CC0200)
    - [Balsamiq](https://balsamiq.com/) - Balsamiq was used in order to create intuitive wireframes during the initial design process.
- ![GitHub](https://img.shields.io/static/v1?label=GitHub&message=Natte2110&color=181717&logo=github&logoColor=ffffff)
    - [GitHub](https://github.com/) - GitHub was used to store and manage the project within a combined online repository.
- ![Visual Studio Code](https://img.shields.io/static/v1?label=VS%20Code&message=1.85.1&color=007ACC&logo=visual%20studio%20code&logoColor=ffffff)
    - [VS Code](https://code.visualstudio.com/) - Visual Studio Code was used as the primary development environment for the project.

### Front-End Technologies

- ![HTML5](https://img.shields.io/static/v1?label=HTML&message=5&color=E34F26&logo=html5&logoColor=ffffff)
    - [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - HTML5 was used as the primary markup language in order to structure and display the elements on the page.
- ![CSS3](https://img.shields.io/static/v1?label=CSS&message=3&color=1572B6&logo=css3&logoColor=ffffff)
    - [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - CSS Was used in order to provide styling to the web pages with custom colours and sizes of elements.
- ![Bootstrap 4.3.1](https://img.shields.io/static/v1?label=Bootstrap&message=4.3.1&color=563d7c)
    - [Bootstrap 4.3.1](https://getbootstrap.com/docs/4.3/getting-started/introduction/) - Bootstrap was used to quickly design and create the layout and look of the website.
- ![jQuery 3.3.1](https://img.shields.io/static/v1?label=jQuery&message=3.3.1&color=0769AD&logo=jquery&logoColor=ffffff)
    - [jQuery 3.3.1](https://code.jquery.com/jquery/) - jQuery was used in conjunction with bootstrap to apply javascript selectors and updating elements more efficiently.

### Back-End Technologies

- ![Python](https://img.shields.io/static/v1?label=Python&message=3.11.2&color=blue&logo=python&logoColor=ffffff)
    - [Python 3.11.2](https://www.python.org/) - Python was used as the back-end management language to pass and handle data to and from the application.
- ![Django](https://img.shields.io/static/v1?label=Django&message=3.2&color=092E20&logo=django&logoColor=ffffff)
    - [Django 3.2](https://www.djangoproject.com/) - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It was used to build the back-end of the application.
- ![PostgreSQL 16.1](https://img.shields.io/static/v1?label=PostgreSQL&message=16.1&color=336791&logo=postgresql)
    - [PostgreSQL 16.1](https://www.postgresql.org/) - PostgreSQL was used as the database in this project in order to store information regarding users, products, and orders.

### Python Modules

In this section I will highlight and explain the use of each additional python package that was used within this project.

- ![Django AllAuth](https://img.shields.io/static/v1?label=Django%20AllAuth&message=0.44.0&color=092E20&logo=django&logoColor=ffffff)
    - [Django AllAuth 0.44.0](https://django-allauth.readthedocs.io/en/latest/) - Django AllAuth was used to manage user registrations, logins, and authentication.
- ![Whitenoise](https://img.shields.io/static/v1?label=Whitenoise&message=5.3.0&color=092E20&logo=django&logoColor=ffffff)
    - [Whitenoise 5.3.0](http://whitenoise.evans.io/en/stable/) - Whitenoise was used to serve static files in production.
- ![Gunicorn](https://img.shields.io/static/v1?label=Gunicorn&message=20.1.0&color=092E20&logo=gunicorn&logoColor=ffffff)
    - [Gunicorn 20.1.0](https://gunicorn.org/) - Gunicorn was used as the WSGI HTTP server for serving the Django application in production.
- ![Boto3](https://img.shields.io/static/v1?label=Boto3&message=1.18.57&color=092E20&logo=aws&logoColor=ffffff)
    - [Boto3 1.18.57](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - Boto3 was used to interact with AWS S3 for storing media files.

### Deployment Technologies

- ![Heroku](https://img.shields.io/static/v1?label=Heroku&message=7.53.0&color=430098&logo=heroku&logoColor=ffffff)
    - [Heroku](https://www.heroku.com/) - Heroku was used to deploy and host the application in the cloud.
- ![AWS S3](https://img.shields.io/static/v1?label=AWS%20S3&message=%20&color=232F3E&logo=amazon-aws&logoColor=ffffff)
    - [AWS S3](https://aws.amazon.com/s3/) - AWS S3 was used to store and serve static and media files.