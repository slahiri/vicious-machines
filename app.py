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

model_list = {
    0: ['Classification', '/classify/']
}

classifiers = {
    0: ['DecisionTreeClassifier', {"key": 0, "height": 170, "weight": 70, "shoe": 43}],
    1: ['Classifier 1', '{}'],
    2: ['Classifier 2', '{}'],
}


@app.route("/", methods=['GET'])
def model_list():
    return [{'model': model_list[idx][0], 'url': model_list[idx][1]}
            for idx in sorted(model_list.keys())]


@app.route("/classify/", methods=['GET', 'POST'])
def gender_classify():
    if request.method == 'POST':
        key = request.data.get('key', '')
        height = request.data.get('height', '')
        weight = request.data.get('weight', '')
        shoe = request.data.get('shoe', '')
        if key == 0:
            prediction = clf.predict([[height, weight, shoe]])
            return {'gender': prediction[0]}
        elif key == 1:
            return '{}', status.HTTP_204_NO_CONTENT
        elif key == 2:
            return '{}', status.HTTP_204_NO_CONTENT
        else:
            return '{}', status.HTTP_204_NO_CONTENT
    return [{'classifier_type': classifiers[idx][0], 'sample': classifiers[idx][1]}
            for idx in sorted(classifiers.keys())]


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
