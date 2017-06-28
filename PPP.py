from tkinter import *
from tkinter import messagebox
import turtle
import time
import random


# Creando ventana
ventana = Tk()



a=random.randint(1,999)
b=random.randint(1,999)
ab = a,"x",b
aib = a*b
c=random.randint(1,100)
d=random.randint(1,100)
cd = c,"x",d
cid = c*d
e=random.randint(1,100)
f=random.randint(1,100)
ef = e,"x",f
eif = e*f
g=random.randint(1,100)
h=random.randint(1,100)
gh = g,"x",h
gih = g*h
i=random.randint(1,100)
j=random.randint(1,100)
ij = i,"x",j
iij = i*j
k=random.randint(1,100)
l=random.randint(1,100)
kl = k,"x",l
kil = k*l
m=random.randint(1,100)
n=random.randint(1,100)
mn = m,"x",n
min = m*n
o=random.randint(1,100)
p=random.randint(1,100)
op = o,"x",p
oip = o*p
q=random.randint(1,100)
r=random.randint(1,100)
qr = q,"x",r
qir = q*r
s=random.randint(1,100)
t=random.randint(1,100)
st = s,"x",t
sit = s*t



# Definiendo nuestras funciones
def pa():
    a = messagebox.showinfo("¿?","¿Quieres empezar " + nombre.get() + "?")
    if a == "ok":
        pe()

def pe():
    ventanat = turtle.Screen()
    ventanat.title("Ahorcado 2.0")
    ventanat.setup(500,500)
    turtle.shape("turtle")
    turtle.bgcolor("black")
    turtle.penup()
    turtle.goto(-20,150)
    turtle.pendown()
    turtle.pencolor("red")
    turtle.right(90)
    turtle.forward(50)

    pi()

