from django.http import HttpResponse
from django.shortcuts import render
from .models import School # import our School class
from django.http import HttpResponse

my_school = School("Django School") # create a school instance


def index(request):
    my_data = { 
        "school_name": my_school.name
    }
    return render(request, "pages/index.html", my_data)



def list_staff(request):
    my_data = {
        "staff_list" : my_school.staff
        }
    return render(request, 'pages/staff.html', my_data)

def staff_detail(request, employee_id):
    employee = ''
    for member in my_school.staff:
        if member.employee_id == int(employee_id):
            employee = member
    return render(request, 'pages/staff_detail.html', {'employee' : employee})


def list_students(request):
    my_data = {
        "students_list" : my_school.students
    }
    return render(request, 'pages/students.html', my_data)


def student_detail(request, student_id):
    student = ''
    for member in my_school.students:
        if member.school_id == int(student_id):
            student = member
    return render(request, 'pages/student_detail.html', {'student' : student})