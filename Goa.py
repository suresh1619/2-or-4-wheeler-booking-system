import time
from datetime import date,timedelta
def print_receipt(transaction):
    b,type_of_wheeler,days_lent,aadhaar,future_date=transaction
    print('__________   ________________  __________   ________')
    print('|   date    | type of wheeler| days_lent |   aadhar |')
    print('__________________________________________________')
    print(b,'  | ',type_of_wheeler,'   |   ',days_lent,'   |  ',aadhaar,'|')
    print('___________________________________________________')
   
    print()
    time.sleep(2)
    print('Return date :',future_date)
    print()
    time.sleep(0.5)
    print('Note: Delay in return  causes extra 500rs/day!')
    




time.sleep(1)
print('_____Welcome to Goa____')
time.sleep(0.1)
print('Thank you for choosing our Travels')
print('1. 2-wheeler')
print('2. 4- wheeler')
time.sleep(0.2)
vehicletype=int(input('Choose the type of vehicle From above:'))
time.sleep(0.5)
if vehicletype==1:
    time.sleep(1)
    print('1. pulsar')
    print('2. Bajaj')
    print('3.RX-100')
    print('4. Royal Enfield')
    two_wheeler={1:'pulsar',2:'Bajaj',3:'Rx-100',4:'Royal Enfield'}
    twowheeler=int(input('Choose one from above:'))
    time.sleep(0.5)
    if twowheeler:
        no_of_days=int(input('Please Enter no_of days for rent:'))
        if no_of_days:
            aadhaar=input('Enter YOur Aadhaar with out spaces:')
            if not aadhaar or len(str(aadhaar))!=12:
                print('Error !')
            license_=input('Enter YOur Driving Lisense:')
            if license_:
                print('please confirm:')
                print('1. Yes   2. No :')
                confirm=int(input())
                time.sleep(0.5)
                if confirm==1:
                    a=date.today()
                    b=a.strftime('%d/%m/%Y')
                    future_date = a + timedelta(days=no_of_days)
                    


                    transanction=[b[:10], two_wheeler[twowheeler],no_of_days,aadhaar[:8]+'xxxx',future_date]
                    print('Processing.............')
                    time.sleep(3)
                    print_receipt(transanction)
                    print()
                elif confirm>=2:
                    print('Sorry for regret')

            else:
                print('Error please confirm')
        else:
            print('Please enter no_of days your want for rent:')
    else:
        print('Please Enter What type of two wheeler you want:') 
elif vehicletype==2:
    print('1.Hundai')
    print('2.swift') 
    print('3.suzuki')
    four_wheeler={1:'Hundai',2:'swift',3:'Suziki'}
    fourwheeler=int(input('Choose one from above:'))
    if fourwheeler:
        no_of_days=int(input('Please Enter no_of days for rent:'))
        if no_of_days:
            aadhaar=input('Enter YOur Aadhaar with out spaces:')
            if not aadhaar or len(str(aadhaar))!=12:
                print('Error !')
            license_=input('Enter YOur Driving Lisense:')
            if license_:
                print('please confirm!')
               
                confirm=int(input('1. Yes 2.NO  :'))
                if confirm:
                    a=date.today()
                    b=a.strftime('%d/%m/%Y')
                    future_date = a + timedelta(days=no_of_days)

                    transanction=[b, four_wheeler[fourwheeler],no_of_days,aadhaar[:8]+'xxxx',future_date]
                    print('Processing.............')
                    time.sleep(3)
                    print_receipt(transanction)

                    print('Your booking is confirmed ')
                    print()
                if not confirm:
                    print(r' "Retry" Your Booking isnot confirmed ')

            else:
                print('Error please confirm')
        else:
            print('Please enter no_of days your want for rent')
    else:
        print('Please Enter What type of four wheeler you want:') 
else:
    print('!Please Enter the Correct Option amongst them.')

    

