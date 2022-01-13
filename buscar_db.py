# update the appointments
from tkinter import *
import tkinter.messagebox 
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

class Application:
    def __init__(self, master):
        self.master = master
        # heading label
        self.heading = Label(master, text="Alquileres registrados",  fg='grey', font=('arial 40 bold'))
        self.heading.place(x=150, y=20)

        # search criteria -->name 
        self.name = Label(master, text="Ingrese el nombre del cliente", font=('arial 18 bold'))
        self.name.place(x=0, y=100)

        # entry for  the name
        self.namenet = Entry(master, width=30)
        self.namenet.place(x=280, y=92)

        # search button
        self.search = Button(master, text="buscar", width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=350, y=132)
    # function to search
    def search_db(self):
        self.input = self.namenet.get()
        # execute sql 

        sql = "SELECT * FROM appointments WHERE name LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.name1 = self.row[0]
            self.age = self.row[1]
            self.gender = self.row[2]
            self.location = self.row[3]
            self.time = self.row[5]
            self.phone = self.row[4]
            self.days = self.row[7]
            self.price = self.row[8]
            self.payment = self.row[9]
        # creating the update form
        self.uname = Label(self.master, text="Nombre cliente", font=('arial 18 bold'))
        self.uname.place(x=0, y=160)

        self.uage = Label(self.master, text="Edad", font=('arial 18 bold'))
        self.uage.place(x=0, y=200)

        self.ugender = Label(self.master, text="Sexo", font=('arial 18 bold'))
        self.ugender.place(x=0, y=240)

        self.ulocation = Label(self.master, text="Dirección", font=('arial 18 bold'))
        self.ulocation.place(x=0, y=280)

        self.utime = Label(self.master, text="Fecha de alquiler", font=('arial 18 bold'))
        self.utime.place(x=0, y=320)

        self.uphone = Label(self.master, text="Telefono", font=('arial 18 bold'))
        self.uphone.place(x=0, y=360)

        self.udays = Label(self.master, text="Dias de alquiler", font=('arial 18 bold'))
        self.udays.place(x=0, y=400)

        self.uprice = Label(self.master, text="Precio", font=('arial 18 bold'))
        self.uprice.place(x=0, y=440)

        self.upayment = Label(self.master, text="Metodo de pago", font=('arial 18 bold'))
        self.upayment.place(x=0, y=480)




        # entries for each labels==========================================================
        # ===================filling the search result in the entry box to update
        self.ent1 = Entry(self.master, width=30)
        self.ent1.place(x=300, y=170)
        self.ent1.insert(END, str(self.name1))

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=300, y=210)
        self.ent2.insert(END, str(self.age))

        self.ent3 = Entry(self.master, width=30)
        self.ent3.place(x=300, y=250)
        self.ent3.insert(END, str(self.gender))

        self.ent4 = Entry(self.master, width=30)
        self.ent4.place(x=300, y=290)
        self.ent4.insert(END, str(self.location))

        self.ent5 = Entry(self.master, width=30)
        self.ent5.place(x=300, y=330)
        self.ent5.insert(END, str(self.time))

        self.ent6 = Entry(self.master, width=30)
        self.ent6.place(x=300, y=370)
        self.ent6.insert(END, str(self.phone))

        self.ent7 = Entry(self.master, width=30)
        self.ent7.place(x=300, y=410)
        self.ent7.insert(END, str(self.days))

        self.ent8 = Entry(self.master, width=30)
        self.ent8.place(x=300, y=450)
        self.ent8.insert(END, str(self.price))

        self.ent9 = Entry(self.master, width=30)
        self.ent9.place(x=300, y=490)
        self.ent9.insert(END, str(self.payment))



        # button to execute update
        self.update = Button(self.master, text="Update?", width=20, height=2,fg='white', bg='black', command=self.update_db)
        self.update.place(x=400, y=500)

        # button to delete
        self.delete = Button(self.master, text="Delete?", width=20, height=2,fg='white', bg='black', command=self.delete_db)
        self.delete.place(x=150, y=500)
    def update_db(self):
        # declaring the variables to update
        self.var1 = self.ent1.get() #updated name
        self.var2 = self.ent2.get() #updated age
        self.var3 = self.ent3.get() #updated gender
        self.var4 = self.ent4.get() #updated location
        self.var5 = self.ent5.get() #updated phone
        self.var6 = self.ent6.get() #updated time
        self.var7 = self.ent7.get()
        self.var8 = self.ent8.get()
        self.var9 = self.ent9.get()

        query = "UPDATE appointments SET name=?, age=?, gender=?, location=?, phone=?, scheduled_time=?, days=?, price=?, payment=? WHERE name LIKE ?"
        c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.var7, self.var8, self.var9, self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Updated", "Successfully Updated.")
    def delete_db(self):
        # delete the appointment
        sql2 = "DELETE FROM appointments WHERE name LIKE ?"
        c.execute(sql2, (self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Deleted Successfully")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.ent5.destroy()
        self.ent6.destroy()
        self.ent7.destroy()
        self.ent8.destroy()
        self.ent9.destroy()

if __name__ == '__main__':
    root = Tk()
    b = Application(root)
    root.title("Buscador")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)
    root.mainloop()