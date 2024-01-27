

import os
import time
# os.getcwd()

import shares

def clique ():

	import click
	@click.group (invoke_without_command = True)
	@click.pass_context
	def group (ctx):
		if ctx.invoked_subcommand is None:
			click.echo ('I was invoked without subcommand')
			start ([], standalone_mode = False)
		else:
			click.echo ('I am about to invoke %s' % ctx.invoked_subcommand)
	
		pass

	import click
	@click.command ("start")
	@click.option ('--port', default = 2345)
	@click.option ('--static-port', is_flag = True, default = False)
	def start (port, static_port):	
		shares.start ({
			"directory": os.getcwd (),
			"relative path": os.getcwd (),
			
			"port": port,
			"static port": static_port,
			"verbose": 1
		})
		
		# close = input ("press close to exit") 
		while True:                                  
			time.sleep (1)  

	group.add_command (start)

	#start ([], standalone_mode=False)

	#group.add_command (clique_group ())
	group ()


	#start ()
	                          
