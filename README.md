
**An algorithm for the Automatic Discovery of Curricular Prerequisites** is my Mathematic's Degree Final Project and my first real contact with the Data World.

The entire project with all its theory, and a step by step guide can be accesed [here](FinalDegreeProject.pdf) (in Spanish).

## INTRODUCTION

In education, knowledge units presented to students, are sequenced according to their
difficulty. Also, a reasonable teaching process design must take into account a proper
organization of the contents, considering the need of prior comprehension of some of
them to comprehend the following ones; that is, they must take into account the existing
prerequisites dependencies between the units themselves.

In this project, the possibilities of using computational methods to generate
automatically such a prerequisites structure between units and subunits, are studied;
with the help of large amounts of data on partial student evaluations. To do so, an algorithm
in programming language python has been designed, implemented and tested
with real student data. In the project are used as well, Probabilistic methods and classic
structures of Artificial Intelligence.

As a result, a model represented as a bayesian network is generated as output. This
way, (i) it can help the professor generate an optimal sequence of the concepts for their
adquirement or (ii), it can be used as reference in a teaching and learning system for an
adaptation of the knowledge sequence varying to the needs of each student.

## CONTENTS

As a first approach, on [Prerequisites Discovery in Random Data](https://github.com/sararuizruiz/Automatic-Prerequisite-Discovery/tree/812ae652d23eaf1b8b041b6fb23fa4fe70a0b6a2/Prerequisites%20Discovery%20in%20Random%20Data), we create an algorithm to analyse the existent prerequisites within a randomly generated data file and based on the results, automatically create a Bayesian Network that helps visualise the dependencies and the associated probabilities via [GeNIe Modeler](https://www.bayesfusion.com/genie/).

Afterwards, on [Prerequisites Discovery Real Data](https://github.com/sararuizruiz/Automatic-Prerequisite-Discovery/tree/812ae652d23eaf1b8b041b6fb23fa4fe70a0b6a2/Prerequisites%20Discovery%20Real%20Data), we apply the algorithm to real world data. The data used for the project corresponds to students evaluations of the 
UNED course 'Discrete Structures', obtained through the platform [SIETTE](https://www.siette.org). The algorithm is applied to obtain the dependencies between the 5 different units the students are asked about, and moreover, it is applied within each unit, to also obtain a structure of prerequisites between subunits.

As an example, here is one of the Bayesian Networks generated by the code with the data:
<img src="https://github.com/sararuizruiz/Automatic-Prerequisite-Discovery/assets/75987848/bdc27ea0-5ca1-4d6d-9ca1-3d52d5170bee" width="500" height="300">




