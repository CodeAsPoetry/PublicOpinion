# coding="utf-8"

import numpy as np
import pandas as pd
import matplotlib as mpl
import sklearn as skl
from sklearn import linear_model,svm

Train_File_Path = "/home/code_as_poetry/lm/lm2.csv"
Test_File_Path = "/home/code_as_poetry/lm/lm3.csv"

def test_SVR_rbf(*data):
    X_train, X_test, y_train, y_test = data
    regr = svm.SVR(kernel='linear',gamma="auto")
    regr.fit(X_train, y_train)
    y = regr.predict(X_test)
    print('预测值',y)
    print('标签值',y_test)



def test_LinearRegression(*data):
    X_train,X_test,y_train,y_test = data
    regr = linear_model.LinearRegression()
    regr.fit(X_train,y_train)
    print('Coefficients:%s,intercept %.2f'%(regr.coef_,regr.intercept_))
    print('Residual sum of squares: %.2f'% np.mean((regr.predict(X_test)-y_test)**2))
    print('Score:%.2f'%regr.score(X_test,y_test))

if __name__=="__main__":
    print(np)
    print(pd)
    print(mpl)
    print(skl)

    train_file = pd.read_csv(Train_File_Path)
    tarin_data = pd.DataFrame(train_file)

    train_X=tarin_data[tarin_data.columns[0:5]]
    train_Y=tarin_data[tarin_data.columns[5]]


    test_file = pd.read_csv(Test_File_Path)
    test_data = pd.DataFrame(test_file)

    test_X = test_data[test_data.columns[0:5]]
    test_Y = test_data[test_data.columns[5]]

    # print(train_X)
    # print(train_Y)
    #
    # print(test_X)
    # print(test_Y)

    # test_LinearRegression(train_X,test_X,train_Y,test_Y)
    test_SVR_rbf(train_X,test_X,train_Y,test_Y)




