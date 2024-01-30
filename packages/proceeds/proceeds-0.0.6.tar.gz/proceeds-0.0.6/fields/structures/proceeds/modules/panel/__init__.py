
'''
	import proceeds.modules.panel as panel
	panel.build ()
'''

def build (molecule):
	return (f'''
<section
	panel
	style="
		box-sizing: border-box;
		padding: .05in;
	"
>
	{ molecule }
</section>	
	''')