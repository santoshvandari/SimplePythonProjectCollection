# python program to generate fake information 
from faker import Faker

def main():
    fake = Faker()
    name=fake.name()
    address=fake.address()
    dateofbirth=fake.date_of_birth()
    email=fake.email()
    phone=fake.phone_number()
    creditcard=fake.credit_card_full()

    print("Name : ",name)
    print("Address : ",address)
    print("Date of Birth : ",dateofbirth)
    print("Email : ",email)
    print("Phone : ",phone)
    print("Credit Card Details : ",creditcard)


if __name__ =="__main__":
    main()