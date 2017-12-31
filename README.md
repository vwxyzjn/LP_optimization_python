# Linear Programming for Optimal Scheduling

You may view the write up in PDF form **[Linear_Programming_for_Optimal_Scheduling.pdf](https://costahuang.me/files/Linear_Programming_for_Optimal_Scheduling.pdf)**
or the jupyter notebook **[here](https://github.com/vwxyzjn/LP_optimization_python/blob/master/Case%20--%20Scheduling%20Student%20Volunteers%20for%20the%20INFORMS%20Annual%20Meeting.ipynb)**

In the given case study for operations research, we need to produce a schedule that meets the following constraints

*   The schedule does not violate the volunteer's availability
*   The schedule meets the conference requirements for staffing

By using Gurobipy, a python optimization package, we were able to model this problem as a Linear Programming (LP) problem,
and hence produced an optimal solution through the simplex method.

