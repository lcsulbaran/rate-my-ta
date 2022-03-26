from django.db import models
from ssl import CERT_NONE, CERT_REQUIRED, SSL_ERROR_SSL, SSL_ERROR_SYSCALL
from django.conf import settings
import pymongo
from bson.objectid import ObjectId
import certifi
from django.contrib.auth.models import User
from fuzzywuzzy import fuzz, process


# function to find all reviews for a specific ta
def findReviews(taId):

    # establich connection to database
    ca = certifi.where()
    connect_string =  f"mongodb+srv://adamabouelhassan:RateMyTA@cluster0.al5jt.mongodb.net/RateMyTA?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connect_string, tlsCAFile=ca)

    dbname = my_client['RateMyTA']
    collection_name = dbname["Reviews"]

    # find all reviews for ta with taId
    reviews = list(collection_name.find({"TA_ID": taId}))

    return reviews


# function to find all of a tas information using their id
def findTAByID(taId):

    # establich connection to database
    ca = certifi.where()
    connect_string =  f"mongodb+srv://adamabouelhassan:RateMyTA@cluster0.al5jt.mongodb.net/RateMyTA?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connect_string, tlsCAFile=ca)

    dbname = my_client['RateMyTA']
    collection_name = dbname["TAs"]

    # find the ta using their taId
    TA = collection_name.find_one({"_id": ObjectId(taId)})

    return TA


# function to search for a ta using a search string for their name
def searchForTA(searchString):

    # establich connection to database
    ca = certifi.where()
    connect_string =  f"mongodb+srv://adamabouelhassan:RateMyTA@cluster0.al5jt.mongodb.net/RateMyTA?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connect_string, tlsCAFile=ca)

    dbname = my_client['RateMyTA']
    collection_name = dbname["TAs"]

    # all of the tas in the database 
    allTas = collection_name.find({})

    fuzzTaResult = list()

    # iterate through all tas to find fuzzy score compared to search string, add them to results if close enough
    for ta in allTas:
        x = fuzz.partial_ratio(searchString, ta["Name"])

        if x > 65:
            fuzzTaResult.append(ta)

    return fuzzTaResult


# function to add a new review
def createReview(title, body, course_code, rating, taId):

    # establich connection to database
    ca = certifi.where()
    connect_string =  f"mongodb+srv://adamabouelhassan:RateMyTA@cluster0.al5jt.mongodb.net/RateMyTA?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connect_string, tlsCAFile=ca)

    dbname = my_client['RateMyTA']
    collection_name = dbname["Reviews"]

    ta_ID = taId
    Review = {
        "Title": title,
        "Body" : body,
        "CourseCode" : course_code,
        "Rating" : rating,
        "TA_ID": ta_ID
    }

    # recalculate rating based on new review
    x = rating

    # add up all rating scores for a ta and average them
    allReviews = list(collection_name.find({"TA_ID": ta_ID}))
    if allReviews != None:
        for review in allReviews:
            x += review["Rating"]

        average = x / (len(allReviews) + 1)

        average = round(average, 2)
    
    else:
        average = x

    # update the database to match newly calculated rating
    ta_collection_name = dbname["TAs"]
    ta_collection_name.update_one({"_id" : ObjectId(ta_ID)}, {"$set": { "Rating": average}})

    collection_name.insert_one(Review)