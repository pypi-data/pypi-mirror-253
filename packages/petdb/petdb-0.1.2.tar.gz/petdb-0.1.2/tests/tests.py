import os
import json
import shutil
import traceback
import uuid
from typing import Callable

from termcolor import colored

from petdb import PetDB, PetCollection

TEST_COLLECTION_NAME = "testcol"

class Tests:

	root: str
	db: PetDB
	col: PetCollection
	sets: list[Callable] = []
	tests: list = []

	@classmethod
	def init(cls):
		cls.root = os.path.join(os.getcwd(), "testdb")
		if os.path.exists(cls.root):
			shutil.rmtree(cls.root)
		os.mkdir(cls.root)
		cls.db = PetDB(cls.root)

	@classmethod
	def setup(cls, init: list, ignore_id: bool):
		cls.db.delete(TEST_COLLECTION_NAME)
		if not ignore_id:
			for doc in init:
				if "_id" not in doc:
					doc["_id"] = str(uuid.uuid4())
		with open(os.path.join(cls.root, "petstorage", f"{TEST_COLLECTION_NAME}.json"), "w") as f:
			json.dump(init, f)
		cls.col = cls.db.create_collection(TEST_COLLECTION_NAME)

	@classmethod
	def run(cls):
		for testset in cls.sets:
			testset()
		failed = []
		for i, test in enumerate(cls.tests, 1):
			try:
				cls.setup(test["init"], test["ignore_id"])
				result = test["func"](cls.col)
				if not test["ignore_id"]:
					cls.remove_ids(result)
					cls.remove_ids(test["expect"])
				if result == test["expect"]:
					print(f"Test {i}: passed")
				else:
					message = f"Test {i} ({test["name"]}): failed (expected {test["expect"]}, got {result})"
					failed.append(message)
					print(colored(message, "red"))
			except Exception:
				message = f"Exception raised during Test {i} ({test["name"]}):\n{traceback.format_exc()}"
				print(message)
				failed.append(message)
		shutil.rmtree(cls.root)
		return failed

	@classmethod
	def remove_ids(cls, entry):
		if isinstance(entry, dict):
			entry.pop("_id", None)
		elif isinstance(entry, list) and len(entry) > 0 and isinstance(entry[0], dict):
			for doc in entry:
				doc.pop("_id", None)

def test(init=None, expect=None, ignore_id: bool = False, init_expectation: bool = True):
	if init is None and expect and init_expectation:
		if isinstance(expect, dict):
			init = [expect]
		elif isinstance(expect, list):
			init = expect[:]
	def decorator(func):
		Tests.tests.append({
			"func": func,
			"init": init or [],
			"expect": expect,
			"ignore_id": ignore_id,
			"name": func.__name__})
	return decorator

def testset(func):
	Tests.sets.append(func)

# BASE

@testset
def base():

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}], expect=[{"a": 1}, {"a": 2}, {"a": 3}])
	def collection_to_list(col: PetCollection):
		return list(col)

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}], expect=[{"a": 1}, {"a": 2}, {"a": 3}])
	def iteration1(col: PetCollection):
		result = []
		for doc in col:
			result.append(doc)
		return result

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}], expect=[1, 2, 3])
	def iteration2(col: PetCollection):
		result = []
		for doc in col:
			result.append(doc["a"])
		return result

# INSERT

@testset
def insertion():

	@test(expect=[{"a": 5}], init_expectation=False)
	def insert_one(col: PetCollection):
		col.insert({"a": 5})
		return list(col)

	@test(expect=[{"a": 1}, {"a": 2}, {"a": 3}], init_expectation=False)
	def insert_many(col: PetCollection):
		col.insert({"a": 1})
		col.insert({"a": 2})
		col.insert({"a": 3})
		return list(col)

	@test(expect=True)
	def id_generation(col: PetCollection):
		doc1 = col.insert({"a": 1})
		doc2 = col.insert({"a": 2})
		return ("_id" in doc1 and len(doc1["_id"]) > 8
				and "_id" in doc2 and len(doc2["_id"]) > 8
				and doc1["_id"] != doc2["_id"])

	@test(expect=[{"a": 5}], init_expectation=False)
	def dump_on_insert(col: PetCollection):
		col.insert({"a": 5})
		with open(os.path.join(Tests.root, "petstorage", f"{TEST_COLLECTION_NAME}.json")) as f:
			return json.load(f)

