from typing import Optional

import numpy as np

from optimization_problem_inspector.bbob_functions import BenchmarkFunction


class GBBOB:
    """A General BBOB problem with any number of variables and objectives and either without constraints or with one
    inequality constraint. The problem is defined by the number of variables and two lists of dictionaries containing
    function and instance numbers for the objectives and constraints. The number of objectives is determined by the
    length of the first list. The second list can either be empty (no constraints) or have a single item.

    The inequality constraint is constructed by shifting the corresponding BBOB function vertically so that part of the
    search space is feasible and part infeasible. The vertical shift is calculated as follows:
        constr_v_shift = - (f_opt + 2 * feas_degree * (f_sample_avg - f_opt)),
    where f_opt is the optimum of the objective function, feas_degree is a number between 0 (no solutions are feasible)
    and 1 (many solutions are feasible) and f_sample_avg is the average objective function value of the feas_n_samples
    samples. The samples are drawn randomly from [-5, 5]^n_var with a uniform distribution. The random seed is fixed to
    the instance number of the constraint.

    When evaluated at solution x, the problem returns a dictionary with the following keys:
    'F': A numpy array containing the objective function values
    'G': A numpy array containing the constraint function value (empty if no constraints are defined)
    'V': A numpy array containing the constraint violation value (contains zero if no constraints are defined)

    :param n_var: Number of variables.
    :param objs: A list of dictionaries containing function and instance numbers for the objective functions.
    :param ineq_const: An empty list (no constraints) or a list with a single dictionary containing function and
    instance numbers for the inequality constraint.
    :param feas_degree: A number between 0 (no solutions are feasible) and 1 (many solutions are feasible) that is
    used to determine the degree of feasibility for the inequality constraint.
    :param feas_n_samples: Number of samples used to determine the degree of feasibility for the inequality constraint.
    """  # noqa E501

    def __init__(
        self,
        n_var: int,
        objs: list,
        ineq_const: Optional[list] = None,
        feas_degree: float = 0.5,
        feas_n_samples: int = 100,
    ):
        def _check_func_inst(
            func_inst: list,
            min_len: Optional[list] = None,
            max_len: Optional[list] = None,
        ):
            if min_len is not None and len(func_inst) < min_len:
                raise ValueError(
                    f"The list of function instances {func_inst}"
                    f" must contain at least {min_len} items."
                )
            if max_len is not None and len(func_inst) > max_len:
                raise ValueError(
                    f"The list of function instances {func_inst}"
                    f" must contain at most {max_len} items."
                )
            for f_i in func_inst:
                if not isinstance(f_i, dict):
                    raise ValueError(
                        "The function instances must be dictionaries."
                    )
                if "f" not in f_i:
                    raise ValueError(
                        'The function instances must have a key "f"'
                        " for the function number."
                    )
                if "i" not in f_i:
                    raise ValueError(
                        'The function instances must have a key "i"'
                        "for the instance number."
                    )
                if not isinstance(f_i["f"], int):
                    raise ValueError("The function number must be an integer.")
                if not isinstance(f_i["i"], int):
                    raise ValueError("The instance number must be an integer.")
                if f_i["f"] < 1 or f_i["f"] > 24:
                    raise ValueError(
                        "The function number must be between 1 and 24."
                    )
                if f_i["i"] < 1:
                    raise ValueError(
                        "The instance number must be larger than 0."
                    )

        # Check number of variables and lists of objectives and constraints
        if n_var < 1:
            raise ValueError("The problem must have at least one variable.")
        _check_func_inst(objs, min_len=1)
        if ineq_const is None:
            ineq_const = []
        _check_func_inst(ineq_const, max_len=1)
        # Check feasibility degree and number of samples
        if not 0 <= feas_degree <= 1:
            raise ValueError("The feasibility degree must be between 0 and 1.")
        if feas_n_samples < 1:
            raise ValueError("The number of samples must be at least 1.")

        self.n_var = n_var
        self.n_obj = len(objs)
        self.n_iqc = len(ineq_const)
        self.name = f"GBBOB(n={self.n_var} m={self.n_obj} k={self.n_iqc})"
        self.fn = []

        # Ideal point for the unconstrained function
        self.unconstr_ideal_point = []

        name_f = ", F=["
        for obj in objs:
            f = obj["f"]
            i = obj["i"]
            # Create the benchmark functions for the objectives
            p = BenchmarkFunction(
                "bbob", dimension=n_var, function=f, instance=i
            )
            name_f += f"f{f}_i{i}, "
            self.fn.append(p)
            self.unconstr_ideal_point.append(p.best_value())
        name_f = name_f[:-2] + "]"

        name_g = ", G=["
        if len(ineq_const) == 1:
            f = ineq_const[0]["f"]
            i = ineq_const[0]["i"]
            # Create the benchmark functions for the inequality constraint
            p = BenchmarkFunction(
                "bbob", dimension=n_var, function=f, instance=i
            )
            self.fn.append(p)
            name_g += f"f{f}_i{i}"
        name_g += "]"

        self.unconstr_ideal_point = np.array(self.unconstr_ideal_point)
        self.name = f"{self.name}{name_f}{name_g}"

        self.constr_v_shift = 0
        # Calculate the vertical shift for the inequality constraint
        if self.n_iqc > 0:
            # Use instance number for random seed
            np.random.seed(ineq_const[0]["i"])
            # Sample points from the search space
            x = np.random.uniform(-5, 5, size=(feas_n_samples, n_var))
            # Calculate the average objective function value of the samples
            f_avg = np.average(self.fn[-1](x))
            # Calculate the vertical shift (to be used in evaluation)
            self.constr_v_shift = -(
                self.fn[-1].best_value()
                + 2 * feas_degree * (f_avg - self.fn[-1].best_value())
            )

    def __call__(self, x, *args, **kwargs):
        return self._evaluate(x)

    def __str__(self):
        return self.name

    def evaluate(self, x):
        return self._evaluate(x)

    def has_constraints(self):
        return self.n_iqc > 0

    def is_feasible(self, x):
        return self._evaluate(x)["V"] == 0.0

    def _evaluate(self, x):
        """Evaluates the problem in solution x. Shifts the constraint function so that it is feasible for a fraction of
        solutions.

        Returns a dictionary with the objective function values, the constraint function value, and the constraint
        violation.
        """  # noqa E501
        ys = []
        for fn in self.fn:
            y = fn(x)
            y = y.copy(order="C")
            ys.append(y)
        y = np.array(ys)
        f, g = y[: self.n_obj], y[self.n_obj :]  # noqa E203
        v = np.zeros(1)
        if self.has_constraints():
            g += self.constr_v_shift
            v = np.maximum(v, g)

        result = {"F": f, "G": g, "V": v}
        return result


if __name__ == "__main__":
    problem = GBBOB(
        n_var=2,
        objs=[{"f": 1, "i": 1}, {"f": 2, "i": 2}],
        ineq_const=[{"f": 3, "i": 3}],
    )
    print(
        f"{problem} unconstrained ideal point = {problem.unconstr_ideal_point}"
        " constraint vertical shift ="
        f" {problem.constr_v_shift}"
    )

    problem = GBBOB(
        n_var=12,
        objs=[{"f": 1, "i": 11}, {"f": 2, "i": 12}, {"f": 3, "i": 13}],
    )
    print(
        f"{problem} unconstrained ideal point = {problem.unconstr_ideal_point}"
        " constraint vertical shift ="
        f" {problem.constr_v_shift}"
    )
