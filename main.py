import webapp2
from vigenere import encrypt
import cgi

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Web Vigenere</title>
</head>
<body>
    <h1>Web Vigenere</h1>
"""

page_footer = """
</body>
</html>
"""
encrypt_form = """
      <form action='/' method='post'>
      <label>
      Encryption Key <input type='text' name='rot' value='%(rot)s'/><label><br>
      <br>Message to encrypt: <br><textarea rows='4' cols='50' name='message'>%(encrypted_message)s</textarea><br>
      <input type='submit' value='Encrypt'/><br>
      </form>
      
      """

class MainPage(webapp2.RequestHandler):
    def get(self, encrypted_message = "", rot = ""):
      content = page_header + encrypt_form % {'encrypted_message':encrypted_message, 'rot':rot} + page_footer
      self.response.write(content)
    
    def post(self):
      rot = self.request.get('rot')
      message = self.request.get('message')
      encrypted_message = encrypt(message,rot)
      encrypted_message = cgi.escape(encrypted_message, quote=True)
      content = page_header + encrypt_form % {'encrypted_message':encrypted_message, 'rot':rot} + page_footer
      self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
