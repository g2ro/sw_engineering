import pymysql
import pandas as pd
import matplotlib.pyplot as plt

def get_menu_id():
    conn = pymysql.connect(host = "localhost",
             user= "root", password = "0000", charset = "utf8")
    cursor = conn.cursor()
    cursor.execute('''SELECT max(menu_id) FROM young_cheline.menu;''')
    menu_data = cursor.fetchall()
    menu_data = menu_data[0][0]
    return menu_data

def get_week_avg(menu_id):
    conn = pymysql.connect(host = "localhost",
        user= "root", password = "0000", charset = "utf8")
    cursor = conn.cursor()

    cursor.execute('''SELECT DATE_FORMAT(time, '%Y-%u') as week, menu_id, avg(flavor)
                FROM young_cheline.evaluate_table
                WHERE menu_id = {}
                GROUP BY week
                ORDER BY menu_id, week;'''.format(menu_id))
    
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['time', 'menu_id', 'flavor'])

    return df


if __name__ == "__main__":
    range_menu = get_menu_id()

    for id in range(1,range_menu + 1):
        df = get_week_avg(id)
        print(df)
