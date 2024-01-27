



def clique ():
	import click
	@click.group ("mints")
	def group ():
		pass


	'''
		bullion mints names
	'''
	import click
	@group.command ("names")
	def names ():
		import bullion.mints.names as mints_names
		mints_names = mints_names.start ()
	
		print (mints_names)
	
		return;

	'''
		bullion mints save --name "mint-1"
	'''
	import click
	@group.command ("save")
	@click.option ('--name', required = True)
	def search (name):
		print ("name:", name)
	
		return;

	return group




#



