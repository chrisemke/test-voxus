from typing import Optional, List
from strawberry import type, field, Schema
from strawberry.fastapi import GraphQLRouter
from resolver.chuck_norris import get_jokes


@type
class Joke:
	categorie: Optional[str]
	free_text_search: Optional[str]
	limit: Optional[int]
	icon_url: str = ''
	id: str = ''
	url: str = ''
	value: str = ''


@type
class Query:
	all_jokes: List[Joke] = field(resolver=get_jokes)


schema = Schema(query=Query)

graphql_app = GraphQLRouter(schema)
