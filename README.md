# Django simple CRUD CLI

## Description:
**Perform Create, Read, Update, and Delete Resident's details using this simple app and execute custom commands via command line interface.**

## Usage:

Change working directory to /myapp


**Add a new Resident by inputting:** python manage.py residents --add_resident
![](assets/images/1.0%20--add_resident.png)


**View Residents by inputting:** python manage.py residents --view_people
![](assets/images//2.%20--view_people.png)
![](assets/images/3.%20--view_people.png)

"Choose Resident's name: " prompt will appear and you can enter the Resident's name to direct you to 'action' prompt.


An Action prompt will let you **Update** or **Delete** a Resident's data. You can press any other key to exit.
"Choose Resident's name: " prompt will appear and you can enter the Resident's name to direct you to 'action' prompt.
![](assets/images/3 Action.png)

**Update Resident by inputting:** x
![](assets/images/4.0%20Action.png)

Enter the details you want to update.
![](assets/images/4.3%20Updating.png)

**Delete Redident by inputting:** Assumming that you're at  "--view_people" again, Enter a Resident's name and by this time input "d" key to delete a Resident record.
![](assets/images/6.1%20Deleting%20success.png)

**Get Resident by last name by inputting:** python manage.py residents --get_resident_by_last_name
![](assets/images/8.0%20get_resident_by%20last_name.png)

Enter the last name of the Resident you want to retrieve.
![](assets/images/8.1%20get_sresitdentbylastname)

![](assets/images/8.2%20Smith_last_name.png)

**View Residents that are updated within a day by inputting:** *python.manage.py residents --get_resident_updated_today
![](assets/images/9.%20Updated_today.png)

**View Residents that are created within a day by inputting:** *python.manage.py residents --get_new_residents
![](assets/images/10.Get_new_residents.png)


[nothing follows]
