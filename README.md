# Simple Inventory Application
This is created to demonstrate few functions of django and django rest framework

## Installation
Please make sure you have install python latest release 3.9+
Please use requirements.txt to install related modules

## Run
database is already created "db.sqlite3"

if you want to restructure the database please run "python manage.py makemigrations"
then run run "python manage.py migrate" to apply the changes

once the setup is done 

## User credentials
Please login to the administrator view using ( /admin )
Then in the login screen please give below details 

- **Username : dell**
- **Password : dell@123**

## Run program
please execute "python manage.py runserver" to run the program

## Test program
please execute "python manage.py test" to test the program

## Exposed URLS Tested
#### Site links
- http://127.0.0.1:8000/inventory/
- http://127.0.0.1:8000/inventory/?name=rice
- http://127.0.0.1:8000/api
- http://127.0.0.1:8000/api/inventory/
- http://127.0.0.1:8000/api/inventory/?name=rice

#### Admin Links
http://127.0.0.1:8000/admin

## Screenshots

### To list all
![image](https://user-images.githubusercontent.com/46668862/167292810-6bc88dde-c81f-407f-b78a-a451b08f998b.png)


### To filter specific name from the list
![image](https://user-images.githubusercontent.com/46668862/167292871-c5a2436c-bc36-42e2-9f50-f1154e1c193b.png)

### To view single item (pleasse click on the name of the item from the list view)
![image](https://user-images.githubusercontent.com/46668862/167292910-2732049a-7ca2-444b-83a1-bc1de516c114.png)

### API overview
![image](https://user-images.githubusercontent.com/46668862/167292942-16fe37f8-0822-4dd9-866e-e41c752e3792.png)


### API inventory list
![image](https://user-images.githubusercontent.com/46668862/167292965-a3a341e2-fa32-4c47-8f20-bad5e6ad5954.png)

### ADMIN view
![image](https://user-images.githubusercontent.com/46668862/167293040-8abe8d04-5f85-40e7-9cd9-064ffa5ce371.png)

## TEST output
![image](https://user-images.githubusercontent.com/46668862/167294667-8e537cda-965c-4232-8e64-e7d48dca673b.png)

