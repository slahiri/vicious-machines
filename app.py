from flask import request, url_for, json, jsonify
from flask.ext.api import FlaskAPI, status, exceptions
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier


app = FlaskAPI(__name__)

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38],
     [154, 54, 37], [166, 65, 40], [190, 90, 47],
     [175, 64, 39], [177, 70, 40], [159, 55, 37],
     [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female',
     'female', 'male', 'male',
     'female', 'female', 'female',
     'male', 'male']

ml = {
    0: ['Classification', '/classify/']
}

classifiers = {
    0: ['DecisionTreeClassifier', '/classify/', {'key': 0, 'height': 170, 'weight': 70, 'shoe': 43}],
    1: ['KNeighborsClassifier', '/classify/', {'key': 1, 'height': 170, 'weight': 70, 'shoe': 43}],
    2: ['LogisticRegression', '/classify/', {'key': 2, 'height': 170, 'weight': 70, 'shoe': 43}],
    3: ['GaussianNB', '/classify/', {'key': 3, 'height': 170, 'weight': 70, 'shoe': 43}],
    4: ['RandomForestClassifier', '/classify/', {'key': 4, 'height': 170, 'weight': 70, 'shoe': 43}],
}


@app.route("/", methods=['GET'])
def ml_list():
    return [{'model': ml[idx][0], 'url': ml[idx][1]}
            for idx in sorted(ml.keys())]


@app.route("/classify/", methods=['GET', 'POST'])
def gender_classify():
    if request.method == 'POST':
        key = request.data.get('key');
        height = request.data.get('height');
        weight = request.data.get('weight');
        shoe = request.data.get('shoe');
        if key == 0:
            clf = DecisionTreeClassifier()
            clf = clf.fit(X, Y)
            prediction = clf.predict([[height, weight, shoe]])
            return {'gender': prediction[0]}
        elif key == 1:
            neigh = KNeighborsClassifier(n_neighbors=3)
            neigh = neigh.fit(X, Y)
            prediction = neigh.predict([[height, weight, shoe]])
            return {'gender': prediction[0]}
        elif key == 2:
            neigh = LogisticRegression()
            neigh = neigh.fit(X, Y)
            prediction = neigh.predict([[height, weight, shoe]])
            return {'gender': prediction[0]}
        elif key == 3:
            gnb = GaussianNB()
            gnb = gnb.fit(X, Y)
            prediction = gnb.predict([[height, weight, shoe]])
            return {'gender': prediction[0]}
        elif key == 4:
            clf = RandomForestClassifier(n_estimators=2)
            clf = clf.fit(X, Y)
            prediction = clf.predict([[height, weight, shoe]])
            return {'gender': prediction[0]}
        else:
            return '{}', status.HTTP_204_NO_CONTENT

    return [{'classifier_type': classifiers[idx][0], 'url': classifiers[idx][1], 'sample': classifiers[idx][2]}
            for idx in sorted(classifiers.keys())]


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
