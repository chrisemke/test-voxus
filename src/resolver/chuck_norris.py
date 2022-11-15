from resolver.sanitize_resolver import Sanitizer
from requests import get
from utils.validator import validate_categories
from urllib.parse import quote
from itertools import islice


def get_jokes(
	category: str = '',
	free_text_search: str = '',
	limit: int = 5
) -> Sanitizer:
	valid_categorie = validate_categories(category)
	if valid_categorie:
		response = get(
			f'https://api.chucknorris.io/jokes/random?category={category}'
		).json()
		return [call_sanitizer(response)]

	if free_text_search != '':
		url_query = quote(free_text_search)
		response = get(
			f'https://api.chucknorris.io/jokes/search?query={url_query}'
		).json()
		if limit:
			response = dict(islice(response.items(), limit))

		return list(map(call_sanitizer, response['result']))


def call_sanitizer(request_content: dict) -> Sanitizer:
	return Sanitizer(
		icon_url=request_content['icon_url'],
		id=request_content['id'],
		url=request_content['url'],
		value=request_content['value']
	)
