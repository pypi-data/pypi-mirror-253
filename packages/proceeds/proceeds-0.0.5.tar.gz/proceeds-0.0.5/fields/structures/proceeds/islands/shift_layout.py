
'''
	1in = 96px
	
	11 * 96 = 1056
'''

'''
	import proceeds.islands.shift_layout as shift_layout
'''

paper_height = 1056

def script ():

	return """

const paper_height = 1056	

function add_article ({ articles, article }) {
	console.log ({ articles, article })
	
	articles.appendChild (article)
}	

function create_article (article_number) {
	const article = document.createElement ("article");
	article.setAttribute ("article-" + article_number.toString (), "")
	article.setAttribute ("paper", "")
	
	article.style.height = paper_height.toString () + 'px'
	article.style.border = '10px solid #FFF'
	article.style.boxSizing = 'border-box'
	article.style.overflow = 'hidden'
	
	return article
}

function proceed () {
		
	const panels = document.querySelectorAll ("[panel]")
	const papers = document.querySelectorAll ("[paper]")
	const articles = document.querySelectorAll ("main[articles]") [0]
	const articles_start = document.querySelectorAll ("div[articles-start]") [0]

	console.log ({ articles })
	
	const articles_list = [
		create_article (1)
	]
		
	function get_position (element) {
		const boundaries = element.getBoundingClientRect ();
		
		const scroll_y = articles_start.scrollTop;
		
		// console.log (boundaries, boundaries.top, window.offsetTop)
		
		
		
		return {
			y1: boundaries.top + scroll_y,
			y2: boundaries.bottom + scroll_y
		};
	}

	

	/*
		proceeds = [
			[
				section_1,
				section_2,
				section_3			
			],
			[
				section_4,
				section_5,
				section_6
			],
			[]	
		]

	*/

	let next_paper = paper_height;

	var proceeds = [
		[]
	]
	var current_proceeds_index = 0

	let shift_y = 0
	let current_paper_content_height = 0
	
	for (let s = 0; s < panels.length; s++) {
		const panel = panels [s]
		const panel_position = get_position (panel)
		
		
		
		if ((panel_position.y2 + shift_y) >= next_paper) {
			console.info ("next paper")
			
			current_proceeds_index += 1;
			next_paper += paper_height;
			
			proceeds [ current_proceeds_index ] = []
			
			articles_list.push (create_article (
				current_proceeds_index + 1
			))
			
			shift_y += (paper_height - current_paper_content_height); 
			current_paper_content_height = 0
		}
		
		proceeds [ current_proceeds_index ].push ({
			element: panel
		})
		current_paper_content_height += panel_position.y2 - panel_position.y1;
		
		console.log ({
			shift_y, 
			y2: panel_position.y2,
			y1: panel_position.y1,
			current_paper_content_height,
			next_paper 
		})
		
		// if past 1056, add to the next paper
	}

	console.log ({ proceeds })
	console.log ('prepared')
	
	for (let s = 0; s < articles_list.length; s++) {
		add_article ({
			articles,
			article: articles_list [s]
		})
	}
	
	for (let s = 0; s < proceeds.length; s++) {
		proceeds_sections = proceeds[s]
		
		for (let s2 = 0; s2 < proceeds_sections.length; s2++) {
			console.log (s, s2, articles_list [s], proceeds_sections [s2].element)
			
			/*
			articles_list [s].appendChild (
				proceeds_sections [s2].element.cloneNode (true)
			)
			*/
			
			articles_list [s].appendChild (
				proceeds_sections [s2].element
			)
		}
	}
}
	
	
document.addEventListener("DOMContentLoaded", function(event) {	
	setTimeout (() => {
		proceed ()
	}, 100)
	
});	

	
	"""