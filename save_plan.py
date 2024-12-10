import os

def create_and_write(name,skill_path,path_desc,role,role_desc,classes:list):
    """
    Keyword arguments:
    
    \nname -- name of text file
    \nskill_path -- skill path user choose
    \npath_desc -- path description
    \nrole -- role user choose
    \nrole_desc -- description of rol
    \nclasses -- classes required for the role
    
    Return: A file with all the variables added
    """
    
    try:
        with open(f"{name}.txt","w") as file:
            text_dump =format(f"Skill Path:{skill_path} \n\nPath Description: {path_desc} \n\nRole: {role}\n\nRole Desciption: {role_desc}\n\nClasses: {classes}") 
            file.write(text_dump.center(40,"\t"))
            file.close()

    except SyntaxWarning:
        pass
 
def print_txtfile(name):
    """
    Does exactly what the name says
    
    \n\tKeyword arguments:
    \n\tname -- name of the file without .txt 
    
    \tReturn: will force print of the file
    """
    
    os.startfile(f"{name}.txt", "print")

def console_print_pretty_list(text_dump:str):
    """
    
    Keyword arguments:
    \ntext_dump --> a string which will split text into blocks of content if seperated with 2 line-breaks in ascii


    Return: a console stdout
    """


    for line in text_dump.split("\n\n"):
                print('\u250c'+'\u2500'*60+'\u2510')
                print('\u2502'+line[0:59]+(' '*(60-len(line[0:59]))+'\u2502'))
                min =59
                if len(line[min:])>0:
                    max = len(line)
                    for i in range(min,len(line)):
                        if (min-60)>max:
                            break
                        print('\u2502'+"-"+line[min: int(*[max if max-min <= 59 else int(*[min+59])])]+(' '*(59-len(line[min:max]))+'\u2502'))
                        if len(line[min:max]) >59:
                            min+=59
                        elif 59>len(line[min:])>0:
                            min += len(line[i:])
                print('\u2515'+'\u2500'*60+'\u2518')




