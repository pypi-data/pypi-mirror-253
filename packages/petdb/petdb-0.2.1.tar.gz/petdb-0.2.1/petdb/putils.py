import re
from typing import Any

from petdb.ptypes import i_remove

class QueryException(Exception):
	pass

class NonExistent:
	def __repr__(self):
		return "[Non-existent-object]"

NON_EXISTENT = NonExistent()

class PetUtils:

	OPERATORS = {
		"$eq": lambda q, v: v == q,
		"$not": lambda q, v: v != q,
		"$ne": lambda q, v: v != q,
		"$lt": lambda q, v: v < q,
		"$<": lambda q, v: v < q,
		"$lte": lambda q, v: v <= q,
		"$<=": lambda q, v: v <= q,
		"$gt": lambda q, v: v > q,
		"$>": lambda q, v: v > q,
		"$gte": lambda q, v: v >= q,
		"$>=": lambda q, v: v >= q,
		"$in": lambda q, v: v in q,
		"$nin": lambda q, v: v not in q,
		"$notin": lambda q, v: v not in q,
		"$exists": lambda q, v: q == (v != NON_EXISTENT),
		"$regex": lambda q, v: v and re.search(q, v),
		"$func": lambda q, v: q(v),
		"$where": lambda q, v: q(v),
		"$f": lambda q, v: q(v),
		"$type": lambda q, v: isinstance(v, q),
		"$is": lambda q, v: isinstance(v, q),
		"$and": lambda q, v: all(PetUtils.match(v, query) for query in q),
		"$all": lambda q, v: all(PetUtils.match(v, query) for query in q),
		"$or": lambda q, v: any(PetUtils.match(v, query) for query in q),
		"$any": lambda q, v: any(PetUtils.match(v, query) for query in q),
	}

	@classmethod
	def match(cls, obj: dict, query: dict) -> bool:
		if not isinstance(query, dict):
			return obj == query
		for key in query:
			if key.startswith("$"):
				if not cls.OPERATORS[key](query[key], obj):
					return False
				continue
			operators_query = cls.is_operators_query(query[key])
			value = cls.get(obj, key)
			if operators_query:
				for operator in query[key]:
					if not cls.OPERATORS[operator](query[key][operator], value):
						return False
			elif isinstance(value, dict) and isinstance(query[key], dict):
				if not cls.match(value, query[key]):
					return False
			elif value != query[key]:
				return False
		return True

	@classmethod
	def is_operators_query(cls, query: dict) -> bool:
		if not isinstance(query, dict) or len(query) == 0:
			return False
		is_operators_query = list(query)[0].startswith("$")
		for key in query:
			if is_operators_query != key.startswith("$"):
				raise QueryException("Invalid query: all keys into operators query must start with $")
		return is_operators_query

	@classmethod
	def get(cls, obj: dict, key: str | int | None = None):
		if key is None:
			if obj is None:
				return NON_EXISTENT
			return obj
		elif isinstance(key, int):
			if not isinstance(obj, list) or key >= len(obj):
				return NON_EXISTENT
			return obj[key]

		value: Any = obj
		for field in key.split("."):
			if isinstance(value, dict):
				if field not in value:
					return NON_EXISTENT
				value = value[field]
			elif isinstance(value, list):
				if not field.isdigit() or int(field) >= len(value):
					return NON_EXISTENT
				value = value[int(field)]
			else:
				return NON_EXISTENT
		return value

	@classmethod
	def remove(cls, data: list[dict], query: i_remove):
		query = cls.__validate_remove_query(query)  # common query or list of docs
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
			raise Exception("Invalid delete query")

	@classmethod
	def __validate_remove_query(cls, query: i_remove) -> dict | list[dict]:
		if isinstance(query, str):
			return {"_id": query}
		elif isinstance(query, list):
			if all(isinstance(item, str) for item in query):
				return {"_id": {"$in": query}}
			elif not all(isinstance(item, dict) for item in query):
				raise Exception("Invalid delete query: it can only be a list of IDs or a list of docs")
			return query
		elif isinstance(query, dict):
			return query
		else:
			raise Exception("Invalid delete query")
