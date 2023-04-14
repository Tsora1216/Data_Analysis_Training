import pandas as pd
import pickle
from sklearn import tree

df = pd.read_csv("Book\Sukkiri_ML\ProjectA\datafiles\KvsT.csv")

x=df[["身長","体重","年代"]]
t=df["派閥"]

model=tree.DecisionTreeClassifier(random_state=0)
print(model.fit(x,t))
print(model.score(x,t))

with open("Book\Sukkiri_ML\ProjectA\KvsT.pkl","wb") as f:
    pickle.dump(model,f)

with open("Book\Sukkiri_ML\ProjectA\KvsT.pkl","rb") as f:
    model2 = pickle.load(f)

suzuki=[[162,75,50]]
print(model.predict(suzuki))