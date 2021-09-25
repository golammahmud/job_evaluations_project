Job Evaluation Project
Ame Coding Pari Na
Instructions for run this code
First you need to git clone the project from my git
repository. Example($ git clonehttps://github.com/libgit2/libgit2
).
Then cd ./amecoding_parina .this way you go to the directory.
To run this code you need to PyCharm or vscode editor and install the
requeirments.txt packages .
After succefully install all the packages go to the terminal and run this command
python manage.py makemigrations
python manage.py migrate
after that you need to create superuser for admin dashboard.run this code on
terminal .
python manage.py createsuperuser
fill all the required fields succefully.after run the flowing project
python manage.py runserver.
Go to the localhost on any browser http://127.0.0.1.:8000
To access this website you need to register yourself .then login and input your
number and match the number with search inputs.
JWT Token Based api
I created simplejwt token based api .for getting all the inputs from data based .i
used jwt globally in settings.py file .also I can get given users based inputs.to
access this api you need to create access token and refresh token by given your
username and password on postman or use httpie .
After getting access token . to get all the input values use
http://127.0.0.1:8000/api/user-based-inputs/
Get users based all the input use this url
http://127.0.0.1:8000/api/all-userinputs/
in this project folder below I create a python third party app to show the api get
operations.
Project descriptions
I try to complete all the given task in this project. I created user authentications
system login, logout and registrations system.
After that I implement the second task user inputs system .I sorted the comma
separated integers value in descending order in the database. And matching it
with search inputs values. And show the result in result section true or false.
After that create the api using simple_jwt
