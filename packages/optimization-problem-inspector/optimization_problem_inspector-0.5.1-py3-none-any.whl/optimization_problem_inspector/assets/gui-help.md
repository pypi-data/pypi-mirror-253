#### Using the {APP_NAME} ({APP_ACRONYM})

The {APP_ACRONYM} application comprises the following parts:

1. **{SEC_PROBLEM_SPECIFICATION}** contains the definition of the optimization problem.
2. **{SEC_SAMPLE_GENERATION}** supports generating sample data according to specifications from  {SEC_PROBLEM_SPECIFICATION}. Sample data can then be used by the evaluator software to populate output columns belonging to objectives, constraints and other output types.
3. **{SEC_DATA}**, here, data can be uploaded to the application for further analysis.
4. **{SEC_REFERENCE_PROBLEMS}** can be used to compare the uploaded data to the results on reference problems.
5. **{SEC_VIZUALIZATION}** supports visualization of the uploaded data.
6. **{SEC_HELP}** presents the application features.

For convenience, the application data is pre-populated by some sample data. This allows one to get familiar with the formats and application usage without specifying own data or running the evaluator software.

The majority of sections is collapsed by default to avoid over-populating the application screen. Clicking on the section name will either expand the whole section widget, when the widget is in the collapsed mode, or collapse the widget, when the widget is in the expanded mode.

When inspecting custom data, one usually interacts with section widgets in the order they are presented:

1. Upload the specification
2. Gather the data sample
3. Upload the evaluated data
4. Compare and visualize the evaluated data

Next, each step is described in more detail.

##### {SEC_PROBLEM_SPECIFICATION}

This part contains two widgets:

1. The upload file area.
2. The file contents preview area.

To upload a new problem specification, either click on the text `{DRAG_AND_DROP_OR_SELECT_FILES}`, which enables selecting the file to upload from the file manager, or simply drag and drop the problem specification file from the file manager to the upload area.

