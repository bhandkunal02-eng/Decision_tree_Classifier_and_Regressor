<p align="center">
  <a href="https://github.com/">
    <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub logo" width="72">
  </a>
</p>

<h1 align="center">Decision Tree Lab</h1>

<p align="center">
  Interactive classification and regression demos based on the lesson notebooks.
</p>

<p align="center">
  <a href="https://streamlit.io/">
    <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Open in Streamlit">
  </a>
  &nbsp;
  <a href="https://github.com/">
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

## Deploy on Streamlit Community Cloud

1. Push this repository to GitHub.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/) with GitHub.
3. Select **Create app**, choose this repository and branch, and set the app file to `app.py`.
4. After deployment, copy the public app URL into the Streamlit badge link above and into this README as a direct **Live app** link.

## Repository setup

Create a GitHub repository, then connect and push this project from the project folder:

```bash
git init
git add README.md .gitignore requirements.txt app.py Dicision_tree_classification.ipynb Dicision_tree_regression.ipynb
git commit -m "Add interactive decision tree demos"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/decision-tree-lab.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. Update the GitHub logo and repository badge links at the top of this README to point to the new repository after creating it.