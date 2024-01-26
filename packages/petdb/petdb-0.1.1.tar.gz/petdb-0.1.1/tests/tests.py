import os
import json
import shutil
import traceback
import uuid

from termcolor import colored

from petdb import PetDB, PetCollection

TEST_COLLECTION_NAME = "testcol"

class Tests:

	root: str
	db: PetDB
	col: PetCollection
	tests: list = []

	@classmethod
	def init(cls):
		cls.root = os.path.join(os.getcwd(), "testdb")
		if os.path.exists(cls.root):
			shutil.rmtree(cls.root)
		os.mkdir(cls.root)
		cls.db = PetDB(cls.root)

	@classmethod
	def setup(cls, init: list, generate_id: bool):
		cls.db.delete(TEST_COLLECTION_NAME)
		if generate_id:
			for doc in init:
				doc["_id"] = str(uuid.uuid4())
		with open(os.path.join(cls.root, "petstorage", f"{TEST_COLLECTION_NAME}.json"), "w") as f:
			json.dump(init, f)
		cls.col = cls.db.create_collection(TEST_COLLECTION_NAME)

	@classmethod
	def run(cls):
		failed = []
		for i, test in enumerate(cls.tests):
			try:
				cls.setup(test["init"], test["generate_id"])
				result = test["func"](cls.col)
				if test["remove_id"]:
					if isinstance(result, list):
						for doc in result:
							doc.pop("_id", None)
					elif isinstance(result, dict):
						result.pop("_id", None)
					if isinstance(test["expect"], list):
						for doc in test["expect"]:
							doc.pop("_id", None)
					elif isinstance(test["expect"], dict):
						test["expect"].pop("_id", None)
				if result == test["expect"]:
					print(f"Test {i}: passed")
				else:
					failed.append(test["name"])
					print(colored(f"Test {i} ({test["name"]}): failed (expected {test["expect"]}, got {result})", "red"))
			except Exception:
				print(f"Exception raised during Test {i} ({test["name"]}):")
				print(traceback.format_exc())
				failed.append(test["name"])
				continue
		shutil.rmtree(cls.root)
		return failed

def test(init=None, expect=None, remove_id: bool = False, generate_id: bool = False, init_expecting: bool = False):
	if init is None and expect and init_expecting:
		init = expect if isinstance(expect, list) else [expect]
	def decorator(func):
		Tests.tests.append({
			"func": func,
			"init": init or [],
			"expect": expect,
			"remove_id": remove_id,
			"generate_id": generate_id,
			"name": func.__name__})
	return decorator

# BASE

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

@test(expect=[{"a": 5}], remove_id=True)
def insert_one(col: PetCollection):
	col.insert({"a": 5})
	return list(col)

@test(expect=[{"a": 1}, {"a": 2}, {"a": 3}], remove_id=True)
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

@test(expect=[{"a": 5}], remove_id=True)
def dump_on_insert(col: PetCollection):
	col.insert({"a": 5})
	with open(os.path.join(Tests.root, "petstorage", f"{TEST_COLLECTION_NAME}.json")) as f:
		return json.load(f)

# SELECTION

@test(expect={"a": 1}, remove_id=True)
def get_by_id1(col: PetCollection):
	doc_id = col.insert({"a": 1})["_id"]
	return col.get(doc_id)

@test(expect=None)
def get_by_id2(col: PetCollection):
	return col.get("12345")

@test(expect={"a": 1}, remove_id=True)
def find_by_id1(col: PetCollection):
	doc_id = col.insert({"a": 1})["_id"]
	return col.find(doc_id)

@test(expect={"a": 5, "b": 10}, init_expecting=True, remove_id=True)
def find1(col: PetCollection):
	return col.find({"a": 5})

@test(init=[{"a": 5, "b": 10}], expect=None)
def find2(col: PetCollection):
	return col.find({"a": 10})

@test(expect={"a": 5, "b": 10, "c": 20}, init_expecting=True, remove_id=True)
def find3(col: PetCollection):
	return col.find({"a": 5, "c": 20})

@test(expect={"a": 5, "b": 10, "c": {"d": 20}}, init_expecting=True, remove_id=True)
def find4(col: PetCollection):
	return col.find({"a": 5, "c.d": 20})

@test(expect={"a": 5, "b": 10, "c": {"d": 20}}, init_expecting=True, remove_id=True)
def find5(col: PetCollection):
	return col.find({"a": 5, "c": {"d": 20}})

@test(expect={"a": 5, "b": 10, "c": {"d": {"e": 20}}}, init_expecting=True, remove_id=True)
def find6(col: PetCollection):
	return col.find({"a": 5, "c": {"d.e": 20}})

@test(expect={"a": 5, "b": 10, "c": {"d": {"e": 20}}}, init_expecting=True, remove_id=True)
def find6(col: PetCollection):
	return col.find({"a": 5, "c.d": {"e": 20}})

