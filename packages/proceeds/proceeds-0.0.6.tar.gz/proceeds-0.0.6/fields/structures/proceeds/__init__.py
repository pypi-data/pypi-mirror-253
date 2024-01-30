

'''
plan:

import proceeds

proceeds.abundantly ({
	"build": [{
		"kind": "header"
	}]
})
'''

import proceeds.kinds.academics as academics_kind
import proceeds.kinds.header as header
import proceeds.kinds.companies as companies_kind
import proceeds.kinds.company as company
import proceeds.kinds.company_2 as company_2
import proceeds.kinds.project as project
import proceeds.kinds.projects as projects
import proceeds.kinds.talents as talents
#
import proceeds.modules.line as line
import proceeds.modules.document as document
#
import proceeds.islands.shift_layout as shift_layout
#
from flask import Flask
#
def abundantly (object):
	print ("starting")

	if ('port' in object):
		port = object ["port"]
	else:
		port = 5000
	
	build = object ["build"]
	

	html_document_main = ""

	for structure in build:
		kind = structure ["kind"]
		fields = structure ["fields"]
		
		if (kind == "header"):
			html_document_main += header.build (fields)
		
		elif (kind == "companies"):
			html_document_main += companies_kind.introduce (fields)
		
		elif (kind == "company"):
			html_document_main += company.introduce (fields)
		
		elif (kind == "company 2"):
			html_document_main += company_2.introduce (fields)
		
		elif (kind == "academics"):
			html_document_main += academics_kind.introduce (fields)
			
		elif (kind == "project"):
			html_document_main += project.present (fields)
		
		elif (kind == "projects"):
			html_document_main += projects.present (fields)
	
		elif (kind == "talents"):
			html_document_main += talents.present (fields)
		
		else:
			print (f'Kind "{ kind }" is not an option.')
		
		
	html_document_scripts = shift_layout.script ()
	
	html_string = document.build (
		main = html_document_main,
		script = html_document_scripts
	)


	app = Flask (__name__)
	
	'''
	@app.route ("/picture.png")
	def picture ():
		return html_string
	'''
	
	@app.route ("/")
	def proceeds ():
		return html_string

	app.run (
		debug = True,
		port = port
	)

	return;