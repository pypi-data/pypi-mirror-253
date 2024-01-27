

import inspect
import os
from os.path import dirname, join, normpath

from bullion.clique import clique
import bullion.config.scan as config_scan
import bullion.climate as bullion_climate

configured = False

def is_configured ():
	return configured

def start ():
	bullion_config = config_scan.start ()

	print ('bullion configuration', bullion_config.configuration)
	
	
	'''
		get the absolute paths
	'''
	bullion_config.configuration ["treasuries"] ["path"] = (
		normpath (join (
			bullion_config.directory_path, 
			bullion_config.configuration ["treasuries"] ["path"]
		))
	)
	bullion_config.configuration ["mints"] ["path"] = (
		normpath (join (
			bullion_config.directory_path, 
			bullion_config.configuration ["mints"] ["path"]
		))
	)

	#print ('bullion configuration', bullion_config.configuration)

	'''
		Add the changed version of the basal config
		to the climate.
	'''
	config = bullion_config.configuration;
	for field in config: 
		bullion_climate.change (field, config [field])
	
	configured = True
	
	print ()
