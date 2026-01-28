# Password Generator

# Import modules needed
import random
import time

# Making the list of Characters that should be in password;

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.!@#$%^&*()_+-=;/"

def main():

    # Print "Let's Begin"
    print("Let's Begin...")
    time.sleep(0.5)
    time.sleep(0.5)
    # Asking the user for the length of the password;

    length = int(input("Enter the length of password you want to generate: "))
    print("Generating password...")
    time.sleep(0.5)
    time.sleep(0.5)

    print("Password generated successfully!")
    # Using Random module generate the password according to user length;
    password = ""
    for i in range(length):
        password = password + random.choice(characters)


    # Asking the user to save the password or to directly show the password;

    ask = input("Do you want to save the password in the file (yes/no): ")
    time.sleep(0.5)
    name = input("Enter your name: ")
    purpose = input("Enter the application in which you are using the password: ")
    time.sleep(0.5)
    time.sleep(0.5)
    print("Saving your details...")


    if ask.lower() == "yes":
        file = open(f"password_{name}_{purpose}_{length}.txt", "w")
        file.write(f" Hy {name}, \nYour password has been creatd successfully for your {purpose}\n Password: {password}\n Thank you for using the password generator and have your password safe from others eyes. Use your password wisely and do not share it with anyone ")
        file.close()
        time.sleep(0.5)
        time.sleep(0.5)
        print("Password has been generated successfully, Please check your files")
    else:
        print(f" Hy {name}, \nYour password has been creatd successfully for your {purpose}\n Password: {password}\n Thank you for using the password generator and have your password safe from others eyes. Use your password wisely and do not share it with anyone ")

    time.sleep(0.5)

    print("Please wait for a while!")

    time.sleep(0.5)
    time.sleep(0.5)
    # Ask the user to generate another password or to exit the program;

    run_again = input("Do you want to generate another password (yes/no): ")
    print("Processing...")
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    print("It will take few seconds, please wait....!")
    time.sleep(0.5)
    time.sleep(0.5)

    if run_again.lower() == "yes":
        main()
    else:
        print("Thank you for using the password generator, see you next time!")

main()


#===================================================== Completed the Project ==================================================