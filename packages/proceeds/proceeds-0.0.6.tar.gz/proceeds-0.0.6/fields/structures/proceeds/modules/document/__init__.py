
'''
	/* list-style-type: circle; */
	// list-style-type: disclosure-closed;
'''


def build (
	main = "",
	script = ""
):

	styles = """
body {
	margin: 0;
	padding: 0;
}

h1, h2, h3, p, ul, li {
	margin: 0;
	padding: 0;
}

h1, h2, h3 {
	font-weight: normal;
	font-style: italic;
}

p {
	font-weight: normal;
	font-style: normal;
}

li {
	list-style-type: none;
	position: relative;
	border-bottom: 1px solid #c8c5c5;
}

li::before {
	// content: '💎';
	padding-right: 10px;
	position: absolute;
	left: -20px;
}

ul {
	box-sizing: border-box;
	//padding-left: 20px;
}

main {
	position: relative;
	margin: 0 auto;
	width: 8.5in;
	height: 11in;
}		

div[articles-start] {
	box-sizing: border-box;
	
	position: relative;
	margin: 0 auto;
	width: 8.5in;
	visibility: hidden;
}

div[articles-start], article[paper] {
	border-left: 10px solid #FFF;
	border-right: 10px solid #FFF;
}

	"""
	


	return (f"""
<!DOCTYPE html>
<html>
<head>
</head>
<body>
<style>
	{ styles }
</style>
<div articles-start>
	{ main }
</div>
<main articles>


</main>
<script>
	{ script }
</script>
</body>
	""")
