import numpy as np
from scipy import constants
from scipy.optimize import minimize
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
from scipy.spatial.distance import cityblock
from scipy import io
from scipy.stats import ttest_ind
from scipy.interpolate import interp1d

print(f"Value of pi: \n {constants.pi}\n")

print(f"Value of speed of light: \n {constants.speed_of_light}\n")


def min(x):
    return x**2 + x + 2


mymin = minimize(min, 0, method="BFGS")
print(f"Minimize a quadratic function: \n {mymin}\n")

arr1 = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

print(
    f"Sparse matrix and convert it to a dense (regular) array: \n {csr_matrix(arr1).data}\n"
)

arr2 = arr = np.array([[0, 1, 2], [1, 0, 0], [2, 0, 0]])

newarr = csr_matrix(arr2)
print(
    f"Represent a graph using SciPy and display its connected components: \n {connected_components(newarr)}\n"
)

p1 = (1, 0)
p2 = (9, 10)

res = cityblock(p1, p2)
print(f"The distance between a set of 2D points: \n {res}\n")

arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

io.savemat("arr.mat", {"vec": arr3})
myarr = io.loadmat("arr.mat")

print(f"After create and save a MATLAB .mat file, then load it back: \n {myarr}\n")

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

res2 = ttest_ind(v1, v2)
print(f"By perform interpolation on a small dataset and plot the result:\n {res2}\n")

xs = np.arange(10)
ys = 2 * xs + 1

interp_func = interp1d(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(
    f"Run a statistical significance test (example: t-test) on two small datasets: \n {newarr}\n"
)
