from django.db import models

# Create your models here.
def addUser(name, email, password):
    User = {
        "Name" : name,
        "Email" : email,
        "Password" : password
    }
    # connect to db
    # add user to db