from requests import get


def validate_categories(categorie: str) -> bool:
	if categorie != '':
		response = get('https://api.chucknorris.io/jokes/categories').json()
		if categorie in response:
			return True
		raise Exception('Invalid category')
