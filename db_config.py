import sqlite3


def return_skillroles()->dict:
    """
    :return: Returns List of [id,Rolename,Roledescription]
    
    """
    lister = []
    db = sqlite3.connect("skill.db")
    db.cursor()
    ob = db.execute('''
    SELECT id,Rolename,Roledescription from skillroles 
''').fetchall()
    for id,Rolename,Roledescription in ob:    
        lister.append([id,Rolename,Roledescription])
    return lister


def return_skillclasses()->dict:
    """
    :return: Returns List of [ClassID,Rolename,id]
    
    """
    lister = []
    db = sqlite3.connect("skill.db")
    db.cursor()
    ob = db.execute('''
    SELECT ClassID,Rolename,id from skillclasses 
''').fetchall()
    for ClassID,Rolename,id in ob:    
        lister.append([ClassID,Rolename,id])
    return lister


def return_skillpaths()->dict:
    """
    :return:  Returns List of [id,skillpathname,skillpathdescription]
    
    """
    lister = []
    db = sqlite3.connect("skill.db")
    db.cursor()
    ob = db.execute('''
    SELECT id,skillpathname,skillpathdescription from skillpaths 
''').fetchall()
    for id,skillpathname,skillpathdescription in ob:    
        lister.append([id,skillpathname,skillpathdescription])
    return lister


