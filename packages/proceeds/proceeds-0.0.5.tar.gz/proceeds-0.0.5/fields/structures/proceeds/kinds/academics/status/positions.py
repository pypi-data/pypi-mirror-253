


def introduce (names):
	names_string = ""
	for name in names:
		names_string += (f"""
			<li>{ name }</li>		
		""")
		
	template = f"""
	<header
		style="
			display: flex;
		"
	>
		<h3
			style="
				width: 100px;
			"
		>position</h3>
		<ul>
			{ names_string }
		</ul>
	</header>
	"""

	return template