"""
authors: Pelin Kömürlüoğlu (pkoemuerlueo@uos.de)
 Deniz Gün (dguen@uos.de)

This module contains helper and test functions for Problemset 3
of the course "Cognitive Modeling" at the University of Osnabrueck.
This module exists in order to load certain functionality into the
assignment notebooks without involuntarily giving students access to
solutions.
"""

import numpy as np


###################
## RUN THIS CELL ##
###################

class StroopNetwork:
    bias = -4
    class Weights:
        # Weights projecting from color input layer to color hidden layer
        scale_ci_ch = 2.0
        c_in_to_c_h = scale_ci_ch * np.array([[1, -1],
                                              [-1, 1]])
        # Weights projecting from color hidden layer to output layer
        scale_ch_co = 2.0
        c_h_to_out = scale_ch_co * np.array([[1, -1],
                                             [-1, 1]])
        # Weights projecting from word input layer to word hidden layer
        scale_wi_wh = 2.0
        w_in_to_w_h = scale_wi_wh * np.array([[1, -1],
                                              [-1, 1]])
        # Weights projecting from word hidden layer to output layer
        scale_wh_wo = 2.0
        w_h_to_out = scale_wh_wo * np.array([[1, -1],
                                            [-1, 1]])
        # Weights projecting from task layer to color hidden layer
        scale_ti_ch = 4.0
        t_in_to_c_h = scale_ti_ch * np.array([[1, 1],
                                             [0, 0]])
        # Weights projecting from task layer to word hidden layer
        scale_ti_wh = 4.0
        t_in_to_w_h = scale_ti_wh * np.array([[0, 0],
                                              [1, 1]])

    class InitialWeights:
        # Weights projecting from color input layer to color hidden layer
        scale_ci_ch = 2.0
        c_in_to_c_h = scale_ci_ch * np.array([[1, -1],
                                              [-1, 1]])
        # Weights projecting from color hidden layer to output layer
        scale_ch_co = 2.0
        c_h_to_out = scale_ch_co * np.array([[1, -1],
                                             [-1, 1]])
        # Weights projecting from word input layer to word hidden layer
        scale_wi_wh = 2.0
        w_in_to_w_h = scale_wi_wh * np.array([[1, -1],
                                              [-1, 1]])
        # Weights projecting from word hidden layer to output layer
        scale_wh_wo = 2.0
        w_h_to_out = scale_wh_wo * np.array([[1, -1],
                                            [-1, 1]])
        # Weights projecting from task layer to color hidden layer
        scale_ti_ch = 4.0
        t_in_to_c_h = scale_ti_ch * np.array([[1, 1],
                                             [0, 0]])
        # Weights projecting from task layer to word hidden layer
        scale_ti_wh = 4.0
        t_in_to_w_h = scale_ti_wh * np.array([[0, 0],
                                              [1, 1]])

    ### Activation Functions ###
    def logistic(x):
        return 1 / (1+np.exp(-x))

    def logistic_derivative(x):
        return x * (1-x)

    def softmax(activation):
      """
      Args:
        activation (2D Array): Represents activation of a layer  as 1xN matrix
      Returns:
        softmax (2D Array): Applies the softmax per column of activation (1xN)
      """
      return np.exp(activation) / np.sum(np.exp(activation))

    ### Layer activations ###
    def color_hidden_activation(color_input, task_input,
                                weights, bias):
      
      if weights is None:
        weights = StroopNetwork.Weights
      if bias is None:
        bias = StroopNetwork.bias

      net_activation =  np.dot(color_input, weights.c_in_to_c_h)
      net_activation += np.dot(task_input, weights.t_in_to_c_h)
      net_activation += bias
      activation = StroopNetwork.logistic(net_activation)
      return activation

    def word_hidden_activation(word_input, task_input,
                               weights, bias):
      if weights is None:
        weights = StroopNetwork.Weights
      if bias is None:
        bias = StroopNetwork.bias

      net_activation =  np.dot(word_input, weights.w_in_to_w_h)
      net_activation += np.dot(task_input, weights.t_in_to_w_h)
      net_activation += bias
      activation = StroopNetwork.logistic(net_activation)
      return activation

    def output_activation(color_hidden_activation,
                          word_hidden_activation,
                          weights):
      net_activation =  np.dot(color_hidden_activation, weights.c_h_to_out)
      net_activation += np.dot(word_hidden_activation, weights.w_h_to_out)
      activation = StroopNetwork.softmax(net_activation)
      return activation

    ### Forward Pass ###
    def forward(color_input, word_input,task_input, return_activations=False,
                weights=None, bias=None):
      """
      Accepts a single input pattern for the color, word and task input layers and produces a response probability at the output layer.

      Arguments:
        color_input (2D array): stores the color value (red vs. green)
        word_input (2D array): stores the word value (RED vs. GREEN)
        task_input (2D array): stores the task value (color naming vs. word reading)

      Returns:
        response_probability (float): probability distribution of the output activation.
        OR
        activations (dict): activations of all layers
                            access via
                            activations["color"]
                            activations["word"],
                            activations["out"]
      """

      if weights is None:
        weights = StroopNetwork.Weights
      if bias is None:
        bias = StroopNetwork.bias
      
      # Compute activation of color hidden layer
      activation_ch = StroopNetwork.color_hidden_activation(color_input,task_input, weights,bias)

      # Compute activation of word hidden layer
      activation_wh = StroopNetwork.word_hidden_activation(word_input, task_input, weights, bias)

      # Compute activation of output layer
      activation_output = StroopNetwork.output_activation(activation_ch, activation_wh,weights)


      if return_activations:
        return {"color":activation_ch,
                "word": activation_wh,
                "out":  activation_output}

      return activation_output


    ### WEIGHT UPDATES ####
    def compute_weight_updates_hidden_to_out(hidden_activation,
                                      output_activation,
                                      error):
        """
        This function calculates the weight update for the weights
        projecting from the hidden color units to the output units.

        Arguments:
            output_activation: activation at the output layer
            error:             discrepancy between output and target

        Returns:
            The weight update to be applied based on backprop
        """

        output_derivative = StroopNetwork.logistic_derivative(output_activation)

        weight_update = np.dot(hidden_activation.T,
                                error*output_derivative)

        return weight_update


    def compute_weight_updates_in_to_hidden(input, weights_h_to_out,
                                            hidden_activation, error):
        """
        Arguments:
            input (2D Array):  e.g. [[1,0]]
            weights_h_to_out (2D Array):  e.g [[2,0],[0,-2]]
            hidden_activation (2D Array):  e.g. [[0.4],[0,9]]
            error (float):             discrepancy between output and target

        Returns:
            weight_update (float): Value which indicates how much the weights   between input and hidden units should change

        """
        # Derivative of error wrt hidden activation
        d_error_to_h = np.dot(error, weights_h_to_out.T)

        # Derivative of hidden activation wrt net activation
        d_h_act_to_h_net = StroopNetwork.logistic_derivative(hidden_activation)

        # Derivative of error wrt to hidden net activation
        d_error_to_h_net = d_error_to_h * d_h_act_to_h_net

        # Derivative of the error wrt to the weights
        weight_update = np.dot(input.T, d_error_to_h_net * d_h_act_to_h_net)

        return weight_update

    ### INITIALIZATION FUNCTIONS ###

    def initialize_weights():

        W_color_input_color_hidden = np.random.randn(2,2)
        W_color_hidden_output = np.random.randn(2,2)

        weights_to_train = [W_color_input_color_hidden, W_color_hidden_output]

        return weights_to_train

    def initialize_inputs():
        possible_inputs = [[[0,1]], [[1,0]]]
        color_input = np.array(random.choice(possible_inputs))  # Random binary color input
        word_input = np.array(random.choice(possible_inputs))   # Random binary word input
        task_input = np.array(random.choice(possible_inputs))    # Random binary task input

        return color_input, word_input, task_input

    ### DATA GENERATION AND SIMULATION ###

    def simulate_stroop(color_input, word_input, task_input):

        response_probabilities = StroopNetwork.forward(color_input, word_input, task_input, weights=problemset3.StroopNetwork.InitialWeights)

        return response_probabilities

    def generate_training_data(n_trials):

        training_data = []

        for trials in range(n_trials):

          color_input, word_input, task_input = StroopNetwork.initialize_inputs()

          response_probabilities = StroopNetwork.simulate_stroop(color_input, word_input, task_input)
          training_data.append([color_input, word_input, task_input, response_probabilities])

        return training_data

    ### TRAINING THE MODEL ###


    def train_stroop(traning_data, n_epochs=100, learning_rate=0.01):

        Weights = problemset3.StroopNetwork.InitialWeights
        Weights.c_in_to_c_h, Weights.c_h_to_out = StroopNetwork.initialize_weights()

        MSE_log = []

        for epoch in range(n_epochs):

          total_loss = 0

          for color_input, word_input, task_input, target_output in training_data:

            result = StroopNetwork.forward(color_input, word_input, task_input, return_activations=True, weights=Weights)

            error = (result["response"] - target_output) ** 2
            MSE_loss = error

            color_activation = StroopNetwork.color_hidden_activation(color_input, task_input, Weights, bias)
            word_activation = StroopNetwork.word_hidden_activation(word_input, task_input, Weights, bias)
            output_activation = StroopNetwork.output_activation(color_activation, word_activation, Weights, bias)

            update_c_h_to_out = StroopNetwork.compute_weight_updates_hidden_to_out(color_activation, output_activation, error)
            update_c_in_to_c_h = StroopNetwork.compute_weight_updates_in_to_hidden(color_input, Weights.c_h_to_out, color_activation, error)

            Weights.c_in_to_c_h -= update_c_h_to_out * learning_rate
            Weights.c_h_to_out -= update_c_h_to_out * learning_rate

            total_loss += MSE_loss

          avg_loss = total_loss / len(training_data)
          MSE_log.append(avg_loss)

          print(f"Epoch{epoch+1}/{n_epochs}, Average Loss: {avg_loss}")


        return MSE_log, Weights


