#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
#Importamos todo el modulo sympy
import sympy
from sympy import *
#ademas importamos las variables simbolicas 'n' y 't'
from sympy.abc import t, n
from sympy import init_printing
import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkFont
from tkinter import Frame as fr
from tkinter import *
from PIL import ImageTk, Image
import time

init_printing()

def enviar():
    ent1=entrada1.get()
    ent2=entrada2.get()
    ent3=entrada3.get()
    ent4=entrada4.get()
    seriedefourier(ent1,ent2,ent3,ent4)

def convert_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        num, denom = frac_str.split('/')
        try:
            leading, num = num.split(' ')
            whole = float(leading)
        except ValueError:
            whole = 0
        frac = float(num) / float(denom)
        return whole - frac if whole < 0 else whole + frac

def seriedefourier(a,b,c,d):
    
    
    ar=a.replace("pi", "3.141592653589793")
    br=b.replace("pi", "3.141592653589793")    
    cr=c.replace("pi", "3.141592653589793")
    dr=d.replace("pi", "3.141592653589793")
    
    arc=convert_to_float(ar)
    brc=convert_to_float(br)
    crc=convert_to_float(cr)
    drc=convert_to_float(dr)
        
    fx=arc
    limit1=brc
    limit2=crc
    arm=int(drc)
    
    ao = integrate((1.0/limit2)*fx, (t, limit1, limit2))
    #integramos la funcion (2/pi) cuya variable es 't'
    #y limites de integracion entre 0 y pi/2

    print ("\n"+"a0 = ")
    pprint(ao)
    #Usamos la funcion pprint para mostrar ao


    an = integrate((1.0/limit2)*fx * cos(((n*pi)/(limit2)) * t), (t, limit1, limit2))
    #integramos la funcion (2/pi)*cos(2nt)
    #Su variable es 't' y sus limites de integracion son 0 y pi/2

    print ("\n"+"an = ")
    pprint(an)
    #Usamos la funcion pprint para mostrar an

    bn = together(integrate((1.0/limit2)*fx * sin(((n*pi)/(limit2)) * t), (t, limit1, limit2)))
    #integramos la funcion (2/pi*cos(2nt)
    #Su variable es 't' y sus limites de integracion
    #son 0 y pi/2. Ademas usamos la funcion "together"
    #para simplificar la expresion

    print ("\n"+"bn = ")
    pprint(bn)
    #Usamos la funcion pprint para mostrar bn

    print ("\n"+"f(x) = ")

    armonicos = arm
    serie = (ao/2)
    for i in range(1, armonicos + 1):
        serie = serie + (an*cos(((n*pi)/(limit2))*t)).subs(n, i)
    for j in range(1, armonicos + 1):
        serie = serie + (bn*sin(((n*pi)/(limit2))*t)).subs(n, j)
    import matplotlib.pyplot as plt
    plt.figure()
    p = plot(serie, ylim=(-(fx+1), (fx+1)), xlim=(-2,int(limit2+limit2)), show=False)
    pprint(serie)#Usando el modulo para graficas de sympy
    backend = p.backend(p)
    backend.process_series()
    backend.fig.savefig('plot.png', dpi=300)
    Image.open("plot.png").show()
    
    
ventana=tk.Tk()
ventana.title("Ventana 1")
ventana.geometry('380x450')
helv18 = tkFont.Font(family='Helvetica', size=18, weight=tkFont.BOLD)
helvnobold18 = tkFont.Font(family='Helvetica', size=18, weight=tkFont.NORMAL)
ventana.configure()

canvas = tk.Canvas(ventana, width = 250, height = 55)      
canvas.pack()      
img = ImageTk.PhotoImage(file="funt.jpg")      
canvas.create_image(10,10, anchor=NW, image=img)

el=tk.Label(ventana,text="f(x):",bg="#98DCE8",fg="black",font=helv18)
el.pack(fill=tk.BOTH,padx=0,pady=0,ipadx=0,ipady=0)
entrada1=tk.Entry(ventana,font=helvnobold18)
entrada1.pack(fill=tk.BOTH,padx=5,pady=0,ipadx=0,ipady=0)

el=tk.Label(ventana,text="a):",bg="#98DCE8",fg="black",font=helv18)
el.pack(fill=tk.BOTH,padx=0,pady=0,ipadx=0,ipady=0)
entrada2=tk.Entry(ventana,font=helvnobold18)
entrada2.pack(fill=tk.BOTH,padx=5,pady=0,ipadx=0,ipady=0)

el=tk.Label(ventana,text="b):",bg="#98DCE8",fg="black",font=helv18)
el.pack(fill=tk.BOTH,padx=0,pady=0,ipadx=0,ipady=0)
entrada3=tk.Entry(ventana,font=helvnobold18)
entrada3.pack(fill=tk.BOTH,padx=5,pady=0,ipadx=0,ipady=0)

el=tk.Label(ventana,text="Armonicos:",bg="#98DCE8",fg="black",font=helv18)
el.pack(fill=tk.BOTH,padx=0,pady=0,ipadx=0,ipady=0)
entrada4=tk.Entry(ventana,font=helvnobold18)
entrada4.pack(fill=tk.BOTH,padx=5,pady=0,ipadx=0,ipady=0)

boton3=tk.Button(ventana,text="Solucion",bg="#98DCE8",fg="black",font=helv18,command=enviar)
boton3.pack(fill=tk.BOTH,padx=20,pady=30,ipadx=20,ipady=30)

ventana.mainloop()