def pi():
    def pi1a():
        if int(pii1.get()) == aib:
            messagebox.showinfo("Correcto")
        if int(pii1.get()) != aib:
            messagebox.showinfo("Incorrecto la respuesta es: ",aib)
            turtle.pencolor("blue")
            turtle.left(72)
            turtle.forward(50)




    def pi2a():
        if int(pii2.get()) == cid:
            messagebox.showinfo("Correcto")
        if int(pii2.get()) != cid:
            messagebox.showinfo("Incorrecto la respuesta es: ",cid)
            turtle.pencolor("green")
            turtle.right(36)
            turtle.forward(50)

    def pi3a():
        if int(pii3.get()) == eif:
            messagebox.showinfo("Correcto")
        if int(pii3.get()) != eif:
            messagebox.showinfo("Incorrecto la respuesta es: ",eif)
            turtle.pencolor("orange")
            turtle.right(36)
            turtle.forward(50)


    def pi4a():
        if int(pii4.get()) == gih:
            messagebox.showinfo("Correcto")
        if int(pii4.get()) != gih:
            messagebox.showinfo("Incorrecto la respuesta es: ",gih)
            turtle.pencolor("skyblue")
            turtle.right(36)
            turtle.forward(50)
    def pi5a():
        if int(pii5.get()) == iij:
            messagebox.showinfo("Correcto")
        if int(pii5.get()) != iij:
            messagebox.showinfo("Incorrecto la respuesta es: ",iij)
            turtle.pencolor("brown")
            turtle.right(36)
            turtle.forward(50)
    def pi6a():
        if int(pii6.get()) == kil:
            messagebox.showinfo("Correcto")
        if int(pii6.get()) != kil:
            messagebox.showinfo("Incorrecto la respuesta es: ",kil)
            turtle.pencolor("pink")
            turtle.right(36)
            turtle.forward(50)
    def pi7a():
        if int(pii7.get()) == min:
            messagebox.showinfo("Correcto")
        if int(pii7.get()) != min:
            messagebox.showinfo("Incorrecto la respuesta es: ",min)
            turtle.pencolor("purple")
            turtle.right(36)
            turtle.forward(50)
    def pi8a():
        if int(pii8.get()) == oip:
            messagebox.showinfo("Correcto")
        if int(pii8.get()) != oip:
            messagebox.showinfo("Incorrecto la respuesta es: ",oip)
            turtle.pencolor("black")
            turtle.right(36)
            turtle.forward(50)
    def pi9a():
        if int(pii9.get()) == qir:
            messagebox.showinfo("Correcto")
        if int(pii9.get()) != qir:
            messagebox.showinfo("Incorrecto la respuesta es: ",qir)
            turtle.pencolor("violet")
            turtle.right(36)
            turtle.forward(50)
    def pi10a():
        if int(pii10.get()) == sit:
            z=messagebox.showinfo("Correcto")

        if int(pii10.get()) != sit:
            z=messagebox.showinfo("Incorrecto la respuesta es: ",sit)
            turtle.pencolor("yellow")
            turtle.right(36)
            turtle.forward(50)





    pii1=StringVar()
    pii2=StringVar()

    pii3=StringVar()

    pii4=StringVar()
    pii5=StringVar()
    pii6=StringVar()
    pii7=StringVar()
    pii8=StringVar()
    pii9=StringVar()
    pii10=StringVar()





    pi1 = Label(ventana,text=ab,font=("Helvetica",30)).place(x=500,y=10)
    pie1= Entry(ventana,textvariable=pii1).place(x=700,y=30)
    botonpi1 = Button(text="O", command=pi1a).place(x=850,y=30)


    pi2 = Label(ventana,text=cd,font=("Helvetica",30)).place(x=500,y=70)
    pie2= Entry(ventana,textvariable=pii2).place(x=700,y=80)
    botonpi2 = Button(text="O", command=pi2a).place(x=850,y=80)

    pi3 = Label(ventana,text=ef,font=("Helvetica",30)).place(x=500,y=130)
    pie3= Entry(ventana,textvariable=pii3).place(x=700,y=140)
    botonpi3 = Button(text="O", command=pi3a).place(x=850,y=140)

    pi4 = Label(ventana,text=gh,font=("Helvetica",30)).place(x=500,y=190)
    pie4= Entry(ventana,textvariable=pii4).place(x=700,y=200)
    botonpi4 = Button(text="O", command=pi4a).place(x=850,y=200)
    pi5 = Label(ventana,text=ij,font=("Helvetica",30)).place(x=500,y=250)
    pie5= Entry(ventana,textvariable=pii5).place(x=700,y=260)
    botonpi5 = Button(text="O", command=pi5a).place(x=850,y=260)
    pi6 = Label(ventana,text=kl,font=("Helvetica",30)).place(x=500,y=310)
    pie6= Entry(ventana,textvariable=pii6).place(x=700,y=320)
    botonpi6 = Button(text="O", command=pi6a).place(x=850,y=320)
    pi7 = Label(ventana,text=mn,font=("Helvetica",30)).place(x=500,y=370)
    pie7= Entry(ventana,textvariable=pii7).place(x=700,y=380)
    botonpi7 = Button(text="O", command=pi7a).place(x=850,y=380)
    pi8 = Label(ventana,text=op,font=("Helvetica",30)).place(x=500,y=430)
    pie8= Entry(ventana,textvariable=pii8).place(x=700,y=440)
    botonpi8 = Button(text="O", command=pi8a).place(x=850,y=440)
    pi9 = Label(ventana,text=qr,font=("Helvetica",30)).place(x=500,y=490)
    pie9= Entry(ventana,textvariable=pii9).place(x=700,y=500)
    botonpi9 = Button(text="O", command=pi9a).place(x=850,y=500)
    pi10 = Label(ventana,text=st,font=("Helvetica",30)).place(x=500,y=550)
    pie10= Entry(ventana,textvariable=pii10).place(x=700,y=560)
    botonpi10 = Button(text="O", command=pi10a).place(x=850,y=560)

# Variables
nombre = StringVar()
# Colocando el titulo
ventana.title("El ahorcado 2.0")
# Definiendo el tamaño de la ventana
ventana.geometry("1200x1080")
# Etiqueta del nombre
etinombre = Label(ventana,text="Escriba su nombre: ").place(x=10,y=10)
# Entrada del nombre
entnombre = Entry(ventana,textvariable=nombre).place(x=120,y=10)
# Boton de Ok
botonOk = Button(ventana,text="Ok",command=pa).place(x=250,y=10)

ventana.mainloop()