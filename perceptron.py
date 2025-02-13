from typing import List, Literal

Binary = Literal[0, 1]


class Perceptron:
    def __init__(self, inputs: List[Binary], weights: List[Binary]):
        if len(inputs) != len(weights):
            raise Exception(
                "The no of weights should be equal to number of inputs"
            )
        self.inputs = inputs
        self.weights = weights
        self.bias = -5

    def output(self) -> Binary:
        summation = sum(weight * input for weight, input in zip(self.weights, self.inputs))
        if summation + self.bias <= 0:
            return 0
        else:
            return 1

weather_good, partner_coming, transport_av = 1, 0, 1
input = [weather_good, partner_coming, transport_av]

perc = Perceptron(input, [2,6,2])
print(perc.output())