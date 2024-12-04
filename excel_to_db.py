from openpyxl import load_workbook
import pandas as pd
import sqlite3



skillpaths = pd.read_excel("Three tables data.xlsx",sheet_name=0)

skillroles = pd.read_excel("Three tables data.xlsx",sheet_name=1)

skillclasses = pd.read_excel("Three tables data.xlsx",sheet_name=2)


conn =  sqlite3.connect("skill.db")
conn.cursor()
def config_table(db,table_name:str,first_param,second_param,third_param,fourth_param):
    """
    Creates a db then sqlite3 table
    :param conn: Is the connection of a SQLite DB connection from SQLite3 which will be created if one doesnt exist
    :param table_name: the name of the table
    :param first_param: Name of the first column
    :param second_param: Name of the Second column
    :param third_param: Name of the Third column
    :param fourth_param: Name of the Fourth column   
    
    """
    conn =  sqlite3.connect(db)
    conn.cursor()
    conn.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
    {first_param} TEXT,              
    {second_param} TEXT,
    {third_param} TEXT NOT NULL,
    {fourth_param} TEXT 
    );""")
def input_db(df):
    """
    checks if the dataframe given matches that of the text then inserts from the excel file to the db file
    :param df: dataframe of the file
    """
    conn =  sqlite3.connect("skill.db")
    conn.cursor()
    
    match df.__str__():
        case 'skillclasses':
            for index,row in skillclasses.iterrows():
                conn.execute('''
                INSERT INTO skillclasses (
                           ClassID,
                           Rolename,
                           id
                           ) VALUES (?,?,?)
''',(row[0],row[1],row[2]))
                conn.commit()
                


        case 'skillpaths':
            for index,row in skillpaths.iterrows():
                conn.execute('''
                INSERT INTO skillpaths (
                           id,
                           skillpathname,
                           skillpathdescription
                           ) VALUES (?,?,?)
''',(row[0],row[1],row[2]))
            conn.commit()

        case 'skillroles':
            for index,row in skillroles.iterrows():
                conn.execute('''
                INSERT INTO skillroles (
                           id,
                           Rolename,
                           Roledescription
                           ) VALUES (?,?,?)
''',(row[0],row[1],row[2]))
            conn.commit()




