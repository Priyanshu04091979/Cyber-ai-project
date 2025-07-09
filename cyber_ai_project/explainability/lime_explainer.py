# import numpy as np
# from lime.lime_tabular import LimeTabularExplainer
# explainer = LimeTabularExplainer(X_train, feature_names=cols)
# exp = explainer.explain_instance(X_test[0], model.predict_proba)
# exp.show_in_notebook()

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from lime.lime_tabular import LimeTabularExplainer
import matplotlib.pyplot as plt

# Load sample data
iris = load_iris()
X = iris.data
y = iris.target
cols = iris.feature_names

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Create LIME explainer
explainer = LimeTabularExplainer(
    training_data=X_train,
    feature_names=cols,
    class_names=iris.target_names.tolist(),
    mode='classification'
)

# Explain a prediction for the first test instance
exp = explainer.explain_instance(
    data_row=X_test[0],
    predict_fn=model.predict_proba
)

# Show explanation
try:
    from IPython.display import display
    exp.show_in_notebook(show_table=True, show_all=False)
except:
    exp.as_pyplot_figure()
    plt.show()

