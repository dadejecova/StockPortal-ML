from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def students(request):
    students_list = [{
        "name": "Alice",
        "age": 20,
        "grade": "A"
    }, {
        "name": "Bob",
        "age": 22,
        "grade": "B"
    }, {
        "name": "Charlie",
        "age": 21,
        "grade": "C"
    }]
    return HttpResponse(', '.join([f"{student['name']} (Age: {student['age']}, Grade: {student['grade']})" for student in students_list]))