# SELECTION

@testset
def selection():

	@test(expect={"a": 1}, init_expectation=False)
	def get_by_id1(col: PetCollection):
		doc_id = col.insert({"a": 1})["_id"]
		return col.get(doc_id)

	@test(expect=None)
	def get_by_id2(col: PetCollection):
		return col.get("12345")

	@test(expect={"a": 1}, init_expectation=False)
	def find_by_id1(col: PetCollection):
		doc_id = col.insert({"a": 1})["_id"]
		return col.find(doc_id)

	@test(expect={"a": 5, "b": 10})
	def find1(col: PetCollection):
		return col.find({"a": 5})

	@test(init=[{"a": 5, "b": 10}], expect=None)
	def find2(col: PetCollection):
		return col.find({"a": 10})

	@test(expect={"a": 5, "b": 10, "c": 20})
	def find3(col: PetCollection):
		return col.find({"a": 5, "c": 20})

	@test(expect={"a": 5, "b": 10, "c": {"d": 20}})
	def find4(col: PetCollection):
		return col.find({"a": 5, "c.d": 20})

	@test(expect={"a": 5, "b": 10, "c": {"d": 20}})
	def find5(col: PetCollection):
		return col.find({"a": 5, "c": {"d": 20}})

	@test(expect={"a": 5, "b": 10, "c": {"d": {"e": 20}}})
	def find6(col: PetCollection):
		return col.find({"a": 5, "c": {"d.e": 20}})

	@test(expect={"a": 5, "b": 10, "c": {"d": {"e": 20}}})
	def find6(col: PetCollection):
		return col.find({"a": 5, "c.d": {"e": 20}})

	@test(expect={"a": 5, "b": 10, "c": {"d": {"e": 20}}})
	def find6(col: PetCollection):
		return col.find({"a": 5, "c": {"d": {"e": 20}}})

	@test(expect=[{"a": 5, "b": 1, "c": 3}, {"a": 6, "b": 1}, {"a": 7, "b": 1}])
	def findall1(col: PetCollection):
		return col.findall({})

	@test(expect=[{"a": 5, "b": 1, "c": 3}, {"a": 6, "b": 1}, {"a": 7, "b": 1}])
	def findall1(col: PetCollection):
		return list(col.findall({}))

	@test(init=[{"a": 5, "c": 3}, {"a": 6, "b": 1}, {"a": 7, "b": 1}], expect=[{"a": 6, "b": 1}, {"a": 7, "b": 1}])
	def findall1(col: PetCollection):
		return col.findall({"b": 1})

	@test(init=[{"a": 5, "b": 2, "c": 3}, {"a": 6, "b": 1}, {"a": 7, "b": 1}], expect=[{"a": 6, "b": 1}, {"a": 7, "b": 1}])
	def findall1(col: PetCollection):
		return col.findall({"b": 1})

	@test(init=[{"a": 5, "b": 2, "c": 3}, {"a": 6, "b": 1}, {"a": 7, "b": 1}], expect=[])
	def findall1(col: PetCollection):
		return col.findall({"b": 3})

# OPERATORS

