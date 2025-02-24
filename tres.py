import pandas as pd
from sklearn import datasets
iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
lst2 = []

def split(df, st, index=0):
    if index >= len(st):
        return [df]
    stl = st[index]
    median = df[stl].median()
    lst2.append(median)
    df1 = df[df[stl] <= median]
    df2 = df[df[stl] > median]
    return (split(df1, st, index + 1) +
            split(df2, st, index + 1))
columns = iris.feature_names
result = split(df, columns)
lst = []
for i, j in enumerate(result):
    mode = j['target'].mode().iloc[0]
    # print(i + 1)
    # print(j)
    lst.append(mode)
    
class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find(start, num):
    if start is None:
        return None
    if start.value == num:
        return num
    if start.value > num:
        return find(start.left, num)
    if start.value < num:
        return find(start.right, num)
    return None


print(*lst)
print(*lst2)
