import re


class StockSymbols:
   def __init__(self, filename, ticker):
       self.f = open(filename)
       self.ticker = ticker
       self.arr_temp = False
       self.com_names()
   #'''Returns array of all tickers'''

   def tickers(self):
      string = self.f.read()
      expression = re.compile("([A-Z]{1,5})\s+")
      self.arr_temp = expression.findall(string)
   #''' Returns name of company based on recieved ticker'''
   def com_names(self):
      string2 = self.f.read()
      lines = string2.split('\n')
      for n in range(len(lines)):
         temp_str = lines[n]
         isIn = re.search(self.ticker, temp_str)
         if isIn:
            temp = re.sub(self.ticker, "", temp_str, 1)
      self.company_name = temp

   def g(self):
      return self.company_name

#print(StockSymbols('NYSE.txt').ComNames('ABC')) #tests to confirm successful run of company name getter