import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder


def TOPSIS(d, w, im):
  Dataf = d
  Name = d[d.columns[0]]
  D = d.drop(d.columns[0],axis=1)
  #Step 1: convert categorical to numerical
  def check_encode(D):
    for column in D.columns:
        if pd.to_numeric(D[column]).all():
            continue
        else:
            le = LabelEncoder()
            D[column] = le.fit_transform(D[column])
    return D
  D=check_encode(D)
  #Step 2: vector normalization
  n = len(D.columns)
  colSqSum = (D**2).sum()
  colSqSumarray = colSqSum.values
  colSqSumRoot = np.sqrt(colSqSumarray)
  vn = D.div(colSqSumRoot)

  #Step 3: weight assignment
  wnv=vn*w
  wnv
  #step 4: calculate ideal best and worst values
  ib = {}
  iw = {}
  for i in range(0,n):
    if im[i]=='+':
        ib[i] = wnv[wnv.columns[i]].max()
        iw[i] = wnv[wnv.columns[i]].min()
    else:
        ib[i] = wnv[wnv.columns[i]].min()
        iw[i] = wnv[wnv.columns[i]].max()

  wnv=wnv.to_numpy()
  #step 5: calculate euclidean distance
  distBest = np.zeros(mm)
  distWorst = np.zeros(mm)
  distB = np.copy(wnv)
  distW = np.copy(wnv)

  for j in range(mm):
    for i in range(n):
        distB[j][i] = (wnv[j][i] - ib[i]) ** 2
        distW[j][i] = (wnv[j][i] - iw[i]) ** 2
        distWorst[j] += distW[j][i]
        distBest[j] += distB[j][i]

  for j in range(mm):
    distWorst[j] = distWorst[j] ** 0.5
    distBest[j] = distBest[j] ** 0.5


  #Step 6: performance score
  score = []
  for i in range(len(distBest)):
    score.append(distWorst[i] / (distBest[i] + distWorst[i]))
  

  #step7: rank
  pData = pd.DataFrame(data ={'Items':Name , 'Performance':score})
  pData['Rank'] = pData['Performance'].rank(ascending=True)

  #Final output
  pData.to_csv('102116116_result.csv',index=False)
  return(pData)