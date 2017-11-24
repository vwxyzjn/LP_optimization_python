# Linear Programming for Optimal Scheduling

You may view the write up in PDF form **[here](https://github.com/vwxyzjn/LP_optimization_python/raw/master/writeup_latex/Case%2B--%2BScheduling%2BStudent%2BVolunteers%2Bfor%2Bthe%2BINFORMS%2BAnnual%2BMeeting.pdf)**
or the jupyter notebook **[here](https://github.com/vwxyzjn/LP_optimization_python/blob/master/Case%20--%20Scheduling%20Student%20Volunteers%20for%20the%20INFORMS%20Annual%20Meeting.ipynb)**

In the given case study for operations research, we needed to produce a schedule that meets the following constraints

*   The schedule does not violate the volunteer's availability
*   The schedule meets the conference requirements for staffing

By using Gurobipy, a python optimization package, we were able to model this problem as a Linear Programming (LP) problem,
and hence produce an optimal solution through the simplex method.

