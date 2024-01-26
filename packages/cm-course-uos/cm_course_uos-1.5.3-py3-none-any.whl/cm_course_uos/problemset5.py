import numpy as np # for doing math easily in python
import matplotlib.pyplot as plt # for plotting in python

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