### END OF CLASS ###

### Functions and Test Functions ###
def logistic(v):
    return 1 / (1+np.exp(-v))

def test_logistic(student_function):
    test_values = np.arange(10)
    for v in test_values:
        v = np.array([v])
        # Mismatch
        if not np.array_equal(student_function(v), logistic(v)):
            print("Your Logistic Function produces incorrect ouputs")
            return

    print("Your Logistic function produces correct outputs.")
    return


def test_color_hidden_activation(student_function, weights=None):
    c_ins = [[0, 1], [1, 0]]
    t_ins = [[0, 1], [1, 0]]
    bias = -3
    for ci in c_ins:
        for ti in t_ins:
            answer = student_function(ci, ti, weights, bias)
            correct = StroopNetwork.color_hidden_activation(
                ci, ti, weights, bias)
            if not np.array_equal(answer, correct):
                print("Your color_hidden_activation produces wrong outputs.")
                return
    print("Your color_hidden_activation produces correct ouputs")
    return


def test_word_hidden_activation(student_function, weights=None):
    c_ins = [[0, 1], [1, 0]]
    t_ins = [[0, 1], [1, 0]]
    bias = -3
    for ci in c_ins:
        for ti in t_ins:
            answer = student_function(ci, ti, weights, bias)
            correct = StroopNetwork.word_hidden_activation(
                ci, ti, weights, bias)
            if not np.array_equal(answer, correct):
                print("Your color_hidden_activation produces wrong outputs.")
                return

    print("Your word_hidden_activation produces correct ouputs")
    return


