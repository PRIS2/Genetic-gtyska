# Basics of genetic aglorithm (population, crossover, mutation)
The code contains generic class of an Individual, Population. The Individual has an possibility to mutate with given probability and the Population can cross with a specific probability.
## In order to check the quality of the code use one of the following links:
- quality gate measured by sonarcloud: https://sonarcloud.io/project/overview?id=PRIS2_Genetic-gtyska
- quality gate measured by codacy: https://app.codacy.com/gh/PRIS2/Genetic-gtyska/dashboard

## Explanation
The code uses python's random method which is considerered by sonarcloud and codacy as not secure. This is the common method used for example in genetic algorithm implementation to calculate the probability of mutation or crossover. In my opinion the best way is just to ignore this errors. Therefore the quality measure in codacy should be A.
