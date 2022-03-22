from django.db import models
from ssl import CERT_NONE, CERT_REQUIRED, SSL_ERROR_SSL, SSL_ERROR_SYSCALL
from django.conf import settings
import pymongo
import certifi

# Create your models here.
def addUser(name, email, password):

    ca = certifi.where()
    connect_string =  f"mongodb+srv://adamabouelhassan:RateMyTA@cluster0.al5jt.mongodb.net/RateMyTA?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connect_string, tlsCAFile=ca)
    
    dbname = my_client['RateMyTA']
    collection_name = dbname["Students"]

    User = {
        "Name" : name,
        "Email" : email,
        "Password" : password
    }

    exists = collection_name.find_one({"Email": email})
    if(exists == None):
        collection_name.insert_one(User)
    else:
        print('email is already used')



def verifyUser(email, password):

    ca = certifi.where()
    connect_string =  f"mongodb+srv://adamabouelhassan:RateMyTA@cluster0.al5jt.mongodb.net/RateMyTA?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connect_string, tlsCAFile=ca)


    dbname = my_client['RateMyTA']
    collection_name = dbname["Students"]

    exists = collection_name.find_one({"Email": email, "Password": password})
    if(exists == None):
        print('login information is incorrect')
    else:
        print('user logged in')



def searchForTA(searchString):

    ca = certifi.where()
    connect_string =  f"mongodb+srv://adamabouelhassan:RateMyTA@cluster0.al5jt.mongodb.net/RateMyTA?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connect_string, tlsCAFile=ca)


    dbname = my_client['RateMyTA']
    collection_name = dbname["TAs"]

    taResult = collection_name.find_one({"Name": searchString})
    if(taResult == None):
        print('ta not found, searchString: ' + searchString)
    else:
        print('there is a ta with that name: ' + taResult['School'])
        print(taResult)



def createReview(title, body, course_code, rating):

    print("inside createReview")

    
    ca = certifi.where()
    connect_string =  f"mongodb+srv://adamabouelhassan:RateMyTA@cluster0.al5jt.mongodb.net/RateMyTA?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connect_string, tlsCAFile=ca)

    dbname = my_client['RateMyTA']
    collection_name = dbname["Reviews"]

    student_ID = 0
    ta_ID = 0

    Review = {
        "Title": title,
        "Body" : body,
        "Course Code" : course_code,
        "Rating" : rating,
        "Student_ID" : student_ID,
        "TA_ID": ta_ID
    }

    if collection_name.insert_one(Review) != None:
        print("Review added")
    else:
        print("Error, review not added")
