from typing import Optional
from strawberry import type


@type
class Sanitizer:
	icon_url: Optional[str]
	id: Optional[str]
	url: Optional[str]
	value: Optional[str]
