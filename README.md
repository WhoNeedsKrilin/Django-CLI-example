# Django simple CRUD CLI

## Description:
**Perform Create, Read, Update, and Delete Resident's details using this simple app and execute custom commands via command line interface.**

## Usage:

Change working directory to /myapp


**Add a new Resident by inputting:** *python manage.py residents --add_resident
![](assets/images/1.0%20--add_resident.png)


**View Residents by inputting:** *python manage.py residents --view_people
![](assets/images//2. --view_people.png)
![](assets/images/3. --view_people.png)

"Choose Resident's name: " prompt will appear and you can enter the Resident's name to direct you to 'action' prompt.


An Action prompt will let you **Update** or **Delete** a Resident's data. You can press any other key to exit.
"Choose Resident's name: " prompt will appear and you can enter the Resident's name to direct you to 'action' prompt.
![alt text](https://raw.githubusercontent.com/WhoNeedsKrilin/django-cli-example/master/assets/images/to/3 Action.png)

**Update Resident by inputting:** *x
![alt text](https://raw.githubusercontent.com/WhoNeedsKrilin/django-cli-example/master/assets/images/to/4.0 Action.png)

Enter the details you want to update.
![alt text](https://raw.githubusercontent.com/WhoNeedsKrilin/django-cli-example/master/assets/images/to/4.3 Updating.png)

**Delete Redident by inputting:** Assumming that you're at  "--view_people" again, Enter a Resident's name and by this time input "d" key to delete a Resident record.
![alt text](https://raw.githubusercontent.com/WhoNeedsKrilin/django-cli-example/master/assets/images/to/6.1  Deleting success.png)

**Get Resident by last name by inputting:** *python manage.py residents --get_resident_by_last_name
![alt text](https://raw.githubusercontent.com/WhoNeedsKrilin/django-cli-example/master/assets/images/to/8.0 get_resident_by last_name.png)

Enter the last name of the Resident you want to retrieve.
![alt text](https://raw.githubusercontent.com/WhoNeedsKrilin/django-cli-example/master/assets/images/to/8.1 
get_sresitdentbylastname)

![alt text](https://raw.githubusercontent.com/WhoNeedsKrilin/django-cli-example/master/assets/images/to/8.2 Smith_last_name.png)

**View Residents that are updated within a day by inputting:** *python.manage.py residents --get_resident_updated_today
![alt text](https://raw.githubusercontent.com/WhoNeedsKrilin/django-cli-example/master/assets/images/to/9. Updated_today.png)

**View Residents that are created within a day by inputting:** *python.manage.py residents --get_new_residents


[nothing follows]
