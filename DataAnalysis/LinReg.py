import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import math
import sklearn
from sklearn import linear_model, preprocessing, svm

df = pd.read_excel('united-states (1).xls', sheet_name='All Homes')

df = df.T
df.drop(df.iloc[:, 1:], inplace = True, axis = 1)
df.drop(df.index[0:3], inplace = True)

forecast_col = 0
df.fillna(value=-99999, inplace=True)
forecast_out = int(math.ceil(0.2 * len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)


x = np.array(df.drop(['label'], 1))
x = preprocessing.scale(x)
x_lately = x[-forecast_out:]
x = x[:-forecast_out]

df.dropna(inplace=True)

y = np.array(df['label'])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)

clf = linear_model.LinearRegression()
clf.fit(x_train, y_train)
accuracy = clf.score(x_test, y_test)

forecast_set = clf.predict(x_lately)
print(forecast_set, accuracy, forecast_out)
df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += 86400
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]

df[0].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
