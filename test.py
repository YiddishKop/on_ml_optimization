# Nelder-Mead solver
from mystic.solvers import fmin

# Rosenbrock function
from mystic.models import rosen

# tools
from mystic.tools import getch
import pylab
pylab.ion()

# draw the plot
def plot_frame():
    pylab.title("Rosenbrock parameter convergence")
    pylab.xlabel("Nelder-Mead solver iterations")
    pylab.ylabel("parameter value")
    pylab.draw()
    return

iter = 0
step, xval, yval, zval = [], [], [], []
# plot the parameter trajectories
def plot_params(params):
    global iter, step, xval, yval, zval
    step.append(iter)
    xval.append(params[0])
    yval.append(params[1])
    zval.append(params[2])
    pylab.plot(step,xval,'b-')
    pylab.plot(step,yval,'g-')
    pylab.plot(step,zval,'r-')
    pylab.legend(["x", "y", "z"])
    pylab.draw()
    iter += 1
    return


if __name__ == '__main__':

    # initial guess
    x0 = [0.8,1.2,0.7]

    # suggest that the user interacts with the solver
    print("NOTE: while solver is running, press 'Ctrl-C' in console window")
    getch()
    plot_frame()

    # use Nelder-Mead to minimize the Rosenbrock function
    solution = fmin(rosen, x0, disp=1, callback=plot_params, handler=True) #<- HERE is the callback
    print(solution)

    # don't exit until user is ready
    getch()
