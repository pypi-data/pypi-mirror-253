

import inspect
import os
from os.path import dirname, join, normpath

from debt.clique import clique
import debt.config.scan as config_scan
import debt.climate as debt_climate

configured = False

def is_configured ():
	return configured

def start ():
	debt_config = config_scan.start ()

	print ('debt configuration', debt_config.configuration)
	
	
	'''
		get the absolute paths
	'''
	debt_config.configuration ["treasuries"] ["path"] = (
		normpath (join (
			debt_config.directory_path, 
			debt_config.configuration ["treasuries"] ["path"]
		))
	)
	debt_config.configuration ["mints"] ["path"] = (
		normpath (join (
			debt_config.directory_path, 
			debt_config.configuration ["mints"] ["path"]
		))
	)

	#print ('debt configuration', debt_config.configuration)

	'''
		Add the changed version of the basal config
		to the climate.
	'''
	config = debt_config.configuration;
	for field in config: 
		debt_climate.change (field, config [field])
	
	configured = True
	
	print ()
