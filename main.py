import random
from datetime import date

states = open('states').read().splitlines()

names = open('names').read().splitlines()

def makeTicket():
  today = date.today()
  day = today.strftime("%B %d, %Y")
  state = random.choice(states)
  fname = random.choice(names)
  lname = random.choice(names)
  name = (fname + ' ' + lname)
  ticket = (f'''Ticket:  
Name:  {name}
Date:  {day}
Flight to:  {state}
''')
  print(ticket)

makeTicket()
