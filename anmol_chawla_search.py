import csv
import json
from firebase import firebase
from collections import defaultdict
import sys


if __name__ == '__main__': 
  answer = []
  firebase = firebase.FirebaseApplication('https://dmhw1-28e4c.firebaseio.com/')
  
  user_input = sys.argv[1]
  user_input.upper()
  user_inputdata = ((user_input.upper()).split())
  l = len(user_inputdata)
  for i in user_inputdata:
      out = firebase.get('menu_update',i)
      if out != None:
          answer.extend(out)
      
  
  solution = set(answer)
  answer = (list(solution))
  stringing = ' '.join(answer)
  final  = stringing.encode('ascii', 'ignore')
  print(final)
      


