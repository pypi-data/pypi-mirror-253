


import proceeds.kinds.company.status as status

import proceeds.modules.line as line
import proceeds.modules.panel as panel

import proceeds.climate as climate
border_width = climate.find () ["layout"] ["border width"]

import proceeds.kinds.company as company_kind


def introduce (fields):
	companies = fields ['companies']
	
	company_molecules = ""
	for company in companies:
		print ('adding company', company)
		
		company_molecules += company_kind.introduce (
			company,
			is_panel = False
		)
		
		if (company != companies [ len (companies) - 1 ]):
			company_molecules += "<div style='height: 5px;'></div>"
			
	return '<div>companies</div>'