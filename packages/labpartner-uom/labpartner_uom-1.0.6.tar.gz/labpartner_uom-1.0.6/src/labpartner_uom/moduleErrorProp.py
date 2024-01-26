import sympy as sp


class errorpropagator:

    @staticmethod
    def propagate_error(func, vars):

        # func: Function f(x, y, z, ...)
        # vars: List of variables, like x or t

        f = sp.parsing.sympy_parser.parse_expr(func)

        # Convert input variables to sympy symbols
        vars = [sp.Symbol(var) for var in vars]

        # Differentiate function with respect to each variable
        derivs = [sp.diff(f, var) for var in vars]

        # Format output
        output = "Δf = "

        if len(vars) == 1:

            output += str(derivs[0]) + " Δ" + str(vars[0])

        else:

            output += "sqrt("

            for i in range(len(vars)):

                err_individual = str(derivs[i]) + " Δ" + str(vars[i])
                output += "(" + err_individual + ")**2"

                if i < (len(vars) - 1):

                    output += " + "

                else:

                    output += ")"

        return output

    @staticmethod
    def print_help():

        startup_info = """
        Error Propagation Tool
        ----------------------
        This software uses the SymPy module to symbolically
        differentiate functions to derive the for the error
        on the dependant variable.

        Usage
        -----
        To use this software, run the following command:
        import labpartner_uom as lp
        lp.errorpropagator.propagate_error(func, vars)

        Where func is the function you wish to differentiate
        and vars is a list of variables in the function.

        Example
        -------
        import labpartner_uom as lp
        prop = lp.errorpropagator.propagate_error("x**2 * y", ["x", "y"])

        Inputting Common Functions
        --------------------------
        coefficient : ax = a*x
        polynomials : x^b = x**b
        exponential : e^(x) = exp(x)
        logarithmic : ln(x) =  log(x), log_b(x) = log(x, b)
        trig functs : sin(x) = sin(x), cos(x) = cos(x), tan(x) = tan(x)
        square root : √x = sqrt(x)

        Greek Alphabet (For Variables)
        ------------------------------
        Α α, Β β, Γ γ, Δ δ, Ε ε, Ζ ζ, Η η, Θ θ,
        Ι ι, Κ κ, Λ λ, Μ μ, Ν ν, Ξ ξ, Ο ο, Π π,
        Ρ ρ, Σ σ, Τ τ, Υ υ, Φ φ, Χ χ, Ψ ψ, Ω ω"""

        print(startup_info)
