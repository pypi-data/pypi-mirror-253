



'''
{
	"kind": "talents",
	"fields": {
		"talents": [{
			"name": "Vue",
			"slider": [ 10, 10 ]
		},{
			"name": "python",
			"slider": [ 8, 10 ]
		}]
		
	}
}

background-image: repeating-linear-gradient(45deg, transparent, transparent 35px, yellow 35px, yellow 70px);
'''

'''
import proceeds.kinds.project as project
project.preset ({
	"name": "",
	"description": ""
})
'''

from mako.template import Template

import proceeds.climate as climate
border_width = climate.find () ["layout"] ["border width"]
border_radius = climate.find () ["layout"] ["border radius"]
repulsion = climate.find () ["layout"] ["repulsion"]
palette = climate.find () ["palette"]

import proceeds.modules.panel as panel

def present (fields):
	talents = fields ['talents']
	
	talents_molecules = ""
	for talent in talents:
		name = talent ["name"]
		slider = talent ["slider"]		

		width_percentage = int (round (
			float (slider [0]) / float (slider [1]),
			2
		) * 100)

		talents_molecules += f"""
<div
	style="
		display: table-row;
	"
>
	<div
		style="
			display: table-cell;
		"
	>
		<p
			style="
				padding: 2px 20px;
				box-sizing: border-box;
			"
		>{ name }</p>
	</div>
	<div 
		style="
			display: table-cell;
		
			position: relative;
			
			box-sizing: border-box;
			height: 15px;
			width: 100%;
			padding: 4px;
			
			border-radius: 4px;
			border: 1px solid #444;
		"
	>
		<div
			style="
				position: absolute;
				top: 2px;
				left: 2px;
				
				height: calc(100% - 4px);
				width: calc({ width_percentage }% - 4px);
				
				background-color: black;
				
				
				box-sizing: border-box;
				border: 1px solid black;
				border-radius: 4px;
			"
		></div>
	</div>
</div>		
		"""
		
		if (talent != talents [ len (talents) - 1 ]):
			talents_molecules += "<div style='height: 5px;'></div>"
		

	name = "talents"
	
	
	'''
		letter-spacing: -0.3px;
	'''
	
	this_template = f"""
<article
	tile
	style="
		//border: { border_width } solid { palette [3] };
		border-radius: { border_radius };
		padding: .15in;		
		
		display: table;
		width: 90%;
	"
>
	<header
		style="
			display: table-cell;
			width: 40px;
			overflow: hidden;
		"
	>
		<h1
			style="
				display: block;
				
				white-space: pre;
			
			
				font-style: normal;
			
				text-orientation: upright;
				writing-mode: vertical-rl;
				line-height: 1;
				
				padding: 5px;
				margin-right: 30px;
				border-radius: 4px;
			
				background: { palette [4] };
			"
		>{ name }</h1>
	</header>
	<div
		style="
			display: table;
			width: 100%
		"
	>
		{ talents_molecules }
	</div>
</article>
	"""
	
	return panel.build (this_template);

	
	
	
	
	
	
	
#