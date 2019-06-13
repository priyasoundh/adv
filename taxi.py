name=input("enter your name:")
while(1):
    print("Select your taxi from coimbatore:")
    print("1 --> Ola")
    print("2 --> Uber")
    print("3 --> Redtaxi")
    print("4 --> Fasttrack")
    a=int(input())
    if(a==1):
        print("you selected Ola")
    if(a==2):
        print("you selected Uber")
    if(a==3):
        print("you selected Redtaxi")
    if(a==4):
        print("you selected Fastrack")
    if(a==1):
        print("Select your destination")
        print("1 --> Kinathukadavu")
        print("2 --> Pollachi")
        print("3 --> Metupalayam")
        n=int(input())
        if(n==1):
            print("you selected Kinathukadavu")
            dist=20
            d="kinathukadavu"
        if(n==2):
            print("you selected Pollachi")
            dist=40
            d="Pollachi     "
        if(n==3):
            print("you selected Metupalayam")
            dist=80
            d="Metupalayam  "
        b=dist-10
        cost=(10*1)+(b*2)
        print("cost is ",cost)
        c="ola     "
    if(a==2):
        print("Select your destination in km")
        print("20kms --> Kinathukadavu")
        print("40kms --> Pollachi")
        print("80kms --> Metupalayam")
        n=int(input())
        cost=n*7
        print("cost is ",cost)
        c="Uber    "
        if(n==20):
            d="kinathukadavu"
        if(n==40):
            d="Pollachi     "
        if(n==80):
            d="Metupalayam  "
    if(a==3):
        print("Select your destination in minutes")
        print("30mins --> Kinathukadavu")
        print("60mins --> Pollachi")
        print("120mins --> Metupalayam")
        n=int(input())
        cost=n*5
        print("cost is ",cost)
        c="Redtaxi "
        if(n==30):
            d="kinathukadavu"
        if(n==60):
            d="Pollachi     "
        if(n==120):
            d="Metupalayam  "
    if(a==4):
        print("Select your destination")
        print("1 --> Kinathukadavu")
        print("2 --> Pollachi")
        print("3 --> Metupalayam")
        n=int(input())
        if(n==1):
            print("you selected Kinathukadavu")
            dist=20
            d="kinathukadavu"
        if(n==2):
            print("you selected Pollachi")
            dist=40
            d="Pollachi     "
        if(n==3):
            print("you selected Metupalayam")
            dist=80
            d="Metupalayam  "
        b=dist-10
        cost=(10*1)+(b*5)
        print("cost is ",cost)
        c="Fastrack"
    cost=str(cost)
    print("******************************************************************")
    print("name:",name)
    print("--------------------------------------------------")
    print("|from      | to            |taxi      |cost      |")
    print("|coimbatore|",d,"|",c,"|",cost,"      |")
    print("--------------------------------------------------")
    file = r'C:\priya\Priyadharshini.txt'
    with open(file,'w') as f:
        f.write("name:")
        f.write(name)
        f.write("\n")
        f.write("--------------------------------------------------")
        f.write("\n")
        f.write("from:")
        f.write("coimbatore")
        f.write("\n")
        f.write("to:")
        f.write(d)
        f.write("\n")
        f.write("taxi:")
        f.write(c)
        f.write("\n")
        f.write("cost:")
        f.write(cost)
        f.write("\n")
        f.write("--------------------------------------------------")
    x=int(input("enter 0 to exit, 1 to continue"))
    if(x==0):
        break
