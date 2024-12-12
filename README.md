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

### Post Endpoints

| **URL** | **Notes** | **HTTP Method** | **CRUD Operation** | **View Type** | **POST/PUT Data Format** |
|---|---|---|---|---|---|
| /posts/ | Notes | GET | READ | LIST | N/A |
| /posts/ | Notes | POST | CREATE | LIST | {<br>    "owner":"string",<br>    "title":"string",<br>    "contente":"string",<br> "category":"id",<br> "image":"string", <br> "created_at":"datetimefield" <br>} |
| /posts/int:pk/ | Notes | GET | READ | DETAIL | N/A |
| /posts/int:pk/ | Notes | PUT | UPDATE | DETAIL | {<br>    "owner":"string",<br>    "title":"string",<br>    "contente":"string",<br> "category":"id",<br> "image":"string", <br> "updated_at":"datetimefield" <br>} |
| /posts/int:pk/ | Notes | DELETE | DELETE | DETAIL | N/A |

## Frameworks, Libraries & Dependencies

## Testing

### Manual Testing

### Python Validation

### Resolved Bugs

#### Bugs Found While Testing API In Isolation

#### Bugs Found While Testing In React

### Unresolved Bugs

## Deployment

## Credits