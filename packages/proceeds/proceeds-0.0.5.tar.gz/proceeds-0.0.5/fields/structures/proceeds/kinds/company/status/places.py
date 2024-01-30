



import proceeds.climate as climate
border_width = climate.find () ["layout"] ["border width"]

def introduce (places):
	start = ("""
	<section
		style="
			display: flex;
		"
	>
		<h3
			style="
				width: 100px;
			"
		>place</h3>
		<ul>
""")
	
	end = ("""
		</ul>
	</section>
""")

	string = ""
	
	for place in places:
		string += (
f"""			<li>{ place }</li>"""
		)
	
	

	return start + string + end;