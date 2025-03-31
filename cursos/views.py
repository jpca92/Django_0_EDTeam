from django.shortcuts import render
from django.http import HttpResponse
from .models import TblCategoria, TblCurso

# Create your views here.
def cursos (request):
    course_list = TblCurso.objects.all()
    print(course_list)
    str_course = '<ul>\n'
    for course in course_list:
        str_course += '<li>' + course.curso_titulo + '</li>'

    str_course += '</ul>'

    return HttpResponse('<center><h1>EDTeam route<h1><center><br>' + str_course)
