from tkinter import * 
import sqlite3 
import tkinter.messagebox 
import os

# Conexion a la base de datos 
conn = sqlite3.connect('database.db')

# Parametro para moverse en la base de datos
c = conn.cursor()

# Lista vacia para añadir los id's de la base de datos
ids = []

# Clase principal para la interfaz grafica.
class Application: 
    def __init__(self, master):
        self.master = master 

        # Creamos los frames en la master
        self.left = Frame(master, width=800, height=720, bg = 'grey')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=600, height=720, bg = 'grey')
        self.right.pack(side = RIGHT)

        # Etiquetas 
        self.heading = Label(self.left, text = "Sistemas de alquiler de Vehiculos", font = ('georgia 40 bold'), 
        fg = 'black', bg = 'grey', )
        self.heading.place(x=0, y=0)

        # Datos del cliente -------------------

        # Nombre
        self.name = Label(self.left, text="Nombre", font=(
            'georgia 18 bold'), fg='black', bg='grey')
        self.name.place(x=0, y=100)

        # edad 
        self.age = Label(self.left, text="Edad", font=(
            'georgia 18 bold'), fg='black', bg='grey')
        self.age.place(x=0, y=140)

        # sexo 
        self.gender = Label(self.left, text="Sexo", font=(
            'georgia 18 bold'), fg='black', bg='grey')
        self.gender.place(x=0, y=180)

        # Direccion 
        self.location = Label(self.left, text="Dirección", font=(
            'georgia 18 bold'), fg='black', bg='grey')
        self.location.place(x=0, y=220)

        # Fecha del alquiler
        self.time = Label(self.left, text="Fecha de alquiler", font=(
            'georgia 18 bold'), fg='black', bg='grey')
        self.time.place(x=0, y=260)

        # Telefono 
        self.phone = Label(self.left, text="Numero telefonico", font=(
            'georgia 18 bold'), fg='black', bg='grey')
        self.phone.place(x=0, y=300)

        # dias
        self.days = Label(self.left, text="Dias de alquiler", font=(
            'georgia 18 bold'), fg='black', bg='grey')
        self.days.place(x=0, y=340)

        # precio 

        # metodo de pago 
        self.payment = Label(self.left, text="Metodo de pago", font=(
            'georgia 18 bold'), fg='black', bg='grey')
        self.payment.place(x=0, y=380)


        # Inputs para todas las entradas 

        self.nombre_ent = Entry(self.left, width=30)
        self.nombre_ent.place(x=250, y=100)

        self.edad_ent = Entry(self.left, width=30)
        self.edad_ent.place(x=250, y=140)

        self.sexo_ent = Entry(self.left, width=30)
        self.sexo_ent.place(x=250, y=180)

        self.direccion_ent = Entry(self.left, width=30)
        self.direccion_ent.place(x=250, y=220)

        self.fecha_ent = Entry(self.left, width=30)
        self.fecha_ent.place(x=250, y=260)

        self.telefono_ent = Entry(self.left, width=30)
        self.telefono_ent.place(x=250, y=300)

        self.days_ent = Entry(self.left, width=30)
        self.days_ent.place(x=250, y=340)

        self.payment_ent = Entry(self.left, width=30)
        self.payment_ent.place(x=250, y=380)

        #Boton guardar (principal)

        self.submit = Button(self.left, text="Guardar", width=20,
                            height=2, bg='white', command=self.add_alquiler)
        self.submit.place(x=150, y=450)

        self.search = Button(self.left, text="Buscar en la base de datos", width=20,
                            height=2, bg='white', command=self.excute_search)
        self.search.place(x=400, y=450)

        # Numero de alquileres para ser observados en el LOG
        sql2 = "SELECT ID FROM appointments"
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

        # ordenar ids 
        self.new = sorted(ids)
        self.final_id = self.new[len(ids)-1]
        # Mostrar logs 
        self.logs = Label(self.right, text = 'Alquileres Registrados', font = ('georgia 28 bold'),
                            fg = 'black', bg = 'grey')
        self.logs.place(x=70, y=10)

        self.box = Text(self.right, width = 150, height = 40)
        self.box.place(x=20, y=60)
        self.box.insert(END, "\n Numero de Alquileres: \n " + 
                str(self.final_id) + " \n "
        )

    # Se ejecuta cuando se hace click en el boton guardar

    def excute_search(self):
        os.system("python3 buscar_db.py")

    def add_alquiler(self):
        self.val1 = self.nombre_ent.get() 
        self.val2 = self.edad_ent.get()
        self.val3 = self.sexo_ent.get()
        self.val4 = self.direccion_ent.get()
        self.val5 = self.fecha_ent.get()
        self.val6 = self.telefono_ent.get()
        self.val7 = self.days_ent.get()
        self.val8 = str(int(int(self.days_ent.get())*25)) #cuesta 25 el dia
        self.val9 = self.payment_ent.get()
        # Revisar si el input esta vacio 

        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '' or self.val6 == '' or self.val7 =='' or self.val9=='':
            tkinter.messagebox.showinfo("Warning", "Porfavor, llene todos los campos.")
        else: 
            # agregamos los valores a la base de datos 
            # now we add to the database
            sql = "INSERT INTO 'appointments' (name, age, gender, location, scheduled_time, phone, days,price,payment) VALUES(?, ?, ?, ?, ?, ?, ?,?,?)"
            c.execute(sql, (self.val1, self.val2, self.val3,
                            self.val4, self.val5, self.val6, self.val7, self.val8, self.val9))
            conn.commit()
            tkinter.messagebox.showinfo(
                "Exito", "\nEl agendamiento para " + str(self.val1) + " ha sido creado!\n")
            self.box.insert(END, 'Agendamiento agreado para ' +
                            str(self.val1) + ' el ' + str(self.val5) + '\n' + "\t Precio: " + self.val8 + "\n")
            

if __name__ == '__main__':
    root = Tk() 
    b = Application(root)
    root.title("Sistema de alquiler de vehiculos.")
    root.geometry("1366x768")

    root.resizable(False,False)

    root.mainloop()