from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
import numpy as np
import pandas as pd
import hssm

hssm.set_floatX("float32")

def run_ddm(drift_rate = 1,
            threshold = 1,
            starting_point = 0.5,
            noise_std = 1,
            non_decision_time = 0,
            dt = 0.01,
            max_time = 200):
    """
    Simulates the Drift Diffusion Model for one run with fixed time increments to match evidence points.

    Parameters are the same as the previous function.

    Arguments:
    - drift_rate: rate of evidence accumulation
    - threshold: evidence needed to reach a decision
    - starting_point: initial condition of the evidence
    - noise_std: standard deviation of the noise term
    - non_decision_time: time not included in the evidence accumulation process
    - dt: time increment
    - max_time: maximum simulation time

    Returns:
    - decision_time: the time taken to reach a decision
    - evidence_over_time: the evidence accumulated over time
    - decision: 1 if the decision boundary reached is the upper threshold, -1 if lower
    """
    # Initialize evidence accumulation process
    time = non_decision_time
    evidence = starting_point
    evidence_over_time = [evidence]

    # Run the simulation until a decision boundary is reached or max time is exceeded)
    while time < max_time:
        # Increment the evidence by the drift and some noise
        evidence += drift_rate * dt + np.sqrt(dt) * noise_std * np.random.normal() # THERE IS A BUG IN THIS LINE
        # evidence += drift_rate + dt + np.sqrt(dt) * noise_std * np.random.normal()
        evidence_over_time.append(evidence)
        time += dt  # Increment the time

        # Check if the evidence has reached either threshold
        if evidence >= threshold: # THERE IS A BUG IN THIS LINE
            return time, evidence_over_time, 1  # Decision made for the upper threshold
        elif evidence <= 0:
            return time, evidence_over_time, -1  # Decision made for the lower threshold

    # If no decision has been made by max_time, return the current state
    return time, evidence_over_time, 0

def test_run_ddm(run_ddm_student):

    v = 1
    a = 1
    z = 0.5
    sigma = 1
    t0 = 0
    dt = 0.01
    max_time = 200

    np.random.seed(0)
    decision_time, evidence_over_time, decision = run_ddm(drift_rate=v,
                                                          threshold=a,
                                                          starting_point=z,
                                                          noise_std=sigma,
                                                          non_decision_time=t0,
                                                          dt=dt,
                                                          max_time=max_time)

    np.random.seed(0)
    student_decision_time, student_evidence_over_time, student_decision = run_ddm_student(drift_rate=v,
                                                                                         threshold=a,
                                                                                         starting_point=z,
                                                                                         noise_std=sigma,
                                                                                         non_decision_time=t0,
                                                                                         dt=dt,
                                                                                         max_time=max_time)

    if not np.allclose(decision_time, student_decision_time, atol=0.01):
        print("Your run_ddm function generates incorrect outputs. Check for mistakes.")
    else:
        print("Your run_ddm function generates correct outputs!")

def get_simulated_histogram_data():
    v_true, a_true, z_true, t_true = [-0.5, 1, 0.5, 0.5]
    dataset = hssm.simulate_data(
        model="ddm",
        theta=[v_true, a_true, z_true, t_true],
        size=1000,
    )

    return dataset

def test_simulated_ddm(v, a, t0, rt_upper, rt_lower):
    looks_good = True

    if v >= 0:
        looks_good = False

    if t0 < 0.3 or t0 > 0.7:
        looks_good = False

    if looks_good:
        print("Your parameters look reasonable.")
    else:
        print("Your parameters may be wrong.")


def get_dot_data_set():
    # Set up trial by trial parameters
    intercept = 0.2
    x = np.random.uniform(-1, 1, size=500)
    v = intercept + (0.5 * x)

    true_values = np.column_stack(
        [v, np.repeat([[1.5, 0.5, 0.5, 0.0]], axis=0, repeats=500)]
    )

    dataset = hssm.simulate_data(
        model="ddm",
        theta=true_values,
        size=1,
    )

    # dataset
    dataset_reg_v = pd.DataFrame(
        {
            "rt": dataset["rt"],
            "response": dataset["response"],
            "coherence": x,
        }
    )

    return dataset_reg_v

def get_threshold_model(coherence_dataset):
    name = "a"
    formula = "a ~ 1 + coherence"

    varying_threshold_model = hssm.HSSM(
        data=coherence_dataset,
        include=[
            {
                "name": name,
                "formula": formula,
            }
        ],
    )
    return varying_threshold_model

def test_threshold_model(name, formula):
    looks_good = True

    if name != "a":
        looks_good = False

    # remove spaces from formula
    formula = formula.replace(" ", "")

    if formula != "a~1+coherence":
        looks_good = False

    if looks_good:
        print("Your model specification is correct.")
    else:
        print("Your model specification is wrong. Check for mistakes.")

def S(g,y):
  """Logistic saturation function, with slope modulated by a gain parameter

  Inputs
  --------
  g: positive scalar neuronal gain
  y: net input to the neural processing unit
  """

  return 1/(1 + np.exp(-g*y))

