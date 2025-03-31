from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import TblCategoria, TblCurso

def cursos(request):
    course_list = TblCurso.objects.all()
    str_course = '<ul>\n'
    for course in course_list:
        str_course += f'<li>{course.curso_titulo}</li>'
    str_course += '</ul>'

    return HttpResponse('<center><h1>EDTeam route</h1></center><br>' + str_course)

def cursosAPI(request):
    courses_list = TblCurso.objects.all()
    final_list = []
    for course in courses_list:
        dict_course = {
            'id': course.curso_id,
            'title': course.curso_titulo,
            'description': course.curso_descripcion
        }
        final_list.append(dict_course)
    
    dataJson = {
        'data':final_list
    }

    # return JsonResponse(final_list, safe=False)  # ✅ recomendado
    return JsonResponse(dataJson)
