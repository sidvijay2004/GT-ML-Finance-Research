from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error
import numpy as np
import pandas as pd
from typing import Tuple

class RFModel:
    def __init__(self, training_X: pd.DataFrame, training_y: pd.DataFrame, 
            max_depth: int, random_state: int):
        self.clf = RandomForestRegressor(max_depth=max_depth, random_state=random_state)
        self.clf.fit(training_X, training_y)


    def test(self, testing_X: pd.DataFrame, testing_y: pd.DataFrame) -> Tuple[float,
            float, float]:
        output = self.clf.predict(testing_X)

        mape, rmse, mbe = self.validate(predicted, realized)

        s = f"MAPE: {mape} | RMSE: {rmse} | MBE: {mbe}"
        l = len(s)
        s = "="*l + "\n" + s + "\n" + "="*l + "\n"
        print(s)
        return mape, rmse, mbe
        

    def validate(self, predicted: np.array, realized: np.array) -> Tuple[float,
            float, float]:
        mape = mean_absolute_percentage_error(realized, predicted)
        rmse = mean_squared_error(realized, predicted)
        mbe = np.mean(realized - predicted)

        return mape, rmse, mbe
