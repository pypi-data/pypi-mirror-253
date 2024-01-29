import os
import json
import uuid
from copy import deepcopy
from types import NoneType
from typing import Optional, Iterator, Self, Callable

from petdb.pexceptions import QueryException
from petdb.putils import PetUtils, NON_EXISTENT
from petdb.ptypes import i_remove, i_sort

class PetCollection:
	"""Pet Collection

	Represents a documents organizer. Provides documents management methods.
	"""

	def __init__(self, path: str):
		self.__path = path
		self.name = os.path.basename(path).rsplit(".", 1)[0]
		if not os.path.exists(self.__path):
			with open(self.__path, "w") as f:
				f.write("[]")
		with open(self.__path, "r", encoding="utf-8") as f:
			self.__data: list[dict] = json.load(f)

	def dump(self) -> None:
		"""Dumps documents into a collection storage file"""
		with open(self.__path, "w", encoding="utf-8") as f:
			json.dump(self.__data, f, indent=4, ensure_ascii=False)

	def save(self) -> None:
		"""Dumps documents into a collection storage file"""
		self.dump()

	def insert(self, entry: dict | list[dict]) -> dict | list[dict]:
		"""Inserts a documents into the current collection. Generates identifiers."""
		if isinstance(entry, list):
			return [self.insert(doc) for doc in entry]
		if "_id" in entry and self.get(entry["_id"]):
			raise QueryException("Duplicate id")
		doc = deepcopy(entry)
		if "_id" not in doc:
			doc["_id"] = str(uuid.uuid4())
		self.__data.append(doc)
		self.dump()
		return doc

	def update(self, update_query: dict, query: str | dict | list[str | dict] = None) -> None:
		"""Applies update query to all documents that matches the given query"""
		if isinstance(query, str):
			PetUtils.update(self.get(query), deepcopy(update_query))
			self.dump()
			return
		if isinstance(query, list):
			if all(isinstance(item, str) for item in query):
				query = {"_id": {"$in": query}}
			elif all(isinstance(item, dict) for item in query):
				query = {"_id": {"$in": [doc["_id"] for doc in query]}}
			else:
				raise QueryException("Invalid query format: query list should contains only ids or only docs")
		for doc in self.findall(query or {}):
			PetUtils.update(doc, deepcopy(update_query))
		self.dump()

	def get(self, id: str) -> Optional[dict]:
		"""Search for a document with the given id"""
		return PetMutable(self, self.__data).get(id)

	def find(self, query: dict) -> Optional[dict]:
		"""Returns the first document that matches the given query"""
		return PetMutable(self, self.__data).find(query)

	def findall(self, query: dict) -> list[dict]:
		"""Returns all documents that matches the given query"""
		return PetMutable(self, self.__data).findall(query)

	def filter(self, query: dict) -> "PetMutable":
		"""Returns mutations object with the filter mutation. Accepts only query object."""
		return PetMutable(self, self.__data).filter(query)

	def map[TP](self, func: Callable[[dict], TP]) -> "PetArray[TP]":
		"""Returns mutations object with the map mutation. Accepts only callable object."""
		return PetArray[TP](self.__data).map(func)

	def sort(self, query: i_sort) -> "PetMutable":
		"""Returns mutations object with the sort mutation. Accepts path, list of paths and sorting function."""
		return PetMutable(self, self.__data).sort(query)

	def flat[TP](self, query: str | int) -> "PetArray[TP]":
		"""Returns mutations object with the flat mutation. Accepts only path."""
		return PetArray[TP](self.__data).flat(query)

	def remove(self, query: i_remove = None) -> list[dict]:
		"""Removes matched documents. Accepts id, query object, list of ids and list of documents.
		Performs clearing if the query is None. Returns removed documents.
		"""
		if query is None:
			return self.clear()
		removed = PetUtils.remove(self.__data, query)
		self.dump()
		return removed

	def clear(self) -> list[dict]:
		"""Removes all documents from the collection. Returns removed documents."""
		deleted = self.__data[:]
		self.__data.clear()
		self.dump()
		return deleted

	def list(self) -> list[dict]:
		"""Returns all documents as a list"""
		return self.__data[:]

	def size(self) -> int:
		"""Returns the amount of all documents in the collection"""
		return len(self.__data)

	def length(self) -> int:
		"""Returns the amount of all documents in the collection"""
		return self.size()

	def __iter__(self) -> Iterator[dict]:
		return iter(self.__data)

	def __getitem__(self, item) -> dict:
		return self.__data[item]