>
> _The problem specification should follow [this schema](https://repo.ijs.si/DIS-CI/optimization-problem-inspector/-/raw/main/specification/optimization_problem_inspector.schema.json)._
>

When the problem specification is uploaded, it is forwarded to the application server and deserialized. Observe application errors and/or alert boxes for cases when data is not in the format expected by {APP_ACRONYM}.

When specification upload and serialization succeeds, one can proceed to the next step.

##### {SEC_SAMPLE_GENERATION}

This part contains two widgets:

1. The inputs, which define the parameters for sampling.
2. The button `{SAMPLE_GENERATION_BUTTON}`, used to generate a sample and initiate its download to the local computer.

In the inputs area, sampler-specific parameters can be defined in the `{SEC_SAMPLE_GENERATION_PARAMETERS}` widget in the `yaml` format. The sampling method names need to be on the first level, while the second level lists parameter names and values for the corresponding method. An example of sampler-specific parameters input is:

```yaml
LHSSampler:
  random_seed: 42
RandomSampler:
  random_seed: 42
SobolSampler:
  random_seed: 42
```

The second input widget is a dropdown menu of sampling methods. Currently available options include:

1. `RandomSampler` - randomly sample instances from the possible combinations as defined in the problem specifications. This sampler works with any kind of variables.
2. `SobolSampler` - sample instances according to the Sobol sampling scheme. This sampler works with numerical variables and was adjusted to take into account integers and step values. Therefore, the sampling result will be rounded to the nearest valid value as defined by the specifications.
3. `LHSSampler` - sample instances according to the Latin hypercube sampling scheme. Again, the sampling scheme was adjusted so that the outputs are rounded to the nearest valid value according to the specifications. Like `SobolSampler`, `LHSSampler` can only be used with numerical variables.

The third widget is a number input widget, where sample size can be defined. 

> 
> _Note, the sampling size for the Sobol sampler should be a power of 2, otherwise it may lose its balance properties._
> 

After all the inputs are defined, one can obtain the sample by clicking the `{SAMPLE_GENERATION_BUTTON}` button.

##### {SEC_DATA}

This part contains two widgets:

1. The data upload area
2. The data preview area

To upload new data, either click on the text `{DRAG_AND_DROP_OR_SELECT_FILES}`, which enables selecting the file to upload from the file manager, or simply drag and drop the problem data file from the file manager to the upload area.

>
> _If there is a mismatch between the uploaded data and problem specification, errors will be shown. Consult the error for hints on what to change in the uploaded data file or specification._
>

In the data preview, the uploaded data is displayed in a paginated table. This enables one to manually check the data correctness, however, it cannot be used for filtering or other interactions that would influence further analysis.

##### {SEC_REFERENCE_PROBLEMS}

Here, some landscape features are computed on the provided data and compared to their values on the set of reference problems.

The part consists of input widgets and the output widgets. Among the input widgets, the following are available:

1. `{REF_PROBLEM_DEFINITIONS_LABEL}` - definitions of reference problems to use in the comparison, given in the `yaml` format.
2. `{SEC_REF_FEATURES_PARAMETERS}` - the parameters to use by the feature computation methods, given in the `yaml` format.
3. `{SEC_REF_FEATURES_SELECT}` - a multi-select widget for choosing which feature computation methods to use.
4. `{SEC_REF_FEATURES_PLOT}` button - used to initiate reference problem sampling and feature computation.

###### {REF_PROBLEM_DEFINITIONS_LABEL}

The default reference problem definition is as follows:

```yaml
ReferenceProblemsGBBOB:
  gbbob_definitions:
  - dimensions: 5
    feasibility_degree: 0.5
    feasibility_sample_size: 100
    ineq_const:
    - f: 1
      i: 3
    objectives:
    - f: 1
      i: 1
    - f: 1
      i: 2
  - dimensions: 5
    feasibility_degree: 0.5
    feasibility_sample_size: 100
    ineq_const:
    - f: 7
      i: 3
    objectives:
    - f: 7
      i: 1
    - f: 7
      i: 2
  - dimensions: 5
    feasibility_degree: 0.5
    feasibility_sample_size: 100
    ineq_const:
    - f: 12
      i: 3
    objectives:
    - f: 12
      i: 1
    - f: 12
      i: 2
  - dimensions: 5
    feasibility_degree: 0.5
    feasibility_sample_size: 100
    ineq_const:
    - f: 15
      i: 3
    objectives:
    - f: 15
      i: 1
    - f: 15
      i: 2
  - dimensions: 5
    feasibility_degree: 0.5
    feasibility_sample_size: 100
    ineq_const:
    - f: 22
      i: 3
    objectives:
    - f: 22
      i: 1
    - f: 22
      i: 2

```

See the [BBOB test suite](http://numbbo.github.io/coco/testsuites/bbob) for the definition of reference (test) functions. Test functions were extended to allow specification of a general BBOB problem with any number of variables and objectives and either without constraints or with one inequality constraint. The problem is defined by the number of variables and two lists containing function and instance numbers for the objectives (key `objectives`) and constraints (key `ineq_const`). Constraints list can be empty or have a single item.

The inequality constraint is constructed by shifting the corresponding BBOB function vertically so that part of the search space is feasible and part infeasible. The vertical shift is calculated as follows:

```
constr_v_shift = - (f_opt + 2 * feas_degree * (f_sample_avg - f_opt)),
```
where `f_opt` is the optimum of the objective function, `feas_degree` is a number between 0 (only the optimal solution is feasible) and 1 (many solutions are feasible) and `f_sample_avg` is the average objective function value of the `feas_n_samples` samples. The samples are drawn randomly from `[-5, 5]^n_var` with a uniform distribution. The random seed is fixed to the instance number of the constraint.

The number of variables (dimensions) and objectives is automatically obtained from the problem definition, e.g., if the problem definition specifies 3 input variables and 2 objectives, then the reference problems will all be defined with 3 input variables and 2 objectives.

Additional parameters for general BBOB problems include:

1. `feasibility_degree` - a number between 0 (only the optimal solution is feasible) and 1 (many solutions are feasible) that is used to determine the degree of feasibility for the inequality constraint.
2. `feasibility_sample_size` - a number of samples used to determine the degree of feasibility for the inequality constraint.

>
> _One may freely adjust the parameters, adding additional reference problems or removing them and using different function or functions instances. However, the number of input variables and objectives (but not constraints) need to match those in the problem specification. Errors will be raised if this is not respected._
>

###### {SEC_REF_FEATURES_PARAMETERS}

In this text input widget, the parameters to be used with the feature computation methods are specified in the `yaml` format. The default value is:

```yaml
neighbourhood_feats:
  number_neighbours: 10

```

The first level of the schema contains the feature computation method name, while the second level specifies  parameter names and values. All possible parameters are already defined in the default input text. One may only adjust the existing values. Consult [the code](https://repo.ijs.si/DIS-CI/optimization-problem-inspector/-/raw/main/optimization_problem_inspector/features.py) for further information about each parameter.

###### {SEC_REF_FEATURES_SELECT}

One can select the feature computation method from a multiselect dropdown menu with the following options:

1. `CorrObj` - correlation of objectives. To be used with numerical objectives.
1. `MinCV` - minimum constraint violation. To be used with numerical objectives.
1. `FR` - feasibility ratio.
1. `UPO_N` - percentage of non-dominated solutions (without taking into account the constraints).
1. `PO_N` - percentage of non-dominated feasible solutions.
1. `neighbourhood_feats` - features explaining the neighbourhood of solutions (e.g., how many neighbours of a solution dominate the solution, how many neighbours are dominated by the solution, how many are incomparable to the solution, how close the neighbouring solutions are, etc.)
1. `constr_obj_corr` - correlation of objectives and the total constraint violation.
1. `H_MAX` - information content for each objective.

>
> _Note that choosing several feature computation methods, especially those based on the non-dominance relation, may greatly increase computation time. This is especially the case when the sample sizes are large and several reference problems are used. Use with caution._
> 

###### {SEC_REFERENCE_PROBLEMS} outputs

After clicking the `{SEC_REF_FEATURES_PLOT}` button, the reference problems are sampled according to the sampling method specified in the `{SEC_SAMPLE_GENERATION}` part and the features are calculated for each specified feature computation method and problem data pair.

The feature values data are then presented in two ways:

1. Visualized with parallel coordinates, each coordinate being one feature value, and each line belonging to a particular problem. This enables one to visually compare the feature values and find reference problems that are most similar to the custom one. By clicking the link `{DOWNLOAD_FIGURE_AS_HTML_BUTTON}` below the parallel coordinates figure, one can save the generated plot to the local computer.
2. Displayed in a table, collapsed by default, in `{REF_PROBLEM_TABLE_NAME}`. Clicking the text expands the table for viewing. The table contains the problem name, feature name and feature value columns. The data displayed in the table can be downloaded by clicking the link `{DOWNLOAD_DATA_AS_CSV_BUTTON}` just below the table.

##### {SEC_VIZUALIZATION}

This part comprises:

1. Input options for setting visualization parameters:
    1. Visualization method - select one of the two available visualization methods from the dropdown menu.
    2. {SEC_VIZUALIZATION_DIMENSION_SELECT} - select data columns to visualize.
    3. {SEC_VIZUALIZATION_SPECIFICATION} - set further plotting parameters.
2. The visualization according to the input settings and the link just below the figure {DOWNLOAD_FIGURE_AS_HTML_BUTTON} that can be used to save it to the local computer.

###### Visualization method

Currently available options are:

1. `scatter_matrix`
2. `parallel_coordinates`

Both options enable extensive brushing and exploration of the data and other interactivity options, using the  [Plotly library](https://plotly.com/python/).

###### {SEC_VIZUALIZATION_DIMENSION_SELECT}

This multi-select dropdown menu enables one to select the columns for plotting.

>
> _Note, a large number of columns combined with many data points may reduce the responsiveness of the figure interactivity and slow down your device used for accessing the application._
>

###### {SEC_VIZUALIZATION_SPECIFICATION}

Additional plot options can be specified in the `yaml` format to enable easier and more responsive exploration of data. The default plot options are:

```yaml
bounds:
    V:
        min: 0.0
        max: 55.98194147582009
display:
    color-dimension: V
    z-order:
        dimension: V
        ascending: true
    color-map: plasma
```

One may alter the values in the default plot options and/or modify the bounds by specifying the bounds name (`V` in the case above) and corresponding `min` and `max` values. Setting the `min` and `max` values to `-inf` or `inf`, respectively, effectively does not enforce any bounding.

>
> _Use the bounds to reduce the number of points visualized, which should improve figure interactivity._
>

Additional adjustable properties include:

1. `color-dimension` sets the name of the column to be used for the color map.
2. `z-order` enables one to display certain points before or behind the other points. E.g., using `dimension: V` and `ascending: true`, will display points with higher values of `V` above those points with lower values of `V`. In other words, points are plotted in order from low to high `V` values.
3. `color-map` specifies the color map to use when plotting. Consult [plotly documentation](https://plotly.com/python/colorscales/) for available options.


##### {SEC_HELP}

This section contains documentations that may prove useful when using {APP_ACRONYM}. Happy inspecting!
