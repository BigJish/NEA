from tkinter import *
import json

user = ""

class window:
    def __init__(self):
        self.win = Tk()
        self.win.title('Login')
        self.win.geometry("300x200")
        
    def remove(self, widgets):
        for i in widgets:
            i.grid_remove()
            
    def stop(self):
        self.win.destroy()
    
    def check(self, username, password):

        f = open("Users.txt","r")
        users = json.load(f)
        f.close()
        
        found = False
        access = False
        
        l1 = Label(self.win, text = "Username not found")
        l2 = Label(self.win, text = "Incorrect password")
        
        try:
            l1.grid_remove()
        except:
            pass
        try:
            l2.grid_remove()
        except:
            pass
        
        for user in users:
            if username == user:
                found = True
                if users[user][0]["password"] == password:
                    self.load(user)
                    
            
        if found != True:
            l1.grid(row = 3, column = 1)
            
        if found == True and access != True:
            l2.grid(row = 3, column = 1)
        
    def add(self, username, password, w):
        f = open("Users.txt","r")
        users = json.load(f)
        f.close()
        
        l1 = Label(self.win, text = "Username already exists")
        w.append(l1)
        
        found = False
        for user in users:
            if username == user:
                found = True
                
        if found != True:
            psword = [{"password":password},{"Total Stars":0},{"Games":{"Game1":{"Highscore":0,"Stars":0,"Status":True,},"Game2":{"Highscore":0,"Stars":0,"Status":False,},"Game3":{"Highscore":0,"Stars":0,"Status":False,},"Game4":{"Highscore":0,"Stars":0,"Status":False,}}}]
            users[username] = psword
            f = open("Users.txt","w")
            json.dump(users, f)
            f.close()
            
            try:
                l1.grid_remove()
            except:
                pass
            
            self.remove(w)
            self.win1()
        
        if found == True:
            l1.grid(row = 3, column = 1)
    
    def load(self, usr):
        global user
        self.stop()
        user = usr
    
    def win1(self):
        
        self.win.columnconfigure(0, weight = 1)
        self.win.columnconfigure(1, weight = 1)
        self.win.rowconfigure(0, weight = 1)
        self.win.rowconfigure(1, weight = 1)
        
        w = []

        l1 = Label(self.win, text = "Welcome!")
        b1 = Button(self.win, text = "New User", command = lambda:[self.signUpWin(), self.remove(w)])
        b2 = Button(self.win, text = "Continue", command = lambda:[self.loginWin(), self.remove(w)])
        
        w.append(l1)
        w.append(b1)
        w.append(b2)
        
        l1.grid(row = 0,column = 0, columnspan = 2)
        b1.grid(row = 1, column = 0, ipadx = 30, ipady = 40)
        b2.grid(row = 1, column = 1, ipadx = 30, ipady = 40)
        
        Font = (None, 36)
        l1.configure(font = Font)
    
    def loginWin(self):
        
        w = []
        
        self.win.columnconfigure(0, weight = 1)
        self.win.columnconfigure(1, weight = 2)
        self.win.rowconfigure(0, weight = 1)
        self.win.rowconfigure(1, weight = 1)
        self.win.rowconfigure(2, weight = 1)
        self.win.rowconfigure(3, weight = 2)

        l1 = Label(self.win, text = "Login")
        l2 = Label(self.win, text = "Username")
        l3 = Label(self.win, text = "Password")
        e1 = Entry(self.win)
        e2 = Entry(self.win, show = "*")
        b1 = Button(self.win, text="Enter", command = lambda:[self.check(e1.get(),e2.get())])
        b2 = Button(self.win, text="Back", command = lambda:[self.win1(), self.remove(w)])

        w.append(l1)
        w.append(l2)
        w.append(l3)
        w.append(e1)
        w.append(e2)
        w.append(b1)
        w.append(b2)

        l1.grid(row = 0, column = 1)
        l2.grid(row = 1, column = 0)
        l3.grid(row = 2, column = 0)
        e1.grid(row = 1, column = 1)
        e2.grid(row = 2, column = 1)
        b1.grid(row = 3, column = 0, ipadx = 25, ipady = 5)
        b2.grid(row = 0, column = 0, ipadx = 25, ipady = 5)
        
        Font = (None, 24)
        l1.configure(font = Font)
#         self.win.bind('<Return>', lambda:[self.check(e1.get(),e2.get())])
    
    def signUpWin(self):
        
        w = []
        
        self.win.columnconfigure(0, weight = 1)
        self.win.columnconfigure(1, weight = 2)
        self.win.rowconfigure(0, weight = 1)
        self.win.rowconfigure(1, weight = 1)
        self.win.rowconfigure(2, weight = 1)
        self.win.rowconfigure(3, weight = 2)

        l1 = Label(self.win, text = "Sign Up")
        l2 = Label(self.win, text = "Username")
        l3 = Label(self.win, text = "Password")
        e1 = Entry(self.win)
        e2 = Entry(self.win)
        b1 = Button(self.win, text="Enter", command = lambda:[self.add(e1.get(),e2.get(), w)])
        b2 = Button(self.win, text="Back", command = lambda:[self.win1(), self.remove(w)])
        
        w.append(l1)
        w.append(l2)
        w.append(l3)
        w.append(e1)
        w.append(e2)
        w.append(b1)
        w.append(b2)

        l1.grid(row = 0, column = 1)
        l2.grid(row = 1, column = 0)
        l3.grid(row = 2, column = 0)
        e1.grid(row = 1, column = 1)
        e2.grid(row = 2, column = 1)
        b1.grid(row = 3, column = 0, ipadx = 25, ipady = 5)
        b2.grid(row = 0, column = 0, ipadx = 25, ipady = 5)
        
        Font = (None, 24)
        l1.configure(font = Font)
#         self.win.bind('<Return>', lambda:[self.add(e1.get(),e2.get(), w)])

    def run(self):
        self.win1()

        self.win.mainloop()

if __name__ == '__main__': 
    window().run()
    
    
from Main import *
game = Game(user)
game.run()