@test(expect={"a": 5, "b": 10, "c": {"d": {"e": 20}}}, init_expecting=True, remove_id=True)
def find6(col: PetCollection):
	return col.find({"a": 5, "c": {"d": {"e": 20}}})

@test(expect=[{"a": 5, "b": 1, "c": 3}, {"a": 6, "b": 1}, {"a": 7, "b": 1}],
	init_expecting=True, remove_id=True)
def findall1(col: PetCollection):
	return col.findall({}).list()

@test(expect=[{"a": 5, "b": 1, "c": 3}, {"a": 6, "b": 1}, {"a": 7, "b": 1}],
	init_expecting=True, remove_id=True)
def findall1(col: PetCollection):
	return list(col.findall({}))

@test(expect=[{"a": 6, "b": 1}, {"a": 7, "b": 1}],
	init=[{"a": 5, "c": 3}, {"a": 6, "b": 1}, {"a": 7, "b": 1}],
	remove_id=True)
def findall1(col: PetCollection):
	return col.findall({"b": 1}).list()

@test(expect=[{"a": 6, "b": 1}, {"a": 7, "b": 1}],
	init=[{"a": 5, "b": 2, "c": 3}, {"a": 6, "b": 1}, {"a": 7, "b": 1}],
	remove_id=True)
def findall1(col: PetCollection):
	return col.findall({"b": 1}).list()

@test(expect=[], init=[{"a": 5, "b": 2, "c": 3}, {"a": 6, "b": 1}, {"a": 7, "b": 1}], remove_id=True)
def findall1(col: PetCollection):
	return col.findall({"b": 3}).list()

# OPERATORS

@test(expect={"a": 5, "b": 10}, init_expecting=True, remove_id=True)
def eq1(col: PetCollection):
	return col.find({"a": {"$eq": 5}})

@test(init=[{"a": 5, "b": 10}], expect=None, remove_id=True)
def eq2(col: PetCollection):
	return col.find({"a": {"$eq": 50}})

@test(expect={"a": 5, "b": 10}, init_expecting=True, remove_id=True)
def not1(col: PetCollection):
	return col.find({"a": {"$not": 1}})

@test(init=[{"a": 5, "b": 10}], expect=None, remove_id=True)
def not2(col: PetCollection):
	return col.find({"a": {"$not": 5}})

@test(expect={"a": 5, "b": 10}, init_expecting=True, remove_id=True)
def ne1(col: PetCollection):
	return col.find({"a": {"$ne": 1}})

@test(init=[{"a": 5, "b": 10}], expect=None, remove_id=True)
def ne2(col: PetCollection):
	return col.find({"a": {"$ne": 5}})

@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[{"a": 5, "b": 10}],
	init_expecting=True, remove_id=True)
def in1(col: PetCollection):
	return col.findall({"a": {"$in": [4, 5, 6]}}).list()

@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[],
	init_expecting=True, remove_id=True)
def in2(col: PetCollection):
	return col.findall({"a": {"$in": [4, 6]}}).list()

@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[{"a": 10, "b": 5}],
	init_expecting=True, remove_id=True)
def nin1(col: PetCollection):
	return col.findall({"a": {"$nin": [1, 4, 5, 6]}}).list()

@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[],
	init_expecting=True, remove_id=True)
def nin2(col: PetCollection):
	return col.findall({"a": {"$nin": [1, 4, 5, 6, 10]}}).list()

@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[{"a": 10, "b": 5}],
	init_expecting=True, remove_id=True)
def notin1(col: PetCollection):
	return col.findall({"a": {"$notin": [1, 4, 5, 6]}}).list()

@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[],
	init_expecting=True, remove_id=True)
def notin2(col: PetCollection):
	return col.findall({"a": {"$notin": [1, 4, 5, 6, 10]}}).list()

@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[{"a": 1, "b": 0}],
	init_expecting=True, remove_id=True)
def lt(col: PetCollection):
	return col.findall({"a": {"$lt": 5}}).list()

@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[{"a": 5, "b": 10}, {"a": 1, "b": 0}],
	init_expecting=True, remove_id=True)
def lte(col: PetCollection):
	return col.findall({"a": {"$lte": 5}}).list()

@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[{"a": 10, "b": 5}],
	init_expecting=True, remove_id=True)
def gt(col: PetCollection):
	return col.findall({"a": {"$gt": 5}}).list()

@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[{"a": 5, "b": 10}, {"a": 10, "b": 5}],
	init_expecting=True, remove_id=True)
def gte(col: PetCollection):
	return col.findall({"a": {"$gte": 5}}).list()

@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[{"a": 5, "b": 10}],
	init_expecting=True, remove_id=True)
def gt_an_lt(col: PetCollection):
	return col.findall({"a": {"$gt": 3, "$lt": 7}}).list()

# DELETION

@test(expect=[], init=[{"a": 5}, {"b": 2}, {"b": 3}])
def remove1(col: PetCollection):
	col.remove({})
	return col.list()

@test(expect=[{"a": 5}, {"b": 2}, {"b": 3}], init_expecting=True, remove_id=True)
def remove2(col: PetCollection):
	return col.remove({})

