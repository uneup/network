import numpy as np


class SevenSegmentNN:
    def __init__(self, learning_rate=0.1):
        self.weights_0_1 = np.random.uniform(0.0, 0.1, (5, 7))
        self.weights_1_2 = np.random.uniform(0.0, 0.1, (10, 5))
        self.learning_rate = np.array([learning_rate])
        self.sigmoid_mapper = np.vectorize(self.sigmoid)
        self.sigmoid_derivative_mapper = np.vectorize(self.sigmoid_derivative)

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def sigmoid_derivative(y):
        return y * (1 - y)

    def predict(self, inputs):
        inputs_1 = np.dot(self.weights_0_1, inputs)
        outputs_1 = self.sigmoid_mapper(inputs_1)

        inputs_2 = np.dot(self.weights_1_2, outputs_1)
        outputs_2 = self.sigmoid_mapper(inputs_2)
        out = np.round(outputs_2, 1)
        print(np.argmax(out))
        return out

    def train(self, inputs, expected_predict):
        #FORWARD
        inputs_1 = np.dot(self.weights_0_1, inputs)
        outputs_1 = self.sigmoid_mapper(inputs_1)

        inputs_2 = np.dot(self.weights_1_2, outputs_1)
        outputs_2 = self.sigmoid_mapper(inputs_2)

        actual_predict = outputs_2

        E = np.mean((expected_predict-actual_predict)**2)
        print('E:', E)

        #BACK
        # error_layer_2 = expected_predict-actual_predict
        # print('ERROR_LAYER_2:' , error_layer_2)
        # gradient_layer_2 = actual_predict * (1 - actual_predict)
        # print(gradient_layer_2)

        e = expected_predict - actual_predict
        print(e, 'LOOOL')
        delta = e * self.sigmoid_derivative_mapper(actual_predict)
        # print('DELTA:', delta)
        # print('OUTPUTS_1:', outputs_1)
        # print('WEIGHTS_1_2:', self.weights_1_2)
        for i in range(len(self.weights_1_2)):
            self.weights_1_2[i] += self.learning_rate * (delta[i] * outputs_1)
        # print('NEW_WEIGHTS_1_2:', self.weights_1_2)


        e2 = np.dot(delta, self.weights_1_2)
        # print(e2)
        delta2 = e2 * self.sigmoid_derivative_mapper(outputs_1)
        # print('DELTA2:', delta2)
        # print('INPUTS:', inputs)
        # print('WEIGHTS_0_1:', self.weights_0_1)
        for i in range(len(self.weights_0_1)):
            self.weights_0_1[i] += self.learning_rate * (delta2[i] * inputs)
        # print('NEW_WEIGHTS_0_1:', self.weights_0_1)



        # print('WEIGHTS_0_1:', self.weights_0_1)
        # for i in range(len(self.weights_0_1)):
        #     self.weights_0_1[i] += self.learning_rate * (delta[i] * inputs)
        # print('NEW_WEIGHTS_0_1:', self.weights_0_1)



x_train = np.array([[1, 1, 1, 1, 1, 1, 0],  # 0
                    [0, 1, 1, 0, 0, 0, 0],  # 1
                    [1, 1, 0, 1, 1, 0, 1],  # 2
                    [1, 1, 1, 1, 0, 0, 1],  # 3
                    [0, 1, 1, 0, 0, 1, 1],  # 4
                    [1, 0, 1, 1, 0, 1, 1],  # 5
                    [1, 0, 1, 1, 1, 1, 1],  # 6
                    [1, 1, 1, 0, 0, 0, 0],  # 7
                    [1, 1, 1, 1, 1, 1, 1],  # 8
                    [1, 1, 1, 1, 0, 1, 1]]) # 9
y_train = np.eye(10, dtype=int)
epochs = 2000
network = SevenSegmentNN(learning_rate=0.5)
print(network.predict([1, 0, 1, 1, 0, 1, 1]))

for e in range(epochs):
    for i in range(len(x_train)):
        network.train(x_train[i], y_train[i])

# print(network.predict([1, 1, 0, 1, 1, 0, 1]))
for x in x_train:
    print(network.predict(x))





