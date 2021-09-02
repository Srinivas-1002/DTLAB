#In[1]:
import os
import sklearn.preprocessing
import numpy
import sys
import tensorflow
import pandas


#In[3]:
class Bank:
    def __init__(self):
        self.input = sys.argv[1].upper()
        self.x_train_NN = pandas.read_csv("D:\\Personal_Projects\\Python\\DTLAB\\Dataset\\Dataset_Merged.csv")        
        self.y_train_NN = pandas.read_csv("D:\\Personal_Projects\\Python\\DTLAB\\Dataset\\Output.csv")
        self.x_train_NN = self.x_train_NN.set_index('DISTRICT')
        self.index = self.x_train_NN.index.get_loc(self.input)
        self.x_train_NN = self.x_train_NN.reset_index()
        self.x_prediction_test_NN = self.x_train_NN.iloc[self.index]
        self.x_train_NN.drop(self.index, axis=0)
        self.x_train_NN = self.x_train_NN.drop("DISTRICT", axis=1)
        self.x_prediction_test = self.x_prediction_test_NN.to_numpy()
        self.x_prediction_test = numpy.delete(self.x_prediction_test,0)
        self.x_prediction_test = self.x_prediction_test.astype(float)
        self.x_train_NN = Simplify.normalize(self.x_train_NN)
        
        if (sys.argv[2] == '1'):
            Neural_Nexus.brain(self)
        
        Neural_Nexus.SavedMemory(self)


#In[4]:
class Neural_Nexus:
    def brain(self):
        self.Connectors = tensorflow.keras.Sequential()
        self.Connectors.add(tensorflow.keras.layers.Dense(units = 2048, kernel_initializer = 'random_normal', bias_initializer = 'zeros', activation= 'sigmoid'))
        self.Connectors.add(tensorflow.keras.layers.BatchNormalization())
        self.Connectors.add(tensorflow.keras.layers.Dense(units = 1024, kernel_initializer = 'random_normal', bias_initializer = 'zeros', activation= 'sigmoid'))
        self.Connectors.add(tensorflow.keras.layers.BatchNormalization())
        self.Connectors.add(tensorflow.keras.layers.Dense(units = 512, kernel_initializer = 'random_normal', bias_initializer = 'zeros', activation= 'sigmoid'))
        self.Connectors.add(tensorflow.keras.layers.BatchNormalization())
        self.Connectors.add(tensorflow.keras.layers.Dense(units = 256, kernel_initializer = 'random_normal', bias_initializer = 'zeros', activation= 'sigmoid'))
        self.Connectors.add(tensorflow.keras.layers.BatchNormalization())
        self.Connectors.add(tensorflow.keras.layers.Dense(units = 128, kernel_initializer = 'random_normal', bias_initializer = 'zeros', activation= 'sigmoid'))
        self.Connectors.add(tensorflow.keras.layers.BatchNormalization())
        self.Connectors.add(tensorflow.keras.layers.Dense(units = 64, kernel_initializer = 'random_normal', bias_initializer = 'zeros', activation= 'sigmoid'))
        self.Connectors.add(tensorflow.keras.layers.BatchNormalization())
        self.Connectors.add(tensorflow.keras.layers.Dense(units = 32, kernel_initializer = 'random_normal', bias_initializer = 'zeros', activation= 'sigmoid'))
        self.Connectors.add(tensorflow.keras.layers.BatchNormalization())
        self.Connectors.add(tensorflow.keras.layers.Dense(units = 16, kernel_initializer = 'random_normal', bias_initializer = 'zeros', activation= 'sigmoid'))
        self.Connectors.add(tensorflow.keras.layers.BatchNormalization())
        self.Connectors.add(tensorflow.keras.layers.Flatten())
        self.Connectors.add(tensorflow.keras.layers.Dense(units = 10, kernel_initializer = 'random_normal', bias_initializer = 'zeros', activation='softmax'))
        self.Connectors.compile(optimizer='adam', loss= 'SparseCategoricalCrossentropy', metrics=['accuracy'])
        self.Connectors.fit(self.x_train_NN, self.y_train_NN, batch_size= 32, epochs= 500, validation_split= 0.2)
        self.Connectors.save("D:\\Personal_Projects\\Python\\DTLAB\\Models\\TrainedModel.h5")
        self.Connectors.save_weights("D:\\Personal_Projects\\Python\\DTLAB\\Models\\TrainedModelWeights")
        self.Land_Classification = numpy.argmax(self.Connectors.predict(self.x_prediction_test.reshape((1,16))))
        Classifier.Output(self)

    def SavedMemory(self):
        model = tensorflow.keras.models.load_model("D:\\Personal_Projects\\Python\\DTLAB\\Models\\TrainedModel.h5")
        model.load_weights("D:\\Personal_Projects\\Python\\DTLAB\\Models\\TrainedModelWeights")
        self.Land_Classification = numpy.argmax(model.predict(self.x_prediction_test.reshape((1,16))))
        Classifier.Output(self)


#In[6]:
class Classifier:
    def Output(self):
        
        self.Land_Classification_Labels = { 0 : "Data Not Available", 1 : "Not Productive", 2 : "Low Productive", 3 : "Moderately Low Productive", 4 : "Moderately Productive", 5 : "Highly Productive"}
        print(self.Land_Classification_Labels[self.Land_Classification])
        if (sys.argv[3] == '1'):
            print("Input Prediction Dataset: ")
            print(self.x_prediction_test)
        exit()

#In[5]:
class Simplify:
    def normalize(x, axis=0):
        return sklearn.preprocessing.normalize(x,axis=axis) 

        
#In[2]:
if __name__ == '__main__':
    os.chdir("D:\\Personal_Projects\\Python\\DTLAB")
    var = Bank()