# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
import StringIO
from checker import BlogCDMailChecker
from sender import MailSender

ACTIVE_MAIL = """
Hi，\r\n
\r\n
Your invitation code in BLOG.CD is：\r\n
\r\n
MjVjNjU5MWQ0ZjQ1YjE4NDNiOTcyNDZiNDRlYjYwNmExMzk2NzA5OTA2\r\n
\r\n
Paste it to the registration form and get a blog.\r\n
\r\n
Thanks for your joining!\r\n
\r\n
(Caution) Because we are using customized Wordpress system, your final password could be different from what you inputted,\r\n
\r\n
please save the password at activation page, and modify after logged into the manage panel.\r\n
"""

def index(request):
  
  mailList = BlogCDMailChecker().listAllUnseenMails(3)
  
  return render_to_response("mailchecker.html", {"mail_list": mailList})

def send(request):
  response = HttpResponse()
  if "mails" not in request.GET:
    response.write("mails parameter not found")
  else:
    szMails = request.GET["mails"]
    response.write(szMails)

  return response