def test_output_activation(student_function, weights=None):
    c_ins = np.array([[0, 1], [1, 0]])
    t_ins = np.array([[0, 1], [1, 0]])
    bias = -3
    for ci in c_ins:
        for ti in t_ins:
            answer = student_function(ci, ti, weights)
            correct = StroopNetwork.output_activation(ci, ti, weights)
            if not np.array_equal(answer, correct):
                print("Your output_activation produces wrong outputs.")
                return

    print("Your output_activation produces correct ouputs")
    return


def test_forward(student_function, weights=None):
    c_ins = [[0, 1], [1, 0]]
    t_ins = [[0, 1], [1, 0]]
    w_ins = [[0, 1], [0, 1]]
    bias = -3
    
    
    if weights is None:
        weights = StroopNetwork.Weights
        
    for ci in c_ins:
        for ti in t_ins:
            for wi in w_ins:
                answer = student_function(ci, ti, wi, weights=weights)
                correct = StroopNetwork.forward(ci, ti, wi, weights=weights)
                if not np.array_equal(answer, correct):
                    print("Your forward produces wrong outputs.")
                    return
                    
    print("Your forward produces correct outputs")
    return



def test_conditions(conditions):
    color_naming = np.array([[1,0]])
    word_reading = np.array([[0,1]])
    neutral = np.array([[0,0]])
    err_msg = "You have defined the conditions incorrectly"

    cn_cong = conditions["cn_congruent"]
    if not np.array_equal(cn_cong[0],cn_cong[1]) or not np.array_equal(cn_cong[2],color_naming):
        print(err_msg)
        return
        
    cn_incong = conditions["cn_incongruent"]
    if np.array_equal(cn_incong[0],cn_incong[1]) or not np.array_equal(cn_incong[2],color_naming):
        print(err_msg)
        return
        
    cn_neutral = conditions["cn_neutral"]
    if np.array_equal(cn_neutral[0], neutral) or not np.array_equal(cn_neutral[1],neutral) or not np.array_equal(cn_neutral[2],color_naming):
        print(err_msg)
        return
        
    cn_cong = conditions["wr_congruent"]
    if not np.array_equal(cn_cong[0],cn_cong[1]) or not np.array_equal(cn_cong[2],word_reading):
        print(err_msg)
        return
        
    cn_incong = conditions["wr_incongruent"]
    if np.array_equal(cn_incong[0],cn_incong[1]) or not np.array_equal(cn_incong[2],word_reading):
        print(err_msg)
        return
        
    cn_neutral = conditions["wr_neutral"]
    if np.array_equal(cn_neutral[1], neutral) or not np.array_equal(cn_neutral[0],neutral) or not np.array_equal(cn_neutral[2],word_reading):
        print(err_msg)
        return    
   
    print("You have defined the conditions correctly")
    return

    

