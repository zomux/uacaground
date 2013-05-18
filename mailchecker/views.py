# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
import StringIO


def index(request):
  response = HttpResponse()
  response.write("AAABBB")
  return response