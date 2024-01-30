py-graph-match
===================

Matching with Graph

`grma`` is a package for finding HLA matches using graphs approach.
The matching is based on [grim's](https://github.com/nmdp-bioinformatics/py-graph-imputation) imputation.


## Pre-requisites

### Data Directory Structure

```
data
├── donors_dir
│   └── donors.txt
├── hpf.csv
└── patients.txt
```

### conf Directory Structure

```
conf
└── minimal-configuration.json
```

Follow these steps for finding matches:

Setup a virtual environment (venv) and run:
```
make install
```

## Quick Getting Started

Get Started with a built-in example.

### Build 'Donors Graph'

```
python test_build_donors_graph.py
```

### Find Matches

Use grma algorthm for finding matches efficiently. You can run the file `test_matching.py`
```
python test_matching.py
```

Find the match results in `results` directory.

# Full Walk through
### Building The Donors' Graph:

The donors' graph is a graph which contains all the donors (the search space). It implemented using a LOL (List of Lists) representation written in cython for better time and memory efficiency.
The building might take a lot of memory and time, so it's recommended to save the graph in a pickle file.

Before building the donors' graph, all the donors' HLAs must be imputed using `grim`.
Then all the imputation files must be saved under the same directory.

```python
import os
from grma.donorsgraph.build_donors_graph import BuildMatchingGraph

PATH_TO_DONORS_DIR = "data/donors_dir"
PATH_TO_DONORS_GRAPH = "output/donors_graph.pkl"

os.makedirs(f"output", exist_ok=True)

build_matching = BuildMatchingGraph(PATH_TO_DONORS_DIR)
graph = build_matching.graph  # access the donors' graph

build_matching.to_pickle(PATH_TO_DONORS_GRAPH)  # save the donors' graph to pickle
```

### Search & Match before imputation to patients
The function `matching` finds matches up to 3 mismatches and return a `pandas.DataFrame` object of the matches sorted by number of mismatches and their score.

The function get these parameters:
* match_graph: a grma donors' graph object - `grma.match.Graph`
* grim_config_file: a path to `grim` configuration file


```python
from grma.match import Graph, matching

PATH_TO_DONORS_GRAPH = "output/donors_graph.pkl"
PATH_CONGIF_FILE = "conf/minimal-configuration.json"


# The donors' graph we built earlier
donors_graph = Graph.from_pickle(PATH_TO_DONORS_GRAPH)


# matching_results is a dict - {patient_id: the patient's result dataframe}
matching_results = matching(donors_graph,PATH_CONGIF_FILE, search_id=1, donors_info=[],
                                    threshold=0.1, cutoff=100, save_to_csv=True, output_dir="results")

```

`matching` takes some optional parameters, which you might want to change:

* search_id: An integer identification of the search. default is 0.
* donors_info: An iterable of fields from the database to include in the results. default is None.
* threshold: Minimal score value for a valid match. default is 0.1.
* cutof: Maximum number of matches to return. default is 50.
* verbose: A boolean flag for whether to print the documentation. default is False
* save_to_csv: A boolean flag for whether to save the matching results into a csv file. default is False.  If the field is set to True, upon completion of the function, it will generate a directory named `search_1`
* `output_dir`: output directory to write match results file to

### Search & Match after imputation to patients

The function `find_mathces` find matches up to 3 mismatches and return a `pandas.DataFrame` object of the matches
 sorted by number of mismatches and their score.

They get these parameters:
* imputation_filename: a path to the file of the patients' typing.
* match_graph: a grma donors' graph object - `grma.match.Graph`

```python
from grma.match import Graph, find_matches

PATH_TO_PATIENTS_FILE = "data/patients_file.txt"
PATH_TO_DONORS_GRAPH = "output/donors_graph.pkl"

# The donors' graph we built earlier
donors_graph = Graph.from_pickle(PATH_TO_DONORS_GRAPH)
matching_results = find_matches(PATH_TO_PATIENTS_FILE, donors_graph)

# matching_results is a dict - {patient_id: the patient's result dataframe}

