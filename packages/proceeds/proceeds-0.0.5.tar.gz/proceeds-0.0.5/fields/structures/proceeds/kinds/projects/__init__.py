



'''
{
	"kind": "projects",
	"fields": {
		"label": "",
		
		"projects": [{
			"name": "project 1",
			"summary": ""
		}]
		
	}
}
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
import proceeds.kinds.project as project_kind

def present (fields):
	projects = fields ['projects']
	
	project_molecules = ""
	for project in projects:
		print ('adding project', project)
		
		project_molecules += project_kind.present (
			project,
			is_panel = False
		)
		
		if (project != projects [ len (projects) - 1 ]):
			project_molecules += "<div style='height: 5px;'></div>"
		
	if ("label" in fields):
		label = fields ["label"]
	else:
		
		# 工程项目
		#name = "Projects"
		#name = "🎁 gifts"
		label = "🎁 ventures"
	
	print (project_molecules)
	
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
		>{ label }</h1>
	</header>
	<div
		style="
			display: table-cell;
			width: 100%
		"
	>
		{ project_molecules }
	</div>
</article>
	"""
	
	return panel.build (this_template);

	
	
	
	
	
	
	
#