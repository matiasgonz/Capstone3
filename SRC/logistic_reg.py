from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn import metrics
from split_2 import *

def logistic():

    X_train, X_test, y_train, y_test = time_test_split(wind=False)

    log_reg = LogisticRegression(random_state=0, n_jobs=-1)
    logreg.fit(X_train, y_train)

    y_pred = logreg.predict(X_test)
    print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

    return()
    