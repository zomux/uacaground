import smtplib



class MailSender(object):
  
  def send(self, fromAddr, toAddr, subject, content):
    msg = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s\r\n" % (fromAddr, toAddr, subject, content)
    server = smtplib.SMTP('smtp.gmail.com')
    server.set_debuglevel(1)
    server.starttls()
    server.login("blogcd@uaca.com", "gx041136")
    server.sendmail(fromAddr, toAddr, msg)
    server.quit()

  def reply(self, fromAddr, toAddr, subject, content):
    subject = "Re: " + subject
    self.send(fromAddr, toAddr, subject, content)

 
if __name__ == "__main__":
  # Test
  MailSender().reply("blogcd@uaca.com", "raphael@uaca.com", "hi", "Going to do")
