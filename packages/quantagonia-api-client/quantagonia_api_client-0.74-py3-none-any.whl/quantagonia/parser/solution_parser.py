"""
Class to parse solution from file.
"""

class SolutionParser:

    def __init__(self):
        """Constructor."""
        pass

    @staticmethod
    def parse(solution_file):
        """
        Parse solution from file.
        """

        if not len(solution_file):  # if file is empty
            return None

        sol_as_list = solution_file.splitlines()

        if "Model status" in sol_as_list[0]:
            # MIP solution
            values = {}

            # find index of 'Primal solution values' keyword
            try:
                key_idx = sol_as_list.index("Primal solution values:")
            except ValueError:
                # no solution
                return values
            solution = sol_as_list[key_idx + 1 :]

            # split entries to have var name and value
            for l in solution:
                var_name, var_val = l.split()
                values[var_name] = float(var_val)

            return values

        else:
            # QUBO solution
            return {idx: val for idx, val in enumerate(sol_as_list)}
