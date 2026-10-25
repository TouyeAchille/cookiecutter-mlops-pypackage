"""Train and run a reproducible tabular regression pipeline."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def build_pipeline(features: pd.DataFrame, alpha: float = 1.0) -> Pipeline:
    """Build a preprocessing and Ridge regression pipeline from feature columns."""
    numeric = features.select_dtypes(include="number").columns.tolist()
    categorical = [column for column in features.columns if column not in numeric]
    transformers: list[tuple[str, Any, list[str]]] = []
    if numeric:
        transformers.append(("numeric", Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scale", StandardScaler()),
        ]), numeric))
    if categorical:
        transformers.append(("categorical", Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encode", OneHotEncoder(handle_unknown="ignore")),
        ]), categorical))
    if not transformers:
        raise ValueError("The dataset must contain at least one feature column.")
    return Pipeline([
        ("preprocess", ColumnTransformer(transformers)),
        ("model", Ridge(alpha=alpha)),
    ])


def train(data_path: str | Path, target: str, output_dir: str | Path = "artifacts",
          test_size: float = 0.2, random_state: int = 42, alpha: float = 1.0) -> dict[str, Any]:
    """Train/evaluate on a CSV and save a model plus run metadata."""
    data_path, output_dir = Path(data_path), Path(output_dir)
    if not 0 < test_size < 1:
        raise ValueError("test_size must be between 0 and 1.")
    if not data_path.is_file():
        raise FileNotFoundError(f"Dataset not found: {data_path}")
    frame = pd.read_csv(data_path)
    if target not in frame.columns:
        raise ValueError(f"Target column {target!r} is missing from {data_path}.")
    frame = frame.dropna(subset=[target])
    if len(frame) < 3:
        raise ValueError("At least three rows with a target value are required.")
    X, y = frame.drop(columns=[target]), frame[target]
    if not pd.api.types.is_numeric_dtype(y):
        raise ValueError("This starter supports numeric regression targets only.")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    estimator = build_pipeline(X_train, alpha=alpha)
    estimator.fit(X_train, y_train)
    predictions = estimator.predict(X_test)
    metrics = {
        "mae": float(mean_absolute_error(y_test, predictions)),
        "rmse": float(mean_squared_error(y_test, predictions) ** 0.5),
        "r2": float(r2_score(y_test, predictions)),
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    joblib.dump(estimator, output_dir / "model.joblib")
    metadata = {
        "target": target, "features": X.columns.tolist(), "rows": len(frame),
        "train_rows": len(X_train), "test_rows": len(X_test),
        "random_state": random_state, "alpha": alpha, "metrics": metrics,
    }
    (output_dir / "metrics.json").write_text(json.dumps(metadata, indent=2) + "\n")
    return metadata


def predict(model_path: str | Path, data_path: str | Path) -> pd.Series:
    """Load a saved model and return predictions for the rows in a CSV."""
    model = joblib.load(model_path)
    features = pd.read_csv(data_path)
    return pd.Series(model.predict(features), name="prediction")
