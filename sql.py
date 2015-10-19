# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 16:57:33 2015

@author: Ofer
"""
import MySQLdb
import json
import matplotlib.pyplot as plt


def query():
    db_var = MySQLdb.connect(host='52.18.16.74',
                             user='ofer',
                             passwd='1qwsdc',
                             db='mango')
    cursor = db_var.cursor()
    sql_query = 'select * from pointValues limit 100'
    cursor.execute(sql_query)
    data = cursor.fetchall()
    return data


def read_json():
    with open('his-shufersal-20151014-0814.json', 'r') as json_file:
        json_data = json.load(json_file)
        json_file.close()
    return json_data


def unicode_to_float(data=json_data[u'rows'][1][u'v0'], start=2, end=-2):
    return float(data[start:end])


def make_list(col_name='v0', data=json_data['rows']):
    new_list = []
    for i in range(len(data)):
        new_list.append(unicode_to_float(data[i][col_name]))
    return new_list


def run():
    json_data = read_json()
    v0 = make_list('v0')
    v1 = make_list('v1')
    v2 = make_list(col_name='v2', data=json_data['rows'])
    v3 = make_list('v3')
    v4 = make_list('v4')  
    v5 = make_list('v5')
    #plt.plot(range(len(v0)), v0)
    #plt.plot(range(len(v0)), v2)
    plt.plot(range(len(v0)), v3)
    plt.plot(range(len(v0)), v4)
    #plt.plot(range(len(v0)), v5)
    plt.show()

if __name__ == '__main__':
    run()
