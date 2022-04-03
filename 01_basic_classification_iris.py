# -*- coding: utf-8 -*-
"""01_Basic_Classification_iris.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wolUQoMBlrWGAKMIoOhdYL8Oe1iAte_D
"""

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

# 붓꽃 데이터 세트 로딩
iris = load_iris()

# iris.data는 피처(feature)만으로 된 데이터를 numpy로 가지고 있다
iris_data = iris.data
# iris.target은 레이블(결정값) 데이터를 numpy로 가지고 있다
iris_label = iris.target

print('target 값:', iris_label)
print('target 이름:', iris.target_names)

"""label 0 - setosa, 1 = versicolor, 2 = virginica"""

# 데이터 세트를 자세히 보기위해 DataFrame으로 변환
iris_df = pd.DataFrame(iris_data,columns=iris.feature_names)
iris_df['label'] = iris.target
iris_df.head(2)

# 학습용 데이터와 테스트용 데이터 분리
# 젠체 데이터 세트 중 테스트 데이터 세트의 비율 = 20%
# random_state 는 지정 하지 않으면 수행할 때마다 다른 학습/테스트 용 데이터를 만들 수 있으니 지정
X_train, X_test, y_train, y_test = train_test_split(iris_data,iris_label,
                                                    test_size=0.2, random_state=11)

# 의사결정 트리 클래스인 DecisionTreeClassifier 객체 생성
df_clf = DecisionTreeClassifier(random_state=11)

# 학습 수행
df_clf.fit(X_train,y_train)

# 학습이 완료된 DecisionTreeClassifier 객체에서 테스트 데이터 세트로 예측
pred = df_clf.predict(X_test)

# 예측 성능 평가 = accuracy_score() 함수 사용
from sklearn.metrics import accuracy_score
accuracy_score(y_test,pred)

