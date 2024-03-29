# Flask Setup
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import os
from flask import Flask, jsonify, request, abort, render_template
app = Flask(__name__)

# Google Sheets API Setup
credential = ServiceAccountCredentials.from_json_keyfile_name("/etc/secrets/cred.json",["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets",
"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"])

client = gspread.authorize(credential)
o = client.open("UserDB")
db = o.worksheet('College')
#corps
studb = client.open("StuDB")
