# CI2024_project-work

## Symbolic Regression

Symbolic regression is a type of regression analysis that searches for mathematical expressions to best fit a given dataset. Unlike traditional regression, it doesn't assume a predefined model structure but discovers the underlying relationships dynamically.

I have implemented this project using genetic algorithms to evolve and derive the mathematical formula that predicts the best fitness for the dataset provided.

## Description

This project implements symbolic regression using genetic algorithms to derive mathematical expressions that best fit a given dataset. The process is as follows:

1. **Import Required Libraries**: All necessary libraries for evaluation and computation are installed and imported.
2. **Load Dataset**: The dataset is loaded to extract input variables (`x`) and output values (`y`).
3. **Dataset Splitting**: The dataset is split into training and testing subsets to evaluate the model's ability to generalize and predict results for unseen data.
4. **Operators, Functions, and Variables**: Define the operators (e.g., `+`, `-`, `*`), mathematical functions (e.g., `sin`, `log`, `cos`), and variables to be used in the expressions.
5. **Generate Random Formulae**: Create random mathematical expressions consisting of variables, constants, and functions.
6. **Validate and Transform Expressions**: Transform generated expressions into valid and safe formulae for further computations, discarding invalid ones.
7. **Fitness Evaluation**: Calculate the fitness of each expression in the population by comparing its output to the actual dataset values. The fitness values are calculated in terms of mse. 
8. **Parent Selection**: Use tournament selection to choose parents with valid and best fitness values. The size of the selection is half the population size.
9. **Crossover**: Perform crossover by swapping parts of the expression trees between two randomly selected parents.
10. **Mutation**: Apply slight modifications to the expressions, such as mutating `sin(x)` to `cos(x)`, to introduce variability in the population.
11. **Population Update**: Combine the parents and offspring to form the population for the next generation.

This iterative process continues over multiple generations, progressively improving the population to find the most accurate mathematical expression for the given dataset.

## Diagram Explaination 

## Dummy Example to understand the structure of the code
 
1. **Initial Population**: Let's consider initial population with its fitness values as follow

| Candidate | Formula                          | Fitness |
|-----------|----------------------------------|---------|
| 1         | \( sin(x0) + cos(x1) + 4 \) | 40      |
| 2         | \( log(exp(2)) + 0.65 \)      | 52      |
| 3         | \( cos(x1) \)                 | 9       |
| 4         | \( x0 + x1 *4 \)         | 1       |
| 5         | \( 4 + 3 * x0 + 3 \)       | 5       |


2. **Selection**:- lets do the selection of the parents based on the tournment selection. In our case we select the further population half the size of the population. 

- Tournament 1:
  Let randomly selects 3 candidates. For example candidate numbers 1, 2 and 5.
  Then we compare its fitness and we select the one with highest fitness so in our case candidate number 2.

- Tournament 2:
    Again we select random 3 population
    then we select the one with best fitness among it

Then in this way we have our candidates selected for further process lets say
candidate 2, 3 and 1 are the winner.

3. **Crossover**: In this process two parents combines their genetic information to produce the offspring.

Lets again select two candidate from the winner candidates
So Parent 1:- Candidate 2 (Fitness = 52) \( log(exp(2)) + 0.65 \)
   Parent 2:- Candidate 3 (Fitness = 9) \( cos(x1) \)

   The results will be as:

   | Offspring | Formula                          | Fitness|
   |-----------|----------------------------------|--------|
   | 1         | \( log(exp(2)) + cos(x1) \)      | 56     |
   | 2         | \( cos(x1) + 0.65 \)             | 43     |

4. **Mutation**: In mutation we do small random change in the individual's genetic.

Example:-

|Offspring | Orignal formula | Mutated Formula | fitness of mutated formula| 
|-----------|----------------------------------|----------------------------------|--------|
| 1         | \( log(exp(2)) + cos(x1) \) | \( log(exp(2)) + sin(x1) \)   | 50 |
|2         | \( cos(x1) + 0.65 \)  | \( cos(x_2) + 0.65 ) | 4|

5. **Population upadte**: Now the combination of newly created offspring and parents will be the next generation parents

| Individual | Formula                               | Fitness  |
|------------|---------------------------------------|----------|
| 1          | \( log(exp(2)) + sin(x1) \)       | 42 |
| 2          | \( x_0 + x1 * 4 \)              | 96 |
| 3          | \( 4 + 3 * x0 + 3 \)            | 8 |
| 4          | \( \cos(x1) \)                       | 75 |
| 5          | \( \sin(x0) + cos(x1) + 4 \)       | 4 |

  