@test(expect=[], init=[{"a": 5}, {"b": 2}, {"b": 3}])
def remove3(col: PetCollection):
	col.remove()
	return col.list()

@test(expect=[{"a": 5}, {"b": 2}, {"b": 3}], init_expecting=True, remove_id=True)
def remove4(col: PetCollection):
	return col.remove()

@test(expect=[{"a": 5}, {"b": 2}], init=[{"a": 5}, {"b": 2}, {"b": 3}], init_expecting=True, remove_id=True)
def remove5(col: PetCollection):
	col.remove({"b": 3})
	return col.list()

@test(expect=[{"b": 2}], init=[{"a": 5}, {"b": 2}, {"b": 3}], init_expecting=True, remove_id=True)
def remove6(col: PetCollection):
	return col.remove({"b": 2})

# MUTABLE BASE

@test(init=[{"a": 1}, {"a": 2}, {"a": 3}], expect=[{"a": 1}, {"a": 2}, {"a": 3}])
def collection_to_list(col: PetCollection):
	return list(col.findall({}))

@test(init=[{"a": 1}, {"a": 2}, {"a": 3}], expect=[{"a": 1}, {"a": 2}, {"a": 3}])
def iteration1(col: PetCollection):
	result = []
	for doc in col.findall({}):
		result.append(doc)
	return result

@test(init=[{"a": 1}, {"a": 2}, {"a": 3}], expect=[1, 2, 3])
def iteration2(col: PetCollection):
	result = []
	for doc in col.findall({}):
		result.append(doc["a"])
	return result

# MUTABLE DELETION

@test(expect=[{"a": 5, "c": 10}, {"a": 5, "c": 1}],
	init=[{"a": 5, "c": 10}, {"a": 5, "c": 1}, {"a": 1, "c": 10}, {"a": 55, "c": 1}],
	remove_id=True, generate_id=True)
def mutable_remove1(col: PetCollection):
	return col.filter({"a": 5}).remove()

@test(expect=[{"a": 1, "c": 10}, {"a": 55, "c": 1}],
	init=[{"a": 5, "c": 10}, {"a": 5, "c": 1}, {"a": 1, "c": 10}, {"a": 55, "c": 1}],
	remove_id=True, generate_id=True)
def mutable_remove2(col: PetCollection):
	col.filter({"a": 5}).remove()
	return col.list()

# SELECTION

@test(init=[{"a": 2}, {"a": 3}], expect={"a": 1}, remove_id=True, generate_id=True)
def mutable_get_by_id1(col: PetCollection):
	doc_id = col.insert({"a": 1})["_id"]
	return col.findall({}).get(doc_id)

@test(expect=None)
def mutable_get_by_id2(col: PetCollection):
	return col.findall({}).get("12345")

@test(expect={"a": 1}, remove_id=True)
def mutable_find_by_id1(col: PetCollection):
	doc_id = col.insert({"a": 1})["_id"]
	return col.findall({}).find(doc_id)

@test(expect={"a": 5, "b": 10}, init_expecting=True, remove_id=True)
def mutable_find1(col: PetCollection):
	return col.findall({}).find({"a": 5})

@test(init=[{"a": 5, "b": 10}], expect=None)
def mutable_find2(col: PetCollection):
	return col.findall({}).find({"a": 10})

@test(expect={"a": 5, "b": 10, "c": 20}, init_expecting=True, remove_id=True)
def mutable_find3(col: PetCollection):
	return col.findall({}).find({"a": 5, "c": 20})

@test(expect={"a": 5, "b": 10, "c": {"d": 20}}, init_expecting=True, remove_id=True)
def mutable_find4(col: PetCollection):
	return col.findall({}).find({"a": 5, "c.d": 20})

@test(expect={"a": 5, "b": 10, "c": {"d": 20}}, init_expecting=True, remove_id=True)
def mutable_find5(col: PetCollection):
	return col.findall({}).find({"a": 5, "c": {"d": 20}})

@test(expect={"a": 5, "b": 10, "c": {"d": {"e": 20}}}, init_expecting=True, remove_id=True)
def mutable_find6(col: PetCollection):
	return col.findall({}).find({"a": 5, "c": {"d.e": 20}})

@test(expect={"a": 5, "b": 10, "c": {"d": {"e": 20}}}, init_expecting=True, remove_id=True)
def mutable_find6(col: PetCollection):
	return col.findall({}).find({"a": 5, "c.d": {"e": 20}})

@test(expect={"a": 5, "b": 10, "c": {"d": {"e": 20}}}, init_expecting=True, remove_id=True)
def mutable_find6(col: PetCollection):
	return col.findall({}).find({"a": 5, "c": {"d": {"e": 20}}})

if __name__ == '__main__':
	print("Running tests...\n")
	Tests.init()
	failed = Tests.run()
	if len(failed) == 0:
		print(colored("\nAll tests passed", "green"))
	else:
		print(colored(f"\nTests failed:\n{"\n".join(failed)}", "red"))
