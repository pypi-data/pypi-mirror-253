import numpy as np # for doing math easily in python
import matplotlib.pyplot as plt # for plotting in python
import itertools


def bayesRule(probHypothesis, probObservation):
  '''
 Calculate the posterior probability with Bayes' Rule.
 Arguments:
  probHypothesis (float): A list of the prior distribution.
  probObservation (float): The probability of the observation.
 Returns:
  probPosterior (float): The probability value of the posterior.
  '''

  jointProb = 0.025
  likelihood = jointProb / probObservation
  probPosterior = likelihood * probHypothesis / probObservation


  return probPosterior

def probabilityDensityFunction(mean, variance, x):
  '''
  Calculates the probability density function in Gaussian form.
  The function returns the inputs mean and variance for convenience to be used later.

  Arguments:
    x(np.array): The input array of the function.
    mean (float): The mean of the function.
    variance (float): The variance of the function, sigma squared.

  Returns:
    mean (float): The given mean of the function.
    varinace (float): The given variance of the function.
    pdf (np.array): The output of the function as the probability density function.

  '''

  pdf = 1 / np.sqrt(2*np.pi*variance) * np.exp(-(x-mean)**2/(2*variance)) # YOUR CODE GOES HERE
  return pdf

def test_probabilityDensityFunction(student_function):
    mean = 0
    variance = 1
    x = np.linspace(-1,1,100)
    pdf_student = student_function(mean, variance, x)
    pdf = probabilityDensityFunction(mean, variance, x)
    isclose = np.allclose(pdf_student, pdf)

    if not isclose:
        print("Your function is not computing correct outputs. Check for mistakes.")
        return
    print("Your function is computing correct outputs!")
    return

def multiplyDistributions(mean1, mean2, var1, var2, x):
  '''
  Multiply two normal distributions.
  Arguments:
    x (np.array): The x values of the distribution.
    mean1 (float): The mean of the first distribution.
    mean2 (float): The mean of the second distribution.
    var1 (float): The variance of the first distribution, sigma squared.
    var2 (float): The variance of the second distribution, sigma sqaured.

  Returns:
    mean_post (float): The mean of the resulting distribution.
    var_post(float): The variance of the resulting distribution.
  '''


  # Define the probability density functions
  mean1, var1, pdf1 = probabilityDensityFunction(mean1, var1, x)
  mean2, var2, pdf2 = probabilityDensityFunction(mean2, var2, x)

  # Calculate the mean and the variance of the probability density function for the posterior
  meanPosterior = (1/var1 * mean1 + 1/var2 * mean2) / (1/var1 + 1/var2)
  varPosterior = 1 / (1/var1 + 1/var2)

  return meanPosterior, varPosterior

def test_multiplyDistributions(student_function):
    student_function = multiplyDistributions
    mean1 = 0
    mean2 = 0
    var1 = 1
    var2 = 1
    x = np.linspace(-1,1,100)
    mean_post_student, var_post_student = student_function(mean1, mean2, var1, var2, x)
    mean_post, var_post = multiplyDistributions(mean1, mean2, var1, var2, x)
    isclose = np.allclose(mean_post_student, mean_post) and np.allclose(var_post_student, var_post)

    if not isclose:
        print("Your function is not computing correct outputs. Check for mistakes.")
        return
    print("Your function is computing correct outputs!")
    return


def bayesUpdate(meanPrior, meanLikelihood, varPrior, varLikelihood, x):

  pdfPrior = probabilityDensityFunction(meanPrior, varPrior, x)
  meanPosterior, varPosterior = multiplyDistributions(meanPrior, meanLikelihood, varPrior, varLikelihood, x) # YOUR CODE GOES HERE

  # Bayesian update

  meanPrior = meanPosterior  # YOUR CODE GOES HERE
  varPrior = varPosterior   # YOUR CODE GOES HERE

  return meanPrior, varPrior, pdfPrior

