import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import math
import sklearn
from sklearn import linear_model, preprocessing, svm

def Forecast(df, forecast_col, predictL):
	df.fillna(value=-99999, inplace=True)
	forecast_out = int(math.ceil(0.05 * len(df)))

	df['label'] = df[forecast_col].shift(-forecast_out)

	x = np.array(df.drop(['label'], 1))
	x = preprocessing.scale(x)
	x_lately = x[-forecast_out:]
	x = x[:-forecast_out]

	df2 = df.drop(['label'], axis=1)
	df.dropna(inplace=True)

	y = np.array(df['label'])

	x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

	clf = linear_model.LinearRegression()
	clf.fit(x_train, y_train)
	accuracy = clf.score(x_test, y_test)

	forecast_set = clf.predict(x_lately)
	# print(forecast_set, accuracy, forecast_out)
	predictL.append(forecast_set)

def getColumn(x, df):
	df = df.drop(df.iloc[:, x+1:], axis = 1)
	df = df.drop(df.iloc[:, :x], axis = 1)
	return df

if __name__ == "__main__":
	predictList = []

	pd.set_option("display.max_rows", None, "display.max_columns", None)
	df = pd.read_excel("united-states (1).xls", sheet_name="Two Bed")
	df1 = df.T
	df1.drop(df1.index[0:3], inplace = True)

	for i in range(0, len(df1.columns)):
		temp = df1
		temp = getColumn(i, temp)
		Forecast(temp, i, predictList)

	last_date = df1.iloc[-1].name
	last_unix = last_date.timestamp()
	one_month = 2628000
	next_unix = last_unix + one_month
	predictTime = []
	for i in range(6):
		next_month = datetime.datetime.fromtimestamp(next_unix)
		next_unix += one_month
		predictTime.append(next_month)
	
	df2 = pd.DataFrame(predictList, columns=predictTime)
	df2 = df2.T

	df = df.T
	df.drop(df.index[3:], inplace = True)
	df = df.append(df2)
	df = df.T
	df.set_index(df.columns[0], inplace = True)
	df.to_csv("Predict Two Bed.csv")