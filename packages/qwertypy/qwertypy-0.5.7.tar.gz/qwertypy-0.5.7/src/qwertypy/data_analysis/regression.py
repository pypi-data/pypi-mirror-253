from sklearn.linear_model import LinearRegression

from .utils import npArrayReshape

class QpyLinearRegression:
    """Wrapper over sklearn LinearRegression"""
    def __init__(self, xTrain, yTrain):
        self.xTrain = npArrayReshape(xTrain)
        self.yTrain = npArrayReshape(yTrain)
        self.model = LinearRegression()

    def train(self):
        self.model.fit(self.xTrain, self.yTrain)

    def getPrediction(self, xPredict = None):
        if not xPredict:
            xPredict = self.xTrain
        else: xPredict = npArrayReshape(xPredict)

        yPredict = [y[0] for y in self.model.predict(xPredict).tolist()]
        return yPredict