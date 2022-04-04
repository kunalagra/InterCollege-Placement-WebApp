
from helpers.mailer import *
from helpers.hashpass import *
from helpers.database import *
from app import app
from flask import request, session
import pandas as pd
import json


def checkloginusername():
    username = request.form["username"]
    check = db.find(username)
    if check is None:
        return "No User"
    else:
        return "User exists"


def checkloginpassword():
    username = request.form["username"]
    a = db.find(username)
    b = db.cell(a.row, 4).value
    password = request.form["password"]
    hashpassword = getHashed(password)
    if hashpassword == b:
        session["username"] = username
        return "correct"
    else:
        return "wrong"


def checkusername():
    username = request.form["username"]
    check = db.find(username)
    if check is None:
        return "Available"
    else:
        return "Username taken"

def getData():
    work = studb.worksheet(session['username'])
    #Skip the heading
    ab = work.get_all_values()[1:]
    return ab

def insertStud():
    values = [request.form[k] for k in request.form]
    work = studb.worksheet(session['username'])
    k=work.row_count
    ab = work.cell(k, 1).value
    a=ab[1:]
    a=int(a)+1
    b = 'S' + str(a).rjust(6,'0')
    values[0] = b
    work.append_row(values,value_input_option='USER_ENTERED')

def getStud():
    values =  request.form["sid"]
    work = studb.worksheet(session['username'])
    a = work.col_values(1)
    try:
        a = a.index(values)
        b=work.row_values(a+1)
        b.insert(0,"Found")
        fields=["Find","Student ID","Name","DOB","Gender","Branch","CGPA", "Graduation Year",	"Placement Status","Higher Studies", "Email"]
        data = dict(zip(fields,b))
    except ValueError as vs:
        data={"Find":"Invalid SID"}
    return data

def getYearStats():
    work = studb.worksheet(session['username'])
    data={
    "Placed":work.col_values(8),
    "Graduation Year":work.col_values(7),
    }
    df = pd.DataFrame(data)
    df=df[1:]
    dff = df.groupby(["Graduation Year","Placed"]).size().to_frame('Count').reset_index()
    dff= dff.pivot_table('Count',['Graduation Year'],'Placed').reset_index()
    return dff.to_dict('list')

def braAyear():
    work = studb.worksheet(session['username'])
    data={
    "Placed":work.col_values(8),
    "Graduation Year":work.col_values(5),
    }
    df = pd.DataFrame(data)
    df=df[1:]
    dff = df.groupby(["Graduation Year","Placed"]).size().to_frame('Count').reset_index()
    dff= dff.pivot_table('Count',['Graduation Year'],'Placed').reset_index()
    print(dff.to_dict('list'))
    return dff.to_dict('list')

def branccurStat():
    work = studb.worksheet(session['username'])
    data={
    "Placed":work.col_values(8),
    "Gdy":work.col_values(7),
    "Branch":work.col_values(5)
    }
    df = pd.DataFrame(data)
    df=df[1:]
    df_g = df.query('Gdy=="2022" & Placed=="Yes"')
    df_g.drop('Gdy',axis=1,inplace=True)

    df_g=df_g.groupby('Branch').count().reset_index()
    print(df_g.to_dict('list'))
    return df_g.to_dict('list')

def updStud():
    sid =  request.form["sid"]
    work = studb.worksheet(session['username'])
    a = work.find(sid)
    A = "A"+str(a.row)
    J="J"+str(a.row)
    values = [request.form[k] for k in request.form]
    values = values[1:]
    work.update('{}:{}'.format(A,J),[values],value_input_option='USER_ENTERED')

def deleteStudent():
    sid =  request.form["sid"]
    work = studb.worksheet(session['username'])
    a = work.find(sid)
    work.delete_rows(a.row)


def registerUser():
    fields = [k for k in request.form]
    values = [request.form[k] for k in request.form]        
    values[3] = getHashed(values[3])
    values = values[:-1]
# data = dict(zip(fields, values))
# user_data = json.loads(json.dumps(data))
# user_data["password"] = getHashed(user_data["password"])
# user_data["confirmpassword"] = getHashed(user_data["confirmpassword"])
    db.append_row(values)
    studb.add_worksheet(title=values[1],rows='1',cols='10')
    studb.worksheet(values[1]).append_row(["Student ID","Name","DOB","Gender","Branch","CGPA","Graduation Year","Placement Status","Higher Studies","Email"])
