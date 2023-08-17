import matplotlib.pyplot as plt
plt.switch_backend('Qt5Agg')

x = [4, 5, 10, 4, 3, 11, 14, 8, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]


plt.scatter(x, y, c=classes)
# Example Scatter plot, on which we'll add a new point and test grouping by distance


# Import of Knn function, nearest neighbor.
from sklearn.neighbors import KNeighborsClassifier  # Classifier = Supervised learning

data = list(zip(x, y))
knn = KNeighborsClassifier(n_neighbors=1)  # means the rule is that the one closest neighbor is the classifier.

knn.fit(data, classes)  # This is the GT creation
# End Knn definition


def add_point_with_prediction(new_x, new_y):
    new_x = new_x
    new_y = new_y
    new_point = [(new_x, new_y)]

    prediction = knn.predict(new_point)

    x.append(new_x)
    y.append(new_y)
    classes.append(prediction[0])

    plt.scatter(x, y, c=classes)
    for i, c in enumerate(classes):
        plt.text(x=x[i] - 0.5, y=y[i], s=f"class: {classes[i]}")

    plt.text(x=new_x - 0.5, y=new_y - 0.7, s=f"new point, class: {prediction[0]}")


plt.show()


