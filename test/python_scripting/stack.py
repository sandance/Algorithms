#!/usr/bin/python

class Stack:
	def __init__(self, start=[]):
		self.stack = []
		for x in start: self.push(x)
		self.reverse()

	def push(self,obj):
		self.stack = [obj] + self.stack
	def pop
