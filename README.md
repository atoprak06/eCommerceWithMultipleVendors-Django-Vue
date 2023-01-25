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



