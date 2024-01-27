import os
import json
import uuid
from types import NoneType
from typing import Optional, Iterator, Self, Callable, Any

from petdb.putils import PetUtils, NON_EXISTENT
from petdb.ptypes import i_remove, i_sort

class PetCollection:

	def __init__(self, path: str):
		self.__path = path
		self.name = os.path.basename(path).rsplit(".", 1)[0]
		if not os.path.exists(self.__path):
			with open(self.__path, "w") as f:
				f.write("[]")
		with open(self.__path, "r", encoding="utf-8") as f:
			self.__data: list[dict] = json.load(f)

	def dump(self):
		with open(self.__path, "w", encoding="utf-8") as f:
			json.dump(self.__data, f, indent=4, ensure_ascii=False)

	def save(self):
		self.dump()

	def insert(self, doc):
		if "_id" in doc and self.get(doc["_id"]):
			raise Exception("Duplicate id")
		if "_id" not in doc:
			doc["_id"] = str(uuid.uuid4())
		self.__data.append(doc)
		self.dump()
		return doc

	def get(self, id: str) -> Optional[dict]:
		return PetMutable(self, self.__data).get(id)

	def find(self, query: dict) -> Optional[dict]:
		return PetMutable(self, self.__data).find(query)

	def findall(self, query: dict) -> list[dict]:
		return PetMutable(self, self.__data).findall(query)

	def filter(self, query: dict) -> "PetMutable":
		return PetMutable(self, self.__data).filter(query)

	def map(self, func: Callable) -> "PetMutable":
		return PetMutable(self, self.__data).map(func)

	def sort(self, query: i_sort) -> "PetMutable":
		return PetMutable(self, self.__data).sort(query)

	def flat(self, query: str | int) -> "PetMutable":
		return PetMutable(self, self.__data).flat(query)

	def remove(self, query: i_remove = None) -> list[dict]:
		if query is None:
			return self.clear()
		removed = PetUtils.remove(self.__data, query)
		self.dump()
		return removed

	def clear(self):
		deleted = self.__data[:]
		self.__data.clear()
		return deleted

	def list(self):
		return self.__data[:]

	def size(self):
		return len(self.__data)

	def length(self):
		return self.size()

	def __iter__(self) -> Iterator[dict]:
		return iter(self.__data)

	def __getitem__(self, item) -> dict:
		return self.__data[item]

class PetMutable:

	def __init__(self, col: PetCollection, data: list[dict]):
		self.__col = col
		self.__mutated_data = data
		self.__mutations = []

	def __mutate(self):
		for mutation, args in self.__mutations:
			mutation(*args)
		self.__mutations.clear()

	def __iter__(self) -> Iterator[dict]:
		self.__mutate()
		return iter(self.__mutated_data)

	def __getitem__(self, item) -> dict:
		self.__mutate()
		return self.__mutated_data[item]

	def get(self, id: str) -> Optional[dict]:
		self.__mutate()
		for doc in self.__mutated_data:
			if doc["_id"] == id:
				return doc

	def find(self, query: dict) -> Optional[dict]:
		self.__mutate()
		for doc in self.__mutated_data:
			if PetUtils.match(doc, query):
				return doc

	def findall(self, query: dict) -> list[dict]:
		self.filter(query)
		self.__mutate()
		return self.__mutated_data[:]

	def filter(self, query: dict) -> Self:
		self.__mutations.append((self.__findall, (query,)))
		return self

	def map(self, func: Callable) -> Self:
		self.__mutations.append((self.__map, (func,)))
		return self

	def sort(self, query: i_sort = None, reverse=False) -> Self:
		self.__mutations.append((self.__sort, (query, reverse)))
		return self

	def flat(self, query: str | int) -> Self:
		self.__mutations.append((self.__flat, (query,)))
		return self

	def remove(self, query: i_remove = None) -> list[dict]:
		self.__mutate()
		if query is None:
			return self.clear()
		removed = PetUtils.remove(self.__mutated_data, query)
		self.__col.remove(removed)
		return removed

	def delete(self, query: i_remove = None) -> Self:
		self.remove(query)
		return self

	def clear(self):
		deleted = self.__col.remove(self.__mutated_data)
		self.__mutated_data = []
		return deleted

	def list(self):
		self.__mutate()
		return self.__mutated_data

	def size(self):
		self.__mutate()
		return len(self.__mutated_data)

	def length(self):
		return self.size()

	def __findall(self, query: dict):
		self.__mutated_data = [doc for doc in self.__mutated_data if PetUtils.match(doc, query)]

	def __map(self, func: Callable[[dict], Any]):
		self.__mutated_data = [func(doc) for doc in self.__mutated_data]

	def __sort(self, query: i_sort, reverse: bool):
		if isinstance(query, (str, int, NoneType)):
			query = [query]
		def key(doc):
			res = []
			for field in query:
				value = PetUtils.get(doc, field)
				res.append((value == NON_EXISTENT, value))
			return res
		self.__mutated_data.sort(key=query if isinstance(query, Callable) else key, reverse=reverse)

	def __flat(self, query: str | int):
		self.__mutated_data = [value for doc in self.__mutated_data
			if (value := PetUtils.get(doc, query)) != NON_EXISTENT]
