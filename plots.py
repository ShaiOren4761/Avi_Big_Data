import matplotlib.pyplot as plt
import pandas as pd
plt.switch_backend('Qt5Agg')  # Enables creating new graphs in debug (interactive)


def create_graphs(dfS, clmn):
    vc = pd.DataFrame(dfS[clmn].value_counts())
    top = 20

    ax = vc.head(top).plot.bar(rot=30, title=f"Top {top} {clmn}")

    plt.figure()
    plt.hist(dfS[clmn])
    plt.title(f"hist of {clmn}")
    plt.show()
