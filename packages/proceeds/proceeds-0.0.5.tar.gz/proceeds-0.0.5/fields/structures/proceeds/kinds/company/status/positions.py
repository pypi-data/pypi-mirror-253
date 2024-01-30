


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
		>status</h3>
		<ul
			style="
				box-sizing: border-box;
				font-weight: bold;
			"
		>
			{ names_string }
		</ul>
	</header>
	"""

	return template