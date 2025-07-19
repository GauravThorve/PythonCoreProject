import getpass
import mysql.connector

class Movie:
    def __init__(self):
        self.db=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Gaurav0177!",
            database="Movie",
            auth_plugin="mysql_native_password"
        )
        self.cursor=self.db.cursor()
        self.name="Movie"
        self.var1=""
        self.var2=""
        self.var3=""
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users  (
            Name VARCHAR(100),
            Password VARCHAR(30),
            Email VARCHAR(30) UNIQUE            
        )""")
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Movie  (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            Title VARCHAR(100),
            Showtime VARCHAR(50)
        )""")
        self.db.commit()



    def Register(self):

        name=input("Enter your Name to Register :")
        if name.isdigit():
            print("Please Enter a Valid Name to Register ")
            return
        email=input("Enter your Email to Register")
        if "@gmail.com" not in email:
            print("Please Enter a Valid Email ID to Register ")
            return
        #self.cursor.execute("SELECT * FROM users WHERE email =%s",(email))
        if self.cursor.fetchone():
            print("This Email ID is Already Exists!!")
            return
        password = input("Create a Password to Register :")
        self.cursor.execute("INSERT INTO users(Name,Password,Email) VALUE(%s,%s,%s)",(name,password,email))
        self.db.commit()
        print("                                        ")
        print("Your Registration Completed Successfully!")

    def Admin_Login(self):
        print("                           ")
        print("Admin Login")
        self.var1=input("Enter your Name :")
        if self.var1.lower()=="gaurav":
            password=input("Enter your Password :")
            if password=="0177":
                print("               ")
                print("Wel-Come Admin")
                while(True):
                    print("\n1)Add New Movie \n2)Add or Edit Showtime \n3)Remove Movies \n4)Exit ")
                    chh=int(input("Enter your Choice :"))
                    if chh==1:
                        self.Add_Movies()
                    elif chh==2:
                        self.Add_or_Edit_Movies()
                    elif chh==3:
                        self.Remove_Movies()
                    elif chh==4:
                        break
                    else:
                        print("Please Enter a Valid Choice!")
            else:
                print("Incorrect Password!")
        else:
            print("Incorrect Username!")



    def User_Login(self):
        Mail=input("Enter your Email ID :")
        if "gmail.com" not in Mail:
            print("Please enter a Valid Email Which is Registered. ")
            return
        self.cursor.execute("SELECT name, password FROM users WHERE email=%s",(Mail,))
        result=self.cursor.fetchone()
        if result:
            self.var2=result[0]
            password=input("Enter a Password :")
            if password==result[1]:
                print(f"----->|Wel-Come {self.var2}|<-----")
                while(True):
                    print("                      ")
                    print("1)Show Movies \n2)Forgot Password \n3)Show MovieTime \n4)Exit")
                    chh=int(input("Enter a Choice :"))
                    if chh==1:
                        self.Show_Movies()
                    elif chh==2:
                        self.Forgot_Password()
                    elif chh==3:
                        self.Show_Movietime()
                    elif chh==4:
                        break
                    else:
                        print("Invalid Choice!")
            else:
                print("Password is Incorrect!")

    def Show_Movies(self):
        self.cursor.execute("SELECT title FROM Movie")
        movies=self.cursor.fetchall()
        print("\n---Available Movies---")
        for index,movie in enumerate(movies,start=1):
            print("          ")
            print(f"{index}){movie}")

    def Forgot_Password(self):
        Mail=input("Enter a Email ID :")
        self.cursor.execute("SELECT * FROM users WHERE Email=%s",(Mail,))
        present=self.cursor.fetchall()
        if present:
            npass = input("Enter a New Password :")
            self.cursor.execute("UPDATE users SET password=%s WHERE Email=%s", (npass, Mail,))
            self.db.commit()
            print("Password Updated Successfully!!")
        else:
            print("Email ID is Incorrect!!")
    def Add_Movies(self):
        Movie_Title=input("Enter a Movie Name : ")
        self.cursor.execute("SELECT * FROM Movie where title=%s",(Movie_Title,))
        result=self.cursor.fetchone()
        if result:
            print("Movie Name Already Exists")
        else:
            self.cursor.execute("INSERT INTO Movie(title)VALUE(%s)",(Movie_Title,))
            self.db.commit()
            print("Movie has Added Successfully!")


    def Remove_Movies(self):
        Mname=input("Enter a Movie which you want to Delete :")
        self.cursor.execute("SELECT * FROM Movie WHERE Title=%s",(Mname,))
        present=self.cursor.fetchone()
        if present:
            self.cursor.execute("DELETE FROM Movie WHERE Title=%s",(Mname,))
            self.db.commit()
            print("Movie Removed Successfully!!")
        else:
            print("Movie Name is Incorrect!!")


    def Add_or_Edit_Movies(self):

        Mname=input("Enter a Movie Name :")
        self.cursor.execute("SELECT * FROM Movie WHERE Title=%s",(Mname,))
        present=self.cursor.fetchone()
        if present:
            print("Movie is Already Exists!")
            Stime=input("Enter a Showtime of the Movie :")
            self.cursor.execute("UPDATE Movie SET Showtime=%s WHERE Title=%s",(Stime,Mname,))
            self.db.commit()
            print("Movie Showtime Updated Successfully!!")
        else:
            Stime = input("Movie not Found.\nEnter a Showtime of the Movie :")
            self.cursor.execute("INSERT INTO Movie(Showtime,Title) VALUES(%s,%s)",(Stime,Mname,))
            self.db.commit()
            print("Movie Title and Showtime is Added Successfully!!")


    def Show_Movietime(self):
        self.cursor.execute("SELECT Title, Showtime FROM Movie")
        Time=self.cursor.fetchall()
        print("---> Available Movie and ShowTime --->")
        for index,i in enumerate(Time,start=1):
            print(f"{index}{i}")

    def Home(self):
        print("Wel-Come to Movie Max")
        while(True):
            print("                                                                        ")
            print("1)User Register \n2)User Login \n3)Admin Login \n4)Show Movies \n5)Exit")
            gett=int(input("Enter your Choice :"))
            if gett==1:
                self.Register()
            elif gett==2:
                self.User_Login()
            elif gett==3:
                self.Admin_Login()
            elif gett==4:
                self.Show_Movies()
            elif gett==5:
                print("Thanks for using our Project")
                break
            else:
                print("Enter a Valid Choice!")



ggg=Movie()
ggg.Home()

