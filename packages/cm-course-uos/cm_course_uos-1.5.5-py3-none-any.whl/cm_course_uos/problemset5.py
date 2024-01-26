import numpy as np # for doing math easily in python
import matplotlib.pyplot as plt # for plotting in python
import itertools

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
        print("Your function is not computing correct outputs. Check for mistakes")

