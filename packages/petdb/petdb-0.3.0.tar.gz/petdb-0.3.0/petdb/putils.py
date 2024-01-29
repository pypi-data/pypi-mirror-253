import re
from typing import Any

from petdb.pexceptions import QueryException
from petdb.ptypes import i_remove

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
		"$contains": lambda q, v: q in v,
		"$notcontains": lambda q, v: q not in v,
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

	UPDATE_OPERATORS = {
		"$set": lambda q, doc: [PetUtils.set(doc, key, value) for key, value in q.items()],
		"$append": lambda q, doc: [PetUtils.append(doc, key, value) for key, value in q.items()],
		"$unset": lambda q, doc: [PetUtils.unset(doc, key) for key, value in q.items() if value],
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

			value = cls.get(obj, key)
			if cls.is_operators_query(query[key]):
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
	def update(cls, obj: dict, query: dict):
		for operator in query:
			cls.UPDATE_OPERATORS[operator](query[operator], obj)

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
	def get(cls, obj: dict, key: str | int = None, fill_path: bool = False):
		if key is None:
			if obj is None:
				return NON_EXISTENT
			return obj
		elif isinstance(key, int):
			if not isinstance(obj, list) or key >= len(obj):
				return NON_EXISTENT
			return obj[key]

		for field in key.split("."):
			if isinstance(obj, dict):
				if field not in obj:
					if not fill_path:
						return NON_EXISTENT
					obj[field] = {}
				obj = obj[field]
			elif isinstance(obj, list):
				if not field.isdigit() or int(field) >= len(obj):
					return NON_EXISTENT
				obj = obj[int(field)]
			else:
				return NON_EXISTENT
		return obj

	@classmethod
	def set(cls, obj: dict, key: str, value: Any):
		if "." not in key:
			obj[key] = value
			return

		obj = cls.get(obj, key.rsplit(".", 1)[0], fill_path=True)
		if obj == NON_EXISTENT:
			raise QueryException(f"Invalid set query: path {key} doesn't exist")
		field = key.rsplit(".", 1)[1]
		if isinstance(obj, dict):
			obj[field] = value
		elif isinstance(obj, list):
			if not field.isdigit():
				raise QueryException("Invalid set query: list index must contains only digits")
			if int(field) >= len(obj):
				raise QueryException("Invalid set query: list index out of range")
			obj[int(field)] = value
		else:
			raise QueryException(f"Invalid set query: path {key} doesn't exist")

	@classmethod
	def unset(cls, obj: dict, key: str) -> Any:
		if "." not in key:
			return obj.pop(key, None)

		obj = cls.get(obj, key.rsplit(".", 1)[0])
		if isinstance(obj, dict):
			obj.pop(key.rsplit(".", 1)[1], None)

	@classmethod
	def append(cls, obj: dict, key: str | int, value: Any):
		if isinstance(key, int):
			if not isinstance(obj, list):
				raise QueryException("Invalid set query: only lists supports integer keys")
			if key >= len(obj):
				raise QueryException("Invalid set query: index out of range")
			if not isinstance(obj[key], list):
				raise QueryException("Invalid set query: it's impossible to append not to a list")
			obj[key].append(value)
			return

		obj = cls.get(obj, key)
		if obj == NON_EXISTENT:
			raise QueryException(f"Invalid set query: path {key} doesn't exist")
		elif not isinstance(obj, list):
			raise QueryException("Invalid set query: it's impossible to append not to a list")
		obj.append(value)

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
			raise QueryException("Invalid delete query")

	@classmethod
	def __validate_remove_query(cls, query: i_remove) -> dict | list[dict]:
		if isinstance(query, str):
			return {"_id": query}
		elif isinstance(query, list):
			if all(isinstance(item, str) for item in query):
				return {"_id": {"$in": query}}
			elif not all(isinstance(item, dict) for item in query):
				raise QueryException("Invalid delete query: it can only be a list of IDs or a list of docs")
			return query
		elif isinstance(query, dict):
			return query
		else:
			raise QueryException("Invalid delete query")
