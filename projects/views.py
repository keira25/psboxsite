from django.shortcuts import render


def projects_all(request):
  return render(request, 'projects/projects_all.html')
