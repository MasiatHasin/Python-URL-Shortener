from termcolor import colored
import authentication
import url
import questionary
from misc import custom_style_fancy as cs
from dbconnection import mycursor, db

print(colored("""=====================================================
Python URL Shortner
Author: Mashiat Hasin Rodoshi (masiathasin@gmail.com)
=====================================================""", 'blue'))

def initialize():
    print("")
    print("Log in to get access to more features.\n")
    method = questionary.select(
        "Please choose one of the following:", style=cs,
        choices=[
            'Log In',
            'Sign Up',
            'Use short URL',
            'Exit'
        ]).ask()

    if method == "Sign Up":
        authentication.signUp()
        initialize()

    if method == "Log In":
        result, email, name = authentication.logIn()
        if result == True:
            userOptions(email, name)
        else:
            initialize()

    if method=="Use short URL":
        url.useURL()
        initialize()

    if method=="Exit":
        mycursor.close()
        db.close()
    
def userOptions(email, name):
    print("")
    task = questionary.select(
            "What do you want to do?", style=cs,
            choices=[
                'Use Short URL',
                'Create Short URL',
                'Create Custom Short URL',
                'View/Delete your Short URLs',
                'Get analytics',
                'Log Out'
            ]).ask()
    
    if task== "Create Short URL":
        url.generate(email)
        userOptions(email, name)

    if task== "Create Custom Short URL":
        url.generateCustom(email)
        userOptions(email, name)

    if task=="Use Short URL":
        url.useURL()
        userOptions(email, name)
    
    if task=="Get analytics":
        url.analytics()
        userOptions(email, name)

    if task=="View/Delete your Short URLs":
        url.viewUserURL(email, name)
        userOptions(email, name)
    
    if task=="Log Out":
        print(colored("\nSuccess! Logged out.", 'green'))
        initialize()

initialize()