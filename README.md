# Table of Content
1. [Functionality](#functionality)
2. [Installation](#installation)
3. [Begginner's Guide](#guide)
4. [Database Models](#databasemodels)
    1. [User Model](#usermodel)
    2. [Product Model](#productmodel)
    3. [Order Model](#ordermodel)
5. [Serializers](#serializers)
    1. [User Serializer](#userserializer)
    2. [Product Serializer](#productserializer)
    3. [Order Serializer](#orderserializer)
6. [Views](#views)
    1. [Product View](#productview)
    1. [Order View](#orderview)
7. [Urls](#urls)


# Functionality <a name="functionality"></a>
With the Ecomm, you can register as a new user and sign in, you can add new products, order products, follow your sold product history, follow your order history, you can navigate user specific products or category specific products,search products,comment on products and more in the future hopefully.

# Installation <a name="installation"></a>
 Project developed in virtual envinroment. You can install Python required packages with requirements.txt, node requirements can be found on package.json.
 For python dependencies initialize;
 `pip install -r requirements.txt`
 and for node modules initialize;
 `npm install`
 in your project directory. Detailed installation guide can be found in the 'Beginners Guide' section for the users who are not familiar with GitHub, Django or Vue.

# Begginner's Guide <a name="guide"></a>
To use E-commerce, first clone repository by using your terminal;
<br/>
`git clone https://github.com/atoprak06/eCommerceWithMultipleVendors-Django-Vue.git`
<br/>
 then cd  into your cloned directory in your terminal
 <br/>
 `cd eCommerceWithMultipleVendors-Django-Vue`
 <br/>
  and create virtual envinroment using 
<br/>
`python -m venv env`
<br/>
using virtual envinroment is recommended by python official docs as it creates seperate envinroment for your dependencies in development phase, detailed info can be found in here: https://docs.python.org/3/library/venv.html
<br/>
After installing virtual environment, open root directory in your code editor. To activate virtual envinroment open new terminal and use command below if you are on windows, if you are not using windows you can find how to activate it on the doc link above.
<br>
`env/scripts/activate`
<br/>
Now you will see `(env)` at the start of your root path in the terminal and it indicates that it's activated successfully. Now we are ready to install dependencies. First, lets install python side depencencies. Using pip in your terminal
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
After it initializes, you will see that there is link points to http://127.0.0.1:8000/ (or different depends on your machine)  on the terminal. Now lets visit admin page where its located at http://127.0.0.1:8000/admin in your browser. Login with username and password that you just created. Now you can see some sections in there which will be explained later in the docs. Before creating new products first we need to create some categories. Add some categories by simply going to 'Categories' under the PRODUCTS section and click 'Add Category'. Enter category name and slug(you can enter same name as category name with all lower case latters and '-' instead of 'spaces').Now you can create products by visiting products section. Now lets start our front end server. Use different terminal and cd into your ecommfrontend directory and trigger command:
<br/>
`npm run serve`
<br/>
After it initializes, you can then visit  http://localhost:8080/ (or different depends on your machine, check your terminal. If it is different modify `CORS_ALLOWED_ORIGINS` in the settings.py file accordingly) and navigate it. From there on, docs will include how the project works.

# Database Models<a name="databasemodels"></a>
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
Every product should have a comment section, so it is created for this purpose and linked to product with one to one relationsip.
### - Comment
Every comment created by users should be stored in database. It is linked to *Comments* model with one to many relationship.

## Order <a name="ordermodel"></a>
There are 2 model created for this section, *Order* and *OrderItem*
### - Order
It represent order created by the users. It is linked to User model with one to many relationship.
### - OrderItem
Products that has been added to order is represented by this model. It is linked to *Order* and *Product* models with one to many relationship.

# Serializers<a name="serializers"></a>
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
This serializer is used for the representation of the user on the api. User can fetch it's information or patch it with the help of the djoser `UserSerializer`. User model is used similary for this.  Note that it is added to djoser settings on the above with the fields of `user` and `current_user`. Key 'user' is used for general users whereas 'current_user' lets you set serializer for special /users/me endpoint. 


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


# Views <a name="views"></a>
Class based views are used for this project. DRF has a nice class called ViewSet and it allows similar logic of the related views to be combined under same class, detailed info can be found in the documentation of the DRF : https://www.django-rest-framework.org/api-guide/viewsets/

## Products <a name="productview"></a>

### ProductViewSet
This viewset is used for the purpose of the how the modeled and serialized product data should look on the API. It inherites from `MultiSerializerViewSet` since there are two different serializer used. MultiSerializerViewSet determines which serializer should be used in different actions, for the default actions listed in the dafault ViewSet methods in the DRF docs, `ProductSerializer` is used. For the `comments` action `CommentSerializer` is used. `actions` are decorators that is used when you want to define custom method for your viewset docs: https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing . Here permission class of `IsOwnerOrReadOnly` is used, since product data should be readonly if user is not authenticated, if user is authenticated, user can update product data if it is their product or can create new product. Also django_filter module is used for the filtering data using `ProductFilter` class which is inherited from `django_filters.FilterSet`, filter fields can be seen in fields array. Django filter allows users to filter queryset based on model fields, detailed info can be found on the documents: https://django-filter.readthedocs.io/en/stable/. Note that in the DRF settings in the settings.py `'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']` is modified like this to use django_filter module as a default filter. There are two custom action defined: `my_products` and `comments`. First one is to determine when user request their products created by them, second one is to get comments on the specific product or post comment on that same product. Note that there is also `perform_create` method that creates slug field when user create new product, slug field is created with the help of `slugify` method.


### CategoryViewSet
This Viewset determines how category data should look like on the API. Here just plain queryset is used.

## Order <a name="orderview"></a>

### OrderViewSet
This viewset did all the job for the order and orderitem data on the API. Permission class is modified as authenticated since authenticated users should be able to make new orders or get their order history data. `get_queryset` returns orders that belongs to the user who requested the data. Default `create` method of modelViewSet is overridden. When the user makes order on the front end, first order data is created then items in the cart that has been sent as a request data is extracted and orderitems are created. Custom `orderedProducts` action is created for the purpose of the user to be able too see products that belongs to them has been sold. Queryset is filtered accorrdingly. Note that there are `paginator` and `page` attributes created in the custom actions or overridden methods (Same for the product viewsets mentioned before) since pagination should be re-defined when creating these methods or overridden default ones. 

# URLS <a name="urls"></a>
In the main url config file, `product`, `category`, `order`, `users` and `token` end points are used for navigation on the API. Additionally static url is added for serving purpose of the media files,such as images in this project. Other url config files modified with the help of DRF's `DefaultRouter` class. This class allows auto creation urls of detail method or custom action methods. Check out documentation for more info: https://www.django-rest-framework.org/api-guide/routers/#defaultrouter. Note that token endpoint is created with the djoser, it is used to created new tokens and destroying tokens when user logins and logouts(token based authentication).
Additional rest_framework.url is added to main url config for login or logout funcionality on the API(not on the front end) on the browser(session based authentication).

# Settings <a name="settings"></a>
 There are nine apps added to installed_apps field of the django settings. From them `corsheaders` and `django_cleanup` should be explained hence other ones are mentioned before. With the corsheaders, it helps front end to connect to our backend service, for this `CORS_ALLOWED_ORIGINS` is modified. Detailed information on corsheader can be found in here: https://pypi.org/project/django-cors-headers/. `django_cleanup` is used for the purpose of the when the product image is changed or when the product itself is deleted, old image is removed from database with the help of this app.Note that in the product model image field is modified as `models.FileField` for this purpose, detailed info can be found about this app on the link: https://pypi.org/project/django-cleanup/ 




