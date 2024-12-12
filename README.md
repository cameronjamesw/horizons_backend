# Horizons API

## Project Goals

## Table of Contents

- [Horizons API](#horizons-api)
  - [Project Goals](#project-goals)
  - [Table of Contents](#table-of-contents)
  - [Planning](#planning)
    * [Data Models](#data-models)
      + [Profile](#profile)
      + [Category](#category)
      + [Favourite](#favourite)
    * [Post](#post)
    * [Comment](#comment)
    * [Like](#like)
    * [Follower](#follower)
  - [API Endpoints](#api-endpoints)
  - [Frameworks, Libraries & Dependencies](#frameworks-libraries--dependencies)
  - [Testing](#testing)
    * [Manual Testing](#manual-testing)
    * [Python Validation](#python-validation)
    * [Resolved Bugs](#resolved-bugs)
      + [Bugs Found While Testing API In Isolation](#bugs-found-while-testing-api-in-isolation)
      + [Bugs Found While Testing In React](#bugs-found-while-testing-in-react)
    * [Unresolved Bugs](#unresolved-bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)

## Planning

Planning started by creating epics and user stories for the frontend application, based on the project goals. The user stories were used to inform wireframes mapping out the intended functionality and 'flow' through the app. See the [repo for the frontend React app](/) for more details.

The user stories requiring implementation to achieve a minimum viable product (MVP) were then mapped to API endpoints required to support the desired functionality.
The user stories themselves are recorded [on this Google sheet](https://docs.google.com/spreadsheets/d/1xT0BXdg621rtGnQodwNQhRxqZqIO8vNXq3Ope-zOwR8/edit?usp=sharing), with the required API endpoints mapped to user stories on [a second sheet on the same document](https://docs.google.com/spreadsheets/d/1xT0BXdg621rtGnQodwNQhRxqZqIO8vNXq3Ope-zOwR8/edit?usp=sharing). You may need to manually select the two worksheets, as the Google docs link to the endpoints worksheet sometimes defaults to the user stories sheet.

### Data Models

#### Profile

Represents the user profile, using a one-to-one relationsip to the user model. A Profile instance is automatically created on user registration. The Profile model includes an `is_admin` field which is added through the Profile Serializer. This field checks whether the profile instance is a superuser, and if so, will be granted admin privileges. This will allow the user to create new categories and delete posts and comments of other users in the view of safeguarding.

Users can edit their own `name`, `island_name`, `friend_code`, `bio` and `image` fields.

#### Category

The category model represents a category within the database - these instances can only be created by admin users, mainly so that they are kept in moderation and they don't spiral out of control. The category model is tied to the post model with a one-to-many relationship. When creating post instances, authorised users are permitted to add their post to a category through a drop down menu - on creation this post instance will then be tied to the category in question.

Users have the option to search for posts based on the category they are part of, and when sifting through categories, the categories will be returned based on their `post_count`, a field added with the `annotate` function. This field will allow users to display the most popular categories - categories which have the most amount of posts tied to them.

When creating and editing a category, admin users can only alter the `name` field.

#### Favourite

### Post

### Comment

### Like

### Follower

## API Endpoints

Here is a table containing the API endpoints

### Django AllAuth Endpoints

| **URL** | **Notes** | **HTTP Method** | **CRUD Operation** | **View Type** | **POST/PUT Data Format** |
|---|---|---|---|---|---|
| /dj-rest-auth/registration/ | Notes | POST | N/A | N/A | {<br>    "username":"string",<br>    "password":"string",<br>    "password2":"string"<br>} |
| /dj-rest-auth/login/ | Notes | POST | N/A | N/A | {<br>    "username":"string",<br>    "password":"string",<br>    "password2":"string"<br>} |
| /dj-rest-auth/logout/ | Notes | POST | N/A | N/A | N/A |

### Profile Endpoints

| **URL** | **Notes** | **HTTP Method** | **CRUD Operation** | **View Type** | **POST/PUT Data Format** |
|---|---|---|---|---|---|
| /profiles/ | Notes | GET | READ | LIST | N/A |
| /profiles/int:pk/ | Notes | GET | READ | DETAIL | N/A |
| /profiles/int:pk/ | Notes | PUT | UPDATE | DETAIL | {<br>    "owner":"string",<br>    "name":"string",<br>    "island_name":"string",<br> "friend_code":"integer",<br> "bio":"string",<br> "image":"string", <br> "updated_at":"datetimefield" <br>} |

### Posts Endpoints

| **URL** | **Notes** | **HTTP Method** | **CRUD Operation** | **View Type** | **POST/PUT Data Format** |
|---|---|---|---|---|---|
| /posts/ | Notes | GET | READ | LIST | N/A |
| /posts/ | Notes | POST | CREATE | LIST | {<br>    "owner":"string",<br>    "title":"string",<br>    "contente":"string",<br> "category":"id",<br> "image":"string", <br> "created_at":"datetimefield" <br>} |
| /posts/int:pk/ | Notes | GET | READ | DETAIL | N/A |
| /posts/int:pk/ | Notes | PUT | UPDATE | DETAIL | {<br>    "owner":"string",<br>    "title":"string",<br>    "contente":"string",<br> "category":"id",<br> "image":"string", <br> "updated_at":"datetimefield" <br>} |
| /posts/int:pk/ | Notes | DELETE | DELETE | DETAIL | N/A |

### Categories Endponts

| **URL** | **Notes** | **HTTP Method** | **CRUD Operation** | **View Type** | **POST/PUT Data Format** |
|---|---|---|---|---|---|
| /categories/ | Notes | GET | READ | LIST | N/A |
| /categories/ | Notes | POST | CREATE | LIST | {<br>    "owner":"string",<br>    "name":"string",<br>    "created_at":"datetimefield"<br>} |
| /categories/int:pk/ | Notes | GET | READ | DETAIL | N/A |
| /categories/int:pk/ | Notes | PUT | UPDATE | DETAIL | {<br>    "owner":"string",<br>    "name":"string",<br>    "updated_at":"datetimefield"<br>} |
| /categories/int:pk/ | Notes | DELETE | DELETE | DETAIL | N/A |

### Comments Endpoints

| **URL** | **Notes** | **HTTP Method** | **CRUD Operation** | **View Type** | **POST/PUT Data Format** |
|---|---|---|---|---|---|
| /comments/ | Notes | GET | READ | LIST | N/A |
| /comments/ | Notes | POST | CREATE | LIST | {<br>    "owner":"string",<br>    "post":"id",<br> "content":"string",<br>    "created_at":"datetimefield"<br>} |
| /comments/int:pk/ | Notes | GET | READ | DETAIL | N/A |
| /comments/int:pk/ | Notes | PUT | UPDATE | DETAIL | {<br>    "owner":"string",<br>    "post":"id",<br> "content":"string",<br>    "updated_at":"datetimefield"<br>} |
| /comments/int:pk/ | Notes | DELETE | DELETE | DETAIL | N/A |

### Favourites Endpoints

| **URL** | **Notes** | **HTTP Method** | **CRUD Operation** | **View Type** | **POST/PUT Data Format** |
|---|---|---|---|---|---|
| /favourites/ | Notes | GET | READ | LIST | N/A |
| /favourites/ | Notes | POST | CREATE | LIST | {<br>    "owner":"string",<br>    "post":"id",<br>    "created_at":"datetimefield"<br>} |
| /favourites/int:pk/ | Notes | GET | READ | DETAIL | N/A |
| /favourites/int:pk/ | Notes | DELETE | DELETE | DETAIL | N/A |

### Likes Endpoints

| **URL** | **Notes** | **HTTP Method** | **CRUD Operation** | **View Type** | **POST/PUT Data Format** |
|---|---|---|---|---|---|
| /likes/ | Notes | GET | READ | LIST | N/A |
| /likes/ | Notes | POST | CREATE | LIST | {<br>    "owner":"string",<br>    "post":"id",<br>    "created_at":"datetimefield"<br>} |
| /likes/int:pk/ | Notes | GET | READ | DETAIL | N/A |
| /likes/int:pk/ | Notes | DELETE | DELETE | DETAIL | N/A |

### Followers Endpoints

| **URL** | **Notes** | **HTTP Method** | **CRUD Operation** | **View Type** | **POST/PUT Data Format** |
|---|---|---|---|---|---|
| /followers/ | Notes | GET | READ | LIST | N/A |
| /followers/ | Notes | POST | CREATE | LIST | {<br>    "owner":"string",<br>    "followed":"id",<br>    "created_at":"datetimefield"<br>} |
| /followers/int:pk/ | Notes | GET | READ | DETAIL | N/A |
| /followers/int:pk/ | Notes | DELETE | DELETE | DETAIL | N/A |

## Frameworks, Libraries & Dependencies
The Horizons API is implemented in Python using [Django](https://www.djangoproject.com) and [Django Rest Framework](https://django-filter.readthedocs.io/en/stable/).

The following additional utilities, apps and modules were also used.

### django-cloudinary-storage
https://pypi.org/project/django-cloudinary-storage/

Enables cloudinary integration for storing user profile images in cloudinary.

### dj-allauth
https://django-allauth.readthedocs.io/en/latest/

Used for user authentication. While not currently utilised, this package enables registration and authentication using a range of social media accounts. This may be implemented in a future update.

### dj-rest-auth
https://dj-rest-auth.readthedocs.io/en/latest/introduction.html

Provides REST API endpoints for login and logout. The user registration endpoints provided by dj-rest-auth are not utilised by the Tribehub frontend, as custom functionality was required and implemented by the Tribehub API.

### djangorestframework-simplejwt
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/

Provides JSON web token authentication.

### dj-database-url
https://pypi.org/project/dj-database-url/

Creates an environment variable to configure the connection to the database.

### psychopg2
https://pypi.org/project/psycopg2/

Database adapater to enable interaction between Python and the PostgreSQL database.

### django-filter
https://django-filter.readthedocs.io/en/stable/

django-filter is used to implement filtering of posts via `categories`, `favourites`, `likes` and `profiles`. It is also used in order to allow the user to search for posts using a search feature which is implemented into the front-end.

### django-cors-headers
https://pypi.org/project/django-cors-headers/

This Django app adds Cross-Origin-Resource Sharing (CORS) headers to responses, to enable the API to respond to requests from origins other than its own host.
Horizons is configured to allow requests from all origins, to facilitate future development of a native mobile app using this API.

## Testing

### Manual Testing

### Python Validation

### Resolved Bugs

#### Bugs Found While Testing API In Isolation

#### Bugs Found While Testing In React

### Unresolved Bugs

## Deployment

The TribeHub API is deployed to Heroku, using an ElephantSQL Postgres database.
To duplicate deployment to Heroku, follow these steps:

- Fork or clone this repository in GitHub.
- You will need a Cloudinary account to host user profile images.
- Login to Cloudinary.
- Select the 'dashboard' option.
- Copy the value of the 'API Environment variable' from the part starting `cloudinary://` to the end. You may need to select the eye icon to view the full environment variable. Paste this value somewhere for safe keeping as you will need it shortly (but destroy after deployment).
- Log in to Heroku.
- Select 'Create new app' from the 'New' menu at the top right.
- Enter a name for the app and select the appropriate region.
- Select 'Create app'.
- Select 'Settings' from the menu at the top.
- Navigate to [CI's Database Maker](https://dbs.ci-dbs.net/) and input your email address upon request.
- Once your email has been entered, you will recieve your `Database URL` shortly in an email from the Code Institue Bot.
- Copy the PostGres database URL to your clipboard (this starts with `postgresql://`).
- Return to the Heroku dashboard.
- Select the 'settings' tab.
- Locate the 'reveal config vars' link and select.
- Enter the following config var names and values:
    - `CLOUDINARY_URL`: *your cloudinary URL as obtained above*
    - `DATABASE_URL`: *your PostGreSQL database URL as obtained above*
    - `SECRET_KEY`: *your secret key*
    - `ALLOWED_HOST`: *the url of your Heroku app (but without the `https://` prefix)*
- Ensure that these values are also in your `env.py` fi;e within the repository you forked/cloned earlier in the steps.
- Select the 'Deploy' tab at the top.
- Select 'GitHub' from the deployment options and confirm you wish to deploy using GitHub. You may be asked to enter your GitHub password.
- Find the 'Connect to GitHub' section and use the search box to locate your repo.
- Select 'Connect' when found.
- Optionally choose the main branch under 'Automatic Deploys' and select 'Enable Automatic Deploys' if you wish your deployed API to be automatically redeployed every time you push changes to GitHub.
- Find the 'Manual Deploy' section, choose 'main' as the branch to deploy and select 'Deploy Branch'.
- Your API will shortly be deployed and you will be given a link to the deployed site when the process is complete.

## Credits