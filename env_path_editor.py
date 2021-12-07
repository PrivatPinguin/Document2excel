class Path:
  def __init__(self):
    self.pytesseract_path = ''
    self.popplerpath = ''
    import re
    file = open("env.pth", "r")
    text = file.read()
    for line in text:
      if re.match(r'[[:upper:]]+_PATH:\[', line):
        if re.match(r'PYTESSERACT_PATH:\[',line):
          
    file.close() 
    
