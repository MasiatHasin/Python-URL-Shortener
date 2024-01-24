from termcolor import colored
import questionary
from questionary import Style
import misc
from misc import custom_style_fancy as cs
from dbconnection import mycursor, db

#======================================
# Create account
#======================================
def signUp():
    name = questionary.text("your name: ", validate=misc.notemptyValidator).ask()
    email = questionary.text("your email: ", validate=misc.notemptyValidator).ask()
    if misc.check(email):
        password = questionary.password("Your Password: ", validate=misc.pwValidator).ask()
        confirm = questionary.password("Confirm your Password: ", validate=misc.pwValidator).ask()
        if password == confirm:
                mycursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
                res = mycursor.fetchall()

                if len(res)>0:
                    print(colored('\nError! An account with this email already exists.', 'red'))
                
                else:
                    hashedpw = misc.hashPassword(password)
                    sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s);"
                    val = (name, email, hashedpw)
                    mycursor.execute(sql, val)
                    db.commit()
                    print(colored('\nSuccess! Account created.', 'green'))
        else:
            print(colored("\nError! Passwords don't match.", 'red'))
    else:
        print(colored('\nError! Email is invalid.', 'red'))

#======================================
# Login to account
#======================================
def logIn():
    email = questionary.text("your email: ", style=cs).ask()
    password = questionary.password("Your Password: ", style=cs).ask()
    mycursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
    res = mycursor.fetchall()
    name = ""
    if len(res)>0:
        hashedpw = res[0][2]
        name = res[0][0]
        if misc.checkPassword(password, hashedpw):
            print(colored('\nSuccess! You are logged in.', 'green'))
            return True, email, name
        else:
            print(colored("\nError! Invalid credentials.", 'red'))
            return False, email, name
    else:
         print(colored("\nError! Invalid credentials.", 'red'))
         return False, email, name
