# python program to generate fake information 
from faker import Faker

def main():
    fake = Faker()
    name=fake.name()
    address=fake.address()
    email=fake.email()
    phone=fake.phone_number()
    creditcard=fake.credit_card_full()
    maritialstatus=fake.random_element(elements=('Single','Married','Divorced'))
    dateofbirth=fake.date_of_birth()



    print("Name: ",name)
    print("Address: ",address)
    print("Email: ",email)
    print("Phone: ",phone)
    print("Credit Card: ",creditcard)
    print("Maritial Status: ",maritialstatus)


if __name__ =="__main__":
    main()