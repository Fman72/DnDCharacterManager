import random
import string

def generateCode():
  return ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