def test_bayesUpdate(student_function):
    meanPrior = 0
    meanLikelihood = 0
    varPrior = 1
    varLikelihood = 1
    x = np.linspace(-1,1,100)
    mean_post_student, var_post_student, pdf_student = student_function(meanPrior, meanLikelihood, varPrior, varLikelihood, x)
    mean_post, var_post, pdf = bayesUpdate(meanPrior, meanLikelihood, varPrior, varLikelihood, x)

    isclose = np.allclose(mean_post_student, mean_post) and np.allclose(var_post_student, var_post) and np.allclose(pdf_student, pdf)

    if not isclose:
        print("Your function is not computing correct outputs. Check for mistakes.")
        return
    print("Your function is computing correct outputs!")
    return

def bipartite_to_dependency(adjacency_matrix_of_bipartite_graph):

  A = adjacency_matrix_of_bipartite_graph

  # determine number of tasks
  num_tasks = int(np.sum(A.flatten()))

  # for each of the tasks below, let's us store their input and output dimensions
  # these will come in handy later on
  task_list = list()
  for row in range(A.shape[0]):
    for col in range(A.shape[1]):
      if A[row, col] == 1: # we found a task
        # we are appending each task as a tuple specifying its input and output dimension
        task_list.append((row, col))

  # set up dependency graph
  dependency_graph = np.eye(num_tasks)

  # we will now enumerate through each pair of tasks
  for task1_id, input_output_tuple1 in enumerate(task_list):
    for task2_id, input_output_tuple2 in enumerate(task_list):
      if task1_id == task2_id:
        continue

      dependency = 0 # let's begin with assuming no dependency

      # first check if the two tasks are structurally dependent,
      # i.e., whether they share an input or output dimension
      if input_output_tuple1[0] == input_output_tuple2[0] or input_output_tuple1[1] == input_output_tuple2[1]:
        dependency = 1

      if dependency == 0:
        # if the task is not structurally dependent, then it may be functionally dependent
        # to determine functional dependence, we have to check if there is a third task in A
        # that either shares an input dimension our an output dimension with our task
        for task3_id, input_output_tuple3 in enumerate(task_list):
          if (input_output_tuple3[0] == input_output_tuple1[0] and input_output_tuple3[1] == input_output_tuple2[1]) or (input_output_tuple3[0] == input_output_tuple2[0] and input_output_tuple3[1] == input_output_tuple1[1]):
            dependency = 1
            break

      dependency_graph[task1_id, task2_id] = dependency
      dependency_graph[task2_id, task1_id] = dependency

  return dependency_graph

def test_bipartite_graph(bipartite_graph_student):
    bipartite_graph = np.array([[1, 0, 0],
                                [0, 1, 0],
                                [1, 0, 1],
                                [0, 1, 0]])

    equal = np.array_equal(bipartite_graph, bipartite_graph_student)

    if equal is True:
        print("Your adjancency matrix is correct!")
    else:
        print("Your adjancency matrix is incorrect. Check for mistakes.")

def get_example_dependency_graph():
    bipartite_graph = np.array([[1, 0, 0],
                                [0, 1, 0],
                                [1, 0, 1],
                                [0, 1, 0]])

    return bipartite_to_dependency(bipartite_graph)

def test_multitaskable_tasks(multitaskable_tasks):
    multitaskable_tasks = list(dict.fromkeys(multitaskable_tasks))

    dependency_graph = get_example_dependency_graph()
    edges = ['a', 'b', 'c', 'd', 'e']
    multitaskable = list()

    for row in range(dependency_graph.shape[0]):
        for col in range(row, dependency_graph.shape[0]):

            if dependency_graph[row, col] == 0:
                multitaskable.append((edges[row], edges[col]))

    for proposed_task_pair in multitaskable_tasks:

        found = False
        for idx, task_pair in enumerate(multitaskable):
            print(task_pair)
            if (proposed_task_pair[0] == task_pair[0] and proposed_task_pair[1] == task_pair[1]) or (
                    proposed_task_pair[0] == task_pair[1] and proposed_task_pair[1] == task_pair[0]):
                found = True
                del multitaskable[idx]
                break

        if found is False:
            print("Your list of multitaskable tasks is incomplete or incorrect. Check for mistakes.")
            return

    if len(multitaskable) == 0:
        print("Your list of multitaskable tasks is correct!")
    else:
        print("Your list of multitaskable tasks is incomplete or incorrect. Check for mistakes.")

