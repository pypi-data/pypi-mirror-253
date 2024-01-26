import os

from petdb.pcollection import PetCollection

class PetDB:

	def __init__(self, root: str):
		if not os.path.exists(root):
			raise Exception("Root directory does not exist")
		self.__root = os.path.join(root, "petstorage")
		os.mkdir(self.__root)
		self.__collections: dict[str, PetCollection] = {}
		self.__load_collections()

	def delete(self, name: str):
		if name not in self.__collections:
			return False
		self.__collections[name].clear()
		self.__collections.pop(name)
		os.remove(os.path.join(self.__root, f"{name}.json"))
		return True

	def create_collection(self, name: str) -> PetCollection:
		if name not in self.__collections:
			return self.__create_collection(name)
		return self.__collections[name]

	def __getattr__(self, name: str) -> PetCollection:
		return self.create_collection(name)

	def __getitem__(self, name: str) -> PetCollection:
		if not isinstance(name, str):
			raise TypeError("Name must be a string")
		return self.create_collection(name)

	def __load_collections(self):
		for file in os.listdir(self.__root):
			if not file.endswith(".json"):
				continue
			self.__collections[file.rsplit(".", 1)[0]] = PetCollection(os.path.join(self.__root, file))

	def __create_collection(self, name: str):
		self.__collections[name] = PetCollection(os.path.join(self.__root, f"{name}.json"))
		return self.__collections[name]
