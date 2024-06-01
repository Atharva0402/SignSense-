import pickle

# from sklearn.ensemble import RandomForestClassifier
from sklearn import svm

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support
import numpy as np


data_dict = pickle.load(open('./data.pickle', 'rb'))

data = data_dict['data']
# data = np.asarray(data_dict['data'])

max_length = max(len(d) for d in data)

# Pad the inner lists with zeros so they all have the same length
padded_data = [d + [0] * (max_length - len(d)) for d in data]

# Convert to NumPy array
data = np.asarray(padded_data)



labels = np.asarray(data_dict['labels'])

x_train, x_test, y_train, y_test = train_test_split(data, labels, train_size=0.8, test_size=0.2, shuffle=True, stratify=labels)

# model = RandomForestClassifier()
model = svm.SVC()
model.fit(x_train, y_train)

y_predict = model.predict(x_test)

y_precision = precision_recall_fscore_support(y_test, y_predict, average='macro')
score = accuracy_score(y_predict, y_test)
print(score)
print(y_precision)

print('{}% of samples were classified correctly !'.format(score * 100))

f = open('model.p', 'wb')
pickle.dump({'model': model}, f)
f.close()
