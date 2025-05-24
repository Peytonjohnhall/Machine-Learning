def step_function(x):
    """ step_function() determines the output of the perceptron """
    return 1 if x > 0 else 0

def perceptron_train(inputs, targets, weights, learning_rate, iterations):
    """ perceptron_train() trains the perceptron with given parameters """
    for iteration in range(iterations):
        print(f"Iteration {iteration + 1}")
        for input_vector, target in zip(inputs, targets):
            # calculate the input to the perceptron
            activation = weights[0] * input_vector[0] + weights[1] * input_vector[1] + weights[2] * input_vector[2]
            # find the output of the perceptron
            output = step_function(activation)
            # Calculate the error
            error = target - output
            # update weights
            weights[0] += learning_rate * error * input_vector[0]
            weights[1] += learning_rate * error * input_vector[1]
            weights[2] += learning_rate * error * input_vector[2]
            print(f"Updated weights: {weights}")
    return weights

inputs = [
    [-1, 0, 0], # x0 is bias input
    [-1, 0, 1],
    [-1, 1, 0],
    [-1, 1, 1]
] # i.e. initial conditions
targets = [0, 0, 0, 1] # i.e. expected outputs for AND
initial_weights = [0.2, 0.5, -0.1] # i.e. w0, w1, w2
learning_rate = 0.25
iterations = 2

final_weights = perceptron_train(inputs, targets, initial_weights, learning_rate, iterations)
print(f"Final weights after training: {final_weights}")