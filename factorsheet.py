import sys

# cash flow factor calculator
def cf_factor(mode, value, interest, time_period) :
    # mode = cash flow factor mode
    # value = cash flow value coefficient
    # interest = interest rate in %
    # time_period = time period of interest
    # e.g. (fp, 100, 5, 4) = 100*(F/P, 5%, 4)
    if mode == ('fp' or '1'):
        return value*(1+interest/100)**time_period
    elif mode == ('pf' or '2'):
        return value/(1+interest/100)**time_period
    elif mode == ('pa' or '3'):
        return value*(((1+interest/100)**time_period-1)/(interest/100*(1+interest/100)**time_period))
    elif mode == ('ap' or '4'):
        return value/(((1+interest/100)**time_period-1)/(interest/100*(1+interest/100)**time_period))
    elif mode == ('af' or '5'):
        return value*((interest/100)/((1+interest/100)**time_period-1))
    elif mode == ('fa' or '6'):
        return value/((interest/100)/((1+interest/100)**time_period-1))
    else:
        return 'Error: Invalid mode'

def main():
    if len(sys.argv) != 5:
        print('Error: Invalid number of arguments \ne.g. : factorsheet.py fp 1 6 20')
        sys.exit(1)
    # get arguments
    mode = sys.argv[1]
    value = float(sys.argv[2])
    interest = float(sys.argv[3])
    time_period = float(sys.argv[4])
    # call cf_factor function
    print(round(cf_factor(mode, value, interest, time_period), 5))


if __name__ == '__main__':
    main()
