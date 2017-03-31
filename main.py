import webapp2
from vigenere import encrypt
from vigenere import decrypt
import cgi

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Web Vigenere</title>
</head>
<body>
    <h1>Web Vigenere</h1>
    <style>
    body {
      text-align:center
    }
    </style>
"""

page_footer = """
</body>
</html>
"""
encrypt_form = """
      <form action='/' method='post'>
      <label>
      Encryption Key: <input type='text' name='rot' value='%(rot)s'/><label><br>
      <br>Message to encrypt: <br><textarea rows='4' cols='50' name='message'>%(encrypted_message)s</textarea><br>
      <input type='submit' value='Encrypt' name='encrypt_button'/><br>
      <br>Message to decrypt:<br><textarea rows='4' cols='50' name='crypted'>%(decrypted_message)s</textarea><br>
      <input type='submit' value='Decrypt' name='decrypt_button'/><br>
      </form>
      
      """


class MainPage(webapp2.RequestHandler):
    def get(self, encrypted_message = "", rot = "", decrypted_message = ""):
      content = page_header + encrypt_form % {'encrypted_message':encrypted_message, 'rot':rot, 'decrypted_message':decrypted_message} + page_footer
      self.response.write(content)
    
    def post(self, encrypted_message = "", decrypted_message = ""):
      encrypt_button = self.request.get('encrypt_button')
      decrypt_button = self.request.get('decrypt_button')
      rot = self.request.get('rot')
      message = self.request.get('message')
      crypted = self.request.get('crypted')
      
      if encrypt_button:
        encrypted_message = encrypt(message,rot)
        encrypted_message = cgi.escape(encrypted_message, quote=True)
        decrypted_message = crypted
      
      if decrypt_button:
        decrypted_message = decrypt(crypted,rot)
        decrypted_message = cgi.escape(decrypted_message, quote=True)
        encrypted_message = message
      content = page_header + encrypt_form % {'encrypted_message':encrypted_message, 'rot':rot, 'decrypted_message':decrypted_message} + page_footer
      self.response.write(content)
      encrypt_button = False
      decrypt_button = False


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
