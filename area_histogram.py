def moving_average(a, n=3):
    import numpy as np
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


def area_histogram(alldat, mouseID=0, filter_size=1, brain_area=0):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    dat_filter = np.array(
        [moving_average(alldat[mouseID]['spks'][brain_area][i], filter_size) for i in range(len(alldat[mouseID]['spks'][brain_area]))])
    dat_filter[dat_filter > 1] = 1
    dat_filter_df = pd.DataFrame(dat_filter)
    plt.hist(dat_filter_df.sum(), bins=10)
    plt.show()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Plot distribution of spikes from a given area of a mouse")
    parser.add_argument('--data', type=str, help='The variable "alldat" from the Jupyter Notebook')
    parser.add_argument('--mouseID', type=str, help='The index for the mouse as in "alldat[11]" from the Jupyter Notebook')
    parser.add_argument('--filter_size', type=str, help='The size of window for moving average')
    parser.add_argument('--brain_area', type=str, help='The brain area given from the index of "alldat[mouseID]["brain_area"]" (next addition will try to take in brain area and create a distribution for all indices that have that brain area)')
    args = parser.parse_args()
    alldat = args.data
    mouseID = args.mouseID
    filter_size = args.filter_size
    brain_area = args.brain_area
    area_histogram(alldat, mouseID, filter_size, brain_area)
 
