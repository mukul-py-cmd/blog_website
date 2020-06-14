from django.shortcuts import render
from django.http import HttpResponse


def test_pass(request):
	return HttpResponse('<h1>fff</h1>')

# Create your views here.
