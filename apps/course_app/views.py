from django.shortcuts import render, redirect
from .models import Course
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    courses = Course.objects.all()
    data = {
        'courses': courses
    }
    return render(request, 'course_app/index.html', data)


def add_course(request):
    Course.objects.create(title=request.POST['title'], description=request.POST['description'])
    return redirect(reverse('index'))


def destroy(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect(reverse('index'))
