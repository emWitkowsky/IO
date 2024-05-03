### AI code:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def ai() -> None:
    # Load the Iris dataset
    iris = datasets.load_iris()
    iris_df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                        columns= iris['feature_names'] + ['target'])

    # Extract sepal width (cm) and sepal length (cm) columns
    sepal_width = iris_df['sepal width (cm)']
    sepal_length = iris_df['sepal length (cm)']

    # Create the original plot of sepal width and length dependence
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.scatter(sepal_width, sepal_length)
    plt.title('Original Plot')
    plt.xlabel('Sepal Width (cm)')
    plt.ylabel('Sepal Length (cm)')

    # Perform z-score transformation
    scaler = StandardScaler()
    sepal_zscore = scaler.fit_transform(np.array([sepal_width, sepal_length]).T)

    # Create the plot of sepal width and length z-score transformation
    plt.subplot(1, 3, 2)
    plt.scatter(sepal_zscore[:, 0], sepal_zscore[:, 1])
    plt.title('Z-Score Transformation')
    plt.xlabel('Sepal Width (Z-Score)')
    plt.ylabel('Sepal Length (Z-Score)')

    # Perform min-max transformation
    min_max_scaler = MinMaxScaler()
    sepal_minmax = min_max_scaler.fit_transform(np.array([sepal_width, sepal_length]).T)

    # Create the plot of sepal width and length min-max transformation
    plt.subplot(1, 3, 3)
    plt.scatter(sepal_minmax[:, 0], sepal_minmax[:, 1])
    plt.title('Min-Max Transformation')
    plt.xlabel('Sepal Width (Min-Max)')
    plt.ylabel('Sepal Length (Min-Max)')

    plt.tight_layout()
    plt.show()

# ai()
    
def ai2() -> None:
    # Load the Iris dataset
    iris = datasets.load_iris()
    iris_df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                        columns= iris['feature_names'] + ['target'])

    # Extract sepal width (cm) and sepal length (cm) columns
    sepal_width = iris_df['sepal width (cm)']
    sepal_length = iris_df['sepal length (cm)']

    # Create the original plot of sepal width and length dependence with switched axes
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.scatter(sepal_length, sepal_width)  # Switched axes
    plt.title('Original Plot')
    plt.xlabel('Sepal Length (cm)')  # Switched axes
    plt.ylabel('Sepal Width (cm)')  # Switched axes

    # Perform z-score transformation
    scaler = StandardScaler()
    sepal_zscore = scaler.fit_transform(np.array([sepal_width, sepal_length]).T)

    # Create the plot of sepal width and length z-score transformation with switched axes
    plt.subplot(1, 3, 2)
    plt.scatter(sepal_zscore[:, 1], sepal_zscore[:, 0])  # Switched axes
    plt.title('Z-Score Transformation')
    plt.xlabel('Sepal Length (Z-Score)')  # Switched axes
    plt.ylabel('Sepal Width (Z-Score)')  # Switched axes

    # Perform min-max transformation
    min_max_scaler = MinMaxScaler()
    sepal_minmax = min_max_scaler.fit_transform(np.array([sepal_width, sepal_length]).T)

    # Create the plot of sepal width and length min-max transformation with switched axes
    plt.subplot(1, 3, 3)
    plt.scatter(sepal_minmax[:, 1], sepal_minmax[:, 0])  # Switched axes
    plt.title('Min-Max Transformation')
    plt.xlabel('Sepal Length (Min-Max)')  # Switched axes
    plt.ylabel('Sepal Width (Min-Max)')  # Switched axes

    plt.tight_layout()
    plt.show()

# ai2()

def ai3() -> None:
    # Load the Iris dataset
    iris = datasets.load_iris()
    iris_df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                        columns= iris['feature_names'] + ['target'])

    # Extract sepal width (cm) and sepal length (cm) columns
    sepal_width = iris_df['sepal width (cm)']
    sepal_length = iris_df['sepal length (cm)']
    variety = iris_df['target']

    # Create the original plot of sepal width and length dependence with switched axes
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.scatter(sepal_length, sepal_width, c=variety, cmap='viridis')  # Switched axes and color based on variety
    plt.title('Original Plot')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Sepal Width (cm)')
    plt.colorbar(label='Variety')

    # Perform z-score transformation
    scaler = StandardScaler()
    sepal_zscore = scaler.fit_transform(np.array([sepal_width, sepal_length]).T)

    # Create the plot of sepal width and length z-score transformation with switched axes
    plt.subplot(1, 3, 2)
    plt.scatter(sepal_zscore[:, 1], sepal_zscore[:, 0], c=variety, cmap='viridis')  # Switched axes and color based on variety
    plt.title('Z-Score Transformation')
    plt.xlabel('Sepal Length (Z-Score)')
    plt.ylabel('Sepal Width (Z-Score)')
    plt.colorbar(label='Variety')

    # Perform min-max transformation
    min_max_scaler = MinMaxScaler()
    sepal_minmax = min_max_scaler.fit_transform(np.array([sepal_width, sepal_length]).T)

    # Create the plot of sepal width and length min-max transformation with switched axes
    plt.subplot(1, 3, 3)
    plt.scatter(sepal_minmax[:, 1], sepal_minmax[:, 0], c=variety, cmap='viridis')  # Switched axes and color based on variety
    plt.title('Min-Max Transformation')
    plt.xlabel('Sepal Length (Min-Max)')
    plt.ylabel('Sepal Width (Min-Max)')
    plt.colorbar(label='Variety')

    plt.tight_layout()
    plt.show()

ai3()

### PROMPTY: (codeium ai, dziala na jakims starszym, nie na gpt4)
# 1
# I have a scikit learn iris dataset, 
# i want to create these 3 following plots with this dataset: 
# the original plot of sepal width and length dependence,
# the plot of sepal width and length z-score transformation,
# the plot of sepal width and length min-max transformation

# 2
# can you switch axes for sepal width and length?

# 3
# can you make the plot points of different varieties different colors?
