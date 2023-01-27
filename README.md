# Functionality
With the Ecomm, you can register as a new user and sign in, you can add new products, order products, follow your sold product history, follow your order history, you can navigate user specific products or category specific products,search products,comment on products and more in the future hopefully.

# Installation
 Project developed in virtual envinroment. You can install Python required packages with requirements.txt, node requirements can be found on package.json.
 For python dependencies initialize;
 `pip install -r requirements.txt`
 and for node modules initialize;
 `npm install`
 in your project directory. Detailed installation guide can be found in the 'Beginners Guide' section for the users who are not familiar with GitHub, Django or Vue.

# Begginner's Guide
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
After it initializes, you can then visit  http://localhost:8080/ (or different depends on your machine, check your terminal) and navigate it. From there on, docs will include how the project works.

# Database Models
## 1- User
For the user model Django default AbstractUser is used with the extra fields. Note that to activate this user model, in the settings you need to point `AUTH_USER_MODEL` field to the user model.
<br/>
`AUTH_USER_MODEL = 'user.UserProfile'`
<br/> 
It's good to mention about *is_vendor* field that has been created. This field's state will decide if that user's product will be presented on the front end or not. User can alter its *is_vendor* state by visiting edit profile on the front end.

## 2- Products
For the products, 4 main model is created. *Category, Product, Comments* and *Comment* models.
### - Category
This model can be altered by just the admin user on the backend. Before creating product instances, there should be categories already created.
### - Product
It is the main product model. *category* and *created_by* fields are linked to Category and User models respectively using one to many relationship.
### - Comments
Every product should have a comment section, so it is created for this purpose and linked to product with one to one relationsip.
### - Comment
Every comment created by users should be stored in database. It is linked to *Comments* model with one to many relationship.

## 3- Order
There are 2 model created for this section, *Order* and *OrderItem*
### - Order
It represent order created by the users. It is linked to User model with one to many relationship.
### - OrderItem
Products that has been added to order is represented by this model. It is linked to *Order* and *Product* models with one to many relationship.

# Serializers
Django default models can't be represented on the API as the way they are, so DRF serializers are used to show them as JSON represented data in this project. ModelSerializers class is used since it is very powerful when creating shortcut representation of models that has been created already. Detailed info can be found on the DRF documents: https://www.django-rest-framework.org/api-guide/serializers


## User  Serializers
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

Note that password retype is activated for the re password field of the registration form. 

### UserRegistrationSerializer
UserRegistrationSerializer is created for the basic user registration with the help of `UserCreatePasswordRetypeSerializer` of the djoser serializers.The `User` model that we created before is used for this serializer. Registration is modified like when the new user is registering re type of the password should be used. Validations of the user register like, if the username that has been used within the form is already exists or not, if the email is already exists, if the passwords are matching or in the correct format is achieved easily with the help of this serializer. Note that it is added to djoser settings on the above with the field of `user_create_password_retype`

### UserSerializer
This serializer is used for the representation of the user on the api. User can fetch it's information or patch it with the help of the djoser `UserSerializer`. User model is used similary for this.  Note that it is added to djoser settings on the above with the fields of `user` and `current_user`. Key 'user' is used for general users whereas 'current_user' lets you set serializer for special /users/me endpoint. 


## Products  Serializers
### ProductSerializer
For the product serializer, Product model is used. `category` and `created_by` related fields of the product is represented on the API with the help of `SlugRelatedField` and `ReadOnlyField` respectively. `category` is represented on the API as the title field of the category model and `created_by` is showed as username field of the user model. Id of the product and created_by can't be updated on the api as it is modified as readonly fields.

### CategorySerializer
For the category serializer, Category model is used. Title and id fields are used in here. 

### CommentSerializer
Comment model is used for this serializer. Related field user is interpreted by `SlugRelatedField` for the API since just username of the user is needed.

## Order Serializers
### OrderItemSerializer
 OrderItem model is used. Related field product is interpreted with the `ProductSerializer` that has been created already. This serializer represents items that has been ordered.

### OrderSerializer 
Order model is used. Related field products is interpreted with the OrderItemSerializer created above. It represents orders and products that belongs to this order. 

### OrderedItemSerializer
This serializer is used for the representation of the products that user has and got bought by the other users. Note that it inherits from the OrderItemSerializer that has been created before. Additionally new class Order is created for the purpose of the order interpretation with the customer and order id fields. Meta class is also inherited from OrderItemSerializer.Meta, just fields changed. So user can see products that he owns and got bought by the others in the format that is meaningful.







