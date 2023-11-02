from numpy import loadtxt
from keras.models import model_from_json
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
x = dataset[:,0:8]
y = dataset[:,8]

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights("model.h5")
print("Loaded model from disk")

predictions = (model.predict(x) > 0.5).astype("int32")
for i in range(10,30):
	print('%s => %d (expected %d)' % (x[i].tolist(), predictions[i], y[i]))
