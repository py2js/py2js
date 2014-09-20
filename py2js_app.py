import logging
import webapp2

from trans import translate

out = """Hi there!

%s

"""

class Translate(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain' #todo: use json
    self.response.write(translate('yo'))

class TestTranslate(webapp2.RequestHandler):
  def get(self):
    self.response.write("""

<html>
<title> py2js </title>
<body>
Hi there
</body
</html>

""")

app = webapp2.WSGIApplication([('/py2js/translate/', Translate),
                               ('/py2js/test_translate/', TestTranslate)
                              ],
                              debug=True)
