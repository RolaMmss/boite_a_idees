from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse(f"""
                        <h1> Hello Django  from container!</h1>""")