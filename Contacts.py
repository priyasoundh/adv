def search(name,dict1):
  if name in dict1:
    return 1
  else:
    return 0

def count(dict1):
  s=0
  for x in dict1.keys():
    s=s+1
  return s
print("Welcome to contacts")

def searchnum(name,dict1):
  if name in dict1:
    return dict1[name]

dict1={}
di={}
while(1):
  print("1--> create a contact")
  print("2--> delete a contact")
  print("3--> edit a contact")
  print("4--> search a contact")
  print("5--> display contact")
  print("6--> exit")
  x=int(input())

  if(x==1):
    name=input("enter the name:")
    number=input("enter the number:")
    mail=input("enter the mailid:")
    di={"number":number,"mail":mail}
    dict1[name]=di
    print("successfully created a contact")

  elif(x==2):
    s=count(dict1)
    if(s==0):
      print("contact list is empty")
    else:
      name=input("enter the name to delete:")
      x=search(name,dict1)
      if(x==1):
        dict1.pop(name)
        print("successfully deleted a contact")
      elif(x==0):
        print("contact doesn't exist")

  elif(x==3):
    s=count(dict1)
    if(s==0):
      print("contact list is empty")
    else:
      print("1--> edit number")
      print("2--> edit Name")
      print("2--> edit mail")
      d=int(input())

      if(d==1):
        name=input("enter the name to edit:")
        x=search(name,dict1)
        if(x==1):
          number=input("enter the number:")
          mail=input("enter the mailid:")
          di={"number":number,"mail":mail}
          dict1[name]=di
          print("successfully edited a contact")
        elif(x==0):
          print("contact doesn't exist")

      if(d==2):
        name=input("enter name to edit:")
        x=search(name,dict1)
        if(x==1):
          num1,mail1=searchnum(name,dict1)
          num=di[num1]
          mail=di[mail1]
          dict1.pop(name)
          name=input("enter the name:")
          di={"number":num,"mail":mail}
          dict1[name]=di
          print("successfully edited a contact")
        elif(x==0):
          print("contact doesn't exist")
      
      if(d==3):
        name=input("enter the name to edit:")
        x=search(name,dict1)
        if(x==1):
          num1,mail1=searchnum(name,dict1)
          num=di[num1]
          dict1.pop(name)
          mail=input("enter the mail:")
          di={"number":num,"mail":mail}
          dict1[name]=di
          print("successfully edited a contact")
        elif(x==0):
          print("contact doesn't exist")

  elif(x==4):
    s=count(dict1)
    if(s==0):
      print("contact list is empty")
    else:
      name=input("enter the name to search:")
      x=search(name,dict1)
      if(x==1):
        print(dict1[name])
      elif(x==0):
        print("contact doesn't exist")
  
  elif(x==5):
    s=count(dict1)
    print("you have ",s," contacts")
    print(dict1)

  elif(x==6):
    print("thank you")
    break

  print("****************************************************")
