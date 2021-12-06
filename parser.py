import pandas as pd
read_file=pd.read_excel('Master.xlsx')
read_file.to_csv(r'login.csv',index=None,header=True)
read_file2=pd.read_excel('fullName.xlsx')
read_file2.to_csv(r'department_info.csv',index=None,header=True)
import json
import csv
def users_data_parsing():
    with open("login.csv", "r") as user_info:
        reader = csv.DictReader(user_info)
        data = []
        for line in reader:
            data.append({"Email": line['Email'], "Password": line['Password']})

        with open("user.json", "w") as user_json:
            json.dump(data, user_json, indent=4)   # data convert into json format with using data list
        with open('user.json','r') as stro:  #here data read from json file
           employe=json.load(stro)
           user_mails = employe[0]['Email']
           user_passwords = employe[0]['Password']
           return user_mails,user_passwords
def jobs_search():
    with open("department_info.csv", "r") as user_info:
        reader = csv.DictReader(user_info)
        departments_data= []
        for line in reader:
            departments_data.append({"Departments": line['What/All Words'], "Locations": line['Where']})
        # data attached key value pair in data list
        with open("job_search.json", "w") as departments_info_json:
            json.dump(departments_data, departments_info_json, indent=4)   # data convert into json format with using data list

        with open('job_search.json','r') as fields_data:  #here data read from json file
           search_data=json.load(fields_data)
           department_info = search_data[1]['Departments']
           locations_info = search_data[1]['Locations']
           return department_info,locations_info
print(jobs_search())
print(users_data_parsing())
