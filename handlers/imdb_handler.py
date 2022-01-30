import aiohttp
import typing as tp
from yarl import URL
import pydantic
from pydantic import BaseModel

imdb_url = URL("https://imdb-api.com/")


class IMDbResponseResult(BaseModel):
    id: str = pydantic.Field(...)
    resultType: str = pydantic.Field(...)
    image: str = pydantic.Field(...)
    title: str = pydantic.Field(...)
    description: str = pydantic.Field(...)


class IMDbResponseData(BaseModel):
    searchType: str = pydantic.Field(...)
    expression: str = pydantic.Field(...)
    results: tp.Optional[list[IMDbResponseResult]] = pydantic.Field(None)
    errorMessage: str = pydantic.Field("")


async def search_by_expression_imdb(apikey: str, expression: str, language: str = "en") -> IMDbResponseData:
    endpoint = imdb_url / language / "API" / "Search" / apikey / expression
    async with aiohttp.ClientSession() as session:
        print('imdb28', endpoint)
        # async with session.get(endpoint) as response:
        response = await session.get(endpoint, ssl=False)
        print('imdb31')
        response_json = await response.json()
        return IMDbResponseData.parse_obj(response_json)