for patient, df in matching_results.items():
    # Use here the dataframe 'df' with the results for 'patient'
    print(patient, df)
```

`find_matches` takes some optional parameters, which you might want to change:
* search_id: An integer identification of the search. default is 0.
* donors_info: An iterable of fields from the database to include in the results. default is None.
* threshold: Minimal score value for a valid match. default is 0.1.
* cutof: Maximum number of matches to return. default is 50.
* verbose: A boolean flag for whether to print the documentation. default is False
* save_to_csv: A boolean flag for whether to save the matching results into a csv file. default is False.
If the field is set to True, upon completion of the function, it will generate a directory named `Matching_Result
s_1`.
* calculate_time: A boolean flag for whether to return the matching time for patient. default is False.
  In case `calculate_time=True` the output will be dict like this: `{patient_id: (results_dataframe, time)}`
* `output_dir`: output directory to write match results file to

### Set Database
In order to get in the matching results more information about the donors than the matching information,
one can set a database that has all the donors' information in it.
The database must be a `pandas.DataFrame` that its indexes are the donors' IDs.

After setting the database, when calling one of the matching functions,
you may set in the `donor_info` variable a `list` with the names of the columns you want to join to the result dataframe from the database.

Example of setting the database:

```python
import pandas as pd
from grma.match import set_database

donors = [0, 1, 2]
database = pd.DataFrame([[30], [32], [25]], columns=["Age"], index=donors)

set_database(database)
```


# How to contribute:

1. Fork the repository: https://github.com/nmdp-bioinformatics/py-graph-match.git
2. Clone the repository locally
    ```shell
    git clone  https://github.com/<Your-Github-ID>/py-graph-match.git
    cd py-graph-match
    ```
3. Make a virtual environment and activate it, run `make venv`
   ```shell
    > make venv
      python3 -m venv venv --prompt urban-potato-venv
      =====================================================================
    To activate the new virtual environment, execute the following from your shell
    source venv/bin/activate
   ```
4. Source the virtual environment
   ```shell
   source venv/bin/activate
   ```
5. Development workflow is driven through `Makefile`. Use `make` to list show all targets.
   ```
    > make
    clean                remove all build, test, coverage and Python artifacts
    clean-build          remove build artifacts
    clean-pyc            remove Python file artifacts
    clean-test           remove test and coverage artifacts
    lint                 check style with flake8
    behave               run the behave tests, generate and serve report
    pytest               run tests quickly with the default Python
    test                 run all(BDD and unit) tests
    coverage             check code coverage quickly with the default Python
    dist                 builds source and wheel package
    docker-build         build a docker image for the service
    docker               build a docker image for the service
    install              install the package to the active Python's site-packages
    venv                 creates a Python3 virtualenv environment in venv
    activate             activate a virtual environment. Run `make venv` before activating.
   ```
6. Install all the development dependencies. Will install packages from all `requirements-*.txt` files.
   ```shell
    make install
   ```
7. The Gherkin Feature files, step files and pytest files go in `tests` directory:
    ```
    tests
    |-- features
    |   |-- algorithm
    |   |   `-- SLUG\ Match.feature
    |   `-- definition
    |       `-- Class\ I\ HLA\ Alleles.feature
    |-- steps
    |   |-- HLA_alleles.py
    |   `-- SLUG_match.py
    `-- unit
        `-- test_py-graph-match.py
    ```
8. Package Module files go in the `py-graph-match` directory.
    ```
    py-graph-match
    |-- __init__.py
    |-- algorithm
    |   `-- match.py
    |-- model
    |   |-- allele.py
    |   `-- slug.py
    `-- py-graph-match.py
    ```
9. Run all tests with `make test` or different tests with `make behave` or `make pytest`. `make behave` will generate report files and open the browser to the report.
10. Use `python app.py` to run the Flask service app in debug mode. Service will be available at http://localhost:8080/
11. Use `make docker-build` to build a docker image using the current `Dockerfile`.
12. `make docker` will build and run the docker image with the service.  Service will be available at http://localhost:8080/