class PetArray[T]:

	def __init__(self, data: list[T]):
		self._mutated_data: list[T] = data

	def __iter__(self) -> Iterator[T]:
		return iter(self._mutated_data)

	def __getitem__(self, item) -> T:
		return self._mutated_data[item]

	def update(self, update_query: dict, query: str | dict = None) -> None:
		"""Applies update query to all elements that matches the given query"""
		for doc in self.findall(query):
			PetUtils.update(doc, deepcopy(update_query))

	def find(self, query: dict) -> Optional[T]:
		"""Returns the first document that matches the given query"""
		for doc in self._mutated_data:
			if PetUtils.match(doc, query):
				return doc

	def findall(self, query: dict) -> list[T]:
		"""Returns all documents that matches the given query"""
		self.filter(query)
		return self._mutated_data[:]

	def filter(self, query: dict) -> Self:
		"""Perform filter mutation. Accepts only query object."""
		self._mutated_data = [doc for doc in self._mutated_data if PetUtils.match(doc, query)]
		return self

	def map[TP](self, func: Callable[[T], TP]) -> "PetArray[TP]":
		"""Perform map mutation. Accepts only callable object."""
		self._mutated_data: list[TP] = [func(doc) for doc in self._mutated_data]
		return self

	def sort(self, query: i_sort = None, reverse=False) -> Self:
		"""Perform sort mutation. Accepts path, list of paths and sorting function."""
		if isinstance(query, (str, int, NoneType)):
			query = [query]

		def key(doc):
			res = []
			for field in query:
				value = PetUtils.get(doc, field)
				res.append((value == NON_EXISTENT, value))
			return res

		self._mutated_data.sort(key=query if isinstance(query, Callable) else key, reverse=reverse)
		return self

	def flat[TP](self, query: str | int) -> "PetArray[TP]":
		"""Perform flat mutation. Accepts only path."""
		self._mutated_data: list[TP] = [value for doc in self._mutated_data
			if (value := PetUtils.get(doc, query)) != NON_EXISTENT]
		return self

	def clear(self) -> list[T]:
		deleted = self._mutated_data[:]
		self._mutated_data.clear()
		return deleted

	def list(self) -> list[T]:
		"""Returns all documents after all mutations as a list"""
		return self._mutated_data[:]

	def size(self) -> int:
		"""Returns the amount of all documents in the mutated collection"""
		return len(self._mutated_data)

	def length(self) -> int:
		"""Returns the amount of all documents in the mutated collection"""
		return self.size()

class PetMutable(PetArray[dict]):

	def __init__(self, col: PetCollection, data: list[dict]):
		super().__init__(data)
		self.__col = col

	def get(self, id: str) -> Optional[dict]:
		"""Search for a document with the given id"""
		for doc in self._mutated_data:
			if doc["_id"] == id:
				return doc

	def update(self, update_query: dict, query: str | dict = None) -> None:
		"""Applies update query to all documents in mutated list
		that matches the given query, affects the original collection"""
		if isinstance(query, str):
			if self.get(query) is not None:
				return self.__col.update(update_query, query)
		self.__col.update(update_query, {"_id": {"$in": [doc["_id"] for doc in self.findall(query)]}})

	def remove(self, query: i_remove = None) -> list[dict]:
		"""Removes matched documents, affects the original collection.
		Accepts id, query object, list of ids and list of documents.
		Performs clearing if the query is None. Returns removed documents.
		"""
		if query is None:
			return self.clear()
		removed = PetUtils.remove(self._mutated_data, query)
		self.__col.remove(removed)
		return removed

	def delete(self, query: i_remove = None) -> Self:
		"""Calls the remove method and returns self"""
		self.remove(query)
		return self

	def clear(self) -> list[dict]:
		"""Removes all documents from mutated collection, affects the original collection. Returns removed documents."""
		deleted = self.__col.remove(self._mutated_data)
		self._mutated_data = []
		return deleted

	def map[TP](self, func: Callable[[dict], TP]) -> PetArray[TP]:
		return PetArray[TP](self._mutated_data).map(func)

	def flat[TP](self, query: str | int) -> PetArray[TP]:
		return PetArray[TP](self._mutated_data).flat(query)
