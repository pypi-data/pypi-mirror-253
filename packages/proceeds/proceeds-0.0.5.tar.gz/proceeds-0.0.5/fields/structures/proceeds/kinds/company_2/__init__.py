




import proceeds.kinds.company_2.status as status
import proceeds.modules.line as line


import proceeds.climate as climate
border_width = climate.find () ["layout"] ["border width"]

import proceeds.modules.panel as panel


def introduce (
	fields,
	is_panel = True
):
	company_2_name = fields ["name"]
	statuses = fields ["statuses"]
	
	START = (
	f"""
<article
	tile
	style="
		border: { border_width } solid black;
		border-radius: .1in;
		padding: .2in;
		margin-bottom: .1in;
	"
>
	<header
		style="
			display: flex;		
		"
	>
		<h2
			style="
				padding-right: .1in;
			"
		>company:</h2>
		<p
			style="
				text-align: center;
				padding-bottom: .1in;
				font-size: 1.5em;
			"
		>{ company_2_name }</p>	
	</header>
""")

	END = (
f"""
</article>"""	
	)
	
	positions_string = ""
	
	index = 0;
	for _status in statuses:
		positions_string += status.introduce (_status)
		
		if (index < len (statuses)):
			positions_string += line.create ()
			
		index += 1
		
	content = START + positions_string + END;
	
	if (is_panel):
		return panel.build (content)
		
	return content;