def test_error_rates(error_rates):
    err_msg = "Implausible error rates."
    if not error_rates["cn_incongruent"] > error_rates["cn_neutral"]:
        print(err_msg)
        return
    if not error_rates["cn_neutral"] > error_rates["cn_congruent"]:
        print(err_msg)
        return
    for wr_condition in ["wr_congruent","wr_incongruent","wr_neutral"]:
        if error_rates[wr_condition] >= error_rates["cn_congruent"]:
            print(err_msg)
            return

    print("The error rates created by your weight choice look plausible!")
    return
  
  
  
def test_compute_weight_updates_hidden_out(student_function):
    # Generating sample data for testing
    hidden_activations = np.array([[2, 0], [0, -2]])
    output_activations = np.array([[0.5, 0.8], [0.3, 0.1]])
    errors = np.array([-2, 1])
    parameters = [(hidden_activations, output_activations, error) for error in errors]
    for values in parameters:
        answer = student_function(values[0],values[1],values[2])
        correct = StroopNetwork.compute_weight_updates_hidden_to_out(values[0],values[1],values[2])
        if not np.array_equal(answer,correct):
            print("Your weight updates are incorrect")
            return
    print("Your weight updates are correct")
    return 



def test_compute_weight_updates_in_hidden(student_function):
    # Generating sample data for testing
    input  = np.array([1,0])
    hidden_activations = np.array([[2, 0], [0, -2]])
    output_activations = np.array([[0.5, 0.8], [0.3, 0.1]])
    errors = np.array([-2, 1])
    parameters = [(input, hidden_activations, output_activations, error) for error in errors]
    for values in parameters:
        answer = student_function(values[0],values[1],values[2], values[3])
        correct = StroopNetwork.compute_weight_updates_in_to_hidden(values[0],values[1],values[2], values[3])
        
        if not np.array_equal(answer,correct):
            print("Your weight updates are incorrect")
            return
            
    print("Your weight updates are correct")
    return 


conditions = {"cn_congruent":    (np.array([[1,0]]),      np.array([[1,0]]),     np.array([[1,0]])),
              "cn_incongruent":  (np.array([[1,0]]),      np.array([[0,1]]),   np.array([[1,0]])),
              "cn_neutral":      (np.array([[0,1]]),  np.array([[0,0]]),   np.array([[1,0]])),
              "wr_congruent":    (np.array([[1,0]]),      np.array([[1,0]]),     np.array([[0,1]])),
              "wr_incongruent":  (np.array([[1,0]]),      np.array([[0,1]]),   np.array([[0,1]])),
              "wr_neutral":      (np.array([[0,0]]),   np.array([[1,0]]),     np.array([[0,1]]))
              }