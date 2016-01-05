#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  edci_reg.py
#  
#  Copyright 2015 asley <asley@edci>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
import sys
import sqlite3
import Tkinter
import tkMessageBox
from Tkinter import *
from tkMessageBox import *
cnn_db = sqlite3.connect('/home/roxy/proyectos/Sistema EDCI/edci_database')
cursor= cnn_db.cursor()
print('database connected')
def salir():
	resp = tkMessageBox.askquestion("Salir del Sistema","¿Seguro quiere Salir?", icon="warning")
	if resp=='no':
		print('XD')
		main					
	else:
		cnn_db.close()
		print ("close database")
		sys.exit()
def main():							
	def nuevo():
		'''ventana de registro'''
		ventana1=Tk()
		ventana1.title("EDCI Registro de usuarios")
		ventana1.geometry("600x600+200+100")
		ventana1.maxsize(800, 400)	
		titulo=Label(ventana1,text="Usuario en el Sistema EDCI",fg="blue",bg="white",height=1,font=('Ravie', 24))
		titulo.pack(pady=2)
		separador=Frame (ventana1,height=10,width=25, bd=20,relief=RIDGE, bg="white")
		separador.pack(padx=3,pady=5)
		l1 = Label(separador,text="Número de Cédula: ",bg="white") 
		l1.pack()
		e1 = Entry(separador)
		e1.pack()
		l2 = Label(separador,text="Nombre: ",bg="white") 
		l2.pack()
		e2 = Entry(separador)
		e2.pack()
		l3 = Label(separador,text="Apellido: ",bg="white") 
		l3.pack()
		e3 = Entry(separador)
		e3.pack()
		l4 = Label(separador,text="télefono: ",bg="white") 
		l4.pack()
		e4 = Entry(separador)
		e4.pack()
		l5 = Label(separador,text="Dirección: ",bg="white") 
		l5.pack()
		e5 = Entry(separador)
		e5.pack()
		def registrar():
			ide=e1.get()
			name=e2.get()
			last_name=e3.get()
			phone=e4.get()
			addr=e5.get()		
			try:
				cursor.execute("INSERT INTO USUARIO (cedula, Nombre, Apellido, telefono, dirección) VALUES ('" + ide + "', '" + name + "','" + last_name + "','" + phone + "','" + addr + "')")
				cnn_db.commit()
				print ("load Asley... next please XD")
				showinfo("Notificación", "registrado con éxito")
			except sqlite3.IntegrityError:
				showerror("Notificación", "ya esta registrado en el sistema ")			
			finally:
				ventana1.destroy()							
		boton_ingreso = Button(ventana1, text="Registrar", width=10,fg='white',bg='blue',command=registrar)
		boton_ingreso.pack()
		ventana1.config(bg="white",menu=menu_bar)
		ventana1.mainloop()
		cnn_db.close()
		print("database closed")
		
	def buscar():
		'''ventana de buscar'''
		def buscar():
			ide=e1.get()
			cursor.execute("SELECT cedula, Nombre, Apellido, telefono, dirección from USUARIO WHERE cedula = '" + ide + "'")
			for raw in cursor:
				marco=('''\n Datos de la Búsqueda''')
				mostrar=Label(ventana2,text=marco,bg="white",fg="blue",font=('Ravie', 14)).pack()
				salida1 =Label(ventana2,text = "Cédula: %s"%raw[0], bg="white",font=('Ravie', 10),fg="blue").pack()
				salida2 =Label(ventana2,text = "Nombre: %s"%raw[1], bg="white",font=('Ravie', 10),fg="blue").pack()
				salida3 =Label(ventana2,text = "Apellido: %s"%raw[2], bg="white",font=('Ravie', 10),fg="blue").pack()
				salida4 =Label(ventana2,text = "Tlf: %s"%raw[3], bg="white",font=('Ravie', 10),fg="blue").pack()
				salida5 =Label(ventana2,text = "Direcc: %s"%raw[4], bg="white",font=('Ravie', 10),fg="blue").pack()
				print('ready')
			busca=cursor.execute("SELECT cedula, Nombre, Apellido, telefono, dirección from USUARIO WHERE cedula = '" + ide + "'")
			comprueba=busca.fetchone()
			if comprueba == None:
				print('not found')
				tkMessageBox.showerror('Alerta del sistema','No registrado')
			else:
				if ide=='' or None or 0:
					tkMessageBox.showwarning('Alerta del sistema','Campo de Búsqueda Vacío')
			e1.delete(0, END)
		def buscando(event):
			buscar()
									
		ventana2=Toplevel()
		ventana2.title("EDCI Administración de Usuarios ")
		ventana2.geometry("600x600+200+100")
		ventana2.maxsize(800, 400)	
		titulo=Label(ventana2,text="*** Sistema EDCI ***",fg="blue",bg="white",height=1,font=('Ravie', 24))
		titulo.pack()	
		titulo_b=Label(ventana2,text="Busqueda de usuario registrado",fg="blue",bg="white",height=1,font=('Ravie', 10))
		titulo_b.pack()
		l1 = Label(ventana2,text="Número de Cédula: ",bg="white") 
		l1.pack(pady=10)
		e1 = Entry(ventana2)
		e1.pack(pady=5)	
		e1.bind("<Return>",buscando)	
		boton_busque = Button(ventana2, text="Buscar", width=10,fg='white',bg='blue',command=buscar)
		boton_busque.pack(pady=5)
		ventana2.config(bg="white",menu=menu_bar)
		ventana2.mainloop()
	
	'''ventana de eliminar'''
	def eliminar():
		def eliminar():
			ide=e1.get()
			if ide=='':
				tkMessageBox.showinfo('Alerta del sistema','no encontrado')
				print("not found")
			cursor.execute("SELECT cedula, Nombre, Apellido, telefono, dirección from USUARIO WHERE cedula = '" + ide + "'")
			resp = tkMessageBox.askquestion("Eliminar del Sistema","¿Seguro quiere eliminar?", icon="warning")
			if resp=='no':
				e1.delete(0, END)
				print("not erase")					
			else:
				e1.delete(0, END)
				cursor.execute("DELETE from USUARIO WHERE cedula = '" + ide + "'")
				tkMessageBox.showinfo('Alerta del sistema','Eliminado con éxito')
				cnn_db.commit()
				print("erased")
			ventana3.destroy()
			
		def eliminando(event):
			eliminar()				
		ventana3=Tk()
		ventana3.title("EDCI Depuración de Usuarios")
		ventana3.geometry("600x600+200+100")
		ventana3.maxsize(800, 400)	
		titulo=Label(ventana3,text="*** Sistema EDCI ***",fg="blue",bg="white",height=1,font=('Ravie', 24))
		titulo.pack()	
		titulo_b=Label(ventana3,text="Borrar usuario registrado",fg="blue",bg="white",height=1,font=('Ravie', 10))
		titulo_b.pack()
		l1 = Label(ventana3,text="Número de Cédula: ",bg="white") 
		l1.pack(pady=10)
		e1 = Entry(ventana3)
		e1.bind("<Return>",eliminando)
		e1.pack(pady=5)
		boton_busque = Button(ventana3, text="Eliminar", width=10,fg='white',bg='blue',command=eliminar)
		boton_busque.pack(pady=5)
		ventana3.config(bg="white",menu=menu_bar)
		ventana3.mainloop()
	
	def edci_acerca():
		'''ventana de acerca'''
		ventana4=Toplevel()
		ventana4.title("EDCI Módulo de Ayuda")
		ventana4.geometry("600x600+200+100")
		ventana4.maxsize(800, 400)	
		titulo=Label(ventana4,text="¿Qué es EDCI?",fg="blue",bg="white",height=1,font=('Ravie', 24))
		titulo.pack()	
		titulo_b=Label(ventana4,text="EDCI pueden ser muchas cosas a la vez\nsus siglas son el acrónimo de muchos significados",fg="blue",bg="white",height=2,font=('Ravie', 10))
		titulo_b.pack()
		imagenlogo= PhotoImage(file="/home/roxy/proyectos/Sistema EDCI/home_registro.gif")
		lab_imagenlogo=Label(ventana4,image=imagenlogo,anchor="center",bg="white").pack()
		titulob=Label(ventana4,fg="blue",bg="white",text="para este momento...Escuela de Desarrollo de Contenido informático",font=('Ravie', 10))
		titulob.pack()		
		ventana4.config(bg="white",menu=menu_bar)
		ventana4.mainloop()
		
	def AYUDA():
		'''ventana de ayuda'''
		ventana5=Tk()
		ventana5.title("EDCI Módulo de Ayuda")
		ventana5.geometry("600x600+200+100")
		ventana5.maxsize(800, 400)	
		titulo=Label(ventana5,text="¿Cómo usar este sistema?",fg="blue",bg="white",height=1,font=('Ravie', 24))
		titulo.pack()	
		titulo_b=Label(ventana5,text="Acerca del Sistema Administrativo EDCI\n",fg="blue",bg="white",height=2,font=('Ravie', 14))
		titulo_b.pack()
		Texto = Text(ventana5, height=20, width=60,bg="white",font=('Ravie', 10),fg="blue",bd=10,relief=RIDGE, )
		Texto.pack()
		#barra= Scrollbar(ventana5)
		#barra.pack(side="right", fill=Y)
		Texto.insert(END, "Este sistema  consiste en un módulo de control de usuarios.\n\n")
		Texto.insert(END, "En él se pueden registrar los datos mas básicos de un usuario\nnormal tales como cédula (campo primario de identificación),\nnombre y apellido, teléfono y dirección de domicilio.\n\n")
		Texto.insert(END, "Menú Registro: Es el principal menú del sistema,en el se encuentran\nlas opciones de nuevo,buscar y eliminar.\n\n")
		Texto.insert(END, "Nuevo usuario: Brinda acceso al formulario de registro de usuario con\nlos campos:cédula, Nombre, Apellido,teléfono, domicilio.\n\n")
		Texto.insert(END, "Buscar usuario: Ofrece el formulario de búsqueda mediante el campo\ncédula del usuario,en este formulario se visualizan los datos\ndel usuario registrado.\n\n")
		Texto.insert(END, "Eliminar usuario: Permite borrar registros del sistema\nde manera permanente.")
		#barra.config(command=Texto.yview)
		#Texto.config(yscrollcommand=barra.set)
		ventana5.config(bg="white",menu=menu_bar)
		ventana5.mainloop()	
	
	def creditos():
		'''ventana de créditos'''
		ventana6=Toplevel()
		ventana6.title("EDCI Módulo de Ayuda")
		ventana6.geometry("600x600+200+100")
		ventana6.maxsize(800, 400)		
		titulo=Label(ventana6,fg="blue",bg="white",text="Sitema Administrativo General EDCI ",font=('Ravie', 20))
		titulo.pack()
		titulo2=Label(ventana6,fg="blue",bg="white",text="programación y diseño por:\n ",font=('Ravie', 14))
		titulo2.pack()
		imagenlogo= PhotoImage(file="/home/roxy/proyectos/Sistema EDCI/pythontux.gif")
		lab_imagenlogo=Label(ventana6,image=imagenlogo,anchor="center",bg="white").pack()
		titulob=Label(ventana6,fg="blue",bg="white",text="Asley B Echarry G",font=('Ravie', 12))
		titulob.pack()
		tituloc=Label(ventana6,fg="blue",bg="white",text="<asleybach@gmail.com>",font=('Ravie', 12))
		tituloc.pack()		
		ventana6.config(bg="white",menu=menu_bar)
		ventana6.mainloop()	
	'''ventana de inicio'''
	ventana=Tk()	
	ventana.title("Bienvenido a EDCI")
	ventana.geometry("600x600+200+100")
	ventana.maxsize(800, 400)	
	ventana.protocol("WM_DELETE_WINDOW",salir)
	titulo=Label(ventana,text="Sistema Administrativo EDCI",fg="blue",bg="white",height=1,font=('Ravie', 26))
	titulo.pack()
	img=PhotoImage(file="edcilogo.gif")
	portada=Label(ventana,image=img,bg="white")
	portada.pack(pady=5)
	menu_bar= Menu(ventana)
	reg= Menu(menu_bar)
	reg.add_command(label="Nuevo usuario",underline=0, command=nuevo)
	reg.add_command(label="Buscar usuario",underline=0, command=buscar)
	reg.add_command(label="Eliminar usuario",underline=0, command=eliminar)
	reg.add_command(label="Salir",underline=0, command=salir)
	reg2= Menu(menu_bar)
	reg2.add_command(label="Acerca de Edci",underline=10, command=edci_acerca)
	reg2.add_command(label="Ayuda",underline=0, command=AYUDA)
	reg2.add_command(label="Créditos",underline=0, command=creditos)
	menu_bar.add_cascade(label="Registro",menu=reg, underline=0)
	menu_bar.add_cascade(label="Ayuda",menu=reg2, underline=0)	
	ventana.config(bg="white",menu=menu_bar)
	ventana.mainloop()
	print ("close database")	
	
if __name__ == '__main__':
	main()
	

