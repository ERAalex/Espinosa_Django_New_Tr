from django.views.generic import ListView
from django.shortcuts import render
from .models import Teacher, Student


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.all()
    teacher = Teacher.objects.all()
    context = {'students': students, 'teacher': teacher}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
