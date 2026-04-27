# Symmetric_Stabilizer_Extent_for_Unitaries
This is the repository with codes that can be used to reproduce the results in the work titled ["Symmetry-accelerated classical simulation of Clifford-dominated circuits"](https://doi.org/10.1103/nnzz-481j)

Functions are organized in the library *sse_library*, to be explained below; some of them benefit of 
parallelized computation and can be modified easily if necessary. We also include some possibly useful data.

An environment with the essential python packages for running the codes in this repository can be created from 
the included .yml file by means of the following code line in your terminal: 'conda env create -f env.yml'.

* [The sse_library](#sse_library)
    * [Target states](#target_states)
    * [Generating diagonal Clifford elements](#generating)
    * [Convex optimization with Gurobi](#optimization)
    * [Permutations twirl](#permutations_twirl)
    * [Non-equivalent Clifford diagonals by CZ category](#non_equivalent)
    * [Example](#example)
* [Data](#data)

* [License](#license)


<a id="sse_library"></a>

### The sse_library
The main library contains all the functions necessary to reproduce the results. It is organized in secctions, the first one 
for initializing some target states, the second one for generating decomposition elements, then followed by one with the 
general function to be called to perform the convex optimization, and finally two other sections for performing permutation 
projection and collecting non-equivalent diagonal Clifford operators by permutation.

<a id="target_states"></a>

##### The target states
The functions **tensor_T**, **multi_RZ**, **multi_CZ** and **multi_CS** can be used to create diagonal unitaries 
corresponding respectively to tensor products of T gates, multi-controlled Z-rotations by a given angle, 
multi-controlled Z gates, and multi-controlled S gates.

<a id="generating"></a>

##### Generating diagonal Clifford elements
The functions **gen_symmetric_Rs** and **gen_symmetric_Rs_for_CZS** are for generating the symmetric matrices in 
correspondence respectively with diagonal and real-diagonal Clifford operators. Then with **diagonal_Clifford_from_R** 
one can get the Clifford operator. And with **diagonal_paulis** the pauli Z operators necessary to construct all the 
diagonal elements of interest.

<a id="optimization"></a>

##### Convex optimization with Gurobi
Once with a target and a decomposition set of diagonals in hands, with **sext_diagonals** one can perfom the convex 
optimization to get the *stabilizer extent* and the optimal solution vector. > **Note**: One needs a valid Gurobi license in 
order to solve optimizations with this function.

<a id="permutations_twirl"></a>

##### Permutations twirl
The function **twirled_A** returns a matrix with the same shape of an input matrix A (assumed to contain diagonal operators 
as columns) with the columns replaced by their permutation projection, or twirl.

<a id="non_equivalent"></a>

##### Non-equivalent Clifford diagonals by CZ category
Functions **Rs_with_phases_from_non_equiv_graphs** and **remove_equivalent_diagonals** can be used to a more systematic 
construction of the non-equivalent permutation-projections of diagonal operators implementing the *strong* and 
*weak* reductions proposed in the work. The first gives a set of diagonals from a non-equivalent set of graphs and the 
second remove further redundacies by checking those that are equivalent by some permutation conjugation.

<a id="example"></a>

##### Example
By running the python file **test.py**, one could test whether one has the right value for stabilizer extent of the T gate printed.

<a id="data"></a>

### Data
It can be found in the repository also the data corresponding to lists of non-equivalent graphs and hypergraphs used along 
the work. They are in form of adjacency matrices if graphs or collections of sets of hyperedges otherwise.

<a id="license"></a>

### License
Copyright: Copyright (C) 2025 Giulio H.C. da Silva

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