@testset
def operations():

	@test(expect={"a": 5, "b": 10})
	def eq1(col: PetCollection):
		return col.find({"a": {"$eq": 5}})

	@test(init=[{"a": 5, "b": 10}], expect=None)
	def eq2(col: PetCollection):
		return col.find({"a": {"$eq": 50}})

	@test(expect={"a": 5, "b": 10})
	def not1(col: PetCollection):
		return col.find({"a": {"$not": 1}})

	@test(init=[{"a": 5, "b": 10}], expect=None)
	def not2(col: PetCollection):
		return col.find({"a": {"$not": 5}})

	@test(expect={"a": 5, "b": 10})
	def ne1(col: PetCollection):
		return col.find({"a": {"$ne": 1}})

	@test(init=[{"a": 5, "b": 10}], expect=None)
	def ne2(col: PetCollection):
		return col.find({"a": {"$ne": 5}})

	@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[{"a": 1, "b": 0}])
	def lt(col: PetCollection):
		return col.findall({"a": {"$lt": 5}})

	@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[{"a": 5, "b": 10}, {"a": 1, "b": 0}])
	def lte(col: PetCollection):
		return col.findall({"a": {"$lte": 5}})

	@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[{"a": 10, "b": 5}])
	def gt(col: PetCollection):
		return col.findall({"a": {"$gt": 5}})

	@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[{"a": 5, "b": 10}, {"a": 10, "b": 5}])
	def gte(col: PetCollection):
		return col.findall({"a": {"$gte": 5}})

	@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[{"a": 5, "b": 10}])
	def gt_an_lt(col: PetCollection):
		return col.findall({"a": {"$gt": 3, "$lt": 7}})

	@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[{"a": 5, "b": 10}])
	def in1(col: PetCollection):
		return col.findall({"a": {"$in": [4, 5, 6]}})

	@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[])
	def in2(col: PetCollection):
		return col.findall({"a": {"$in": [4, 6]}})

	@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[{"a": 10, "b": 5}])
	def nin1(col: PetCollection):
		return col.findall({"a": {"$nin": [1, 4, 5, 6]}})

	@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[])
	def nin2(col: PetCollection):
		return col.findall({"a": {"$nin": [1, 4, 5, 6, 10]}})

	@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[{"a": 10, "b": 5}])
	def notin1(col: PetCollection):
		return col.findall({"a": {"$notin": [1, 4, 5, 6]}})

	@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[])
	def notin2(col: PetCollection):
		return col.findall({"a": {"$notin": [1, 4, 5, 6, 10]}})

	@test(expect=[{"a": 5}])
	def exists1(col: PetCollection):
		return col.findall({"a": {"$exists": True}})

	@test(init=[{"a": 5}], expect=[])
	def exists2(col: PetCollection):
		return col.findall({"b": {"$exists": True}})

	@test(init=[{"a": 5}, {"a": 6}, {"b": 10}], expect=[{"a": 5}, {"a": 6}])
	def exists3(col: PetCollection):
		return col.findall({"a": {"$exists": True}})

	@test(init=[{"a": 5}, {"a": 6}, {"b": 10}], expect=[{"b": 10}])
	def exists4(col: PetCollection):
		return col.findall({"a": {"$exists": False}})

	@test(expect=[{"a": 5}, {"a": 6}, {"b": 10}])
	def exists5(col: PetCollection):
		return col.findall({"a.b": {"$exists": False}})

	@test(init=[{"a": 5}, {"a": 6}, {"b": 10}], expect=[])
	def exists6(col: PetCollection):
		return col.findall({"a.b": {"$exists": True}})

	@test(expect=[{"a": "12345"}, {"a": "67890"}])
	def regex1(col: PetCollection):
		return col.findall({"a": {"$regex": "\\d{5}"}})

	@test(init=[{"a": "12345"}, {"a": "67890"}], expect=[])
	def regex2(col: PetCollection):
		return col.findall({"a": {"$regex": "\\D{5}"}})

	@test(init=[{"a": "12345"}, {"a": "678901"}], expect=[{"a": "12345"}])
	def regex3(col: PetCollection):
		return col.findall({"a": {"$regex": "^1"}})

	@test(init=[{"a": "12345"}, {"a": "678901"}], expect=[{"a": "12345"}])
	def regex4(col: PetCollection):
		return col.findall({"a": {"$regex": "5$"}})

	@test(init=[{"a": "12345"}, {"a": "abcde"}, {"a": 12345}], expect=[{"a": "12345"}])
	def func1(col: PetCollection):
		return col.findall({"a": {"$func": str.isdigit}})

# DELETION

@testset
def deletion():

	@test(init=[{"a": 5}, {"b": 2}, {"b": 3}], expect=[])
	def remove1(col: PetCollection):
		col.remove({})
		return col.list()

	@test(expect=[{"a": 5}, {"b": 2}, {"b": 3}])
	def remove2(col: PetCollection):
		return col.remove({})

	@test(expect=[], init=[{"a": 5}, {"b": 2}, {"b": 3}])
	def remove3(col: PetCollection):
		col.remove()
		return col.list()

	@test(expect=[{"a": 5}, {"b": 2}, {"b": 3}])
	def remove4(col: PetCollection):
		return col.remove()

	@test(expect=[{"a": 5}, {"b": 2}], init=[{"a": 5}, {"b": 2}, {"b": 3}])
	def remove5(col: PetCollection):
		col.remove({"b": 3})
		return col.list()

	@test(expect=[{"b": 2}], init=[{"a": 5}, {"b": 2}, {"b": 3}])
	def remove6(col: PetCollection):
		return col.remove({"b": 2})

