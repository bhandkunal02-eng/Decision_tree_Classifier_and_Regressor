from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from sklearn.compose import ColumnTransformer
from sklearn.datasets import load_diabetes
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, confusion_matrix, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor, plot_tree


st.set_page_config(page_title="Decision Tree Lab", page_icon="🌳", layout="wide")


@st.cache_data
def load_titanic() -> pd.DataFrame:
    return sns.load_dataset("titanic")


@st.cache_data
def load_diabetes_data() -> tuple[pd.DataFrame, pd.Series]:
    dataset = load_diabetes(as_frame=True)
    return dataset.data, dataset.target


def classification_demo() -> None:
    st.subheader("Titanic survival classification")
    st.write(
        "Train a decision tree to predict passenger survival from ticket class, "
        "sex, fare, port of embarkation, and age."
    )

    try:
        titanic = load_titanic()
    except Exception as error:
        st.error(f"Could not load the Titanic dataset. Check the app's internet access. ({error})")
        return

    features = ["pclass", "sex", "fare", "embarked", "age"]
    target = "survived"
    data = titanic[features + [target]].dropna(subset=[target])
    X = data[features]
    y = data[target].astype(int)

    numeric_features = ["pclass", "fare", "age"]
    categorical_features = ["sex", "embarked"]
    preprocessing = ColumnTransformer(
        transformers=[
            ("numeric", SimpleImputer(strategy="median"), numeric_features),
            (
                "categorical",
                Pipeline(
                    steps=[
                        ("imputer", SimpleImputer(strategy="most_frequent")),
                        ("encoder", OneHotEncoder(handle_unknown="ignore")),
                    ]
                ),
                categorical_features,
            ),
        ]
    )

    depth = st.slider("Maximum tree depth", min_value=1, max_value=12, value=6)
    min_split = st.slider("Minimum samples to split", min_value=2, max_value=30, value=10)
    model = Pipeline(
        steps=[
            ("preprocessing", preprocessing),
            (
                "tree",
                DecisionTreeClassifier(
                    max_depth=depth,
                    min_samples_split=min_split,
                    random_state=42,
                ),
            ),
        ]
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    metric, samples = st.columns(2)
    metric.metric("Test accuracy", f"{accuracy:.1%}")
    samples.metric("Passengers", f"{len(data):,}")

    st.markdown("#### Try a passenger")
    passenger_columns = st.columns(5)
    passenger = pd.DataFrame(
        [
            {
                "pclass": passenger_columns[0].selectbox("Class", [1, 2, 3], index=2),
                "sex": passenger_columns[1].selectbox("Sex", ["female", "male"]),
                "fare": passenger_columns[2].number_input(
                    "Fare", min_value=0.0, max_value=600.0, value=32.2, step=1.0
                ),
                "embarked": passenger_columns[3].selectbox(
                    "Embarked", ["S", "C", "Q"]
                ),
                "age": passenger_columns[4].number_input(
                    "Age", min_value=0.0, max_value=100.0, value=29.0, step=1.0
                ),
            }
        ]
    )
    survival_probability = model.predict_proba(passenger)[0, 1]
    st.info(f"Estimated survival probability: **{survival_probability:.1%}**")

    left, right = st.columns(2)
    with left:
        st.markdown("#### Test-set confusion matrix")
        matrix = confusion_matrix(y_test, predictions, labels=[0, 1])
        st.dataframe(
            pd.DataFrame(
                matrix,
                index=["Actual: died", "Actual: survived"],
                columns=["Predicted: died", "Predicted: survived"],
            ),
            width="stretch",
        )
    with right:
        st.markdown("#### Tree overview")
        transformed_names = model.named_steps["preprocessing"].get_feature_names_out()
        figure, axis = plt.subplots(figsize=(12, 6))
        plot_tree(
            model.named_steps["tree"],
            feature_names=transformed_names,
            class_names=["Died", "Survived"],
            filled=True,
            max_depth=3,
            ax=axis,
        )
        figure.tight_layout()
        st.pyplot(figure)
        plt.close(figure)


def regression_demo() -> None:
    st.subheader("Diabetes progression regression")
    st.write(
        "Fit a decision tree to the built-in diabetes dataset and explore how "
        "tree depth changes prediction quality."
    )
    X, y = load_diabetes_data()
    depth = st.slider("Maximum tree depth", min_value=1, max_value=12, value=5)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    model = DecisionTreeRegressor(max_depth=depth, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    score = r2_score(y_test, predictions)

    metric, score_metric, samples = st.columns(3)
    metric.metric("Test mean squared error", f"{mse:,.1f}")
    score_metric.metric("Test R²", f"{score:.3f}")
    samples.metric("Test samples", f"{len(y_test):,}")

    st.markdown("#### Predict from feature values")
    with st.expander("Adjust the 10 input features", expanded=True):
        feature_values: dict[str, float] = {}
        columns = st.columns(2)
        for index, feature in enumerate(X.columns):
            minimum = float(X[feature].min())
            maximum = float(X[feature].max())
            step = max((maximum - minimum) / 100, 0.001)
            feature_values[feature] = columns[index % 2].number_input(
                feature,
                min_value=minimum,
                max_value=maximum,
                value=float(X[feature].median()),
                step=step,
                format="%.3f",
            )
    prediction = model.predict(pd.DataFrame([feature_values]))[0]
    st.info(f"Predicted disease progression measure: **{prediction:.1f}**")

    left, right = st.columns(2)
    with left:
        st.markdown("#### Actual vs. predicted")
        figure, axis = plt.subplots(figsize=(6, 4))
        axis.scatter(y_test, predictions, alpha=0.7, color="#167d75")
        axis.set_xlabel("Actual")
        axis.set_ylabel("Predicted")
        axis.grid(alpha=0.2)
        figure.tight_layout()
        st.pyplot(figure)
        plt.close(figure)
    with right:
        st.markdown("#### Tree overview")
        figure, axis = plt.subplots(figsize=(12, 6))
        plot_tree(
            model,
            feature_names=X.columns,
            filled=True,
            max_depth=2,
            ax=axis,
        )
        figure.tight_layout()
        st.pyplot(figure)
        plt.close(figure)


st.title("Decision Tree Lab")
st.caption("Two interactive lessons: classification and regression")
classification_tab, regression_tab = st.tabs(
    ["Classification · Titanic", "Regression · Diabetes"]
)
with classification_tab:
    classification_demo()
with regression_tab:
    regression_demo()