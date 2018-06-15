from django.core.management.base import BaseCommand, CommandError
from residents.models import Address, Resident
from django.utils import timezone
from datetime import datetime
import time, sys, os



class Command(BaseCommand):


    def add_arguments(self, parser):

        parser.add_argument(
            '--add_resident',
            action = 'store_true',
            dest = 'add_resident',
            help = 'Add a new Resident',
        )
    
        parser.add_argument(
            '--view_people',
            action = 'store_true',
            dest = 'view_people',
            help = 'View People',
        )
        parser.add_argument(
            '--get_resident_by_last_name',
            action = 'store_true',
            dest = 'get_resident_by_last_name',
            help = 'get_resident_by_last_name',
        )
        parser.add_argument(
            '--get_resident_updated_today',
            action = 'store_true',
            dest = 'get_resident_updated_today',
            help = 'get_resident_updated_today',
        )
        parser.add_argument(
            '--get_new_residents',
            action = 'store_true',
            dest = 'get_new_residents',
            help = 'get_new_residents',
        )




    def handle(self,*args, **options):


        def delay_print(s):
            for c in s:
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(0.05)


        def update(id):
            ## Get resident base on primary key
            resident = Resident.objects.get(pk=id)
            print('Name: '+ str(resident) +'\nAddress: '+str(resident.address))
            resident.date_update = timezone.now()
            resident.date_created = resident.date_created
            resident.first_name = str(input("Firstname: "))
            resident.last_name = str(input("Lastname: "))
            resident.age = int(input('Age: '))
            address = Address.objects.get(street=resident.address.street, baranggay=resident.address.baranggay, city=resident.address)
            address.street = str(input('New Street: '))
            address.baranggay = str(input('New Brgy: '))
            address.city = str(input('New City: '))
            address.save()
            resident.save()
            delay_print('Updated successfully!\n')
            view_residents()


        def delete(id):
            ## Delete resident base on primary key
            resident = Resident.objects.get(pk=id)
            print('Name: '+ str(resident) +'\nAddress: '+str(resident.address))
            conf = str(input('Enter Y to confirm, N to cancel.\n'))
            if conf.upper() == 'Y':
                resident.delete()
                delay_print('Deleted successfully!\n')
                view_residents()
            else:
                delay_print('Deletion cancelled.\n')
                view_residents()


        def view_residents():

            os.system('cls' if os.name == 'nt' else 'clear')
            residents = Resident.objects.all()

            if residents != 'null':
                print('---- List of Residents ----')
                print('\n    Full Name     |         Address         |   Date Joined   \n')
                for res in residents:
                    print(str(res)+' | '+str(res.address.street)+' '+str(res.address.baranggay)+' '+str(res.address)+' | '+
                            str(res.date_created.strftime('%m/%d/%y')))

                print('\n\n---------------------------------------------------------------- ')
                name = str(input("Choose Resident's name: "))
                person = Resident.objects.get(first_name=name)
                print('\nChosen: ['+str(person)+' from '+str(person.address)+']\n')
                inp = str(input('What action do you want to do? [X] UPDATE [D] DELETE [~]'+
                    ' Anything to Cancel :'))

                if inp.upper() == 'X':

                    try:
                        chosen = Resident.objects.get(first_name=name)
                        update(chosen.pk)
                    except:
                        raise CommandError('Ooops, No residents like that!')

                elif inp.upper() == 'D':

                    try:
                        chosen = Resident.objects.get(first_name=name)
                        delete(chosen.pk)
                    except:
                        raise CommandError('No residents like that!')

            else:
                raise CommandError('Please add some residents!')

        if options['add_resident']:
            date = timezone.now()
            fname = str(input("Firstname: "))
            lname = str(input("Lastname: "))
            age = int(input('Age: '))
            street = str(input("Enter street:"))
            brgy = str(input("Enter brgy:"))
            city = str(input("Enter city: "))
            address = Address(street=street,baranggay=brgy,city=city)
            address.save()
            name = Resident(first_name = fname, last_name = lname, age = age, date_created = date, date_updated = date, address = address)
            name.save()
            print('success!')

        if options['view_people']:
            view_residents()

        if options['get_resident_by_last_name']:
           
            lname = str(input("Enter Resident's last name: "))
            try:
                ud_by_last_name = Resident.objects.get(last_name=lname)
                # print(search_by_last_name.address)
                print('---- List of Residents ----')
                print('\n    Full Name     |         Address         |   Date Joined   \n')
                print(str(search_by_last_name)+' | '+str(search_by_last_name.address.street)+' '+str(search_by_last_name.address.baranggay)+' '+str(search_by_last_name.address)+' | '+str(search_by_last_name.date_created.strftime('%m/%d/%y')))
                print('\n\n---------------------------------------------------------------- ')
            except:
                raise CommandError('No residents like that!')

        if options['get_resident_updated_today']:
            
            current_day = timezone.now().day
   
            updated_today = Resident.objects.filter(date_updated__day=current_day)
            try:
                print('---- List of Residents ----')
                print('\n    Full Name     |         Address         |   Date Joined   \n')
                for ud in updated_today:
                    print(str(ud)+' | '+str(ud.address.street)+' '+str(ud.address.baranggay)+' '+str(ud.address)+' | '+str(ud.date_created.strftime('%m/%d/%y')))
                
                print('\n\n---------------------------------------------------------------- ')

            except:
                raise CommandError('Not Found!')

        if options['get_new_residents']:
            
            current_day = timezone.now().day
   
            created_today = Resident.objects.filter(date_created__day=current_day)
            try:
                print('---- List of Residents ----')
                print('\n    Full Name     |         Address         |   Date Joined   \n')
                for ud in created_today:
                    print(str(ud)+' | '+str(ud.address.street)+' '+str(ud.address.baranggay)+' '+str(ud.address)+' | '+str(ud.date_created.strftime('%m/%d/%y')))

                print('\n\n---------------------------------------------------------------- ')

            except:
                raise CommandError('Not Found!')
         
