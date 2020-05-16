import csv
import numpy as np

from sklearn import svm, tree
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier, RadiusNeighborsClassifier
from sklearn.model_selection import StratifiedKFold, StratifiedShuffleSplit, cross_val_score

filename = "log.txt"

csvfile = open(filename)
reader = csv.reader(csvfile, delimiter="|")

challenges = []
output = []

for line in reader:
    c = [int(n) for n in line[0].strip('()').split(',')]
    challenges.append(np.array(c))

    output.append(int(line[1]))

X = np.array(challenges)
Y = np.array(output)


# Define validation constants
k_fold = StratifiedShuffleSplit(3, random_state=0)
#SCORING = ["recall_micro", "precision_micro", "accuracy", "f1_micro", "recall_macro", "precision_macro", "f1_macro", "recall_weighted", "precision_weighted", "f1_weighted"]
SCORING = ["recall_weighted", "precision_weighted", "f1_weighted"]
N_NEIGHBORS = 3
classifiers = {
    'svc': svm.SVC(gamma=0.001, C=100.),
    'DT': tree.DecisionTreeClassifier(),
    'RF': RandomForestClassifier(n_estimators=50, max_depth=20, random_state=3),
    'KNN': KNeighborsClassifier(n_neighbors=N_NEIGHBORS),
    'KNNd': KNeighborsClassifier(n_neighbors=N_NEIGHBORS, weights='distance'),
    'AdaBoost': AdaBoostClassifier(n_estimators=100)
}

for clf_name in classifiers:
    clf = classifiers[clf_name]
    print("Classifier:", clf_name)

    for score in SCORING:
        scores = cross_val_score(clf, X, Y, cv=k_fold, n_jobs=-1, scoring=score)
        print("\t\t", score, ":\t", scores.mean())
