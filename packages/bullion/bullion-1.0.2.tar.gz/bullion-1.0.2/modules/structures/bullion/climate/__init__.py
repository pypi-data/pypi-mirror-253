

'''
	import bullion.climate as bullion_climate
	bullion_climate.change ("treasuries", {
		"path": treasuries_path
	})

	import bullion.climate as bullion_climate
	climate_treasuries = bullion_climate.find ("treasuries")
	climate_mints = bullion_climate.find ("mints")


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