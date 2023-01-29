# Table of Content
1. [Functionality](#functionality)
2. [Installation](#installation)
3. [Beginner's Guide](#guide)
4. [Backend Database Models](#databasemodels)
    1. [User Model](#usermodel)
    2. [Product Model](#productmodel)
    3. [Order Model](#ordermodel)
5. [Backend Serializers](#serializers)
    1. [User Serializer](#userserializer)
    2. [Product Serializer](#productserializer)
    3. [Order Serializer](#orderserializer)
6. [Backend Views](#views)
    1. [Product View](#productview)
    2. [Order View](#orderview)
7. [Backend Urls](#urls)
8. [Backend Settings](#settings)
9. [Frontend Store](#stores)
    1. [Token Store](#tokenstore)
    2. [Cart Store](#cartstore)
    3. [Request Store](#requeststore)
10. [Frontend Components](#components)
11. [Frontend Views](#frontendviews)  
    1. [Home View](#homeview)
        1. [Pagination](#pagination)
        2. [Watcher for Search Input](#searchwatcher)
        3. [Vue Toast](#vuetoast)
    2. [Product View](#productview)
    3. [Categories View](#categoryview)
    4. [Vendors View](#vendorview)
    5. [Add Product View](#addproductview)
    6. [Cart View](#cartview)
    7. [User Page View](#userpageview)
    8. [Register SignIn and Edit Profile View](#registersignineditprofileview)
12. [Frontend Router](#frontendrouter)






# Functionality <a name="functionality"></a>
With the Ecomm, you can register as a new user and sign in, you can add new products, order products, follow your sold product history, follow your order history, you can navigate user specific products or category specific products,search products,comment on products and more in the future hopefully.

# Installation <a name="installation"></a>
 Project developed in virtual environment. You can install Python required packages with requirements.txt, node requirements can be found on package.json.
 For python dependencies initialize;
 `pip install -r requirements.txt`
 and for node modules initialize;
 `npm install`
 in your project directory. Detailed installation guide can be found in the 'Beginners Guide' section for the users who are not familiar with GitHub, Django or Vue.

# Beginner's Guide <a name="guide"></a>
To use E-commerce, first clone repository by using your terminal;
<br/>
`git clone https://github.com/atoprak06/eCommerceWithMultipleVendors-Django-Vue.git`
<br/>
 then cd  into your cloned directory in your terminal
 <br/>
 `cd eCommerceWithMultipleVendors-Django-Vue`
 <br/>
  and create virtual environment using 
<br/>
`python -m venv env`
<br/>
using virtual environment is recommended by python official docs as it creates separate environment for your dependencies in development phase, detailed info can be found in here: https://docs.python.org/3/library/venv.html
<br/>
After installing virtual environment, open root directory in your code editor. To activate virtual environment open new terminal and use command below if you are on windows, if you are not using windows you can find how to activate it on the doc link above.
<br>
`env/scripts/activate`
<br/>
Now you will see `(env)` at the start of your root path in the terminal and it indicates that it's activated successfully. Now we are ready to install dependencies. First, lets install python side dependencies. Using pip in your terminal
<br/>
`pip install -r requirements.txt`
<br/>
will install all backend related dependencies used in this project and their related dependencies. You can see all of it,  by using command below if you are interested.
<br/>
`pip list`
<br/>
Now we are ready to install front end side dependencies. In your terminal cd into your front end directory
<br/>
`cd ecommfrontend`
<br/>
Note that for the front end you need to have Node.js installed. If you are not sure if it's installed you can check it by using command below in your terminal
<br/>
`node -v`
<br/>
If you can see any version then its good to go, but if there is nothing, visit https://nodejs.org/en/ and install it with LTS labeled option.
Now we can install front end dependencies with the command :
<br />
`npm install`
<br/>
With that project is installed successfully and ready to start servers.
Before starting backend server we need to migrate our database. First cd into ecommbackend and then use command below to migrate models and create database.
<br/>
`python manage.py migrate`
<br/>
Note that, here, we used default sqlite3 database provided by Django.  Also let's create admin user to see our admin panel by using
<br/>
`python manage.py createsuperuser`
<br/>
Enter your username and password in the terminal and you will create your first admin user. Finally we can start our server using command:
<br/>
`python manage.py runserver`
<br/>
After it initializes, you will see that there is link points to http://127.0.0.1:8000/ (or different depends on your machine)  on the terminal. Now lets visit admin page where its located at http://127.0.0.1:8000/admin in your browser. Login with username and password that you just created. Now you can see some sections in there which will be explained later in the docs. Before creating new products first we need to create some categories. Add some categories by simply going to 'Categories' under the PRODUCTS section and click 'Add Category'. Enter category name and slug(you can enter same name as category name with all lower case letters and '-' instead of 'spaces').Now you can create products by visiting products section. Now lets start our front end server. Use different terminal and cd into your ecommfrontend directory and trigger command:
<br/>
`npm run serve`
<br/>
After it initializes, you can then visit  http://localhost:8080/ (or different depends on your machine, check your terminal. If it is different modify `CORS_ALLOWED_ORIGINS` in the settings.py file accordingly) and navigate it. From there on, docs will include how the project works.

# Backend Database Models<a name="databasemodels"></a>
## User <a name="usermodel"></a>
For the user model Django default AbstractUser is used with the extra fields. Note that to activate this user model, in the settings you need to point `AUTH_USER_MODEL` field to the user model.
<br/>
`AUTH_USER_MODEL = 'user.UserProfile'`
<br/> 
It's good to mention about *is_vendor* field that has been created. This field's state will decide if that user's product will be presented on the front end or not. User can alter its *is_vendor* state by visiting edit profile on the front end.

## Products <a name="productmodel"></a>
For the products, 4 main model is created. *Category, Product, Comments* and *Comment* models.
### - Category
This model can be altered by just the admin user on the backend. Before creating product instances, there should be categories already created.
### - Product
It is the main product model. *category* and *created_by* fields are linked to Category and User models respectively using one to many relationship.
### - Comments
Every product should have a comment section, so it is created for this purpose and linked to product with one to one relationship.
### - Comment
Every comment created by users should be stored in database. It is linked to *Comments* model with one to many relationship.

## Order <a name="ordermodel"></a>
There are 2 model created for this section, *Order* and *OrderItem*
### - Order
It represent order created by the users. It is linked to User model with one to many relationship.
### - OrderItem
Products that has been added to order is represented by this model. It is linked to *Order* and *Product* models with one to many relationship.

# Backend Serializers<a name="serializers"></a>
Django default models can't be represented on the API as the way they are, so DRF serializers are used to show them as JSON represented data in this project. ModelSerializers class is used since it is very powerful when creating shortcut representation of models that has been created already. Detailed info can be found on the DRF documents: https://www.django-rest-framework.org/api-guide/serializers


## User  Serializers <a name="userserializes"></a>
In this project token based authentication is used
for the user authentication. Token creating, token destroy, registration of the user is made with the help of the third party module called `Djoser`. It is REST implementation of Django authentication system, it provides already built-in Views for the registration, login, logout, password reset and account activation. Detailed info can be found in the link: https://djoser.readthedocs.io/en/latest/index.html. Before explaining of the User serializers, in the settings of django, djoser settings should be added as below.

 `DJOSER =
 `<br/>`
  {
    `<br/>`    
    'SERIALIZERS': {
      `<br/>`
         'user' : 'user.serializers.UserShowSerializerEdit',
         'current_user' :'user.serializers.UserShowSerializerEdit',         
         'user_create_password_retype': 'user.serializers.UserRegistrationSerializer',
    `<br/>`
    },
    `<br/>`
    'USER_CREATE_PASSWORD_RETYPE':True,
    `<br/>`   
}`

Note that password retype is activated for the re password field of the registration form. Also DRF settings in the settings.py modified as token based authentication for the front end and session based authentication on the API end points. Default permissions are modified as if user is authenticated or readonly. It can be seen at the below.
<br/>
`REST_FRAMEWORK = {   
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 16,
    'DEFAULT_AUTHENTICATION_CLASSES':(
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES':(
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}`
<br/>
Note that pagination is activated with the 16 items per page.

### UserRegistrationSerializer
UserRegistrationSerializer is created for the basic user registration with the help of `UserCreatePasswordRetypeSerializer` of the djoser serializers.The `User` model that we created before is used for this serializer. Registration is modified like when the new user is registering re type of the password should be used. Validations of the user register like, if the username that has been used within the form is already exists or not, if the email is already exists, if the passwords are matching or in the correct format is achieved easily with the help of this serializer. Note that it is added to djoser settings on the above with the field of `user_create_password_retype`

### UserSerializer
This serializer is used for the representation of the user on the api. User can fetch it's information or patch it with the help of the djoser `UserSerializer`. User model is used similarly for this.  Note that it is added to djoser settings on the above with the fields of `user` and `current_user`. Key 'user' is used for general users whereas 'current_user' lets you set serializer for special /users/me endpoint. 


## Products  Serializers <a name="productserializer"></a>
### ProductSerializer
For the product serializer, Product model is used. `category` and `created_by` related fields of the product is represented on the API with the help of `SlugRelatedField` and `ReadOnlyField` respectively. `category` is represented on the API as the title field of the category model and `created_by` is showed as username field of the user model. Id of the product and created_by can't be updated on the api as it is modified as readonly fields.

### CategorySerializer
For the category serializer, Category model is used. Title and id fields are used in here. 

### CommentSerializer
Comment model is used for this serializer. Related field user is interpreted by `SlugRelatedField` for the API since just username of the user is needed.

## Order Serializers <a name="orderserializer"></a>
### OrderItemSerializer
 OrderItem model is used. Related field product is interpreted with the `ProductSerializer` that has been created already. This serializer represents items that has been ordered.

### OrderSerializer 
Order model is used. Related field products is interpreted with the OrderItemSerializer created above. It represents orders and products that belongs to this order. 

### OrderedItemSerializer
This serializer is used for the representation of the products that user has and got bought by the other users. Note that it inherits from the OrderItemSerializer that has been created before. Additionally new class Order is created for the purpose of the order interpretation with the customer and order id fields. Meta class is also inherited from OrderItemSerializer.Meta, just fields changed. So user can see products that he owns and got bought by the others in the format that is meaningful.


# Backend Views <a name="views"></a>
Class based views are used for this project. DRF has a nice class called ViewSet and it allows similar logic of the related views to be combined under same class, detailed info can be found in the documentation of the DRF : https://www.django-rest-framework.org/api-guide/viewsets/

## Products <a name="productview"></a>

### ProductViewSet
This viewset is used for the purpose of the how the modeled and serialized product data should look on the API. It inherits from `MultiSerializerViewSet` since there are two different serializer used. MultiSerializerViewSet determines which serializer should be used in different actions, for the default actions listed in the default ViewSet methods in the DRF docs, `ProductSerializer` is used. For the `comments` action `CommentSerializer` is used. `actions` are decorators that is used when you want to define custom method for your viewset docs: https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing . Here permission class of `IsOwnerOrReadOnly` is used, since product data should be readonly if user is not authenticated, if user is authenticated, user can update product data if it is their product or can create new product. Also django_filter module is used for the filtering data using `ProductFilter` class which is inherited from `django_filters.FilterSet`, filter fields can be seen in fields array. Django filter allows users to filter queryset based on model fields, detailed info can be found on the documents: https://django-filter.readthedocs.io/en/stable/. Note that in the DRF settings in the settings.py `'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']` is modified like this to use django_filter module as a default filter. There are two custom action defined: `my_products` and `comments`. First one is to determine when user request their products created by them, second one is to get comments on the specific product or post comment on that same product. Note that there is also `perform_create` method that creates slug field when user create new product, slug field is created with the help of `slugify` method.


### CategoryViewSet
This Viewset determines how category data should look like on the API. Here just plain queryset is used.

## Order <a name="orderview"></a>

### OrderViewSet
This viewset did all the job for the order and orderitem data on the API. Permission class is modified as authenticated since authenticated users should be able to make new orders or get their order history data. `get_queryset` returns orders that belongs to the user who requested the data. Default `create` method of modelViewSet is overridden. When the user makes order on the front end, first order data is created then items in the cart that has been sent as a request data is extracted and orderitems are created. Custom `orderedProducts` action is created for the purpose of the user to be able too see products that belongs to them has been sold. Queryset is filtered accordingly. Note that there are `paginator` and `page` attributes created in the custom actions or overridden methods (Same for the product viewsets mentioned before) since pagination should be re-defined when creating these methods or overridden default ones. 

# Backend URLS <a name="urls"></a>
In the main url config file, `product`, `category`, `order`, `users` and `token` end points are used for navigation on the API. Additionally static url is added for serving purpose of the media files,such as images in this project. Other url config files modified with the help of DRF's `DefaultRouter` class. This class allows auto creation urls of detail method or custom action methods. Check out documentation for more info: https://www.django-rest-framework.org/api-guide/routers/#defaultrouter. Note that token endpoint is created with the djoser, it is used to created new tokens and destroying tokens when user logins and logouts(token based authentication).
Additional rest_framework.url is added to main url config for login or logout functionality on the API(not on the front end) on the browser(session based authentication).

# Backend Settings <a name="settings"></a>
 There are nine apps added to installed_apps field of the django settings. From them `corsheaders` and `django_cleanup` should be explained hence other ones are mentioned before. With the corsheaders, it helps front end to connect to our backend service, for this `CORS_ALLOWED_ORIGINS` is modified. Detailed information on corsheader can be found in here: https://pypi.org/project/django-cors-headers/. `django_cleanup` is used for the purpose of the when the product image is changed or when the product itself is deleted, old image is removed from database with the help of this app.Note that in the product model image field is modified as `models.FileField` for this purpose, detailed info can be found about this app on the link: https://pypi.org/project/django-cleanup/ 

# Frontend Store <a name="stores"></a>
In this project, since user and cart values are needed for multiple views, state management is used with the help of the `pinia` package. `pinia` is recommended by Vue itself officially instead of `vuex`. It both works with composition api and options api, detailed info can be found on: https://pinia.vuejs.org/introduction.html

## TokenStore <a name="tokenstore"></a>
This store manages authentication state, user login, user logout and retrieving user data from backend with the help of `axios`. Axios is promise-based HTTP client, it simplifies http requests, detailed documentation: https://axios-http.com/docs/intro. Three state is created for this store, `user`, `token` and `isAuthenticated`. Each state is modified with the current user action on the front end. Firstly, `initializeToken` is called to check if user is already logged or not, user token data is stored as localstorage item in the browser. `removeToken` is used when user logs out, it makes request to the backend and destroy token for that user.`getUser` is used to retrieve user data from backend.Lastly `setToken` is used to set retrieved token from backend when user logged in as a state to make use later with axios.

## CartStore <a name="cartstore"></a>
This store is used with the purpose of creating cart items and modifies them. There is single state called `cart`. Firstly `initializeCart` is called to check if localstorage has a cart or not. `getCartTotal` returns sum of the quantity of the items in the cart, `getCartPriceTotal` return sum of the prices of the items in the cart, `removeCart` deletes all items in the cart. Note that they are created as `getters` since there is no need to pass arguments to them(they only rely on state,getters are good compared to actions since they are cached). As an actions, there are four methods. `addToCart` is used for adding items to the cart, it first check if item is already in there or not then it modifies quantity accordingly.`removeProduct` removes single item from cart, if the quantity of item is zero, it deletes that item from the cart. `getProductPriceTotal` calculates total price of the item in the cart. `deleteProduct` deletes item from the cart.

## RequestStore <a name="requeststore"></a>
This store is created for making requests, since there are many request in every view. There are two states created, products and pageCount. Get,post,patch and addional getResponse actions are created for making requests. They used as `plain` requests but additionally in the first get action, states that are created changes accordingly. Other ones just returns responses from API.


# Frontend Components <a name="components"></a>
## Navbar
Classic navigation bar from the `bootstrap` module is used. It should be good to mention about category dropdown values are retrieved when this component is created from the backend. Also when logged out, tokenstore is used to destroy token.

## Product
This component takes product data object as a prob and uses it.It is created since product is used on multiple views.

## Order
It takes order data object as prop, it is used on `UserPageView` for the purpose of the showing orders of the current user.

## Footer
Basic footer, it shows username if user is authenticated and user can go to `EditProfileView` to edit current profile via edit profile route.

# Frontend Views <a name="frontendviews"></a>

## HomeView <a name="homeview"></a>
Its the front page of the app. It gets product data from the back end when its created, and data is passed to the `product` component as a prop to show data on the web app. Note that vue is used with the `options api` in this project. This view also has functionality of pagination and search data on the API with the help of the pagination component and watcher functions of the vue. Its good to mention about pagination and search functionality in here since they are used in multiple views. Also vue-toast for notifying user can be explained too.
### Pagination <a name="pagination"></a>
Pagination is achieved through third party component called `vuejs-paginate-next`. Its ready to serve component and has a lot of cool functionality. Detailed info is in the link: https://www.npmjs.com/package/vuejs-paginate-next. In this project, 16 items par page is used when paginating, total page number calculated by receiving `count` value of items from backend and divided by 16 simply with the help of the `Math.ceil` built in java method. Each `click-handler` of the pagination, makes request to the API and gets data from pagenumber passed to it as an argument.
### Watcher for Search Input <a name="searchwatcher"></a>
Watchers are useful when we need to react to state changes, for more info check here:https://vuejs.org/guide/essentials/watchers.html. In this project, search input from the navbar emitted to main app and then passed as a prop to all views needed. Watcher here react to state of the input value and makes request to API and gets relevant data. In the backend query is used together with the django_filter to find relevant data. It uses title value of the product when searching with the request like `api/products/?category=&product_state=active&title=${this.searchQuery}`. Note that when getting product data, state of the product is active in every request.
### Vue Toast <a name="vuetoast"></a>
Toast is simple and strong message notifying third party package. When user interacts with the app for example adding product to cart or editing profile or more, it sends success notifications or error notifications. You can check main github link for this package : https://github.com/Maronato/vue-toastification , it also has live-demo website to create toast options easily: https://vue-toastification.maronato.dev/.

## Product View <a name="productview"></a>
This view is used to show single product data, editing product data if it is viewed by the `owner` user, reading comments and making comments on the product if the user is authenticated. Firstly when this view is mounted, it gets single product data from the API by using id of the product. Product id is passed through route as a parameter. It also get comments if there is any when its mounted.
User can edit this product if product is created by them, if not product editing form is not available. Note that there is `getTime` and `uploadImg` methods are created in here. getTime method is used in multiple views also to convert time data to more readable format, it uses package called `moment` : https://momentjs.com/. uploadImg method is used for when user upload new image, to make user to be able to see preview of the new image. When user makes new comment, product can be rated also. These rates are showed as stars on the comment right top. Comments are paginated here also if it exceeds 16 comment.

## Categories View <a name="categoryview"></a>
This view is almost the same as homeview except it uses category parameter when requesting data from the API using query of `api/products/?category=${this.$route.params.id}&product_state=active&title=${this.searchQuery}` . Note that category is selected by the category.id and used in watcher to get data whenever category selection changes. This view also has pagination and search functionality too. 

## Vendors View <a name="vendorview"></a>
Vendor View is used to specify products by the user that created them. It is similar to homeview and categoryview, it uses query of `api/products/?created_by__username=${this.$route.params.username}&product_state=active&page=${selected}&title=${this.searchQuery}`.
username is passes as parameter in the router and used in watcher. It also has pagination and search functionality.

## Add Product View <a name="addproductview"></a>
Simple view to create new product if the user is authenticated. Note that axios post method is modified with the headers of multipart/form-data since image is attached to the form.

## Cart View <a name="cartview"></a>
Basic cart view to show items that has been added to cart. User can change quantity of the product in the cart or delete it from the cart. For now there is no paying method included in here, but maybe `stripe api` can be used later. When user request to buy items, first it checks if there is any item in the cart then checks if  the user is authenticated. It also checks if user has all address data is presented to in their profile.

## User Page View <a name="userpageview"></a>
Main user page. User can see products that is created by them, can navigate orders made by them and if they have any products that has been sold. User can see order details separately and also go to add product view in here. When its created first, it retrieves all data mentioned in the above from the API, check how the queries made in the view. Note that there are 3 pagination used separately for my products, my orders, and my sold products.

## Register Sign In and Edit Profile View <a name="registersignineditprofileview"></a>
Basic user registration and sign in form are presented in these views. In the sign in view, request made to API and then request is used by djoser. If user provided correct username and password, backend sends token as an response. That token then used in the tokenStore and axios's common `Authorization` value since djoser requires it that way to check authentications, ref to docs:https://djoser.readthedocs.io/en/latest/sample_usage.html. In the register view, basic user creation form is presented and submitted to back end. Djoser checks validations if the user provided correct username,password and email. In the Edit Profile view, user can edit data belongs to them.

# Frontend Router <a name="frontendrouter"></a>
Collection of routes for the views that has been created. From all of them product, vendors and categories expect parameters. For the product router, slug and id passed. Vendors route get username. Lastly categories get title and id parameters. Each parameter is used to retrieve data from the API on the backend. Router guard is used in here against non authorized users. UserPage, NewProduct and EditProfile routers are available to authorized users only. If unauthorized user tries to use them, it redirects to SignIn page. More information can be found on the vue docs: https://router.vuejs.org/guide/advanced/navigation-guards.html
