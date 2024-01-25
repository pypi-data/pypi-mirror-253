

'''
	import debt.climate as debt_climate
	debt_climate.change ("treasuries", {
		"path": treasuries_path
	})

	import debt.climate as debt_climate
	climate_treasuries = debt_climate.find ("treasuries")
	climate_mints = debt_climate.find ("mints")


	print ('climate_treasuries', climate_treasuries)
	print ('climate_mints', climate_mints)
'''

import copy

climate = {}

def change (field, plant):
	#global CLIMATE;
	climate [ field ] = plant


def find (field):
	#print ("climate:", climate)

	return copy.deepcopy (climate) [ field ]