





def introduce (socials):
	socials_string = ""
	for social in socials:
		socials_string += (f"""
			<li><b>{ social }</b></li>		
		""")
		
	template = f"""
	<div
		style="
			position: relative;
		"
	>
		<label>socials</label>
		<ul
			style="
				box-sizing: border-box;
			"
		>
			{ socials_string }
		</ul>
	</div>
	"""

	return template