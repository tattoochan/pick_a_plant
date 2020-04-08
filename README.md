# PROJECT 3 : PICK A PLANT

### Objective :   
    To build a protocol website for an ecommerce website to sell plants

#### SCOPE
The website allows User to :
    
    CREATE
    * submit a new listing for a new plant
    READ
    * Assess the database and display the details in the data
    UPDATE
    * edit and update an existing listing
    DELETE
    * select and remove an existing listing

#### Demo

A live demo can be found here : https://pick-a-plant.herokuapp.com

#### UX
    My Considerations for the website:
    * user able to submit, make changes and remove a plant listing on the website
    * display all the pots for sale and easy for user to select

#### Technologies
    1. HTML
    2. CSS
    3. Bootstrap (3.3.7)
    4. MongoDB
    5. Python 3
    6. Flask
    7. Jinja

#### Features
				
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

    All codes are uploaded to GitHub and links are made to Heroku by installing in bash terminal in projects.
    Regular commits are push to the Github subsequently push to heroku to deploy.
    .gitignore file is added to remove files that are not required or files that we do not wish to be uploaded to Github

_Deploy Heroku:_

    i) Install Heroku using bash
    ii) Login to Heroku
    iii) Install gunicorn
    iv) Create Procfile and requirements.txt
    V) Commit and push to Heroku 
    vi) Set up the Environment Vasriables
    vii) Update Dependencies


#### Credits
    Uses W3School for many reference (https://www.w3schools.com/)
    Uses fontawesome for the social media icons (https://fontawesome.com/)
    Uses Bootstrap for templates (https://getbootstrap.com/)

 