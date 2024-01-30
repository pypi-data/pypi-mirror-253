







from .group import clique as clique_group

def clique ():
	print ("clique")

	import click
	@click.group ()
	def group ():
		pass

		
	import click
	@click.command ("internal-status")
	@click.option ('--glob-string', default = "")
	def onesie_onesie (glob_string):
		
		if (len (glob_string) >= 1):
			import pathlib
			from os.path import dirname, join, normpath
			this_folder = pathlib.Path (__file__).parent.resolve ()

			structures = normpath (join (this_folder, "../../.."))
			monitors = str (normpath (join (this_folder, "..")))
	
			glob_string = monitors + "/" + glob_string
	
		import onesie._status.establish as establish_status
		establish_status.start (
			glob_string = glob_string
		)
	


	group.add_command (shares)	
	group.add_command (onesie_onesie)	
	group.add_command (status)
	
	group.add_command (clique_group ())
	group ()




#
