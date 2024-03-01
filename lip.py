from tkinter import *

root=Tk()

root.title("MANAGEMENT")
root.geometry("660x660")
root.config(bg="green")

lblh=Label(root, text="WELCOME TO LIB MNG\n FIND YOUR BOOKS HERE!", bg="green",font="Times 25 bold",fg="black")
lblh.place(x=180,y=0)
lblsh=Label(root,text="Fill All The Details",bg="green",font="LUCIDA 20")
lblsh.place(x=220,y=100)

lbl_Name= Label(root,text="YOUR NAME:",bg="green",font="times 15 bold")
lbl_Name.place(x=100,y=170)
txt_Name=Entry(root,fg="black",width="35")
txt_Name.place(x=300,y=170)

lbl_BRAN= Label(root, text="BRANCH:",bg="green",font="times 15 bold")
lbl_BRAN.place(x=100,y=220)
txt_BRAN=Entry(root,fg="black",width="35")
txt_BRAN.place(x=300,y=220)

lbl_Cllg= Label(root, text="COLLEGE:",bg="green",font="times 15 bold")
lbl_Cllg.place(x=100,y=270)
txt_Cllg=Entry(root,fg="black",width="35")
txt_Cllg.place(x=300,y=270)

lbl_Con= Label(root, text="CONTACT NO:",bg="green",font="times 15 bold")
lbl_Con.place(x=100,y=320)
txt_Con=Entry(root,fg="black",width="35")
txt_Con.place(x=300,y=320)

lbl_Bday= Label(root, text="DD/MM/YYYY",bg="green",font="times 15 bold")
lbl_Bday.place(x=90,y=370)
txt_Bday=Entry(root,fg="black",width="35")
txt_Bday.place(x=300,y=370)

lbl_Roll= Label(root, text="UNIVERSITY ROLLNO.",bg="green",font="times 15 bold")
lbl_Roll.place(x=90,y=420)
txt_Roll=Entry(root,fg="black",width="35")
txt_Roll.place(x=300,y=420)

lbl_Id= Label(root, text="COLLEGE ID:",bg="green",font="times 15 bold")
lbl_Id.place(x=100,y=470)
txt_Id=Entry(root,fg="black",width="35")
txt_Id.place(x=300,y=470)



        
        
    
        
