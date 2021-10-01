from typing import ClassVar
from users_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,id,first_name,last_name,email,created_at,updated_at):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created = created_at
        self.updated = updated_at

    @classmethod
    def get_all_users (cls):
        query = "Select * FROM users;"
        results = connectToMySQL("university").query_db(query)
        print (results) #This will be an array of different dictionaries. name['key']
        users = []
        for user in results:
            users.append(User(user['id'], user['first_name'], user['last_name'], user['email'], user['created_at'], user['updated_at']))
        print (users) # This will be an array of different objects, which are easier to write and work with "self.field"
        return users #This is being passed to the controller file.

    @classmethod
    def add_user (cls, newuser):
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"
        data = {
            "first_name" : newuser.first_name,
            "last_name" : newuser.last_name,
            "email" : newuser.email
        }
        results = connectToMySQL("university").query_db(query,data) #calling the functions on the mysqlconnection file, needs to include the data
        print ("RESULTS", results)
        return results

    @classmethod
    def get_user(cls,idnum):
        query = "Select * FROM users WHERE id = %(id)s;"
        data = {
            "id" : idnum
        }
        results = connectToMySQL("university").query_db(query,data)
        print (results) #This will be an array of different dictionaries. name['key']
        userinfo = []
        for userline in results:
            userinfo.append(User(userline['id'], userline['first_name'], userline['last_name'], userline['email'], userline['created_at'], userline['updated_at']))
        print (userinfo) # This will be an array of different objects, which are easier to write and work with "self.field"
        return userinfo #This is being passed to the controller file.

    @classmethod
    def update (cls, updateduser):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s,email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        data = {
            "first_name" : updateduser.first_name,
            "last_name" : updateduser.last_name,
            "email" : updateduser.email,
            "id" : updateduser.id,
        }
        print ("this is data", data)
        results = connectToMySQL("university").query_db(query,data) #calling the functions on the mysqlconnection file, needs to include the data
        return results

    @classmethod
    def deleteuser(cls,idnum):
        query = "DELETE FROM users WHERE id = %(id)s;"
        data = {
            "id" : idnum
        }
        print ("THE ID", idnum)
        results = connectToMySQL("university").query_db(query,data)
        return results #This is being passed to the controller file.