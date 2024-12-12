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
`TestUser1` is a superuser that has admin privelleges, so should be able to create, edit and deletes categories, as well as delete posts and comments of other users in the view of safeguarding.
`TestUser2` is a standard user who will be authenticated throughout the testing process. They should be able to create and edit their own posts, like, comment and favourite post too. But they are denied admin priveleges, so they will not be able to update or delete another user's post or comment, and they will not be able to access the category detail view, as well as create a category.
`TestUser3` will be an unauthenticated user, so they will be able to view the data fetched with the API, but they will not be able to mutilate it in anyway.

These tests will be group by endpoint to viewing more manageable.

**Profile Testing**

| Test ID | Endpoint | Test Case | Expected Outcome | Actual Putcome | Pass |
| --- | --- | --- | --- | --- | --- |
| Test |

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