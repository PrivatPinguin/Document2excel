class EnvPath:
  def __init__(self):
    self.pytesseract_path = ''
    self.poppler_path = ''
    import re
    file = open("env.pth", "r")
    text = file.read()
    for line in text:
      if re.match(r'[[:upper:]]+_PATH:\[', line):
        if re.match(r'PYTESSERACT_PATH:\[',line):
          self.pytesseract_path = line.replace(r'PYTESSERACT_PATH:\[', '').[:-1]
        elif re.match(r'POPPLER_PATH:\[',line):
          self.pytesseract_path = line.replace(r'POPPLER_PATH:\[', '').[:-1]          
    file.close() 
  
  def __replaceLine__(self, text_path, line_id):
    file = open("env.pth", "r")
    list_of_lines = file.readlines()
    for cnt,line in enumarete(list_of_lines):
      if line_id == 'POPPLER_PATH':
        if re.match(r'POPPLER_PATH:\[',line):
          list_of_lines[cnt] = r'POPPLER_PATH:\[' + text_path + ']'
      elif line_id == 'PYTESSERACT_PATH':
        if re.match(r'PYTESSERACT_PATH:\[',line):
          list_of_lines[cnt] = r'PYTESSERACT_PATH:\[' + text_path + ']'

    file = open("env.pth", "w", encoding="utf-8")
    file.writelines(list_of_lines)
    file.close()
  
  def getPoppler(self):
    return self.poppler_path
  
  def getPyTessreact(self):
    return self.poppler_path
  
  def setPoppler(self, new_poppler_path):
    self.poppler_path = new_poppler_path 
    self.__replaceLine__(new_poppler_path, 'POPPLER_PATH')

  def setPyTesseract(self, new_pytesseract_path):
    self.pytesseract_path = new_pytesseract_path 
    self.__replaceLine__(new_pytesseract_path, 'PYTESSERACT_PATH')     
  
  def self_Update(self):
    __init__(self)
