#!/usr/bin/python

import numpy as np
import random

sigmoid = lambda x: 1.0 / (1 + np.exp(-x))


class Input:


    def __init__(self, value):
        self.value = value
        self.values = {}


    def add_neuron(self, neuron):
        self.values[neuron] = self.value


class Neuron:


    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs
        self.values = {}
        for output in outputs:
            self.values[output] = None
        self.weights = [ [ random.random() for i in inputs ] for o in outputs ]
        self.bias = 1


    def compute(self):
        
        print(self.weights)
        print([a.value for a in self.inputs])
        adjusted_values = [ [ self.weights[o][i] * self.inputs[i].values[self] for i in xrange(len(self.inputs)) ] for o in xrange(len(self.outputs)) ]
        print(adjusted_values)
        for o in xrange(len(self.outputs)):
            self.values[self.outputs[o]] = sigmoid( sum(adjusted_values[o]) + self.bias )


i = [Input(5), Input(6)]
h = Neuron(i, ['a'])
for x in i:
  x.add_neuron(h)
h.compute()
print(h.values)