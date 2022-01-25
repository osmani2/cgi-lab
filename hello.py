#!/usr/bin/env python3

import os, json

# 1. Examine environment variables
# print("Content-Type: text/plain")
# print(os.environ)

# 2. Make your CGI script serve the environment back as JSON.
# print("Content-Type: application/json")
# print()
# print(json.dumps(dict(os.environ)))

#    What changes if we add query parameters? Modify your CGI script to report the values of the query parameters in the HTML.
print("Content-Type: text/html")
print()
print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")

# STUDENT RESPONSIBILITY
# 3. Modify your CGI script to report the user’s browser in the HTML.
print(f"<p>HTTP_USER_AGENT={os.environ['HTTP_USER_AGENT']}</p>")