import datetime
import db
def send_msg_to_db(company_title,job_descriptiom):
    msgCollection = db.connect_to_collection('comapny')


    data = {
        'Company ': company_title,
        'messageId': job_descriptiom,
    }
    msgCollection.insert_one(data)
