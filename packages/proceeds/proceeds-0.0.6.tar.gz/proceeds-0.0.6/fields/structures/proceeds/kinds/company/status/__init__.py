


import proceeds.climate as climate
border_width = climate.find () ["layout"] ["border width"]
palette = climate.find () ["palette"]

import proceeds.kinds.company.status.places as places
import proceeds.kinds.company.status.dates as dates
import proceeds.kinds.company.status.feats as feats
import proceeds.kinds.company.status.positions as positions

import proceeds.modules.panel as panel
	

def introduce (dictionary):
	names = dictionary ["names"]

	start = (
	f"""
<article
	style="
		border: { border_width } solid { palette [3] };
		background: { palette [4] };
	
		border-radius: .1in;
		padding: .25in;
		
		margin-bottom: .1in;
	"
>
	{ positions.introduce (names) }
""")

	end = (
f"""
</article>"""	
	)	

	structure = ""
	if ("places" in dictionary):
		structure += places.introduce (dictionary ["places"])
		
	if ("dates" in dictionary):
		structure += dates.introduce (dictionary ["dates"])
		
	if ("feats" in dictionary):
		structure += feats.introduce (dictionary ["feats"])

	content = start + structure + end;
	
	return content