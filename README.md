<div align=center>
<img src="./design/logo-card.png" height=200px>
</div>

# [Parsley PCs]()

![Python](https://img.shields.io/static/v1?label=python&message=3.11.2&color=blue) 
![Django](https://img.shields.io/static/v1?label=django&message=3.2&color=092E20&logo=django)

![GitHub repo size](https://img.shields.io/github/repo-size/Natte2110/CI-Milestone-04?color=orange) ![GitHub pull requests](https://img.shields.io/github/issues-pr/Natte2110/CI-Milestone-04)

This is a project for the Code Institute Milestone Project 4. Parsley PCs is an e-commerce site that enables users to purchase individual computer parts, or to build an entire PC interactively.

The users of this website will be able to create an account, browse current available products and offers, and interactively build a PC with parts of their choice that can be built and delivered to them.

The users will be able to create accounts and track their cart/orders, or simply browse and purchase items as a guest.

View the live project [Placeholder!](https://github.com/Natte2110/CI-Milestone-04)

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

<div align=center>
<img src="./design/wireframes/home-page.png" >
</div>