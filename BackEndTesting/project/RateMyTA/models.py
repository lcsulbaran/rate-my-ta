from django.db import models
from ssl import CERT_NONE, CERT_REQUIRED, SSL_ERROR_SSL, SSL_ERROR_SYSCALL
from django.conf import settings
import pymongo
from bson.objectid import ObjectId
import certifi
from django.contrib.auth.models import User

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



def verifyUser(username, password):

    ca = certifi.where()
    connect_string =  f"mongodb+srv://adamabouelhassan:RateMyTA@cluster0.al5jt.mongodb.net/RateMyTA?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connect_string, tlsCAFile=ca)


    dbname = my_client['RateMyTA']
    collection_name = dbname["Students"]

    exists = collection_name.find_one({"Username": username, "Password": password})
    if(exists == None):
        print('login information is incorrect')
    else:
        print('user logged in')


def findReviews(taId):

    ca = certifi.where()
    connect_string =  f"mongodb+srv://adamabouelhassan:RateMyTA@cluster0.al5jt.mongodb.net/RateMyTA?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connect_string, tlsCAFile=ca)


    dbname = my_client['RateMyTA']
    collection_name = dbname["Reviews"]

    reviews = list(collection_name.find({"TA_ID": taId}))
    if reviews == None:
        print("No reviews found for this TA")
    else:
        print(reviews)
    return reviews

def findTAByID(taId):

    ca = certifi.where()
    connect_string =  f"mongodb+srv://adamabouelhassan:RateMyTA@cluster0.al5jt.mongodb.net/RateMyTA?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connect_string, tlsCAFile=ca)


    dbname = my_client['RateMyTA']
    collection_name = dbname["TAs"]

    TA = collection_name.find_one({"_id": ObjectId(taId)})
    if TA == None:
        print("No TA found")
    else:
        print(TA)
    return TA


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
        print(taResult)
        print(taResult['_id'])
    
    return taResult



def createReview(title, body, course_code, rating, taId):

    print("inside createReview")

    
    ca = certifi.where()
    connect_string =  f"mongodb+srv://adamabouelhassan:RateMyTA@cluster0.al5jt.mongodb.net/RateMyTA?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connect_string, tlsCAFile=ca)

    dbname = my_client['RateMyTA']
    collection_name = dbname["Reviews"]

    ta_ID = taId

    Review = {
        "Title": title,
        "Body" : body,
        "Course Code" : course_code,
        "Rating" : rating,
        "TA_ID": ta_ID
    }

    if collection_name.insert_one(Review) != None:
        print("Review added")
    else:
        print("Error, review not added")
