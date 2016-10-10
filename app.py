from flask import request, url_for, json, jsonify
from flask.ext.api import FlaskAPI, status, exceptions
from sklearn import tree

clf = tree.DecisionTreeClassifier()
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

clf = clf.fit(X, Y)

ml = {
    0: ['Classification', '/classify/']
}

classifiers = {
    0: ['DecisionTreeClassifier', '/classify/0/'],
    1: ['Classifier 1', '/classify/1/'],
    2: ['Classifier 2', '/classify/2/'],
}


@app.route("/", methods=['GET'])
def ml_list():
    return [{'model': ml[idx][0], 'url': ml[idx][1]}
            for idx in sorted(ml.keys())]


@app.route("/classify/", methods=['GET'])
def classification_list():
    return [{'classifier_type': classifiers[idx][0], 'url': classifiers[idx][1]}
            for idx in sorted(classifiers.keys())]


@app.route("/classify/<int:key>/", methods=['GET'])
def gender_classify(key):
    if key == 0:
        prediction = clf.predict([[170, 70, 43]])
        return {'gender': prediction[0]}
    elif key == 1:
        return '{}', status.HTTP_204_NO_CONTENT
    elif key == 2:
        return '{}', status.HTTP_204_NO_CONTENT
    else:
        return '{}', status.HTTP_204_NO_CONTENT


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
