import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use('Qt5Agg')  # Enables creating new graphs in debug (interactive)


def create_graphs(dfS, clmn):
    vc = pd.DataFrame(dfS[clmn].value_counts())
    top = 20

    ax = vc.head(top).plot.bar(rot=30, title=f"Top {top} {clmn}")

    sellers = pd.read_pickle("my_supermarket\\my_sellers.pkl") # Challenge, show top 20 salesmen.
    # top 20 bar graph with their names!
    plt.figure()
    plt.hist(dfS[clmn])
    plt.title(f"hist of {clmn}")
    plt.show()



