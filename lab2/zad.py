import pandas as pd 
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import IrisData as iris
import matplotlib.pyplot as plt

def main()-> None: 

    # --------------------------------------------------------------------------------------------
    ### ZAD1
    print("Zad 1 ------------------------------------------------------------------\n")
    # --------------------------------------------------------------------------------------------

    new_iris = iris.IrisData()
    print(new_iris.df)
    # prints missing data summary
    print(new_iris.df.isnull().sum())

    # saves missing data rows to csv
    new_iris.na_df.to_csv("data/iris_missing_rows.csv", index=False)

    def count_lines():
        with open("data/iris_missing_rows.csv", 'r') as file:
            lines = 0
            for line in file:
                lines += 1
        print("Liczba brakujących: ", lines-1)

    count_lines()
    # clean up variety names and values not between <0; 15>
    new_iris.clean_false_data()

    # original dataframe cleanup: set missing values to median, 
    new_iris.clean_final_data()

    # saves cleaned data to csv
    new_iris.df.to_csv("data/iris_cleaned.csv", index=False)
    
    # --------------------------------------------------------------------------------------------
    ### ZAD2
    print("Zad 2 ------------------------------------------------------------------\n")
    # --------------------------------------------------------------------------------------------
    clean_dataset = datasets.load_iris()
    x = pd.DataFrame(clean_dataset.data, columns=clean_dataset.feature_names)
    y = pd.Series(clean_dataset.target, name='FlowerType')
    print(x.head())
    # we set count of components
    pca_dataset = PCA(n_components=2).fit(clean_dataset.data)

    print("1-DATASET-----------------------------------------------------------\n")
    print(pca_dataset)
    print("2-EXPLAINED-VARIANCE-RATIO------------------------------------------\n")
    print(pca_dataset.explained_variance_ratio_) 
    print("3-COMPONENTS--------------------------------------------------------\n")
    print(pca_dataset.components_)
    print("4-TRANSFORMED-DATASET-----------------------------------------------\n")
    print(pca_dataset.transform(clean_dataset.data))

    target_names = clean_dataset.target_names
    #PCA
    x_r = pca_dataset.fit(x).transform(x)

    plt.figure()
    colors = ["lightgreen", "lightblue", "pink"]
    lw = 2
    for color, i, target_name in zip(colors, [0, 1, 2], target_names):
        plt.scatter(x_r[y == i, 0], x_r[y == i, 1], color=color, alpha=0.8, lw=lw, label=target_name)
    plt.legend(loc='best', shadow=False, scatterpoints=1)
    plt.title("PCA Iris dataset")
    ### plt.show()

    # --------------------------------------------------------------------------------------------
    ### ZAD3
    print("Zad 3 ------------------------------------------------------------------\n")
    # --------------------------------------------------------------------------------------------
    # original data
    _, ax = plt.subplots()
    scatter = ax.scatter(clean_dataset.data[:, 0], clean_dataset.data[:, 1], c=clean_dataset.target)
    ax.set(xlabel=clean_dataset.feature_names[0], ylabel=clean_dataset.feature_names[1])
    _ = ax.legend(scatter.legend_elements()[0], clean_dataset.target_names, loc="upper right", title="Classes")
    # plt.show()

    # min max scaled data
    scaler = MinMaxScaler()
    sepal_data = clean_dataset.data[:, :2]
    scaler.fit(sepal_data)
    scaled_sepal_data = scaler.transform(sepal_data)
    _, ax = plt.subplots()
    scatter = ax.scatter(scaled_sepal_data[:, 0], scaled_sepal_data[:, 1], c=clean_dataset.target)
    ax.set(xlabel=clean_dataset.feature_names[0], ylabel=clean_dataset.feature_names[1])
    _ = ax.legend(scatter.legend_elements()[0], clean_dataset.target_names, loc="upper right", title="Classes")
    # plt.show()

    # z score scaled data
    zscore_scaler = StandardScaler()
    zscore_scaler.fit(sepal_data)
    print(zscore_scaler.mean_)
    zscore_sepal_data = zscore_scaler.transform(sepal_data)
    _, ax = plt.subplots()
    scatter = ax.scatter(zscore_sepal_data[:, 0], zscore_sepal_data[:, 1], c=clean_dataset.target)
    ax.set(xlabel=clean_dataset.feature_names[0], ylabel=clean_dataset.feature_names[1])
    _ = ax.legend(scatter.legend_elements()[0], clean_dataset.target_names, loc="upper right", title="Classes")
    plt.show()

    # series z sepal.length i sepal.width
    length_series = pd.Series(clean_dataset.data[:, 0])
    width_series = pd.Series(clean_dataset.data[:, 1])
    print(length_series.describe())
    print(width_series.describe())

main()