def find():
        root1=Tk()
        root1.geometry("600x600")
        root1.title("MANDATORY POINTS")
        root1.config(bg="yellow")

        lblh1=Label(root1, text="🤥MANDATORY POINTS-!", bg="yellow",font="Times 30 bold",fg="red")
        lblh1.pack()

        lblh2=Label(root1, text="* DO NOT TAKE ANY BOOK OR OTHER LIBRAARY MATERIAL OUT OF \nTHE LIBRARY W/O FOLLOWING THE BORROWING PROCEDURE",fg="red",font = "times 15 ",bg="yellow")
        lblh2.place(x=20,y=110)

        lblh3=Label(root1, text="* MAKE SURE TO REURN THE BORROWED ITEMS BY THE DUE DATE ",fg="red",font = "Times 15 ",bg="yellow")
        lblh3.place(x=20,y=160)

        lblh4=Label(root1, text="* IN CASE ANY OF THE BORROWED ITEMS BEING LOST ,DAMAGE,\nOR DESTROYED ,YOU ARE REQUIRED TO REPLACE THE LOST/DAMAGE\n/DESTROYED ITEMS WITH A NEW ONE ",fg="red",bg="yellow",font = "times 15")
        lblh4.place(x=20,y=210)

        lblh5=Label(root1, text="* NEVER WRITE IN BOOKS OR CUT PAGES OUT OF THEM  ",fg="red",font = "times 15 ",bg="yellow")
        lblh5.place(x=20,y=260)

        lblh6=Label(root1, text="* RETURN BOOKS/MATERIALS TO THEIR ORIGINAL LOCATION ON THE \nBOOK SELF.  ",fg="red",font = "times 15 ",bg="yellow")
        lblh6.place(x=20,y=310)

        lblh7=Label(root1, text="* USER CAN ALSO RENEW THE BOOKS AGAIN AFTER THE COMPLETION  \nOF CHARGING PERIOD, SUBJECT TO NOT BEING REQUESTED FROM \nSOME OTHER USER.  ",fg="red",font = "times 15 ",bg="yellow")
        lblh7.place(x=20,y=360)

        lblh8=Label(root1, text="* READERS SHOULD NOT MARK,UNDERLINE,DOG-EAR,WRITE,TEAR PAGES  \nOR OTHERWISE DAMAGE THE LIBRARY DOCUMENTS.  ",fg="red",font = "times 15 ",bg="yellow")
        lblh8.place(x=20,y=410)

        lblh9=Label(root1, text="* NO LIBRARY MATERIALS CAN BE TAKEN OUT OF THE LIBRARY W/O \nPERMISSION.  ",fg="red",font = "times 15 ",bg="yellow")
        lblh9.place(x=20,y=460)
        bran=txt_BRAN.get().lower()

        def std_list():
            frame_3=Tk()
            frame_3.title("BOOK LIST ")
            frame_3.geometry("600x400")
            frame_3.config(bg="yellow")

            BRANCH=bran
            lbl_match=Label(frame_3,bg="yellow",font="Times 15 bold")
            lbl_match.place(x=100,y=150)
            if(BRANCH == "cs"):
                
                    lbl_books=Label(text="LIST OF BOOKS FOR YOUR SELECTED BRANCH ARE-",bg="yellow",fg="red",font="times 20")
                    lbl_books.place(x=65,y=0)
                    lbl_match.config(text="1. CRYPTOGRAPHY AND NETWORK SECURITY \n2. DATABASE ENGINEERING \n3. REAL TIME SYSTEM\n4. COMPLEX NETWORKS \n5. PHYSICS \n6. MACHINE LEARNING")
                    
            elif (BRANCH == "it"):
                    
                    lbl_books=Label(text="LIST OF BOOKS FOR YOUR SELECTED BRANCH ARE-",bg="yellow",fg="red",font="times 20")
                    lbl_books.place(x=65,y=0)
                    lbl_match.config(text="1. COMPUTER ORGANISATION AND ARCHITECTURE\n2. THEORY OF COMPUTATION\n3. COMPUTER NETWORKS\n4. ARTIFICIAL INTELLIGENCE\n5. MICROPROCESSORS AND MICROCONTROLLERS ")

            elif (BRANCH == "ec"):
                        
                    lbl_books=Label(text="LIST OF BOOKS FOR YOUR SELECTED BRANCH ARE-",bg="yellow",fg="red",font="times 20")
                    lbl_books.place(x=65,y=0)
                    lbl_match.config(text="1. INTRODUCTION TO ELECTRODYNAMICS\n2. A TEXTBOOK OF ELECTRICAL TECHNOLOGY\n3. PRINCIPAL OF ELECTROMAGNETICS\n4. ABOUT LOGIC GATES\n5. MICRO CIRCUITS ")
            
            elif (BRANCH == "ee"):
                    
                    lbl_books=Label(text="LIST OF BOOKS FOR YOUR SELECTED BRANCH ARE-",bg="yellow",fg="red",font="times 20")
                    lbl_books.place(x=65,y=0)
                    lbl_match.config(text="1. LINEAR AND NON LINEAR CIRCUITS\n2. ANALYSIS AND DESIGN OF AMPLIFIERS\n3. FEEDBACK CONTROL SYSTEM\n4. MICROCHIPS\n5.  MICROCHIPS CONTROLLERS ")
            
            elif (BRANCH == "me"):
                    
                    lbl_books=Label(text="LIST OF BOOKS FOR YOUR SELECTED BRANCH ARE-",bg="yellow",fg="red",font="times 20")
                    lbl_books.place(x=65,y=0)
                    lbl_match.config(text="1. DESIGN OF MACHINE ELEMENTS\n2. FLUID MECHANICS \n3. SHIGLEY'S MECHANICAL ENGINEERING DESIGN\n4. FUNDAMENTAL POF THERMODYNAMICS ")
            
            elif (BRANCH == "ce"):
                    
                    lbl_books=Label(text="LIST OF BOOKS FOR YOUR SELECTED BRANCH ARE-",bg="yellow",fg="red",font="times 20")
                    lbl_books.place(x=65,y=0)
                    lbl_match.config(text="1. STENGTH OF MATERIALS\n2. STRUCTURAL ANALYSIS\n3. THE CIVIL ENGINEERING AHND BOOK \n4. WHY BUILDINGS FALL DOWN\n5. CIVIL ENGINEERING FORMULAS")
            
            root1.destroy()
            frame_3.mainloop()        

        btn_next = Button(root1,text="      Next     ",font="Times 15 bold",bg="green",command=std_list)
        btn_next.place(x=280,y=550)            
           
            
            

        root.destroy()

        root1.mainloop()

            
btn1=Button(root,text="SUBMIT",font="LUCIDA 15 bold",bg="white",command=find)
btn1.place(x=380,y=560)

btn2=Button(root,text="   EXIT   ",font="LUCIDA 15 bold",bg="red",command=root.quit)
btn2.place(x=250,y=560)
    
 
root.mainloop()