def signup():
    global usname 
    global pasw 
    usname=input('create uour aura username here ->:')
    pasw=input('create your password here.pstt dont share it unlessss ->:')
signup()

def auth():
    pass
   #now update a sql table of userdata in the project 
def signin():
    global inusername
    global inpassword
    inusername=input('enter your username')
    inpassword=input('enter your password')
    auth(inusername,inpassword)


    
