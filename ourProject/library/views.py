from ast import Lambda
from django.shortcuts import render

books = [
    { 'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
    { 'id': 2, 'title': 'The Meaning of Liff', 'author': 'Douglas Adams'},
    { 'id': 3, 'title': 'The No. 1 Ladies\' Detective Agency', 'author': 'Alexander McCall Smith'}
]


def home(request):
    data = { 'books': books }
    return render(request, 'home.html', data)

def show(request, id):
    book = list(filter(lambda book: book['id'] == id, books))
    data = { 'book': book[0]}
    return render(request, 'show.html', data)
    
