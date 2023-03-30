import numpy as np

def main():

    uniform10 = np.random.uniform(-1, 1, size=10)
    uniform10000 = np.random.uniform(-1, 1, size=10000)

    gaus10 = np.random.normal(loc=0.0, scale=1.0, size=10)
    gaus10000 = np.random.normal(loc=0.0, scale=1.0, size=10000)

    print(uniform10)
    print(gaus10)

    print('uniform10 mean : {}'.format(uniform10.mean()))
    print('gaus10 mean : {}'.format(gaus10.mean()))

    print('uniform1000 mean : {}'.format(uniform10000.mean()))
    print('gaus10000 mean : {}'.format(gaus10000.mean()))

if __name__=='__main__':
    main()