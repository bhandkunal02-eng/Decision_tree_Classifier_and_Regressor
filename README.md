<p align="center">
  <a href="https://github.com/bhandkunal02-eng/Decision_tree_Classifier_and_Regressor">
    <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub logo" width="72">
  </a>
</p>

<h1 align="center">Decision Tree Lab</h1>

<p align="center">
  Interactive classification and regression demos based on the lesson notebooks.
</p>

<p align="center">
  <a href="https://decision-tree-lab.streamlit.app/">
    <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Open the live Streamlit app">
  </a>
  &nbsp;
  <a href="https://github.com/bhandkunal02-eng/Decision_tree_Classifier_and_Regressor">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?logo=github" alt="GitHub repository">
  </a>
</p>

## Models

- **Classification:** Titanic passenger survival using a decision tree. Adjust tree depth and split size, try a passenger profile, and inspect test accuracy, the confusion matrix, and a tree overview.
- **Regression:** Diabetes progression using a decision tree. Adjust tree depth, edit the ten input features, and inspect test-set error, R², and actual-versus-predicted values.

The original lesson notebooks are included:

- [`Dicision_tree_classification.ipynb`](Dicision_tree_classification.ipynb)
- [`Dicision_tree_regression.ipynb`](Dicision_tree_regression.ipynb)

## Run locally

```bash
python -m venv .venv
```

Activate the environment, then install and launch:

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

The Titanic dataset is loaded through seaborn and needs internet access the first time. The regression dataset is included with scikit-learn.

## Live app

Open [Decision Tree Lab](https://decision-tree-lab.streamlit.app/). It is deployed from `main` and runs `app.py`.

## Repository setup

Clone the GitHub repository:

```bash
git clone https://github.com/bhandkunal02-eng/Decision_tree_Classifier_and_Regressor.git
cd Decision_tree_Classifier_and_Regressor
```

The GitHub logo and repository badge link to this repository. New commits to `main` are deployed automatically.