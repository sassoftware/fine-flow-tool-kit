# FINE Flow Tool Kit

## Overview
Welcome to the FINE Flow Tool Kit. This set of Python utilities demonstrates an implementation of the FINE team classification process, and the associated FINE flow equations. The tool kit can be used as an evaluation of team organization with a view to identifying a necessary value stream reference architecture that is optimized for efficient delivery of value. Collectively, these tools can also be useful when adopting the [Value Stream Implementation Roadmap](https://www.vsmconsortium.org/implementation/the-value-stream-management-implementation-roadmap) as prescribed by the VSM Consortium.

The FINE Flow Tool Kit demonstrates how we can think of, and reason about, value delivery in the follwing terms:

```
F = Flow of value.
I = Impediments that slow down the flow of value.
N = Needs that drive the potential for flow to happen.
E = Energy that is used in the form of cognitive load.
```

### What's New
> Everything! ...This is our first release of the FINE Flow Tool Kit.

## Getting Started - The Three Primary FINE Modules

> The toolkit is arranged into three primary FINE modules. One that supports the process of team classification, and two that support the process of flow evaluation. 

### [teamtopology.py](/source/teamtopology.py)
This module is used to perform team topology and team type identification using the FINE team classification process. It is recommended that use of the toolkit starts with this module by leveraging the "findTopology" method to perform an organizational analysis. Input to the method is provided in the form of a dictionary that represents an adjacency matrix of dependencies that are observed between the teams of the organization. Output from the method is identification of the teams into one of four types; stream aligned (SA), enabling (EN), complex sub-system (CS), and platform (PF) teams. Optionally, output can also include metrics by which the analysis is made. The best way to understand how this module works is through exploration of the unit tests in the file: [teamtopology_test.py](/source/teamtopology_test.py). The tests demonstrate how the findTopology method can be used to identify the different team types that exist. Formal validation of the FINE team classification process is provided using tests that include sample dictionaries for the general case, and non-general case, of dependencies that exist between the four different team types.

### [fineflowevalution.py](/source/fineflowevalution.py)
This module is used to perform analysis using the FINE flow equations. There are two methods implemented in this module. The first method is an “evaluate” function which is similar to the “findTopology” method of the FINE team classification process. The evaluate method takes as input an adjacency matrix of dependencies between the teams which also includes the observed interaction styles of how the teams work together. The interaction styles are x-as-a-service (X), collaboration (C), and facilitation (F). The analysis uses these interaction styles to compute cognitive load for each team which is represented as a value of energy (E) in the FINE flow equations. The second method of this module is the “compute” function. This method can be used to compute individual FINE flow values. The values computed represent flow (F), impediments (I), needs (N) and energy (E). The best way to understand how this module works is through exploration of the unit tests in the file: [fineflowevalution_test.py](/source/fineflowevalution_test.py). The unit tests use a dictionary that present an adjacency matrix for the general dependencies and interactions that occur between the four team types. This dictionary is used as input to the evaluate method and demonstrates the expected FINE values for the generalized case. A further test also includes output that demonstrates values of resilience for each team type. Tests are also included that demonstrate the use of the compute method to determine FINE values when any two dimensions are given.

### [flowratio.py](/source/flowratio.py)
This module is used to compute flow ratio values that can be used as part of the FINE flow analysis. There are methods that compute flow ratio as well as methods that compute flow entropy and flow resilience. Flow ratio is computed as the odds of bad flow (defects and errors) versus good flow (items of true value). This metric is then used as the basis to compute flow entropy and flow resilience. Flow entropy is the observation that impediments increase proportionally to flow ratio which, in turn, results in changes to the other FINE values. The “computeEntropy” method can be used to model the impact of flow ratio for any given FINE starting values. The method supports the additional inputs of batch-size, with other control variables for fixed flow, maximum energy, and drop output. The “flowResilience” method can be used to model and simulate the number of cycles that are required before a team reaches maximum energy and flow entropy starts to take effect. This method is used as part of the FINE flow evaluation, described earlier, for any given team topology and organizational structure. As with the previous modules, the best way to understand how this module works is through exploration of the unit tests in the file: [flowratio_test.py](/source/flowratio_test.py).

## Supporting Modules
> The following modules are not intended for direct use in performing the team classification and FINE flow analysis. A description of each is given here for the more curious.

### [betweeness.py](/source/betweeness.py)
This module contains a single method that computes betweenness centrality for a given graph. The “betweenness” method takes in a numpy array that represents an adjacency matrix of the edges that exist in the graph under analysis. The output from the method is a vector of betweenness scores for each vertex of the graph. The method is implemented using the networkx library: https://networkx.org/documentation/stable/index.html. The betweenness model is used as part of the FINE team type classification process. A set of unit tests are provided for this module in the file: [betweenness_test.py](/source/betweenness_test.py)

### [pagerank.py](/source/pagerank.py)
This module contains a method that computes pagerank centrality for a given graph. The “pagerank” method takes in a numpy array that represents an adjacency matrix of the edges that exist in the graph under analysis. It also allows input for the maximum number of iterations and for the damping factor used in the analysis. Optionally, normalization of the output can also be specified. The output from the method is an optionally normalized vector of ranks computed by the analysis. Other methods contained in this module assist with the FINE team type classification process and also provide a dictionary to array conversion function. The pagerank module is used as part of the FINE team type classification process and for assessment of the potential to impede value in the FINE flow analysis. A set of unit tests are provided for this module in the file: [pagerank_test.py](/source/pagerank_test.py)

### [cognitiveslope.py](/source/cognitiveslope.py)
This module contains a method that computes the cognitive slope for each node of a given graph. The “findCognitiveSlope” method takes in a dictionary as input that represents an adjacency matrix of dependencies between the teams where the observed interaction styles are also included. It optionally allows computed output variables to be enabled. These include the summed slope value, and values for flow, impediments, needs and energy. An output value for resilience can also be enabled. Other methods in this module assist with the conversion of the input dictionary to array formats for further processing by the FINE analysis. A set of unit tests are provided for this module in the file: [cognitiveslope_test.py](/source/cognitiveslope_test.py)

### Prerequisites
> This tool kit runs as a set of Python utilities. We recommend Python version 3.11 or later be installed on your system to run these utilities. The following external dependencies are required to use the FINE FLow Tool Kit. Please use the latest stable release of these products.

| Dependency | Install Instructions                                            |
|------------|-----------------------------------------------------------------|
| NetworkX   | https://networkx.org/documentation/stable/install.html          |
| Numpy      | https://numpy.org/install/                                      |

The following global modules are used from the standard python libraries:

| Module     | Documentation                                                   |
|------------|-----------------------------------------------------------------|
| Math       | https://docs.python.org/3/library/math.html                     |
| Unittest   | https://docs.python.org/3/library/unittest.html#module-unittest |

### Installation
> No special installation is required to use the Python files contained in this tool kit.

Simply clone or download this project and run the files from your local Python installation. We recommend running the utilites as tests that you create in your unit testing framework of choice. Running and keeping all of the Python files together in a single folder is the simplest approach.

## Running
The easiest way to use the FINE Flow Evaluation Tool Kit is to create your own tests that can be run under the Python UnitTest or similar testing framework. An example test file is provided that demonstrates this approach: [test_BakersUnlimited.py](/source/test_BakersUnlimited.py). To create your own tests, begin by adding the following imports into your test file to use the tool kit:

```python
import teamtopology as tt
import fineflowevaluation as fine
import flowratio as fr
```
## Examples
The following examples show how to use the FINE team classification process, the FINE flow evaluation, and the FINE flow ratio tools.

### FINE Team Classification

> ### [teamtopology](/source/teamtopology.py).findToplogy

In the set-up for the test, create a dictionary that can be used as input to the analysis. To perform the FINE team classification process, the dictionary will need to define the dependencies that exist between the teams. The following dictionary provides the team dependencies for the fictitious “Bakers Unlimited” organization:

```python
        #Team flow for Bakers Unlimited Example
        self.BU_TeamFlow = {'StoreRO':  ['CRM', 'QE', 'DataEC'],
                            'OnlineRO': ['CRM', 'UX', 'QE', 'DataEC'],
                            'CRM':      ['DataEC', 'CloudES'],
                            'UX':       [],
                            'QE':       [],
                            'DataEC':   ['QE', 'CloudES'],
                            'CloudES':  ['QE']
        }
```

In the above example, we can see from the first row of the dictionary that the "StoreRO" team has a dependency on the “CRM” team, the “QE” team, and the “DataEC” team. In the second row, we can see that the "OnlineRO" team has a dependency on the "CRM" team, the "UX" team, the "QE" team, and the "DataEC" team. The lists of dependencies for each team of the organization appear on subsequent rows of the dictionary. Notice that the “UX” and “QE” teams are not dependent on any of the other teams and so are provided with an empty list []. A team that has no dependencies must still be included in the dictionary.

To perform a test, create an assertion that compares expected to actual results. The output from the FINE team classification process will be a dictionary of the computed values. You can first create a failing test by providing an empty dictionary as the expected output. The test should be designed to print the actual result in the event that the test fails. You can then use the actual result printed to update the test so that it passes. Using this approach is a modified form of Test Driven Development (TDD). Ideally, you would know the expected result when you first design the test. Since performing the analysis is the objective of using the tool, then setting an initial dictionary that is empty is an acceptable approach to allow experimentation. An example passing test that performs the FINE team classification for the Bakers Unlimited organization is shown below:

```python
    def test_whenGivenBUTeamFlowThenTopologyIsAsExpected(self):

        ttopology = tt.findTopology(self.BU_TeamFlow)

        expected = {'StoreRO':  ['SA'],
                    'OnlineRO': ['SA'],
                    'CRM':      ['CS'],
                    'UX':       ['EN'],
                    'QE':       ['EN'],
                    'DataEC':   ['PF'],
                    'CloudES':  ['PF']
                    }

        if ttopology != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', ttopology)

        assert ttopology == expected
```

The output of the classification process shows that the "StoreRO" and "OnlineRO" teams have been identified as stream aligned teams (SA). The CRM team is identified as a complicated sub-system team (CS), with the "UX" and "QE" teams being shown as enabling teams (EN). The "DataEC" and the "CloudES" teams are both identified as platform teams (PF).

### FINE Flow Evaluation

> ### [fineflowevaluation](/source/fineflowevaluation.py).evaluate

To perform the FINE flow evaluation, it is also necessary to capture the interaction styles that exist in the team dependencies. The dictionary below provides the team dependencies with interaction styles for the Bakers Unlimited organization:

```python
#Team flow for Bakers Unlimited Example with interactions
self.BU_TeamFlowWithInteractions = {'StoreRO':  [('CRM', 'C'), ('QE', 'F'), ('DataEC', 'X')],
                                    'OnlineRO': [('CRM', 'C'), ('UX', 'F'), ('QE', 'F'), ('DataEC', 'X')],
                                    'CRM':      [('DataEC', 'X'), ('CloudES', 'X')],
                                    'UX':       [],
                                    'QE':       [],
                                    'DataEC':   [('QE', 'F'), ('CloudES', 'X')],
                                    'CloudES':  [('QE', 'F')]}
```

Just like the previous example, we can see from the first row of the dictionary that the “StoreRO” team has a dependency on the “CRM” team, “QE” team, and the “DataEC” team. This time however, the combined dependency and interaction style is provided as a tuple. We can see that the teams StoreRO is dependent upon provide interaction styles of collaboration (C), facilitation (F), and x-as-as-service (X), respectively.

As before, we can create a test with an assertion that compares expected to actual results. If the test fails, it should print the actual result which can then be used to update the test so that it passes. An example passing test that performs the FINE flow evaluation for the Bakers Unlimited organization is shown below:

```python
   def test_whenGivenBUExampleThenValuesAreAsExpected(self):

        ttopology = fine.evaluate(self.BU_TeamFlowWithInteractions, flow=True, imp=True, need=True, energy=True, resilience=True)

                                #flow    #imps   #need   #energy #resilience
        expected = {'StoreRO':  [3.2313, 0.0599, 0.1934, 0.625,  5 ],
                    'OnlineRO': [3.2953, 0.0599, 0.1973, 0.65,   5 ],
                    'CRM':      [1.7555, 0.1622, 0.2848, 0.5,    8 ],
                    'UX':       [2.3723, 0.1111, 0.2635, 0.625,  5 ],
                    'QE':       [0.7029, 0.8097, 0.5691, 0.4,    10],
                    'DataEC':   [1.534,  0.301,  0.4617, 0.7083, 4 ],
                    'CloudES':  [1.3348, 0.456,  0.6087, 0.8125, 3 ]}

        if ttopology != expected:
            print('\n01: Unexpected result! \nExpected:', expected, '\nInstead :', ttopology)

        assert ttopology == expected
```

In the above example, we have selected to output flow, impediments, need, energy and resilience from the FINE flow analysis. We can see that the "StoreRO" and "OnlineRO" teams have higher values of flow when compared to the other teams. This makes sense when you consider that they were both identified as stream aligned teams by the FINE team classification process. It is also interesting to note that the "QE", "DataEC", and "CloudES" teams have a higher potential to impede flow when compared to the other teams. This is because of the high dependence that other teams place upon them. Despite this, the "QE" team has the highest amount of resilience. This is because their interaction style of facilitation helps to reduce their overall cognitive load (energy) when compared to other teams. There are many other observations we can make from the results of the analysis. Further simulations of the organization can also be made by simply updating the dictionary and running new tests to create more insight.

### FINE Flow Ratio & Flow Entropy

> ### [flowratio](/source/flowratio.py).computeEntropy

We can use the output from the previous FINE evaluation to examine the effect that flow ratio (bad flow over good flow) has on flow entropy. Flow ratio represents the 'odds' of bad flow in the form of errors, defects, misaligned features, or anything else that the end user may not find valuable. Items of bad flow generally have to be corrected. This corrective re-work acts as an impediment that prevents new flow from being created on the next cycle. Flow entropy is the tendency for flow to reduce as impediments build up due to flow ratio.

In the example below, we use values for impediments and energy that were observed previously for the "StoreRO" team in the FINE flow evaluation of the Bakers Unlimited organization. These values are 0.0599 and 0.625 respectively. Using a flow ratio of 0.1 (1 unit of bad flow over 10 units of good flow), a batch size of 1, a maximum energy of 1, computing for 10 cycles, and attempting to keep flow constant, we can see that flow entropy starts to occur after 5 cycles. When maximum energy is reached, constant flow can no longer be sustained as impediments continue to rise. Under these conditions, we can state that the "StoreRO" team has a resilience of 5 cycles. They will see flow start to reduce at this point. The team should take a stabilization break after the 5th cycle to remove excess impediments that have accumulated in the form of technical debt. This will allow flow levels to be regained to the original starting value. Flow for the team can be efficiently managed when they recognize the limit before which flow entropy occurs. The test below demonstrates the use of the flow ratio module to simulate flow entropy for the “StoreRO” team:

```python
    def test_whenGivenBUExampleWithCappedEnergyThenFlowDecreasesAsExpected(self):

        flowEntropy = fr.computeEntropy(bad=1, good=10, batchSize=1, cycles=10, imps=0.0599, energy=0.625, fixedFlow=True, energyMax=1)

        expected = {'ratio': 0.1,
                     1: {'flow': 3.2302, 'imps': 0.0599, 'need': 0.1935, 'energy': 0.625},
                     2: {'flow': 3.2302, 'imps': 0.0659, 'need': 0.2129, 'energy': 0.6876},
                     3: {'flow': 3.2302, 'imps': 0.0725, 'need': 0.2342, 'energy': 0.7565},
                     4: {'flow': 3.2301, 'imps': 0.0798, 'need': 0.2578, 'energy': 0.8326},
                     5: {'flow': 3.2302, 'imps': 0.0878, 'need': 0.2836, 'energy': 0.9161},
                     6: {'flow': 3.2174, 'imps': 0.0966, 'need': 0.3108, 'energy': 1},
                     7: {'flow': 3.0671, 'imps': 0.1063, 'need': 0.326,  'energy': 1},
                     8: {'flow': 2.9248, 'imps': 0.1169, 'need': 0.3419, 'energy': 1},
                     9: {'flow': 2.7886, 'imps': 0.1286, 'need': 0.3586, 'energy': 1},
                    10: {'flow': 2.6584, 'imps': 0.1415, 'need': 0.3762, 'energy': 1}}

        if flowEntropy != expected:
            print('\n07: Unexpected result! \nExpected:', expected, '\nInstead :', flowEntropy)

        assert flowEntropy == expected
```
## Contributing
> We welcome your contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to submit contributions to this project. 

## License
> This project is licensed under the [Apache 2.0 License](LICENSE).

## Additional Resources
The FINE Flow Tool Kit is the result of a research collaboration between Dr. Craig Statham of SAS, and Stephen Walters of GitLab. As experts in the field of Sofware Development, DevOps, and Value Stream Management, Statham and Walters found a joint curiosity around trying to understand why software teams work the way they do, and attempting to formulate the relationship that exists between flow of user value and team organization. The FINE flow model was born out of this curiosity and resulted in the tool kit you see here today. The authors welcome feedback and comments. Please feel free connect with them on LinkedIn.

[Dr. Craig Statham - SAS Institute Inc.](https://www.linkedin.com/in/craig-statham/)<br />
[Stephen Walters - GitLab Inc.](https://www.linkedin.com/in/1stephenwalters/)

## Further Reading

### Published Paper: Value Stream Reference Architecture (DevOps Institute)

If you would like to know more about the original research behind the FINE Flow Evaluation Tool Kit, a published paper by Statham and Walters is available. The paper can be accessed from the DevOps Institute through their (Free) "SKILup IT Learning Lite" site: https://www.devopsinstitute.com/skilup-it-learning/. Sign up to [access the site](https://member.devopsinstitute.com/skitl-lite-sign-up) and then select the lesson on "Value Stream Reference Architecure" using the link: https://skilupit.thinkific.com/courses/value-stream-reference-architecture-paper

### Book: Team Topologies

For background reading, the book "Team Topologies" by Matthew Skelton and Manuel Pais is highly recommended. This book was published by [ITRevolution](https://itrevolution.com/) and is available from [Amazon.com](https://a.co/d/gZXZWu7) and other good book sellers. The book describes the the foundation behind the four primary team types and the three main interaction styles that are referenced in this tool kit. Although Skelton & Pais are not in any way associated with the development of the FINE Flow Tool Kit, their book helped to inspire the original research work of Statham and Walters. Thanks is extended to Matthew and Manuel for sparking a curiosity which led to the development of the FINE flow team classification process.

## Copyright Notice
Copyright © 2023, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at:

> https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.