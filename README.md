# DTLAB
The Project was done using JAVAFX and Python.
The Frontend uses .fxml concept of the JAVAFX for UI Designing and Calls the python interpreter for performing the Backend Operations such as Classification.
The application accecepts the input as the name of the District in India and Classifies the Ouput on the average productivity of the District.
The application connects with the google maps to locate the district entered in the seach feild. A web engine from the Javafxpackages is used for this purpose.
The Backend uses Python which uses Pandas Library for accessing data elements and Tensorflow Keras for Machine Learning Applications.
Due,to the lack of dataset collection the prediction data was not seperatly stored instead when a district from the stored Elements is entered, It drops that specific element out
and trains the model with the rest of the elements.
The model breaks the input elements in the ratio of 8:2 for training data and test data.
The model uses adam Optimizer and Sigmoid Activation Function on the input and the hidden layers while using softmax Function on the output layer.
The model uses a method called back-propagation, a well-known technique in which the model compares its output with the given output to make better predictions by adjusting weights
on its previous layer edges. Thus, Modifying its output for the better.
