import random
from termcolor import colored
import questionary
from questionary import Style
from misc import custom_style_fancy as cs
import string
import webbrowser
import misc
from datetime import datetime
from dbconnection import mycursor, db
from questionary import Validator, ValidationError, prompt

#======================================
# Create short URL
#======================================
def generate(email):
    original = questionary.text("original URL: ").ask()
    if misc.validUrl(original) == True:
        expirationDate = questionary.text("Expiration Date (Format: YYYY-MM-DD | Optional): ").ask()
        if len(expirationDate)<1:
            expirationDate = None
        length = 6
        characters = string.ascii_letters + string.digits
        short_alias = ''.join(random.choice(characters) for _ in range(length))
        short = f"http://short.url/{short_alias}"
        mycursor.execute(f"SELECT * FROM links WHERE short_URL = '{short}'")
        res = mycursor.fetchall()
        while len(res)>0:
            characters = string.ascii_letters + string.digits
            short_alias = ''.join(random.choice(characters) for _ in range(length))
            short = f"http://short.url/{short_alias}"
            mycursor.execute(f"SELECT * FROM links WHERE short_URL = '{short}'")
            res = mycursor.fetchall()
        sql = "INSERT INTO links (email, original_URL, short_URL, clicks, expiration) VALUES (%s, %s, %s, %s, %s);"
        val = (email, original, short, 0, expirationDate)
        mycursor.execute(sql, val)
        db.commit()
        print(colored(f"\nSuccess! Short URL: {short}", 'green'))
    else:
        print(colored("\nError! Invalid URL.", 'red'))


#======================================
# Create custom short URL
#======================================
def generateCustom(email):
    original = questionary.text("original URL: ").ask()
    if misc.validUrl(original) == True:
        expirationDate = questionary.text("Expiration Date (Format: YYYY-MM-DD | Optional): ").ask()
        if len(expirationDate)<1:
            expirationDate = None
        customString = questionary.text("Custom String (eg. ug28uwfci will produce http://short.url/ug28uwfci): ", validate= misc.linkValidator).ask()
        short = f"http://short.url/{customString}"
        mycursor.execute(f"SELECT * FROM links WHERE short_URL = '{short}'")
        res = mycursor.fetchall()
        if len(res)>0:
            print(colored("\nError! This short URL already exists.", 'red'))
        else:
            sql = "INSERT INTO links (email, original_URL, short_URL, clicks, expiration) VALUES (%s, %s, %s, %s, %s);"
            val = (email, original, short, 0, expirationDate)
            mycursor.execute(sql, val)
            db.commit()
            print(colored(f"\nSuccess! Short URL: {short}", 'green'))
    else:
        print(colored("\nError! Invalid URL.", 'red'))

#======================================
# View/Delete user generated short URL
#======================================
def viewUserURL(email, name):
    print(colored(f"------------------------------------\nShort URLs created by {name}\n------------------------------------", 'blue'))
    mycursor.execute(f"SELECT * FROM links WHERE email = '{email}'")
    res = mycursor.fetchall()
    if len(res)>0:
        urls = []
        for i in range (0, len(res), 1):
            originalUrl = res[i][1]
            if len(originalUrl)>50:
                originalUrl = originalUrl[:50]+"..."
            expirationDate = res[i][4]
            currentDate = datetime.now().date()
            if expirationDate != None and currentDate > expirationDate:
                validity = "Invalid"
            else:
                validity = "valid"
            urls.append(f'{originalUrl} - {res[i][2]} - {validity}')

        selected = questionary.checkbox("Select URLs to Delete: ", style=cs, choices=urls).ask()
        toDelete = [info.split('-')[1].strip() for info in selected]
        print(toDelete)
        
        if len(toDelete)>0:
            for i in range(0, len(toDelete), 1):
                try: 
                    sql = f"DELETE FROM links WHERE short_URL = '{toDelete[i]}'"
                    mycursor.execute(sql)
                    db.commit()
                except:
                    print(colored("\nError! Something went wrong.", 'red'))
            print(colored('\nSuccess! Deleted the selected links.', 'green'))
    else:
        print(colored("\nYou haven't created any short URLs yet.", 'yellow'))

#======================================
# Access short URL
#======================================
def useURL():
    url = questionary.text("Short URL: ").ask()
    print("I work")
    mycursor.execute(f"SELECT * FROM links WHERE short_URL = '{url}'")
    res = mycursor.fetchall()
    if len(res)>0:
        expirationDate = res[0][4]
        currentDate = datetime.now().date()
        originalUrl = res[0][1]
        if expirationDate != None and currentDate > expirationDate:
            print(colored("\nError! Expired link.", 'red'))
        else:
            sql = f"UPDATE links SET clicks = clicks + 1 WHERE short_URL = '{url}'"
            mycursor.execute(sql)
            db.commit()
            webbrowser.open(originalUrl)
    else:
        print(colored("\nError! Invalid link.", 'red'))

#======================================
# Get short URL analytics (clicks)
#======================================
def getAnalytics(url):
    mycursor.execute(f"SELECT * FROM links WHERE short_URL = '{url}'")
    res = mycursor.fetchall()
    if len(res)>0:
        clicks = res[0][3]
        return clicks
    else:
        print(colored("\nError! Invalid link.", 'red'))


def analytics():
    url = questionary.text("Short URL: ").ask()
    if len(url)>0:
        clicks = getAnalytics(url)
        if clicks>1:
            clicks = str(clicks) + ' times'
        else:
            clicks = str(clicks) + ' time'
        print(colored(f'\nThis URL has been accessed {clicks}.', 'green'))
    else:
        print(colored("\nError! Invalid link.", 'red'))