def add_shared_representations(adjacency_matrix, p):
    for row in range(adjacency_matrix.shape[0]):
        for col in range(adjacency_matrix.shape[1]):
            if row == col:
                continue
            else:
                randnum = np.random.rand()
                if randnum < p:
                    adjacency_matrix[row, col] = 1
                    adjacency_matrix[col, row] = 1
    return adjacency_matrix

def is_independent_set(adjacency_matrix, node_set):
    """Check if a set of nodes is an independent set."""
    for i in node_set:
        for j in node_set:
            if i != j and adjacency_matrix[i, j] == 1:
                return False
    return True

def maximum_independent_set(adjacency_matrix, verbose=False):
    """Find the maximum independent set of a graph given its adjacency matrix."""
    n = len(adjacency_matrix)
    max_set = set()

    for size in range(1, n + 1):
        for subset in itertools.combinations(range(n), size):
            if verbose:
                print(str(subset) + str(is_independent_set(adjacency_matrix, subset)))
            if is_independent_set(adjacency_matrix, subset):
                if len(subset) > len(max_set):
                    max_set = set(subset)
    return max_set

def get_MIS_cardinality(adjacency_matrix):
    """determine the cardinality of the maximum independent set"""
    max_set = maximum_independent_set(adjacency_matrix)

    return len(max_set)

def compute_parallel_processing_capability(N, p):
    '''
    This function computes the parallel procesing capability of a graph.

    Arguments:
    - N: number of input/output nodes in the bipartite graph
    - p: edge probability (index for representation sharing)

    Returns:
    - MIS_cardinality: cardinality of the maximum independent set (single number)
    '''

    bipartite_graph = np.eye(N)
    bipartite_graph = add_shared_representations(bipartite_graph, p)
    dependency_graph = bipartite_to_dependency(bipartite_graph)
    MIS_size = get_MIS_cardinality(dependency_graph)

    return MIS_size

def test_compute_parallel_processing_capability(student_function):

    passed = True

    N = 5
    p = 0.5
    np.random.seed(0)
    MIS_size = compute_parallel_processing_capability(N, p)
    np.random.seed(0)
    student_MIS_size = student_function(N, p)
    if MIS_size != student_MIS_size:
        passed = False

    N = 4
    p = 0
    np.random.seed(0)
    MIS_size = compute_parallel_processing_capability(N, p)
    np.random.seed(0)
    student_MIS_size = student_function(N, p)
    if MIS_size != student_MIS_size:
        passed = False

    N = 4
    p = 1
    np.random.seed(0)
    MIS_size = compute_parallel_processing_capability(N, p)
    np.random.seed(0)
    student_MIS_size = student_function(N, p)
    if MIS_size != student_MIS_size:
        passed = False

    if passed is True:
        print("It looks like your function is computing correct outputs.")
    else:
        print("Your function is not computing correct outputs. Check for mistakes.")


def compute_E(correct_response_probability, N):
  num_keys = N
  p_resp = correct_response_probability
  p_nonresp = (1-p_resp)/(num_keys-1)
  p_prior = 1/num_keys
  return (num_keys-1) * p_nonresp * np.log(p_nonresp/p_prior) + p_resp * np.log(p_resp/p_prior)

def test_compute_E(student_function):
  for p in np.linspace(0.01, 0.99, 10):
    for N in range(2, 10):
      if not np.isclose(compute_E(p, N), student_function(p, N)):
        print("Your function is not computing correct outputs. Check for mistakes.")
        return
  print("It looks like your function is computing correct outputs.")
  return