


import proceeds.climate as climate
border_width = climate.find () ["layout"] ["border width"]
	
	
def two_dates (dates):
	string = ""

	string = f'''
<li>
	<span>{ dates[0] }</span>
	<span
		style="
			opacity: 1
		"
	> to </span>
	<span>{ dates[1] }</span>	
</li>
	'''
		
	return string;
	
def introduce (dates):
	string = ""
	
	if (len (dates) == 2):
		if (
			type (dates [0]) == str and 
			type (dates [1]) == str
		):
			string += two_dates (dates)


	template = (f"""
	<section
		style="
			display: flex;
		"
	>
		<h3
			style="
				width: 100px;
			"
		>dates</h3>
		<ul>
			{ string }
		</ul>
	</section>
""")
	

	
	
	
	

	return template