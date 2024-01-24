import re
import bcrypt
import questionary
from questionary import Style
from questionary import Validator, ValidationError, prompt

def check(email):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return bool(re.match(pat,email))

def validUrl(url):
    pat = re.compile(r'https?://\S+')
    return bool(pat.match(url))
    
def hashPassword(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def checkPassword(password, hashedpw):
    return bcrypt.checkpw(password.encode('utf-8'), hashedpw.encode('utf-8'))

class linkValidator(Validator):
    def validate(self, document):
        if len(document.text) < 6:
            raise ValidationError(
                message="Must be at least 6 characters long.",
                cursor_position=len(document.text),
            )

class notemptyValidator(Validator):
    def validate(self, document):
        if len(document.text) < 1:
            raise ValidationError(
                message="Must not be empty.",
                cursor_position=len(document.text),
            )
        
class pwValidator(Validator):
    def validate(self, document):
        if len(document.text) < 8:
            raise ValidationError(
                message="Must be at least 8 characters long.",
                cursor_position=len(document.text),
            )
        
custom_style_fancy = Style([
    ('highlighted', 'fg:#ffff00'), # pointed-at choice in select and checkbox prompts
])