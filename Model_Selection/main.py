"""Model Selection practice for clasasification model."""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings("ignore")


FILE_ROUTE="iris.csv"

def preprocessing(route):
    """Preprocessing of the dataset. In this case it will be extremely simply."""
    data=pd.read_csv(route)
    data.set_index('Id', inplace=True)
    data["Species"] = [str(x).replace("Iris-", "").capitalize() for x in data["Species"].values]
    return data 

def basic_exploration(data):
    """Performs a basic exploration of the dataset.
    :param data: dataset (iris, pandas dataframe format).
    """
    print("Dataset description: ")
    print(data.describe())
    print("\nDataset categories: ")
    print(data.groupby('Species').size())
    print("\n")

def basic_plots(data):
    """Plotting the dataset."""
    # ===== #
    # SEPAL #
    # ===== #
    sns.FacetGrid(data=data, hue="Species", palette="deep", size=5).map(plt.scatter, "SepalLengthCm", "SepalWidthCm") \
                        .add_legend() \
                            .set(title="\n \nIris Sepal data", xlabel='Length (cms)', ylabel='Width (cms)')
    plt.subplots_adjust(top=0.9)
    plt.savefig("images/IrisSepal.png")
    plt.show()

    # ===== #
    # PETAL #
    # ===== #
    sns.FacetGrid(data=data, hue="Species", palette="deep", size=5).map(plt.scatter, "PetalLengthCm", "PetalWidthCm") \
        .add_legend() \
            .set(title="\n \nIris Petal data", xlabel='Length (cms)', ylabel='Width (cms)')
    plt.subplots_adjust(top=0.9)
    plt.savefig("images/IrisPetal.png")
    plt.show()

def apply_LogisticRegression(X_train, y_train, X_test, y_test, print_stuff=False):
    """Appy Logistic Regression.
    :param X_train: self-explanatory.
    :param y_train: self-explanatory.
    :param X_test: self-explanatory.
    :param y_test: self-explanatory.
    :return metric_accuracy: self-explanatory.
    """
    mod_lr = LogisticRegression()
    mod_lr.fit(X_train,y_train)
    prediction_lr=mod_lr.predict(X_test)
    metric_accuracy=metrics.accuracy_score(prediction_lr,y_test)

    if print_stuff:
        print("The accuracy of the Logistic Regression is", "{:.3f}".format(metric_accuracy))
    return metric_accuracy

def apply_DecisionTreeClassifier(X_train, y_train, X_test, y_test, print_stuff=False):
    """Appy Decision Tree Classifier.
    :param X_train: self-explanatory.
    :param y_train: self-explanatory.
    :param X_test: self-explanatory.
    :param y_test: self-explanatory.
    :return metric_accuracy: self-explanatory.
    """
    mod_dt = DecisionTreeClassifier(max_depth = 3, random_state = 1)
    mod_dt.fit(X_train,y_train)
    prediction_dt=mod_dt.predict(X_test)
    metric_accuracy=metrics.accuracy_score(prediction_dt,y_test)

    if print_stuff:
        print("The accuracy of the Decision Tree is", "{:.3f}".format(metric_accuracy))

    # Print feature importances
    #print(mod_dt.feature_importances_)

    # Print Decission Tree
    #plt.figure(figsize = (10,8))
    #plot_tree(mod_dt, feature_names = ['sl','sw','pl','pw'], class_names = ["Setosa", "Versicolor", "Virginica"], filled = True)
    #plt.show()
    return metric_accuracy

if __name__ == "__main__":

    NUMBER_EXPERIMENTS = 100
    data=preprocessing("iris.csv")       # Load the dataset
    # Basic plots
    #basic_plots(data=data)            

    # Basic exploration
    #basic_exploration(data)
    results = {
        "DT": [],
        "LR": [],
    }
    
    print("Number of experiments: ", NUMBER_EXPERIMENTS)
    for _ in range(NUMBER_EXPERIMENTS):
        # 30% to test
        train, test = train_test_split(data, test_size = 0.3, stratify = data["Species"]) #, random_state = 42)
        X_train = train[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
        y_train = train["Species"]
        X_test = test[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
        y_test = test["Species"]

        results["DT"].append(apply_DecisionTreeClassifier(X_train, y_train, X_test, y_test))
        results["LR"].append(apply_LogisticRegression(X_train, y_train, X_test, y_test))
    print("DT mean: ", np.round(np.mean(results["DT"]), 4), " - std: ", np.round(np.std(results["DT"]), 4))
    print("LR mean: ", np.round(np.mean(results["LR"]), 4), " - std: ", np.round(np.std(results["LR"]), 4))

    
    

