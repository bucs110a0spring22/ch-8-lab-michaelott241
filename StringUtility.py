class StringUtility:
  def __init__(self,string):
    self.string = string 
  def __str__(self):  
    return self.string

  def vowels(self):  
    count = 0
    vowel = set("aeiouAEIOU")
    for i in self.string:
      if i in vowel: 
        count += 1
    if count >= 5: 
      return "many"
    else: 
      return str(count)
  
  def bothEnds(self): 
    if len(self.string) <= 2:
      return ""
    else:
      return self.string[0:2] + self.string[-2:]

  def fixStart(self):
    repeat_letter = ""
    if len(self.string) <=1:
      return self.string
    else:
      repeat_letter += self.string[0]
      for index in range(1, len(self.string)): 
        if self.string[index] == repeat_letter[0]:
          repeat_letter += '*'
        else:
          repeat_letter += self.string[index]
    return repeat_letter 

  def asciiSum(self):  
    return sum(map(ord,self.string))

  
  
      
      
    
  
      
    

      

  


