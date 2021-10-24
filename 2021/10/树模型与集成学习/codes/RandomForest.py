import numpy as np
from sklearn.metrics import accuracy_score, r2_score, mean_squared_error
from sklearn.datasets import make_classification, make_regression
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.ensemble import RandomForestRegressor as RFR
import sys
sys.path.append(".")
from CART import DecisionTreeClassifier, DecisionTreeRegressor

class RandomForestClassifier:
    def __init__(self, n_estimators, max_depth):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.trees = []

    def fit(self, X, y):
        for tree_id in range(self.n_estimators):
            index = np.random.randint(0, X.shape[0], X.shape[0])
            random_X = X[index]
            random_y = y[index]
            tree = DecisionTreeClassifier(self.max_depth)
            tree.fit(random_X, random_y)
            self.trees.append(tree)

    def predict(self, X):
        results = []

        for x in X:
            estimator_result = []
            for tree in self.trees:
                estimator_result.append(tree.predict(x.reshape(1, -1))[0])

            results.append(np.argmax(np.bincount(estimator_result)))
        return np.array(results)

class RandomForestRegressor:
    def __init__(self, n_estimators, max_depth):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.trees = []
    

    def fit(self, X, y):
        for tree_id in range(self.n_estimators):
            index = np.random.randint(0, X.shape[0], X.shape[0])
            random_X = X[index]
            random_y = y[index]
            tree = DecisionTreeRegressor(self.max_depth)
            tree.fit(random_X, random_y)
    

    def predict(self, X):
        results = []

        for x in X:
            estimator_result = []
            for tree in self.trees:
                estimator_result.append(tree.predict(x.reshape(1, -1))[0])

            results.append(np.mean(estimator_result))
        return np.array(results)


if __name__ == "__main__":
    X, y = make_classification(n_samples=200, n_features=8, n_informative=4, random_state=2)

    RF1 = RandomForestClassifier(n_estimators=10, max_depth=3)
    RF2 = RFC(n_estimators=10, max_depth=3)

    RF1.fit(X, y)
    res1 = RF1.predict(X)

    RF2.fit(X, y)
    res2 = RF2.predict(X)

    print('结果一样的比例', (np.abs(res1 - res2) < 1e-5).mean())

    X, y = make_regression(n_samples=200, random_state=2)

    RF1 = RandomForestRegressor(n_estimators=10, max_depth=3)
    RF2 = RFR(n_estimators=10, max_depth=3)

    RF1.fit(X, y)
    res1 = RF1.predict(X)

    RF2.fit(X, y)
    res2 = RF2.predict(X)

    print('r2', (r2_score(res1, res2)))
