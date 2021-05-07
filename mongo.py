import pymongo


def insert_data(name,email,phone,password):
    myClient = pymongo.MongoClient()
    db = myClient["foodOrdering"]
    col= db["customersDetails"]
    rec1 = {
        "name":name,
        "email":email,
        "phone":phone,
        "pass":password
    }
    rec_id = col.insert_one(rec1)
    print("Data inserted with record id ",rec_id)
    cursor = col.find()
    for x in cursor:
        print(x)


def select_data(phone,password):
    myClient = pymongo.MongoClient()
    db = myClient["foodOrdering"]
    col = db["customersDetails"]
    rec1 = {
        "phone": phone,
        "pass": password
    }
    sel = list(col.find(rec1))
    print(sel)




