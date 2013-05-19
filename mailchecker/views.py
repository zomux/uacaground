# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
import StringIO
from checker import BlogCDMailChecker

def index(request):
  
  mailList = BlogCDMailChecker().listAllUnseenMails(3)
  
  return render_to_response("mailchecker.html", {"mail_list": mailList})