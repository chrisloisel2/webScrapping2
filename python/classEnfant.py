class Animal:
	def __init__(self):
		# Constructor code here
		self.nom = "Bob"
		pass

	# self c'est la surcharge de ma fonction
	def respire(): # fonction d'intance
		print("Mon animal respire ")

bob = Animal()
bob.nom = "Boulot"
Animal.respire()
