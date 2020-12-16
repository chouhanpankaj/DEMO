from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    msg = {'data' :'this from view first page.'}
    return render(request,'app/html/index.html',context = msg)
# Create your views here.
