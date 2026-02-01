# Solveconn

Welcome!

Solveconn is a python codebase that can be used to solve theoretical macroeconomic models. Specifically, it is constructed to solve dynamic stochastic general equilibrium (DSGE) models. A description of what it means to "solve" a DSGE model is left for the reader below. However, it should be noted before proceeding that this can already be done by a MATLAB package called Dynare. Dynare offers a means of solving DSGE models via a linear approximation around the model's steady state. This package differs in its methodology for solving such models, as described below. Although the solving methodology differs from Dynare, many of the features following the convergence to a solution are intended to be quite similar to Dynare. Particularly, the package can perform shocks on the system and simulate the return to steady state using the solution policy function. Additionally, this code base does not accept the .mod files that Dynare takes. However, it does accept .txt files that are in the exact same format. As such, all .mod files prepa red along the Dynare guidelines are completely valid for use with the Sovleconn codebase.




