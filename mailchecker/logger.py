from logentries import LogentriesHandler
import logging,os
import logentries

TOKEN = "0e7f7bce-2f27-448c-b072-0ea589be47d7"

class InfoLogger(object):

  def __init__(self):
    self.log = logging.getLogger('logentries')
    self.log.addHandler(LogentriesHandler(TOKEN))

  def info(self, message):
    self.log.warn(message)



if __name__ == "__main__":
  print "test"
  InfoLogger().info("Im a test message.")

