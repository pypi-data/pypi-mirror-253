




'''
import proceeds.climate as climate
climate.change ("", {})
'''

'''
import proceeds.climate as climate
border_width = climate.find () ["layout"] ["border width"]
border_radius = climate.find () ["layout"] ["border radius"]
repulsion = climate.find () ["layout"] ["repulsion"]

border_width = climate.find () ["layout"] ["article"] ["border_width"]

palette = climate.find () ["palette"]

'''

import copy

climate = {
	"layout": {
		"border width": ".03in",
		"border radius": ".07in",
		
		"repulsion": "0.1in",
		
		"article": {
			"border_width": 10
		}
	},
	"palette": {
		1: "#FFF",
		2: "#000",
		
		# borders
		3: "#DFDFDF",
		
		#4: "linear-gradient(45deg, rgb(225, 225, 225), rgb(255, 255, 255), rgb(221, 221, 221))",
		4: "#FFF"
	}
}

def change (ellipse, planet):
	climate [ ellipse ] = planet


def find ():
	return copy.deepcopy (climate)