'''
This is a basic queue class.
'''

class queue(object):
	internal_list = []
	def add(self, item):
		self.internal_list = [item] + self.internal_list
		return self.internal_list
	def get(self, index):
		return self.internal_list[index]
	def get_all(self):
		return self.internal_list
	def remove(self, item):
		del self.internal_list[self.internal_list.index(item)]
		return self.internal_list
	def pop(self):
		return self.internal_list.pop()
