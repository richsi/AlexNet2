# ImageNet Classification with Deep Convolutional Neural Networks

Classifies images using a neural network with 60 million parameters and 650,000 neurons. The neural network consists of five convolutional layers, some of which are followed by max-pooling layers, and three fully-connected layers with a final 1000-way softmax.

## ImageNet Overview

### Dataset
I use the ImageNet1K dataset, also known as ILSVRC 2012, which is a subset of the larger ImageNet dataset. Loaded from huggingface. 

From [paperswithcode](https://paperswithcode.com/dataset/imagenet-1k-1)

1. It spans 1000 object classes
2. It contains 1,281,167 training images, 50,000 validation images, and 100,000 test images. 
3. The images in the dataset are organized according to the WordNet hierarchy.
4. Each meaningful concept in WordNet, possibly described by multiple words or phrases, is called a "synonym set" or "synset".


