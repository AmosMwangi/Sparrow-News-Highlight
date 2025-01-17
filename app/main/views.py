from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_articles
from ..models import Sources


#views
@main.route('/')
def index():
	'''
	view root page function that returns the index the page and its data
	'''
	general = get_sources('general')
	sports_sources = get_sources('sports')
	technology_sources = get_sources('technology')
	entertainment_sources = get_sources('entertainment')
	title = "Sparrow News"

	return render_template('index.html',title = title, general = general, sports_sources = sports_sources,technology_sources = technology_sources,entertainment_sources = entertainment_sources)

@main.route('/sources/<id>')
def sources(id):
	'''
	view articles page
	'''
	articles = get_articles(id)
	title = f'{id}'

	return render_template('article.html', title= title,articles = articles)
