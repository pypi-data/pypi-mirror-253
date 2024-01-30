




import proceeds.kinds.company.status as status

import proceeds.modules.line as line
import proceeds.modules.panel as panel

import proceeds.climate as climate
border_width = climate.find () ["layout"] ["border width"]
palette = climate.find () ["palette"]

def introduce (fields, is_panel = True):
	name = fields ["name"]
	statuses = fields ["statuses"]
	description = fields ["description"]
	
	label = "🐾 academics"
	label = "🌱 academics"
	
	start = (
	f"""
<article
	tile
	kind-company
	style="
		display: table;

		margin-bottom: .1in;		
		box-sizing: border-box;
		// border: { border_width } solid { palette[3] };
		padding: .15in;

		// background: { palette [4] };

		border-radius: .1in;
	"
>
	<header
		style="
			display: flex;
		
		"
	>
		<h1
			style="
				font-style: normal;
			
				text-orientation: upright;
				writing-mode: vertical-rl;
				line-height: 1;
				
				padding: 5px;
				margin-right: 30px;
				border-radius: 4px;
			
				background: { palette [4] };
			"
		>{ label }</h1>
	</header>
	<div
		style="
			display: table-cell;
		"
	>	
		<table>
			<tbody>
				<tr
					style="
						padding: 0 10px;
					"
				>
					<td
						style="
							width: 100px;
							font-style: italic;
						"
					>name</td>
					<td
						style="
							font-size: 1.5em;
							font-weight: bold;
						"
					>{ name }</td>	
				</tr>
				
				<tr>
					<td
						style="
							width: 100px;
							font-style: italic;
						"
					>description</td>
					<td>{ description }</td>
				</tr>
			</tbody>
		</table>
""")




	end = (f"""</div></article>""")
	
	positions_string = ""
	
	index = 0;
	for _status in statuses:
		positions_string += status.introduce (_status)
		
		if (index < len (statuses) - 1):
			positions_string += line.create ()
			
		index += 1
		
		
		
	content = start + positions_string + end;
	
	if (is_panel):
		return panel.build (content)
		
	return content;