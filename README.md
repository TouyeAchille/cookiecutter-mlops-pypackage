---
noteId: "c3ce2de0d1ae11f1a8d84fc388289bff"
tags: []

---

# MLOps Python package template

A Cookiecutter starter for a Python machine learning project. It generates a `uv`-managed package with a tabular regression training and prediction pipeline, project configuration, and places for data, artifacts, notebooks, configuration, and documentation.

## Generate a project

Install [uv](https://docs.astral.sh/uv/) and run this from the directory where you want the new project:

```bash
uvx cruft create https://github.com/TouyeAchille/cookiecutter-mlops-pypackage.git
```

Answer the Cookiecutter prompts for the project name, Python package name, Python version, description, author, email, and version. To render the checked-out template instead, run:

```bash
uvx cookiecutter .
```

## What the generated package contains

- A Python package under `src/<package_name>/` and a `pyproject.toml` configured for `uv` builds.
- A starter scikit-learn pipeline that imputes and scales numeric features, imputes and one-hot encodes categorical features, then fits Ridge regression.
- Training helpers that split a CSV dataset, calculate MAE, RMSE, and R², and save a model and run metadata under `artifacts/`.
- A prediction helper that loads a saved model and predicts rows from a CSV file.
- Starter directories for configuration, data, documentation, environment files, MLflow tracking, notebooks, and tests.
- Docker, pre-commit, contribution, changelog, and license files to customize as the project grows.

The training and prediction functions are currently Python APIs in `src/<package_name>/scripts.py`. The generated console-script entry is a placeholder and needs a `main` function before it can be used as a command-line interface.

## Develop the generated project

From the generated project directory, install dependencies and activate its environment:

```bash
uv sync
source .venv/bin/activate
```

Put a CSV dataset in `data/` and call the training helper, replacing `my_package` and `target_column` with your package and target names:

```python
from my_package.scripts import predict, train

result = train("data/dataset.csv", target="target_column")
print(result["metrics"])

predictions = predict("artifacts/model.joblib", "data/new_rows.csv")
predictions.to_csv("predictions.csv", index=False)
```

The input dataset must have at least three rows with a non-empty numeric target column and at least one feature column. `new_rows.csv` should contain the same feature columns used for training.

## Maintain the template

Edit files under `{{cookiecutter.package_name}}/` to change the generated project. Update `cookiecutter.json` when changing template prompts or defaults. Render the local template to a temporary directory to review the generated result.
