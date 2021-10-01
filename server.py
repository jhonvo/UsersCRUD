from flask import Flask, render_template, request, redirect, session
from users_app import app #Adding this so it is connected to the __init__ file.
from users_app.controllers import users_controller

if __name__ == "__main__":
    app.run( debug = True ) #This needs to do at te end of the app so it takes all the commands included above during the debug 