# MUTABLE BASE

@testset
def mutable_base():

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}], expect=[{"a": 1}, {"a": 2}, {"a": 3}])
	def collection_to_list(col: PetCollection):
		return list(col.filter({}))

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}], expect=[{"a": 1}, {"a": 2}, {"a": 3}])
	def iteration1(col: PetCollection):
		result = []
		for doc in col.filter({}):
			result.append(doc)
		return result

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}], expect=[1, 2, 3])
	def iteration2(col: PetCollection):
		result = []
		for doc in col.filter({}):
			result.append(doc["a"])
		return result

# MUTABLE DELETION

@testset
def mutable_deletion():

	@test(init=[{"a": 5, "c": 10}, {"a": 5, "c": 1}, {"a": 1, "c": 10}, {"a": 55, "c": 1}],
		expect=[{"a": 5, "c": 10}, {"a": 5, "c": 1}])
	def mutable_remove1(col: PetCollection):
		return col.filter({"a": 5}).remove()

	@test(init=[{"a": 5, "c": 10}, {"a": 5, "c": 1}, {"a": 1, "c": 10}, {"a": 55, "c": 1}],
		expect=[{"a": 1, "c": 10}, {"a": 55, "c": 1}])
	def mutable_remove2(col: PetCollection):
		col.filter({"a": 5}).remove()
		return col.list()

# MUTABLE SELECTION

@testset
def mutable_selection():

	@test(init=[{"a": 2}, {"a": 3}], expect={"a": 1})
	def mutable_get_by_id1(col: PetCollection):
		doc_id = col.insert({"a": 1})["_id"]
		return col.filter({}).get(doc_id)

	@test(expect=None)
	def mutable_get_by_id2(col: PetCollection):
		return col.filter({}).get("12345")

	@test(expect={"a": 1}, init_expectation=False)
	def mutable_find_by_id1(col: PetCollection):
		doc_id = col.insert({"a": 1})["_id"]
		return col.filter({}).find(doc_id)

	@test(expect={"a": 5, "b": 10})
	def mutable_find1(col: PetCollection):
		return col.filter({}).find({"a": 5})

	@test(init=[{"a": 5, "b": 10}], expect=None)
	def mutable_find2(col: PetCollection):
		return col.filter({}).find({"a": 10})

	@test(expect={"a": 5, "b": 10, "c": 20})
	def mutable_find3(col: PetCollection):
		return col.filter({}).find({"a": 5, "c": 20})

	@test(expect={"a": 5, "b": 10, "c": {"d": 20}})
	def mutable_find4(col: PetCollection):
		return col.filter({}).find({"a": 5, "c.d": 20})

	@test(expect={"a": 5, "b": 10, "c": {"d": 20}})
	def mutable_find5(col: PetCollection):
		return col.filter({}).find({"a": 5, "c": {"d": 20}})

	@test(expect={"a": 5, "b": 10, "c": {"d": {"e": 20}}})
	def mutable_find6(col: PetCollection):
		return col.filter({}).find({"a": 5, "c": {"d.e": 20}})

	@test(expect={"a": 5, "b": 10, "c": {"d": {"e": 20}}})
	def mutable_find6(col: PetCollection):
		return col.filter({}).find({"a": 5, "c.d": {"e": 20}})

	@test(expect={"a": 5, "b": 10, "c": {"d": {"e": 20}}})
	def mutable_find6(col: PetCollection):
		return col.filter({}).find({"a": 5, "c": {"d": {"e": 20}}})

if __name__ == '__main__':
	print("Running tests...\n")
	Tests.init()
	failed = Tests.run()
	if len(failed) == 0:
		print(colored("\nAll tests passed", "green"))
	else:
		print(colored(f"\nTests failed:\n{"\n".join(failed)}", "red"))
