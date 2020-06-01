# PROJECT 3 : PICK A PLANT
Link : https://pick-a-plant.herokuapp.com/

## Objective :   
This is a prototype to allow plant-sellers to create a community where

## UX
    
As a user, 
- they will be able to post their items for sale on the website
- they will be able to make changes to their listing
- they will be able to remove the listing
- they will be able to sell their items on the website 
- they will be able to build a community
- they will be able to create their own profile (future development)

As a browser 
- they will be able to browse and make purchase for the plant they chosen (future development)
- they will be able to message the seller (future development)

As a host of the website
- we will build the community for sellers and buyers to transact
- we will generate revenue from transactions
- we will generate revenue from advertisers who will list on our webste

## Demo

A live demo can be found here : https://pick-a-plant.herokuapp.com


## Technologies

1. HTML
2. CSS
3. Bootstrap (3.3.7)
4. MongoDB
5. Python 3
6. Flask
7. Jinja

## Features
				
**My Design of the site :**

    * Design for plants ecommerce, so design focus on plants and hence color used are green-based
    * Easy for user to browse, add, update and remove
    
    Limitations: 
    * no search function implement yet (future development)
    * search function not implement due to time limitation
    * Social media links not link not set up

#### Testing
Manual Testing is done to ensure that the all functions are functional.
Test Results as follows :

*No* | *Steps* | *Expected Results* | *Observations*
--- | --- | --- | ---
1 | `On the Landing Page, click on the "New plant for sale" in navbar`| `Link to the submission of new inventory page and show entry form`| **Pass** 
2 | `Enter the details in form and submit`|`add the inventory to database and return to index page` | **Pass** 
3a | `On the Landing Page, click "Make changes" link beside name of plant`|`Show form with details of selected plant and allow user to enter new info or upload new image` | **Pass** 
3b | `Click "Make Changes" to save the changes`|`save the changes to database and return to index page` | **Pass** 
4a | `On the Landing Page, click "x" link on top right of image`|`Render page to check with user to confirm removal of selected listing` | **Pass** 
4b | `Click "Delete`|`delete selected listing from database and return to index page` | **Pass** 
5 | `In any pages, click "Home" link on top left of page`|`Return to landing page` | **Pass** 

#### Deployment
This site is hosted using Heroku App Link : 
_https://pick-a-plant.herokuapp.com/_

Regular commits are made to Github. Below are the commands to initalise and make regular commits, enter the commands in bash terminal in AWS

- git init .
- git add .
- git commit -m "Commit Message"
- git remote add origin https://github.com/tattoochan/project2.git
- git push -u origin master

_Deploy Heroku:_

- Install Heroku using bash
- Login to Heroku
- Install gunicorn
- Create Procfile and requirements.txt
- Commit and push to Heroku 
- Set up the Environment Vasriables
- Update Dependencies


#### Credits
    Uses W3School for many reference (https://www.w3schools.com/)
    Uses fontawesome for the social media icons (https://fontawesome.com/)
    Uses Bootstrap for templates (https://getbootstrap.com/)

 