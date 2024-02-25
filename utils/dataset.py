from datasets import load_dataset
from itertools import islice

class ILSVRC_Dataset():
	"""
	Loader for ImageNet1k dataset
	"""

	def __init__(self, set_type: str):
		self.batch_size = None
		self.data = None

		dataset = load_dataset("imagenet-1k", streaming=True, trust_remote_code=True)

		if set_type == "val":
			self.data = list(islice(dataset["validation"], 200))	
		else:
			self.data = list(islice(dataset["train"], 1000))
	
	
	def __getitem__(self, idx):
		return self.data[idx]

	def __len__(self):
		return len(self.data)	
