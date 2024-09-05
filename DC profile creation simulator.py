import os 
import pwinput
from time import sleep
import progressbar
os.system("cls")


print("Welcome to Discord!")
sleep(1)

name = input("Enter user name: ")

e_mail = input("Enter your email for future verification:  ")




password = pwinput.pwinput(prompt="Enter a password of a least 5: ", mask="*")


def animated_marker():
     
    widgets = ['Loading: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
     
    for i in range(50):
        sleep(0.1)
        bar.update(i)
         

animated_marker()


if len(password) < 5:
    print("Password too short! It must be at least 5 characters.")
else:
    print("Password accept")
    
    
print()

print(f"Welcome to Discord {name}!")

print()  

print(f"{name}, your Discord accont has been created :D. Your Discord password is: {password}")
print()
print(f"Email address of registered user: {e_mail}")
print()
print("REMEMBER TO PROTECT YOUR PASSWORD! ")
print()
print("IDEA: Use my application to generate a strong password and 2FA key available on GitHub")
print()
print("Click -> https://github.com/Ola-Kaznowska/Secure-login-with-password-and-2FA-key")
 