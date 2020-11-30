from tkinter import *
from tkinter import scrolledtext
from Models.models import Marvels
root = Tk()


def agregarmarvel():
    o = Marvels()

    for persons in Marvels:
        nuevo_id = persons.id + 1

    atributos = ('id, alignment, durability, energy_projection, fighting_skills,'
                 ' gender, height_m, hometown, intelligence, '
                 'name, popularity, speed, strength, weight_kg').split(', ')
    valores = (str(nuevo_id) + ',' + str(introducir_alignment.get()) + ',' + str(introducir_durability.get()) +
               ',' + str(introducir_energy_projection.get()) + ',' + str(introducir_fighting_skills.get()) +
               ',' + str(introducir_gender.get()) + ',' + str(introducir_height.get()) +
               ',' + str(introducir_hometown.get()) + ',' + str(introducir_intelligence.get()) +
               ',' + str(introducir_name.get()) + ',' + str(introducir_popularity.get()) +
               ',' + str(introducir_speed.get()) + ',' + str(introducir_strength.get()) +
               ',' + str(introducir_weight.get())).split(',')

    for val in valores:
        if val == '':
            txt.delete(1.0, END)
            txt.insert(INSERT, 'Se deben de ingresar todos los campos')
            return

    i = 0
    txt.delete(1.0, END)
    txt.insert(INSERT, 'Se agrego al registro \n')
    for attr in atributos:
        setattr(o, attr, (valores[i]))
        txt.insert(INSERT,'\n' + attr + ':' + valores[i])
        i += 1
    Marvels().agregar(o)


def modificarmarvel():
    id = eliminarInput.get()
    atributos = ('alignment, durability, energy_projection, fighting_skills,'
                 ' gender, height_m, hometown, intelligence, '
                 'name, popularity, speed, strength, weight_kg').split(', ')
    valores = (str(introducir_alignment.get()) + ',' + str(introducir_durability.get()) +
               ',' + str(introducir_energy_projection.get()) + ',' + str(introducir_fighting_skills.get()) +
               ',' + str(introducir_gender.get()) + ',' + str(introducir_height.get()) + ',' + str(
                introducir_hometown.get()) +
               ',' + str(introducir_intelligence.get()) + ',' + str(introducir_name.get()) +
               ',' + str(introducir_popularity.get()) + ',' + str(introducir_speed.get()) +
               ',' + str(introducir_strength.get()) + ',' + str(introducir_weight.get())).split(',')
    print(atributos)
    print(valores)
    o = Marvels()
    i = 0
    txt.delete(1.0, END)
    flag = 1
    for attr in atributos:
        if valores[i] != '':
            o.actualizar(id, attr, valores[i])
            txt.insert(INSERT, 'Se han modificado los campos \n' + '\n' + attr + ':' + valores[i])
            flag = 0
        i += 1
    if flag == 1:
        txt.insert(INSERT, "No se ha ingresado ningún atributo o ID a modificar")

def eliminarmarvel():
    print(eliminarInput.get())
    resultado = Marvels.eliminar(Marvels(), eliminarInput.get())
    txt.delete(1.0, END)
    if resultado == 0:
        txt.insert(INSERT, "No se ha encontrado el id")
    else:
        txt.insert(INSERT, 'Se ha eliminado el registro con el ID: ' + eliminarInput.get())


def buscarmarvel():
    id = eliminarInput.get()
    if id != '':
        obtenido = Marvels().obtener(id)
        txt.delete(1.0, END)
        txt.insert(INSERT, obtenido)


root.title("Examen_LM")
root.resizable(1, 1)

label = Label(root, text="Alignment")
label.grid(row=0, column=0, sticky="e", padx=5, pady=5)
introducir_alignment = Entry(root)
introducir_alignment.grid(row=0, column=1)

label2 = Label(root, text="Durability")
label2.grid(row=1, column=0, sticky="e", padx=5, pady=5)
introducir_durability = Entry(root)
introducir_durability.grid(row=1, column=1)

label3 = Label(root, text="Energy projection")
label3.grid(row=2, column=0, sticky="e", padx=5, pady=5)
introducir_energy_projection = Entry(root)
introducir_energy_projection.grid(row=2, column=1)

label4 = Label(root, text="Fighting skills")
label4.grid(row=3, column=0, sticky="e", padx=5, pady=5)
introducir_fighting_skills = Entry(root)
introducir_fighting_skills.grid(row=3, column=1)

label5 = Label(root, text="Gender")
label5.grid(row=4, column=0, sticky="e", padx=5, pady=5)
introducir_gender = Entry(root)
introducir_gender.grid(row=4, column=1)

label6 = Label(root, text="Height")
label6.grid(row=5, column=0, sticky="e", padx=5, pady=5)
introducir_height = Entry(root)
introducir_height .grid(row=5, column=1)

label7 = Label(root, text="Hometown")
label7.grid(row=6, column=0, sticky="e", padx=5, pady=5)
introducir_hometown = Entry(root)
introducir_hometown.grid(row=6, column=1)

label8 = Label(root, text="Intelligence")
label8.grid(row=7, column=0, sticky="e", padx=5, pady=5)
introducir_intelligence = Entry(root)
introducir_intelligence.grid(row=7, column=1)

label9 = Label(root, text="Name")
label9.grid(row=8, column=0, sticky="e", padx=5, pady=5)
introducir_name = Entry(root)
introducir_name.grid(row=8, column=1)

label10 = Label(root, text="Popularity")
label10.grid(row=9, column=0, sticky="e", padx=5, pady=5)
introducir_popularity = Entry(root)
introducir_popularity.grid(row=9, column=1)

label11 = Label(root, text="Speed")
label11.grid(row=10, column=0, sticky="e", padx=5, pady=5)
introducir_speed = Entry(root)
introducir_speed.grid(row=10, column=1)

label12 = Label(root, text="Strength")
label12.grid(row=11, column=0, sticky="e", padx=5, pady=5)
introducir_strength = Entry(root)
introducir_strength.grid(row=11, column=1)

label13 = Label(root, text="Weight")
label13.grid(row=12, column=0, sticky="e", padx=5, pady=5)
introducir_weight = Entry(root)
introducir_weight.grid(row=12, column=1)

boton = Button(root, text="Ingresar nuevo personaje", command=agregarmarvel)
boton.grid(row=13, column=1)

label14 = Label(root, text=" ID")
label14.grid(row=0, column=3, sticky="e", padx=5, pady=5)
eliminarInput = Entry(root)
eliminarInput.grid(row=0, column=4)

eliminarBoton = Button(root, text="Eliminar con el ID", command=eliminarmarvel)
eliminarBoton.grid(row=1, column=4)

buscarBoton = Button(root, text="Buscar", command=buscarmarvel)
buscarBoton.grid(row=0, column=5)

cambiarBoton = Button(root, text="Cambiar los valor con el ID", command=modificarmarvel)
cambiarBoton.grid(row=3, column=4)

txt = scrolledtext.ScrolledText(root, width=40, height=20)
txt.grid(column=4, row=4, columnspan=6, rowspan=7)


root.mainloop()
