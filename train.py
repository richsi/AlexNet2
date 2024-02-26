import argparse
import yaml

from utils.dataset import ILSVRC_Dataset
from utils.model import create_model

def train(config_fn: str) -> None:
	with open(config_fn, 'r') as stream:
		config = yaml.safe_load(stream)

	train_dataset = ILSVRC_Dataset(set_type = "train")	
	val_dataset = ILSVRC_Dataset(set_type = "val")

	print(train_dataset[:5])
	print('\n type(train_dataset)')		



if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--config', type = str, required = True, help = 'path to yaml config')
	args = parser.parse_args()
	train(config_fn = args.config)
	
