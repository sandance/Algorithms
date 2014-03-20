
from stack import Stack

def parChecker(symbolString):
	s=Stack()
	balanace=True
	index =0
	while index < len(symbolString):
		symbol=symbolString[index]
		if symbol == '(':
			s.push(symbol)
		else:
			if s.isEmpty():
				balance=False
			else:
				s.pop()
		index =index+1

	if balanced and s.isEmpty():
		return True
	else:
		return False

print (parChecker('(())'))

		
				
