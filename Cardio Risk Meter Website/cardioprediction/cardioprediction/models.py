# Importing Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

class MLModel:
    def model(self,age,gender,chestpain,restingbp,serumcholestrol,fastingbs,restingrelectro,maxheartrate,exerciseangia,oldpeak,slope,noofmajvessels):
        result = None
        
        # Importing Dataset
        dataset = pd.read_csv("Cardiovascular_Disease_Dataset.csv")
        
        # Extracting Independent and Dependent Variables
        x = dataset.iloc[:,1:13]
        y = dataset.iloc[:,13:14]
        
        # Splitting the dataset into Training and Testing Sets
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
        
        # Feature Scaling
        fscaling = StandardScaler()
        x_train = fscaling.fit_transform(x_train)
        x_test = fscaling.fit_transform(x_test)
        
        # Fitting Random Forest Classifier to the Traing Set
        classifier = RandomForestClassifier(n_estimators=10, criterion="entropy")
        classifier.fit(x_train, y_train)
        
        # Predicting the Test Set result
        y_predict = classifier.predict(x_test)
        #print("Prediction: ", classifier.predict([[40,1,2,173,295,1,1,192,1,3.7,1,1]]))
        result = classifier.predict([[age,gender,chestpain,restingbp,serumcholestrol,fastingbs,restingrelectro,maxheartrate,exerciseangia,oldpeak,slope,noofmajvessels]])
        
        # Accuracy of the Model
        # 1. Confusion Matrix
        cmat = confusion_matrix(y_test, y_predict)
        # 2. Accuracy Score
        accscore = accuracy_score(y_test, y_predict)
        # 3. Score
        accuracy = classifier.score(x_test,y_test)

        return result, accuracy
