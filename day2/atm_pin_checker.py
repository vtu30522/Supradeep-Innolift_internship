correct_pin = 1234
attempts = 0

while attempts < 3:
    pin = int(input("Enter ATM PIN: "))

    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        attempts += 1
        if attempts == 3:
            print("Card Blocked")
        else:
            print("Wrong PIN. Try again.")