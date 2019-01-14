from django.shortcuts import render
from django.utils import timezone
from .models import MkPro

# Create your views here.
def post_list(request):
    pros = MkPro.objects.filter().order_by('stars')
    return render(request, 'teacher/post_list.html', {'pros':pros})