def sim_trajectories(t, x, g, I1, I2, sigma):
  """ Dynamical model

  ------
  t: scalar time (you can ignore this variable)
  x: array [x1,x2] of activities of the neural units corresponding to tasks 1,2
  w_{12} = w{21} = 1
  g: gain
  I1: input to x_1 (cue for task 1)
  I2: input to x_2 (cue for task 2)
  sigma: standard deviation of Gaussian noise added to the net input


  Output
  -------
  dx1/dt(t,x): - x1 + S(-w_{12} x2 + I1)
  dx2/dt(t,x): - x2 + S(-w_{21} x1 + I2)    where S(y) = 1/(1 + e^(-g y))

  """
  # inhibitory weights
  w1_2=1
  w2_1=1

  # initial conditions
  x1 = x[0]
  x2 = x[1]

  ###Exercise 1.c START###

  dx1_dt = - x1 + S(g, -w1_2 * x2 + I1 + sigma * np.random.normal()) # YOUR CODE GOES HERE   (0.5 points)

  dx2_dt = - x2 + S(g, -w2_1 * x1 + I2 + sigma * np.random.normal()) # YOUR CODE GOES HERE   (0.5 points)

  ###Exercise 1.c END###

  return np.array([dx1_dt, dx2_dt])

def test_sim_trajectories(sim_trajectories_student):

    t = 0
    np.random.seed(0)
    x_0 = np.array([np.random.uniform(),np.random.uniform()])        # Initial condition (x1(0), x2(0)) (must have the same number of entries as your list of variables!)
    I1 = 1.2; I2 = 0.5; g = 5          # parameters
    sigma = 0.1

    np.random.seed(0)
    dx1_dt, dx2_dt = sim_trajectories(t, x_0, g, I1, I2, sigma)

    np.random.seed(0)
    dx1_dt_student, dx2_dt_student = sim_trajectories_student(t, x_0, g, I1, I2, sigma)

    if not np.allclose(dx1_dt, dx1_dt_student, atol=0.01):
        print("Your sim_trajectories function generates incorrect outputs. Check for mistakes.")
    elif not np.allclose(dx2_dt, dx2_dt_student, atol=0.01):
        print("Your sim_trajectories function generates incorrect outputs. Check for mistakes.")
    else:
        print("Your sim_trajectories function generates correct outputs!")

def compute_dx_dt(x_i, x_j, g, I, sigma):
  """ Activation Difference Function

  ------
  x_i: activity of the neural unit x_i corresponding to task 1 or task 2
  x_j: activity of the other neural unit x_i corresponding to task 2 or task 1
  g: gain
  I: input to the neural unit x_i
  sigma: standard deviation of Gaussian noise added to the net input

  Output
  -------
  dxi/dt
  """

  dx_dt = - x_i + S(g, -1 * x_j + I + sigma * np.random.normal())

  return dx_dt

def plot_trajectory(T, g, I1, I2, sigma, x1_0, x1_1, ax=None):
  # Initial condition (x1(0), x2(0)) (must have the same number of entries as your list of variables!)
  x_0 = np.array([x1_0, x1_1])

  # Integrate differential equation
  x_out = solve_ivp(sim_trajectories,
                    np.array([0,T]),
                    x_0,                # initial condition
                    dense_output=True,  # dense_output = True allows us to compute x at any time points on the interval T
                    args = [g, I1, I2, sigma]) # pass additional arguments to the simulation functon

  # First, extract values of the simulation at the desired time grid:
  ts = np.linspace(0,T,100)         # list of 100 evenly spaced points in the time interval we are considering
  xt = x_out.sol(ts)                # solution of the integral at the specified time points
  x1 = xt[0,:]                      # the values of x1(t) are in the first column of the matrix xt
  x2 = xt[1,:]                      # the values of x2(t) are in the second column of the matrix xt

  if ax is None:
    # Next, visualize the trajectories:
    plt.plot(ts,x1,label='x1')        # this plots the time trajectory of x1
    plt.plot(ts,x2,label='x2')        # this plots the time trajectory of x2
    plt.legend()                      # show the legend
    plt.xlabel('t')                   # this labels the horizontal axis
    plt.ylim([0, 1.0])                # this sets the upper and lower bounds for the vertical axis
  else:
    ax.plot(ts,x1,label='x1')        # this plots the time trajectory of x1
    ax.plot(ts,x2,label='x2')        # this plots the time trajectory of x2
    ax.legend()                      # show the legend
    ax.set_xlabel('t')                   # this labels the horizontal axis
    ax.set_ylim([0, 1.0])                # this sets the upper and lower bounds for the vertical axis

def plot_control_participant():
    # Parameters
    T = 50  # Length of time for the simulation (keep this fixed for now)
    g = 10  # Gain parameter (you may tweak this for the exercise)
    I1 = 0  # Input to task 1 (keep this fixed for now)
    I2 = 0  # Input to task 2 (keep this fixed for now)
    x1_0 = 1  # Initial condition of task 1 variable (you may tweak this for the exercise)
    x1_1 = 0  # Initial condition of task 1 variable (you may tweak this for the exercise)

    np.random.seed(0)

    # plot noise-less environment
    sigma = 0
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))  # 1 row, 2 columns
    plot_trajectory(T, g, I1, I2, sigma, x1_0, x1_1, axs[0])
    axs[0].set_title('Healthy Patient Without Noise')

    # plot noisy environment
    sigma = 0.2
    plot_trajectory(T, g, I1, I2, sigma, x1_0, x1_1, axs[1])
    axs[1].set_title('Healthy Patient With Noise')

    plt.tight_layout()
    plt.show()