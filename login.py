#!/usr/bin/env python3

# Import needed libraries
import cgi,cgitb,secret,os
from tkinter import N
from templates import login_page,after_login_incorrect,secret_page
from http.cookies import SimpleCookie

cgitb.enable()

# 4. POST form to self
# Setup cgi and assign fields
c = cgi.FieldStorage()
username = c.getfirst("username")
password = c.getfirst("password")

# Everything prints to html
print("Content-Type: text/html")

# 5. Modify your CGI script to set a cookie if the login is correct.
# initialize cookie
cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_user = None
cookie_pass = None
# Check if cookie exists, use fields if it does
if cookie.get("username"):
    cookie_user = cookie.get("username").value

if cookie.get("password"):
    cookie_pass = cookie.get("password").value

# If cookie is secret key, use that
if cookie_user == secret.username and cookie_pass == secret.password:
    username = cookie_user
    password = cookie_pass

# Set cookie if login okay
if username==secret.username and password==secret.password:
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")
print()

# 6. Modify your CGI script so it displays a secret message if the cookie says the user is logged in. 
#    You may use secret_page() from templates.py.

# If no input, keep displaying login page
if (not username) and (not password):
    print(login_page())

# Else if secret info, display secret page
elif username==secret.username and password==secret.password:
    print(secret_page(username,password))

# Else incorrect login
else:
    print(after_login_incorrect())
