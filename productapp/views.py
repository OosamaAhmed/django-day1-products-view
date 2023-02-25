from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# myproducts dict
myproducts = [
    {
        "id": 1,
        "name": "Apple",
        "price": 1000,
        "description": "This is a very good apple",
    },
    {
        "id": 2,
        "name": "Orange",
        "price": 2000,
        "description": "This is a very good orange",
    },
    {
        "id": 3,
        "name": "Banana",
        "price": 3000,
        "description": "This is a very good banana",
    },
    {
        "id": 4,
        "name": "Pear",
        "price": 4000,
        "description": "This is a very good pear",
    },
    {
        "id": 5,
        "name": "Grape",
        "price": 5000,
        "description": "This is a very good grape",
    },
    {
        "id": 6,
        "name": "Strawberry",
        "price": 6000,
        "description": "This is a very good strawberry", },
    {
        "id": 7,
        "name": "Cherry",
        "price": 7000,
        "description": "This is a very good cherry", },
    {
        "id": 8,
        "name": "Mango",
        "price": 8000,
        "description": "This is a very good mango", },
    {
        "id": 9,
        "name": "Pineapple",
        "price": 9000,
        "description": "This is a very good pineapple", },
    {
        "id": 10,
        "name": "Peach",
        "price": 10000,
        "description": "This is a very good peach", },
    {
        "id": 11,
        "name": "Peach",
        "price": 10430,
        "description": "This is a very good peach", },
        {
        "id": 12,
        "name": "Peach",
        "price": 10430,
        "description": "This is a very good peach", },
        {
        "id": 13,
        "name": "Peach",
        "price": 10430,
        "description": "This is a very good peach", },
        {
        "id": 14,
        "name": "Peach",
        "price": 10430,
        "description": "This is a very good peach", },
        {
        "id": 15,
        "name": "Peach",
        "price": 10430,
        "description": "This is a very good peach", },
        {
        "id": 16,
        "name": "Peach",
        "price": 10430,
        "description": "This is a very good peach", },
        {
        "id": 17,
        "name": "Peach",
        "price": 10430,
        "description": "This is a very good peach", },
        {
        "id": 18,
        "name": "Peach",
        "price": 10430,
        "description": "This is a very good peach", },
        {
        "id": 19,
        "name": "Peach",
        "price": 10430,
        "description": "This is a very good peach", },
        {
        "id": 20,
        "name": "Peach",
        "price": 10430,
        "description": "This is a very good peach", },
        {
        "id": 21,
        "name": "Peach",
        "price": 10430,
        "description": "This is a very good peach", },
        {
        "id": 22,
        "name": "Peach",
        "price": 10430,
        "description": "This is a very good peach", },
        {
        "id": 23,
        "name": "Peach",
        "price": 10430,
        "description": "This is a very good peach", },








]




def homepage(request):
  
    return render(request, 'main.html' , context={"myproducts":myproducts})

def showproduct(request,id):
     for n in myproducts:
         if  n['id'] == id:
            return render(request, 'showproduct.html', context={"n":n})
     else:
         return HttpResponse("not found")



def contactus(request):
    return render(request, 'contact.html')


def aboutus(request):
    return render(request, 'about.html')
