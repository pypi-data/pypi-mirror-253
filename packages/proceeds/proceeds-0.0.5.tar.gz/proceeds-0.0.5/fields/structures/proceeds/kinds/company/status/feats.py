



import proceeds.climate as climate
border_width = climate.find () ["layout"] ["border width"]
	
	
def introduce (feats):
	START = ("""
	<section
		style="
			display: flex;
		"
	>
		<h3
			style="
				width: 100px;
			"
		>feats</h3>
		<ul
			style="
				width: calc(100% - 100px)
			"
		>
""")
	
	END = ("""
		</ul>
	</section>
""")

	STRING = ""
	
	for FEAT in feats:
		STRING += (
f"""			<li>{ FEAT }</li>"""
		)

	return START + STRING + END;