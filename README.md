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

### Data Models

#### Profile

#### Category

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

## Credits