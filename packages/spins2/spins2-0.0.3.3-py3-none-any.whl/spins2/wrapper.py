import argparse, os, numba, platform
import numpy as np
from spins2 import __version__

def main():
    parser = argparse.ArgumentParser(description='spins2: A Monte Carlo Simulation Code for the Phase Transition in 2D/3D Materials',
                                     epilog='''
configurations:       init:                                 parameters:
square                fm, afm1, afm2, afm3                  Ja, Jb, Jc
bilayer-ab            fm, afm1, afm2, afm3, afm4, afm5      J0, J1, Ja, Jb, J1_
triangular            fm, afm1, afm2, afm3                  Ja, Jb, Jc

default values:
x, y, z = 64, 64, 64
iterations for equilibrium, works = 1000, 1000
exchange coupling (meV) = 1.0
single-ion anisotropy (meV) = 0.1
temperatures = 35

Example:
spins2 -x 100 -y 100 -e 2000 -w 5000 -n 8 -t 35 -r
''',
    formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-v', "--version",      action="version", version="spins2 "+__version__+" from "+os.path.dirname(__file__)+' (python'+platform.python_version()+')')
    parser.add_argument('-n', "--np",           type=int,   default=4   )
    parser.add_argument('-x', "--length",       type=int,   default=64  )
    parser.add_argument('-y', "--width",        type=int,   default=64  )
    parser.add_argument('-z', "--height",       type=int,   default=64  )
    parser.add_argument('-e', "--equilibrium",  type=int,   default=1000)
    parser.add_argument('-w', "--works",        type=int,   default=1000)
    parser.add_argument('-a', "--single",       type=float, default=None,  nargs='*')
    parser.add_argument('-p', "--parameters",   type=float, default=[1.0], nargs='+')
    parser.add_argument('-j', "--parameterX",   type=float, default=[],    nargs='+')
    parser.add_argument('-k', "--parameterY",   type=float, default=[],    nargs='+')
    parser.add_argument('-t', "--temperatur",   type=float, default=[35],  nargs='+')
    parser.add_argument('-l', "--labl",         type=str,   default='',    help='图例')
    parser.add_argument('-r', "--export",       action='store_true',       help="结束后绘图")
    parser.add_argument('-o', "--plot",         type=str,                  help="日志文件绘图")
    parser.add_argument('-f', "--format",       default="png",             type=str.lower, choices=['png', 'pdf', 'svg', 'jpg', 'tif'])
    parser.add_argument('-i', "--init",         default="fm",              type=str.lower, choices=['fm', 'afm1', 'afm2','afm3', 'afm4', 'afm5', 'random'])
    parser.add_argument('-c', "--config",       default="square",          type=str.lower, choices=['square', 'bilayer-ab', 'triangular'])
    args = parser.parse_args()

    NP = args.np
    numba.set_num_threads(NP)

    X = check(args.length)
    Y = check(args.width)
    Z = check(args.height)
    config = args.config
    init = args.init

    arrays_temperatures = temperatures(args.temperatur)

    nequilibrium = args.equilibrium
    nworks       = args.works
    J  = args.parameters
    JX = args.parameterX
    JY = args.parameterY
    format = args.format
    legend = args.labl

    if args.plot and os.path.exists(args.plot):
        from spins2 import plots
        plots.main(args.plot, format, legend)
    else:
        if args.single is not None:
            A = [0.1] if args.single == [] else args.single
            if config == "square":
                file = '{}_single_{}_{}.log'.format(config, X, Y)
                from spins2.single import square
                square.run(file, init, X, Y, J, A, arrays_temperatures, nequilibrium, nworks)
            elif config == "bilayer-ab":
                file = '{}_single_{}_{}.log'.format(config, X, Y)
                from spins2.single import bilayer_ab
                bilayer_ab.run(file, init, X, Y, J, A, arrays_temperatures, nequilibrium, nworks)
            elif config == "triangular":
                file = '{}_single_{}_{}.log'.format(config, X, Y)
                from spins2.single import triangular
                triangular.run(file, init, X, Y, J, A, arrays_temperatures, nequilibrium, nworks)
            else:
                print("Inconsistent parameters...")
        else:
            if config == "square":
                file = '{}_Ising_{}_{}.log'.format(config, X, Y)
                from spins2.ising import square
                square.run(file, init, X, Y, J, arrays_temperatures, nequilibrium, nworks)
            elif config == "bilayer-ab":
                file = '{}_Ising_{}_{}.log'.format(config, X, Y)
                from spins2.ising import bilayer_ab
                bilayer_ab.run(file, init, X, Y, J, arrays_temperatures, nequilibrium, nworks)
            elif config == "triangular":
                file = '{}_Ising_{}_{}.log'.format(config, X, Y)
                from spins2.ising import triangular
                triangular.run(file, init, X, Y, J, arrays_temperatures, nequilibrium, nworks)
            else:
                print("Inconsistent parameters...")

        if args.export and os.path.exists(file):
            from spins2 import plots
            plots.main(file, format, legend)

def check(num):
    if num < 10:
        num = 10
    if num % 2 != 0:
        num += 1
    if num % 4 != 0:
        num += 2
#    if num % 8 != 0:
#        num += 4
    return num

def temperatures(arr_temperatures):
    i = len(arr_temperatures)
    if i == 1:
        return np.arange(arr_temperatures[0]+1)
    elif i == 2:
        return np.arange(arr_temperatures[0], arr_temperatures[1]+1)
    else:
        k = i // 3
        l = i % 3
        j = 0
        while j < k:
            if j == 0:
                arrays_temperatures = np.arange(arr_temperatures[0], arr_temperatures[1], arr_temperatures[2])
            else:
                arrays_temperatures=np.concatenate((arrays_temperatures,
                    np.arange(arr_temperatures[j * 3], arr_temperatures[j * 3 + 1], arr_temperatures[j * 3 + 2])))
            if arrays_temperatures[-1] != arr_temperatures[j * 3 + 1]:
                arrays_temperatures = np.append(arrays_temperatures, arr_temperatures[j * 3 + 1])
            j += 1
        if l == 2:
            arrays_temperatures=np.concatenate((arrays_temperatures,
                np.arange(arr_temperatures[j * 3], arr_temperatures[j * 3 + 1]+1)))
        return arrays_temperatures
