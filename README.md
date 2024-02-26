# ImageNet Classification with a Reimplementation of AlexNet

This is a reimplementaiton of AlexNet by Krizhevsky.

## ImageNet Overview

#### Dataset
ImageNet1K dataset, also known as ILSVRC 2012, is a subset of the larger ImageNet dataset.

From [paperswithcode](https://paperswithcode.com/dataset/imagenet-1k-1)

1. It spans 1000 object classes
2. It contains 1,281,167 training images, 50,000 validation images, and 100,000 test images. 
3. The images in the dataset are organized according to the WordNet hierarchy.
4. Each meaningful concept in WordNet, possibly described by multiple words or phrases, is called a "synonym set" or "synset".

#### Model Results:

## Project Structure
```
├── LICENSE
├── README.md
├── config.yaml
├── docs
│   └── NIPS-2012-imagenet-classification-with-deep-convolutional-neural-networks-Paper.pdf
├── notebooks
├── train.py
└── utils
    ├── __pycache__
    │   └── dataset.cpython-311.pyc
    ├── dataset.py
    └── model.py
```

- **utils/dataset.py** - data loader for ILSVRC dataset
- **utils/model.py** - model architecture
- **train.py** - python script for training model
- **config.yaml** - file with training parameters

## Usage
```
python3 train.py --config config.yaml
```

## License
This project is licensed under the terms of the [MIT license](https://choosealicense.com/licenses/mit/). 
