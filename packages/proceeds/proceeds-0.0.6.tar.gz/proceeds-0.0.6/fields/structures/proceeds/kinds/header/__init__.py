
'''
import proceeds.kinds.header as header
header.build (structure)
'''
from mako.template import Template
import proceeds.modules.paragraph as paragraph

import proceeds.climate as climate
import proceeds.modules.panel as panel
palette = climate.find () ["palette"]
	
import proceeds.kinds.header.sections.socials as socials_section


def build (structure):
	name = structure ["name"]
	summary = structure ["summary"]

	if ("background" in structure):
		background = structure ["background"]
	else:
		background = "none"
		
	if ("socials" in structure):
		socials = socials_section.introduce (structure ["socials"])
	else:
		socials = ""

	p1 = paragraph.build (name)
	p2 = paragraph.build (summary)
	
	border_width = climate.find () ["layout"] ["border width"]
	
	mako_template = Template (
f"""
<section
	kind-header
	tile
	style="
		position: relative;
		overflow: hidden;
	
		border: { border_width } solid { palette[3] };
		border-radius: .1in;
		padding: .25in;
	
		border-bottom: .1in solid none;
	
		// display: flex;
		justify-content: space-between;
	"
>
	<img 
		style="
			position: absolute;
			top: 0;
			left: 0;
			
			width: 100%;
			
			opacity: .3;
		"
	
		src="{ background }" 
	/>
		
	<div
		style="
			position: relative;
			margin-bottom: 10px;
		"
	>
		<label>name</label>
		{ p1 }
	</div>
	
	<div
		style="
			position: relative;
			margin-bottom: 10px;
		"
	>
		<label>intro</label>
		<p
			style="
				white-space: pre-wrap;
				font-weight: bold;
			"
		>{ summary }</p>
	</div>
	
	{ socials }
</section>
""")

	return panel.build (
		mako_template.render (name = name)
	)

