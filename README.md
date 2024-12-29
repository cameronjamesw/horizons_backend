# Horizons API

![AmIResponsive Image](/assets/amiresponsive.png)

## Project Goals

Prior to developing Horizons, I had 3 major goals in mind that I wanted to achieve with creating this application:
- I wanted to create a sense of community within a particular niche, whereby the content and data provided, as well as the inputted data from the user, were all based around the same theme and community.
- I also wanted to add categorisation to the content in which users were creating - this would make it easier for other users to engage with content that was relevent to them, and it also enables them to filter out any content that they choose not to engage with.
- I wanted to give the user a sense of individuality within their own profile - whereby they could add user-specific information that is strictly relevent to themselves yet allows other users to retrieve and engage with this.
- Finally, I want an 'admin role' to have important within my application, whereby admins can act as mediators to ensure that content which is being shared it relevent and appropiate. These admin users will have the ability to not only retrieve other user's content, but they will also have the ability to destroy another user's content if it is in the best interest of protecting the community.

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
  - [Deployment](#deployment)
  - [Credits](#credits)

## Planning

Planning started by creating epics and user stories for the frontend application, based on the project goals. The user stories were used to inform wireframes mapping out the intended functionality and 'flow' through the app. See the [repo for the frontend React app](/) for more details.

The user stories requiring implementation to achieve a minimum viable product (MVP) were then mapped to API endpoints required to support the desired functionality.
The user stories themselves are recorded [on this Google sheet](https://docs.google.com/spreadsheets/d/1xT0BXdg621rtGnQodwNQhRxqZqIO8vNXq3Ope-zOwR8/edit?usp=sharing), with the required API endpoints mapped to user stories on [a second sheet on the same document](https://docs.google.com/spreadsheets/d/1xT0BXdg621rtGnQodwNQhRxqZqIO8vNXq3Ope-zOwR8/edit?usp=sharing). You may need to manually select the two worksheets, as the Google docs link to the endpoints worksheet sometimes defaults to the user stories sheet.

### Data Models

Data model schema were planned in parallel with the API endpoints, using an entity relationship diagram.

Custom models implemented for Tribehub are: `profile`, `category` and `favourite`.

Below is the database schema in the form of an ERD

![A photo contain the ERDs for the Horizons API](/assets//Model%20databases.png)

#### Profile

Represents the user profile, using a one-to-one relationsip to the user model. A Profile instance is automatically created on user registration. The Profile model includes an `is_admin` field which is added through the Profile Serializer. This field checks whether the profile instance is a superuser, and if so, will be granted admin privileges. This will allow the user to create new categories and delete posts and comments of other users in the view of safeguarding.

Users can edit their own `name`, `island_name`, `friend_code`, `bio` and `image` fields.

#### Category

The category model represents a category within the database - these instances can only be created by admin users, mainly so that they are kept in moderation and they don't spiral out of control. The category model is tied to the post model with a one-to-many relationship. When creating post instances, authorised users are permitted to add their post to a category through a drop down menu - on creation this post instance will then be tied to the category in question.

Users have the option to search for posts based on the category they are part of, and when sifting through categories, the categories will be returned based on their `post_count`, a field added with the `annotate` function. This field will allow users to display the most popular categories - categories which have the most amount of posts tied to them.

When creating and editing a category, admin users can only alter the `name` field.

#### Favourite

The favourite model represents an instance whereby the user can `favourite` a post, and as such the favourite model is tied to the post model in a one-to-many relationship. Users can favourite a post, and the have this post appear in their favourites list on their profile - a component which will only be visible to themselves.

Within the **FavouriteSerializer**, it is ensured that a user will not be able to 'double-favourite' a post - whereby leading to poor UX. This is done through using the `unique_together` field within the favourites/models.py. This insures that the `owner` and `post` feilds are unique together within the database and in turn prevents any duplicates.

### Post

The post model represents an instance within the database whereby authenticated users can create their own post. When creating a post instance, the instance will be tied to the User model, this being accessed through the `owner` field which contains a ForeignKey to the User Model.

Furthermore, users have the option to select a `category`. Upon selecting the field, a dropdown menu of the pre--exsiting categories will be listed to the user - they can choose to add their post to a category if they want to; however, this is not required. This is because the default value within the ForeignKey field is set to `Null`, so a post an exist without being tied to a category. In addiion to this, upon a category being deleted, any posts that are tied to that category will not be deleted, and instead have their value set to `Null`. This is because of the `on-delete=Models.SET_NULL` attribute of the ForeignKey field. If posts got deleted upon the deletion of a category this would provide poor UX. 

Users are able to add and edit fields such as `title`, `content`, `images` and `category`.
Only the post owners will be able to edit and delete their posts - `admins` will be permitted to delete posts is they feel it is necessary in the way of safeguarding.

### Comment

The Comment model is designed to manage user-generated comments on specific posts. Each comment is associated with an `owner` - connected through a ForeignKey to the `User Model` - and a post, again connected through a ForeignKey. 

When creating and editing comments users will be able to edit the `content` field only. The `created_at` and `updated_at` fields will also be returned respectively. The model ensures that comments are displayed in reverse chronological order by default, showing the most recent ones first.

The associated **CommentSerializer** handles the serialization of comment data, including details about the user who made the comment, their profile picture, and the timestamps formatted in a human-readable manner. The **CommentDetailSerializer** extends this by providing additional details, such as the ID of the associated Posts event. This setup enables efficient management and display of comments within the application, fostering interaction and discussion around Posts events.

`Admin users` will also be permitted to delete comments in the view of safeguarding.

### Like

The likes model represents a user liking a specific post for showing their interest. Each like links a user to a Posts, recording when the likes was created. The model enforces that a user can only likes a post once, ensuring no duplicates. The associated **likesSerializer** is responsible for handling the serialization of likes data, including the user and event details. It also includes validation logic to raise an error if a user attempts to likes the same event more than once. This structure supports a clean and efficient way to manage user likes within the application.

### Follower

The Follower model manages the relationships where users follow other users within the application. It establishes a connection between the `owner` (the user who is following) and the `followed` (the user being followed), allowing for tracking of these interactions. Both the fields, `owner` and `followed` have an attribute of a `related_name` when referencing the ForeignKey. This allows the API to easily distinguish between the two fields - as both are referencing the User Model in their ForeignKey. Each follow relationship is time-stamped, showing when it was created, and the model enforces uniqueness to prevent duplicate follow relationships. The data is ordered by the most recent followings by default.

The **FollowerSerializer** is responsible for converting these follow relationships into a serialized format for API responses. It includes fields for the usernames of both the follower and the followed, and it prevents users from following themselves or following the same user multiple times. This ensures the integrity of the following system within the application, supporting functionalities like displaying followers, following counts, and managing user connections.

## API Endpoints

Here is a table containing the API endpoints

### Django AllAuth Endpoints

| **URL** | **Notes** | **HTTP Method** | **CRUD Operation** | **View Type** | **POST/PUT Data Format** |
|---|---|---|---|---|---|
| /dj-rest-auth/registration/ | This allows the user to create an account. It creates a new user instance which in turn creates a new profile instance too. | POST | N/A | N/A | {<br>    "username":"string",<br>    "password":"string",<br>    "password2":"string"<br>} |
| /dj-rest-auth/login/ | This allows the user to log into a pre-existing account by checking the provided data agianst their credentials | POST | N/A | N/A | {<br>    "username":"string",<br>    "password":"string",<br>    "password2":"string"<br>} |
| /dj-rest-auth/logout/ | This allows the user to log out of their account and enter an unauthenticated state. | POST | N/A | N/A | N/A |

### Profile Endpoints

| **URL** | **Notes** | **HTTP Method** | **CRUD Operation** | **View Type** | **POST/PUT Data Format** |
|---|---|---|---|---|---|
| /profiles/ | This endpoint provides a list of profiles to the user. Profiles will be ordered in descending order of creation. | GET | READ | LIST | N/A |
| /profiles/int:pk/ | This endpoint allows the user to retrieve specific profile information and data. | GET | READ | DETAIL | N/A |
| /profiles/int:pk/ | When using the PUT method on the profile detail, only the owner of the profile will be able to update it. Permissions are in place to ensure this. | PUT | UPDATE | DETAIL | {<br>    "owner":"string",<br>    "name":"string",<br>    "island_name":"string",<br> "friend_code":"integer",<br> "bio":"string",<br> "image":"string", <br> "updated_at":"datetimefield" <br>} |

### Posts Endpoints

| **URL** | **Notes** | **HTTP Method** | **CRUD Operation** | **View Type** | **POST/PUT Data Format** |
|---|---|---|---|---|---|
| /posts/ | This endpoint allows the user to retrieve a list of current posts. | GET | READ | LIST | N/A |
| /posts/ | This endpoint allows authenticated users to create new posts. If the data is not valid then the data will not be submitted. | POST | CREATE | LIST | {<br>    "owner":"string",<br>    "title":"string",<br>    "contente":"string",<br> "category":"id",<br> "image":"string", <br> "created_at":"datetimefield" <br>} |
| /posts/int:pk/ | This endpoint allows users to retrieve specific information regarding posts. Any user, authenticated or not, is able to access this endpoint. | GET | READ | DETAIL | N/A |
| /posts/int:pk/ | When updaing posts using this endpoint, only the authenticated post owner, or a site admin, will be able to update a post. Permissions are in place to ensure this. | PUT | UPDATE | DETAIL | {<br>    "owner":"string",<br>    "title":"string",<br>    "contente":"string",<br> "category":"id",<br> "image":"string", <br> "updated_at":"datetimefield" <br>} |
| /posts/int:pk/ | This endpoint allows users to delete their posts if needed. Only the post owner and site admins will be able to delete posts. | DELETE | DELETE | DETAIL | N/A |

### Categories Endponts

| **URL** | **Notes** | **HTTP Method** | **CRUD Operation** | **View Type** | **POST/PUT Data Format** |
|---|---|---|---|---|---|
| /categories/ | This endpoint returns a list of the categories to the user. When recieving the list of categories, users will be able to see how many posts are part of each category. | GET | READ | LIST | N/A |
| /categories/ | This endpoint allows admin users to create new categories, it is reserved for site admins only | POST | CREATE | LIST | {<br>    "owner":"string",<br>    "name":"string",<br>    "created_at":"datetimefield"<br>} |
| /categories/int:pk/ | Here admin users are able to retrieve the details of categories. This endpoint is again reserved for admins. | GET | READ | DETAIL | N/A |
| /categories/int:pk/ | The PUT method endpoint is again reserved for admin users only. Specific permissions are put in place to guarantee this. | PUT | UPDATE | DETAIL | {<br>    "owner":"string",<br>    "name":"string",<br>    "updated_at":"datetimefield"<br>} |
| /categories/int:pk/ | When deleting categories, this endpoint is reserved specifically for admin users. Upon deletion, any posts that are related to the deleted category will have their category set to NULL. | DELETE | DELETE | DETAIL | N/A |

### Comments Endpoints

| **URL** | **Notes** | **HTTP Method** | **CRUD Operation** | **View Type** | **POST/PUT Data Format** |
|---|---|---|---|---|---|
| /comments/ | When using this endpoint, a list of comments are returned to the user, each comment is related to a post. Upon deletion of a post, all comments related to that post are deleted too. | GET | READ | LIST | N/A |
| /comments/ | This endpoint allows authenticated users to create comments which will be linked to the related post. | POST | CREATE | LIST | {<br>    "owner":"string",<br>    "post":"id",<br> "content":"string",<br>    "created_at":"datetimefield"<br>} |
| /comments/int:pk/ | This endpoint returns the detail of a specific comment by fetching it with it's comment ID. | GET | READ | DETAIL | N/A |
| /comments/int:pk/ | This endpoint allows authenticated owners to update their comment if needed. Admin users are also permitted to update other user's comment if neccessary. | PUT | UPDATE | DETAIL | {<br>    "owner":"string",<br>    "post":"id",<br> "content":"string",<br>    "updated_at":"datetimefield"<br>} |
| /comments/int:pk/ | This endpoint allows users to delete their comment from a post. Only the comment owner and admin users have the permission to delete comments. | DELETE | DELETE | DETAIL | N/A |

### Favourites Endpoints

| **URL** | **Notes** | **HTTP Method** | **CRUD Operation** | **View Type** | **POST/PUT Data Format** |
|---|---|---|---|---|---|
| /favourites/ | When using this endpoint a list of the favourite instances are returned to the user. | GET | READ | LIST | N/A |
| /favourites/ | Upon using this endpoint, authenticated users are able to create a new instance of a favourite. Each favourite instance is tied to a post, and users will be unable to favourite a post more than once. | POST | CREATE | LIST | {<br>    "owner":"string",<br>    "post":"id",<br>    "created_at":"datetimefield"<br>} |
| /favourites/int:pk/ | This endpoint returns details about the specific favourite instance requested. | GET | READ | DETAIL | N/A |
| /favourites/int:pk/ | This allows the owner of the favourite instance to delete the favourite. Permissions are in place to ensure that only the owners are permitted to do so. | DELETE | DELETE | DETAIL | N/A |

### Likes Endpoints

| **URL** | **Notes** | **HTTP Method** | **CRUD Operation** | **View Type** | **POST/PUT Data Format** |
|---|---|---|---|---|---|
| /likes/ | This endpoint returns a list of all the like instances to the user upon request. | GET | READ | LIST | N/A |
| /likes/ | This endpoint allows authenticated users to create a new like instance. Permissions are in place to ensure that only authenticated users are able to access this endpoint. | POST | CREATE | LIST | {<br>    "owner":"string",<br>    "post":"id",<br>    "created_at":"datetimefield"<br>} |
| /likes/int:pk/ | By following this endpoint, users are able to retrieve a detailed view of the specific like instance requested with the ID. | GET | READ | DETAIL | N/A |
| /likes/int:pk/ | This endpoint allows users to delete their like instance, this permission is reserved for the like owner. | DELETE | DELETE | DETAIL | N/A |

### Followers Endpoints

| **URL** | **Notes** | **HTTP Method** | **CRUD Operation** | **View Type** | **POST/PUT Data Format** |
|---|---|---|---|---|---|
| /followers/ | This endpoint returns a list all of the follower instances. | GET | READ | LIST | N/A |
| /followers/ | When authenticated, this endpoint allows users to create their own follower instance, essentially following another user. Permissions are in place to prohibit unauthenticated users from accessing this endpoint. Users are unable to create two follower instances that are tied to the same profile. | POST | CREATE | LIST | {<br>    "owner":"string",<br>    "followed":"id",<br>    "created_at":"datetimefield"<br>} |
| /followers/int:pk/ | This endpoint displays a detailed view of specific follower instances. | GET | READ | DETAIL | N/A |
| /followers/int:pk/ | This endpoint allows the owners of the follower instances to delete their instance. | DELETE | DELETE | DETAIL | N/A |

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

Testing for the Horizons API can be found in the [TESTING.md](/TESTING.md) folder.

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

- [Very Academy](https://www.youtube.com/watch?v=W_5KQeU4Qtg&list=PLOLrQ9Pn6cazL1rwTY2d66M9VppexGL-_&index=17) - This video of theirs gave me a great deal of inspiration when designing my Entity Relationship Diagrams.

- [This article](https://stackoverflow.com/questions/37968770/django-rest-framework-permission-isadminorreadonly) from Stack Overflow helped me design the `IsAdminOrReadOnly` permission in `horizons_backend.permissions.py`

- [This article](https://stackoverflow.com/questions/45563194/django-rest-permissions-allow-both-isadmin-and-custom-permission) from Stack Overflow helped me code the `IsOwnerOrAdmin` permission is `horizons_backend.permissions.py`

- Credit to Andy Gutteridge and his exceptional [ReadMe](https://github.com/andy-guttridge/tribehub_drf) which helped me grasp an efficient and effective structure moving forward.

- Credit to Code Institutes's content regarding serializers, in particular the post and likes serializers.