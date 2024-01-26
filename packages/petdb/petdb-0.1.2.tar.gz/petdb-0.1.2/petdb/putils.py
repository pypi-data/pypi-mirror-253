import re
from typing import Any, Callable

class PetUtils:

	@classmethod
	def match(cls, doc: dict, query: dict):
		for key in query:
			value = cls.get_field(doc, key)
			if isinstance(value, dict) and isinstance(query[key], dict):
				if not cls.match(value, query[key]):
					return False
			elif isinstance(query[key], dict):
				for operator in query[key]:
					if not cls.apply_operator(operator, query[key][operator], value):
						return False
			elif value != query[key]:
				return False
		return True

	@classmethod
	def apply_operator(cls, operator: str, query: Any, value: Any) -> bool:
		def func(query: Callable, doc: dict):
			try: return query(doc)
			except Exception: return False
		return {
			"$eq": lambda q, v: v == q,
			"$not": lambda q, v: v != q,
			"$ne": lambda q, v: v != q,
			"$lt": lambda q, v: v < q,
			"$lte": lambda q, v: v <= q,
			"$gt": lambda q, v: v > q,
			"$gte": lambda q, v: v >= q,
			"$in": lambda q, v: v in q,
			"$nin": lambda q, v: v not in q,
			"$notin": lambda q, v: v not in q,
			"$exists": lambda q, v: not (q ^ (v is not None)),
			"$regex": lambda q, v: v and re.search(q, v),
			"$func": func
		}[operator](query, value)

	@classmethod
	def get_field(cls, doc: dict, key: str):
		value: Any = doc
		for field in key.split("."):
			if not isinstance(value, dict):
				return None
			value = value.get(field, None)
		return value

	@classmethod
	def remove(cls, data: list[dict], query: dict | list):
		query = cls.__validate_remove_query(query)
		if isinstance(query, list):
			deleted = []
			for doc in query:
				try:
					data.remove(doc)
					deleted.append(doc)
				except ValueError:
					pass
			return deleted
		elif isinstance(query, dict):
			deleted = [doc for doc in data if cls.match(doc, query)]
			for doc in deleted:
				data.remove(doc)
			return deleted
		else:
			raise Exception("Invalid query")

	@classmethod
	def __validate_remove_query(cls, query: str | dict | list[str | dict]):
		if isinstance(query, str):
			return {"_id": query}
		elif isinstance(query, list):
			if all(isinstance(item, str) for item in query):
				return {"_id": {"$in": query}}
			elif not all(isinstance(item, dict) for item in query):
				raise Exception("Invalid input: query can only be a list of str or a list of dict")
			return query
		elif isinstance(query, dict):
			return query
		else:
			raise Exception("Invalid query")
