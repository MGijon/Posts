"""Model Selection practice for clasasification model."""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

FILE_ROUTE="iris.csv"

def preprocessing(route):
    """Preprocessing of the dataset. In this case it will be extremely simply."""
    data=pd.read_csv(route)
    data.set_index('Id', inplace=True)
    data["Species"] = [str(x).replace("Iris-", "").capitalize() for x in data["Species"].values]
    return data 

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

if __name__ == "__main__":
    data=preprocessing("iris.csv")

    #basic_plots(data=data)


#### 
#names = data["Species"].values
    #print("\n", names)
    #names = data['target_names']
    #feature_names = data['feature_names']
    """
    color_mapping = {
        "Setosa": "red",
        "Virginica": "green", 
        "Versicolor": "blue"
    }
    """
    #plt.style.use('ggplot')
    
    """
    cas
    fig, axes = plt.subplots(2, 1, figsize=(18, 10))
    fig.suptitle('Iris Dataset exploration')

    sns.(ax=axes[0], 
                  data=data, 
                  hue="Species", 
                  palette="husl", 
                  size=5).map(plt.scatter, "SepalLengthCm", "SepalWidthCm").add_legend()
    sns.scatterplot(ax=axes[1],
                  data=data, 
                  hue="Species",
                  palette="husl", 
                  size=5).map(plt.scatter, "PetalLengthCm", "PetalWidthCm").add_legend()
    """


    """
    plt.figure(figsize=(16, 6))


    plt.subplot(1, 2, 1)    
    sns.FacetGrid(data, hue="Species", palette="husl", size=5).map(plt.scatter, "SepalLengthCm", "SepalWidthCm").add_legend()
    plt.subplot(1, 2, 2)    
    sns.FacetGrid(data, hue="Species", palette="husl", size=5).map(plt.scatter, "PetalLengthCm", "PetalWidthCm").add_legend()
    """
    """
    for i in range(data.shape[0]):
        plt.scatter(data.iloc[i, 0], 
            data.iloc[i, 1], 
            label=data.iloc[:,4].values[i])
    for target, target_name in enumerate(names):
        X_plot = X[y == target]
        plt.plot(X_plot[:, 0], X_plot[:, 1], linestyle='none', marker='o', label=target_name)
    plt.xlabel(feature_names[0])
    plt.ylabel(feature_names[1])
  
    plt.xlabel("Length (cms)")
    plt.xlabel("Width (cms)")
    plt.title('Sepal')
    plt.legend();"
    plt.subplot(1, 2, 2)
    for target, target_name in enumerate(names):
        X_plot = X[y == target]
        plt.plot(X_plot[:, 2], X_plot[:, 3], linestyle='none', marker='o', label=target_name)
    plt.xlabel(feature_names[2])
    plt.ylabel(feature_names[3])
    
    plt.xlabel("Length (cms)")
    plt.xlabel("Width (cms)")
    plt.title('Petal')
    plt.legend()
    """