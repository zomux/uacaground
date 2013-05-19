import imaplib
import email
import quopri
from email.header import decode_header


def get_first_text_block(email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message_instance.get_payload()
    return ""

class BlogCDMailChecker(object):

  def listAllUnseenMails(self, count=5):
      mail = imaplib.IMAP4_SSL('imap.gmail.com')
      mail.login('raphael@uaca.com', 'rafa$ch82')
      # Out: list of "folders" aka labels in gmail.
      mail.select("BLOGCD-SERVICE") # connect to inbox.
      result, data = mail.search(None, "UnSeen")
       
      ids = data[0] # data is a list.
      id_list = ids.split() # ids is a space separated string
      returnList = []
      for id in id_list[:count]:
        result, data = mail.fetch(id, "(BODY.PEEK[])") # fetch the email body (RFC822) for the given ID
        raw_email = data[0][1] # here's the body, which is raw text of the whole email
        # including headers and alternate payloads
        email_message = email.message_from_string(raw_email)
        returnList.append( self.getMailContent(email_message) )
      return returnList
    
  def decodeHeaderString(self, text):
    sz, charset = decode_header(text)[0]
    if charset and "utf" not in charset:
      sz = sz.decode(charset, "ignore").encode("utf-8", "ignore")
    return sz

  def extractMail(self, emailObject):
    subject = self.decodeHeaderString(emailObject["Subject"])
    name, addr = email.utils.parseaddr(emailObject['From'])
    name = self.decodeHeaderString(name)
    
    return {"from": addr,
            "name": name,
            "content": quopri.decodestring(get_first_text_block(emailObject)).decode("GB2312").encode("utf-8"),
            "subject": (subject)}

  def getMailContent(self, emailObject):
    email = self.extractMail(emailObject)
    return email

if __name__ == "__main__":
  print "Test"
  # Test
  checker = BlogCDMailChecker()
  print checker.listAllUnseenMails(3)