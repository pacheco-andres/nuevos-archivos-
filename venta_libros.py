#!/usr/bin/env python
# -*- coding: utf-8 -*-
books = {"matematicas": 100, "espaniol": 90, "biologia": 70, "historia": 80, "fisica":110}

def show_books():
    counter = 1
    print("VENTA DE LIBROS")
    for book in books.keys():
        print ('%s.- %s')  %(counter, book)
        counter += 1

def get_input():
    try:
        book_id = int(input("ingresa el numero del libro: "))
        return book_id 
    except:
        return 0

def find_book():
    book_id = get_input()
    book_names_array = books.keys()
    if book_id > 0 and book_id <= len(book_names_array):
        book_key = book_names_array[book_id-1]
        print('Libro: %s Costo: $%s') %(book_key, books[book_key]) #en cada %s se guarda un argumento en este caso en el 1 es book_key
    elif book_id == 0:
        print("Porfavor ingresa un numero")
    else:
        print("No se encontro ningun libro")
    
show_books()
find_book()



