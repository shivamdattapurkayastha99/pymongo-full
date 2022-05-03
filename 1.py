from multiprocessing.connection import Client
from pip import main
import pymongo
if __name__=="__main__":
    client = pymongo.MongoClient('localhost', 27017)
    db=Client['ShivamSchool']
    # db = client.test_database
    # collection = db['test-collection']
    collection=db.class1
    print(collection)
    posts = db.posts
    # post_id = posts.insert_one({"p":1}).inserted_id
    studentInfo={
        'name':'Shivam',
        'section':1,
        'maths':100,
        'cs':99
    }
    student_id = collection.insert_one(studentInfo).inserted_id
    print(student_id)