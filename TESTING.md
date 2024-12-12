# Horizons API

## Project Goals

## Table of Contents

- [Horizons API](#horizons-api)
  - [Project Goals](#project-goals)
  - [Table of Contents](#table-of-contents)
  - [Testing](#testing)
    * [Manual Testing](#manual-testing)
    * [Python Validation](#python-validation)
    * [Resolved Bugs](#resolved-bugs)
      + [Bugs Found While Testing API In Isolation](#bugs-found-while-testing-api-in-isolation)
      + [Bugs Found While Testing In React](#bugs-found-while-testing-in-react)
    * [Unresolved Bugs](#unresolved-bugs)

## Testing

### Manual Testing

#### Testing Methodology

A series of manual tests have been planned out accordingly to the end points previously noted in [ReadMe.md](/README.md). 

A series of `TestUsers` have been created in the view of testing, and these accounts shall be used when testing the application.
- `TestUser1` is a superuser that has admin privelleges, so should be able to create, edit and deletes categories, as well as delete posts and comments of other users in the view of safeguarding.
- `TestUser2` is a standard user who will be authenticated throughout the testing process. They should be able to create and edit their own posts, like, comment and favourite post too. But they are denied admin priveleges, so they will not be able to update or delete another user's post or comment, and they will not be able to access the category detail view, as well as create a category.
- `TestUser3` will be an unauthenticated user, so they will be able to view the data fetched with the API, but they will not be able to mutilate it in anyway.

These tests will be group by endpoint to viewing more manageable.

**Profile Testing**

| Test ID | Endpoint | HTTP Method | User | Test Case | Expected Outcome | Actual Outcome | Pass |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | /profiles/ | GET | TestUser1 | Navigate to /profiles/ | Retrieve a list of profiles with 200 status code | Profiles displayed along with HTTP 200 OK | Pass |
| 2 | /profiles/id | GET | TestUser1 | Navigate to /profiles/1 | Retrieve profile with id of 1 | Profile #1 displayed along with HTTP 200 OK | Pass |
| 3 | /profiles/id | PUT | TestUser1 | Update TestUser1's profile | Successfully update profile with Status 200 code | Profile updated with correct data along with HTTP 200 OK | Pass |
| 4 | /profiles/id | PUT | TestUser1 | Add more than 12 characters to friendcode field | Status 400 error with error message, maximum of 12 characters | Status 400 Error, ensure this field has no more than 12 characters  | Pass |
| 5 | /profiles/id | PUT | TestUser1 | Update TestUser2's profile | 403 Forbidden Code | Status code 403 Forbidden - You do not have permission to perform this action | Pass |
| 6 | /profiles/id | PUT | TestUser2 | Update TestUser2's profile | Successfully update profile with Status 200 code | Profile updated with correct data along with HTTP 200 OK |Passs |
| 7 | /profiles/id | PUT | TestUser3 | Update TestUser3's profile while unauthenticated | Unable to update profile as unauthenticated | Status 403 Code - Authentication credentials not provided | Pass |

**Category Testing**

| Test ID | Endpoint | HTTP Method | User | Test Case | Expected Outcome | Actual Outcome | Pass |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | /categories/ | GET | TestUser1 | Navigate to /categories/ | Return a list of categories with status 200 code | Returned list of categories, status code 200 | Pass |
| 9 | /categories/ | GET | TestUser3 | Navigate to /categories/ while unauthenticated | Return a list of categories with status 200 code | Returned list of categories, status code 200 | Pass |
| 10 | /categories/ | POST | TestUser1 | Create a new category as admin | Successfully create new category with status 201 code | Created new category, status code 201 - created | Pass |
| 12 | /categories/ | POST | TestUser2 | Create a new category as user | Not permitted, 403 error | Status code 403 Forbidden - You do not have permission to perform this action | Pass |
| 13 | /categories/ | POST | TestUser3 | Create a new category while unauthenticated | Not permitted, 403 error | Status code 403 Forbidden - You do not have permission to perform this action | Pass |
| 14 | /categories/id | PUT | TestUser1 | Edit category as admin | Successfully updated category with status 200 code | Updated category, status code 200 - ok | Pass |
| 15 | /categories/id | PUT | TestUser2 | Navigate to categories/id as user | Status 403 Code - Forbidden | Status 403 Code, Forbidden - You do not have permission to perform this action | Pass |
| 16 | /categories/id | PUT | TestUser3 | Navigate to categories/id while unauthenticated | Status 403 Code - Forbidden | Status 403 Code, Forbidden - Authenticated credentials were not provided | Pass |
| 17 | /categories/id | DELETE | TestUser1 | Delete category | Successfully deleted categpry | Status 204 Code, No content - Category successfully deleted | Pass |

**Post Testing**

| Test ID | Endpoint | HTTP Method | User | Test Case | Expected Outcome | Actual Outcome | Pass |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 18 | /posts/ | GET | TestUser1 | Navigate to /posts/ as admin | Display list of posts | Displayed list of posts, status 200 code | Pass |
| 19 | /posts/ | GET | TestUser2 | Navigate to /posts/ as user | Display list of posts | Displayed list of posts, status 200 code | Pass |
| 20 | /posts/ | GET | TestUser3 | Navigate to /posts/ while unauthenticated | Display list of posts | Displayed list of posts, status 200 code | Pass |
| 21 | /posts/ | POST | TestUser1 | Create new post as admin | Successfully create new post | Post created, status 201 code - created | Pass |
| 22 | /posts/ | POST | TestUser2 | Create new post as user | Successfully create new post | Post created, status 201 code - created | Pass |
| 23 | /posts/ | POST | TestUser3 | Create a new post while unauthenticated | Not permitted, 403 error | Status code 403 Forbidden - Authentication credentials were not provided | Pass |
| 24 | /posts/id | GET | TestUser1 | Navigate to /posts/id as admin | Display specific post by ID | Displayed specific post by ID, status 200 code | Pass |
| 25 | /posts/id | GET | TestUser2 | Navigate to /posts/id as user | Display specific post by ID | Displayed specific post by ID, status 200 code | Pass |
| 26 | /posts/id | GET | TestUser3 | Navigate to /posts/id while unauthenticated | Display specific post by ID | Displayed specific post by ID, status 200 code | Pass |
| 27 | /posts/id | PUT | TestUser1 | Update specific post with new data as admin | Post updated successfully, status code 200 | Successfully updated post, status 200 code | Pass |
| 28 | /posts/id | PUT | TestUser2 | Update specific post with new data as user | Post updated successfully, status code 200 | Successfully updated post, status 200 code | Pass |
| 29 | /posts/id | PUT | TestUser3 | Update specific post with new data while unauthenticated | Error, status 403 code | Status 403 code, forbidden - Authentication credentials were not provided | Pass |
| 30 | /posts/id | PUT | TestUser1 | Update TestUser2's post as admin | Post updated successfully, status code 200 | Successfully updated post, status 200 code | Pass |
| 31 | /posts/id | PUT | TestUser2 | Update another user's post | Status 403 Code - Forbidden | Status 403 Code, Forbidden - You do not have permission to perform this action | Pass |
| 32 | /posts/id | DELETE | TestUser1 | Delete post | Post deleted successfully, status code 204 | Successfully deleted post, status 204 code | Pass |
| 33 | /posts/id | DELETE | TestUser1 | Delete TestUser2's post | Post deleted successfully, status code 204 | Successfully deleted post, status 204 code | Pass |
| 34 | /posts/id | DELETE | TestUser2 | Delete own post | Post deleted successfully, status code 204 | Successfully deleted post, status 204 code | Pass |
| 35 | /posts/id | DELETE | TestUser2 | Delete another user's post | Status 403 Code - Forbidden | Status 403 Code, Forbidden - You do not have permission to perform this action | Pass |
| 36 | /posts/id | DELETE | TestUser3 | Delete another user's post while unauthenticatedd | Status 403 Code - Forbidden | Status 403 Code, Forbidden - Authentication credentials were not provided | Pass |

**Comments Testing**

| Test ID | Endpoint | HTTP Method | User | Test Case | Expected Outcome | Actual Outcome | Pass |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 37 | /comments/ | GET | TestUser1 | Navigate to /comments/ as admin | Display list of comments | Displayed list of comments, status 200 code | Pass |
| 38 | /comments/ | GET | TestUser2 | Navigate to /comments/ as user | Display list of comments | Displayed list of comments, status 200 code | Pass |
| 39 | /comments/ | GET | TestUser3 | Navigate to /comments/ while unauthenticated | Display list of comments | Displayed list of comments, status 200 code | Pass |
| 40 | /comments/ | POST | TestUser1 | Create new comment as admin | Successfully create new comment | Comment created, status 201 code - created | Pass |
| 41 | /comments/ | POST | TestUser2 | Create new comment as user | Successfully create new comment | Comment created, status 201 code - created | Pass |
| 42 | /comments/ | POST | TestUser3 | Create a new comment while unauthenticated | Not permitted, unable to access comment form | Status code 403 Forbidden - Authentication credentials were not provided | Pass |
| 43 | /comments/id | GET | TestUser1 | Navigate to /comments/id as admin | Display specific comment by ID | Displayed specific comment by ID, status 200 code | Pass |
| 44 | /comments/id | GET | TestUser2 | Navigate to /comments/id as user | Display specific comment by ID | Displayed specific comment by ID, status 200 code | Pass |
| 45 | /comments/id | GET | TestUser3 | Navigate to /comments/id while unauthenticated | Display specific comment by ID | Displayed specific comment by ID, status 200 code | Pass |
| 46 | /comments/id | PUT | TestUser1 | Update specific comment with new data as admin | Comment updated successfully, status code 200 | Successfully updated comment, status 200 code | Pass |
| 47 | /comments/id | PUT | TestUser2 | Update specific comment with new data as user | Comment updated successfully, status code 200 | Successfully updated comment, status 200 code | Pass |
| 48 | /comments/id | PUT | TestUser3 | Update specific comment with new data while unauthenticated | Error, status 403 code | Status 403 code, forbidden - Authentication credentials were not provided | Pass |
| 49 | /comments/id | PUT | TestUser1 | Update TestUser2's comment as admin | Comment updated successfully, status code 200 | Successfully updated comment, status 200 code | Pass |
| 50 | /comments/id | PUT | TestUser2 | Update another user's comment | Status 403 Code - Forbidden | Status 403 Code, Forbidden - You do not have permission to perform this action | Pass |
| 51 | /comments/id | DELETE | TestUser1 | Delete comment | Comment deleted successfully, status code 204 | Successfully deleted comment, status 204 code | Pass |
| 52 | /comments/id | DELETE | TestUser1 | Delete TestUser2's comment | Post deleted successfully, status code 204 | Successfully deleted comment, status 204 code | Pass |
| 53 | /comments/id | DELETE | TestUser2 | Delete own comment | Comment deleted successfully, status code 204 | Successfully deleted comment, status 204 code | Pass |
| 54 | /comments/id | DELETE | TestUser2 | Delete another user's comment | Status 403 Code - Forbidden | Status 403 Code, Forbidden - You do not have permission to perform this action | Pass |
| 55 | /comments/id | DELETE | TestUser3 | Delete another user's comment while unauthenticatedd | Status 403 Code - Forbidden | Status 403 Code, Forbidden - Authentication credentials were not provided | Pass |

**Followers Testing**

| Test ID | Endpoint | HTTP Method | User | Test Case | Expected Outcome | Actual Outcome | Pass |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 56 | /followers/ | GET | TestUser1 | Navigate to /followers/ as admin | Display list of followers | Displayed list of followers, status 200 code | Pass |
| 57 | /followers/ | GET | TestUser2 | Navigate to /followers/ as user | Display list of followers | Displayed list of followers, status 200 code | Pass |
| 58 | /followers/ | GET | TestUser3 | Navigate to /followers/ while unauthenticated | Display list of followers | Displayed list of comments, status 200 code | Pass |
| 59 | /followers/ | POST | TestUser1 | Create new follower instance as admin | Successfully create new follower instance | Instance created, status 201 code - created | Pass |
| 60 | /followers/ | POST | TestUser2 | Create new follower instance as user | Successfully create new follower instance | Instance created, status 201 code - created | Pass |
| 61 | /followers/ | POST | TestUser3 | Create a new follower instance while unauthenticated | Not permitted, unable to follow user | Status code 403 Forbidden - Authentication credentials were not provided | Pass |
| 62 | /followers/ | POST | TestUser2 | Attempt to double follow a user already followed | Error, possible duplicate | 400 Bad Request, possible duplicate | Pass |
| 63 | /followers/id | DELETE | TestUser1 | Delete follow instance | Instance deleted successfully, status code 204 | Successfully deleted follow instance, status 204 code | Pass |
| 64 | /followers/id | DELETE | TestUser2 | Delete own follow instance | Instance deleted successfully, status code 204 | Successfully deleted follow instance, status 204 code | Pass |
| 65 | /followers/id | DELETE | TestUser2 | Delete another user's follow instance | Status 403 Code - Forbidden | Status 403 Code, Forbidden - You do not have permission to perform this action | Pass |
| 66 | /followers/id | DELETE | TestUser3 | Delete another user's follow instance while unauthenticatedd | Status 403 Code - Forbidden | Status 403 Code, Forbidden - Authentication credentials were not provided | Pass | 

**Likes Testing**

| Test ID | Endpoint | HTTP Method | User | Test Case | Expected Outcome | Actual Outcome | Pass |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 67 | /likes/ | GET | TestUser1 | Navigate to likes/ as admin | Display list of likes | Displayed list of likes, status 200 code | Pass |
| 68 | /likes/ | GET | TestUser2 | Navigate to /likes/ as user | Display list of likes | Displayed list of likes, status 200 code | Pass |
| 69 | /likes/ | GET | TestUser3 | Navigate to /likes/ while unauthenticated | Display list of likes | Displayed list of comments, status 200 code | Pass |
| 70 | /likes/ | POST | TestUser1 | Create new like instance as admin | Successfully create new like instance | Instance created, status 201 code - created | Pass |
| 71 | /likes/ | POST | TestUser2 | Create new like instance as user | Successfully create new like instance | Instance created, status 201 code - created | Pass |
| 72 | /likes/ | POST | TestUser3 | Create a new like instance while unauthenticated | Not permitted, unable to like user | Status code 403 Forbidden - Authentication credentials were not provided | Pass |
| 73 | /likes/ | POST | TestUser2 | Attempt to double like a user's post that is already liked | Error, possible duplicate | 400 Bad Request, possible duplicate | Pass |
| 74 | /likes/id | DELETE | TestUser1 | Delete like instance | Instance deleted successfully, status code 204 | Successfully deleted like instance, status 204 code | Pass |
| 75 | /likes/id | DELETE | TestUser2 | Delete own like instance | Instance deleted successfully, status code 204 | Successfully deleted like instance, status 204 code | Pass |
| 76 | /likes/id | DELETE | TestUser2 | Delete another user's like instance | Status 403 Code - Forbidden | Status 403 Code, Forbidden - You do not have permission to perform this action | Pass |
| 77 | /likes/id | DELETE | TestUser3 | Delete another user's like instance while unauthenticatedd | Status 403 Code - Forbidden | Status 403 Code, Forbidden - Authentication credentials were not provided | Pass |

**Favourites Testing**

| Test ID | Endpoint | HTTP Method | User | Test Case | Expected Outcome | Actual Outcome | Pass |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | /favourites/ | GET | TestUser1 | Navigate to favourites/ as admin | Display list of favourites | Displayed list of favourites, status 200 code | Pass |
| 79 | /favourites/ | GET | TestUser2 | Navigate to /favourites/ as user | Display list of favourites | Displayed list of favourites, status 200 code | Pass |
| 80 | /favourites/ | GET | TestUser3 | Navigate to /favourites/ while unauthenticated | Display list of favourites | Displayed list of comments, status 200 code | Pass |
| 81 | /favourites/ | POST | TestUser1 | Create new favourite instance as admin | Successfully create new favourite instance | Instance created, status 201 code - created | Pass |
| 82 | /favourites/ | POST | TestUser2 | Create new favourite instance as user | Successfully create new favourite instance | Instance created, status 201 code - created | Pass |
| 83 | /favourites/ | POST | TestUser3 | Create a new favourite instance while unauthenticated | Not permitted, unable to favourite user | Status code 403 Forbidden - Authentication credentials were not provided | Pass |
| 84 | /favourites/ | POST | TestUser2 | Attempt to double favourite a user's post that is already favourited | Error, possible duplicate | 400 Bad Request, possible duplicate | Pass |
| 85 | /favourites/id | GET | TestUser1 | Navigate to /favourites/id as admin | Display specific favourite instance by ID | Displayed specific favourite instance by ID, status 200 code | Pass |
| 86 | /favourites/id | GET | TestUser2 | Navigate to /favourites/id as user | Display specific favourite instance by ID | Displayed specific favourite instance by ID, status 200 code | Pass |
| 87 | /favourites/id | GET | TestUser3 | Navigate to /favourites/id while unauthenticated | Display specific favourite instance by ID | Displayed specific favourite instance by ID, status 200 code | Pass |
| 88 | /favourites/id | DELETE | TestUser1 | Delete favourite instance | Instance deleted successfully, status code 204 | Successfully deleted favourite instance, status 204 code | Pass |
| 89 | /favourites/id | DELETE | TestUser2 | Delete own favourite instance | Instance deleted successfully, status code 204 | Successfully deleted favourite instance, status 204 code | Pass |
| 90 | /favourites/id | DELETE | TestUser2 | Delete another user's favourite instance | Status 403 Code - Forbidden | Status 403 Code, Forbidden - You do not have permission to perform this action | Pass |
| 91 | /favourites/id | DELETE | TestUser3 | Delete another user's favourite instance while unauthenticatedd | Status 403 Code - Forbidden | Status 403 Code, Forbidden - Authentication credentials were not provided | Pass |

### Python Validation

All files containing custom Python code were validated using the [Code Institute Python Linter](https://pep8ci.herokuapp.com/):

- `category/admin.py`: no errors found
- `category/models.py`: no errors found
- `category/serializers.py`: no errors found
- `category/urls.py`: no errors found
- `category/views.py`: no errors found

- `comments/admin.py`: no errors found
- `comments/models.py`: no errors found
- `comments/serializers.py`: no errors found
- `comments/urls.py`: no errors found
- `comments/views.py`: no errors found

- `favourites/admin.py`: no errors found
- `favourites/models.py`: no errors found
- `favourites/serializers.py`: no errors found
- `favourites/urls.py`: no errors found
- `favourites/views.py`: no errors found

- `followers/admin.py`: no errors found
- `followers/models.py`: no errors found
- `followers/serializers.py`: no errors found
- `followers/urls.py`: no errors found
- `followers/views.py`: no errors found

- `horizons_backend/permissions.py`: no errors found
- `horizons_backend/settings.py`: no errors found
- `horizons_backend/serializers.py`: no errors found
- `horizons_backend/urls.py`: no errors found
- `horizons_backend/views.py`: no errors found

- `likes/admin.py`: no errors found
- `likes/models.py`: no errors found
- `likes/serializers.py`: no errors found
- `likes/urls.py`: no errors found
- `likes/views.py`: no errors found

- `posts/admin.py`: no errors found
- `posts/models.py`: no errors found
- `posts/serializers.py`: no errors found
- `posts/urls.py`: no errors found
- `posts/views.py`: no errors found

- `profiles/admin.py`: no errors found
- `profiles/models.py`: no errors found
- `profiles/tests.py`: no errors found
- `profiles/serializers.py`: no errors found
- `profiles/urls.py`: no errors found
- `profiles/views.py`: no errors found

### Resolved Bugs

#### Bugs Found While Testing API In Isolation

#### Bugs Found While Testing In React

### Unresolved Bugs