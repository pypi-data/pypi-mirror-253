import os
import json
import uuid
from typing import Optional, Iterator, Self

from petdb.putils import PetUtils

type i_find = str | dict
type i_remove = str | dict | list[str | dict]

class PetCollection:

	def __init__(self, path: str):
		self.__path = path
		self.name = os.path.basename(path).rsplit(".", 1)[0]
		if not os.path.exists(self.__path):
			with open(self.__path, "w") as f:
				f.write("[]")
		with open(self.__path, "r", encoding="utf-8") as f:
			self.data: list[dict] = json.load(f)

	def dump(self):
		with open(self.__path, "w", encoding="utf-8") as f:
			json.dump(self.data, f, indent=4, ensure_ascii=False)

	def insert(self, doc):
		if "_id" in doc and self.get(doc["_id"]):
			raise Exception("Duplicate id")
		if "_id" not in doc:
			doc["_id"] = str(uuid.uuid4())
		self.data.append(doc)
		self.dump()
		return doc

	def get(self, id: str) -> Optional[dict]:
		return PetMutable(self).get(id)

	def find(self, query: i_find) -> Optional[dict]:
		return PetMutable(self).find(query)

	def findall(self, query: i_find) -> "PetMutable":
		return PetMutable(self).findall(query)

	def filter(self, query: i_find) -> "PetMutable":
		return PetMutable(self).filter(query)

	def remove(self, query: i_remove = None) -> list[dict]:
		if query is None:
			return self.clear()
		return PetUtils.remove(self.data, query)

	def delete(self, query: i_remove = None) -> Self:
		self.remove(query)
		return self

	def clear(self):
		deleted = self.data[:]
		self.data.clear()
		return deleted

	def list(self):
		return self.data[:]

	def __iter__(self) -> Iterator[dict]:
		return iter(self.data)

class PetMutable:

	def __init__(self, col: PetCollection):
		self.__col = col
		self.__mutations = []
		self.__mutated_data = self.__col.data[:]

	def __mutate(self):
		for mutation, args, kwargs in self.__mutations:
			mutation(*args, **kwargs)
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

	def find(self, query: i_find) -> Optional[dict]:
		self.__mutate()
		if isinstance(query, str):
			query = {"_id": query}
		for doc in self.__mutated_data:
			if PetUtils.match(doc, query):
				return doc

	def findall(self, query: i_find) -> Self:
		if isinstance(query, str):
			query = {"_id": query}
		self.__mutations.append((self.__findall, (query,), {}))
		return self

	def filter(self, query: i_find) -> Self:
		return self.findall(query)

	def remove(self, query: i_remove = None) -> list[dict]:
		self.__mutate()
		if query is None:
			return self.clear()
		deleted = PetUtils.remove(self.__mutated_data, query)
		self.__col.remove(deleted)
		return deleted

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

	def __findall(self, query: dict):
		self.__mutated_data = [doc for doc in self.__mutated_data if PetUtils.match(doc, query)]
