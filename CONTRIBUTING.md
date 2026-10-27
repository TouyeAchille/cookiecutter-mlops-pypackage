# Contributing Guide

Thank you for contributing to this project!

CONTRIBUTING.md is a file that explains how developers should contribute to a project. It defines the workflow for submitting changes, reporting bugs, writing tests, and following the project's standards.

In an AI/ML or MLOps repository, it helps ensure that contributions from developers and AI coding agents follow the same process.

## 1. Development Setup

- Install the required tools with `mise install`.
- Install project dependencies using the documented setup command.
- Read `README.md` and `AGENTS.md` before making changes.

## 2. Branching

- Create a branch for each change.
- Use descriptive names, such as:
  - `feat/model-monitoring`
  - `fix/data-validation`
  - `docs/update-readme`

## 3. Code Quality

- Follow PEP 8 conventions.
- Use type hints where appropriate.
- Keep functions modular and testable.
- Run `ruff check .` before submitting.

## 4. Testing

- Add tests for new functionality.
- Run `pytest` before opening a pull request.
- Never use production data containing sensitive information in tests.

## 5. Machine Learning

- Prevent data leakage.
- Document important changes to features and preprocessing.
- Record relevant model evaluation metrics.
- Never claim improved model performance without evidence.

## 6. Pull Requests

- Explain what changed and why.
- Include relevant tests and results.
- Update documentation when necessary.
- Do not include secrets, credentials, or unintended data files.

## 7. Changelog

- Document significant user-facing changes in `CHANGELOG.md`.

## 1. Development Setup

- Install the required tools with `mise install`.
- Install project dependencies using the documented setup command.
- Read `README.md` and `AGENTS.md` before making changes.

## 2. Branching

- Create a branch for each change.
- Use descriptive names, such as:
  - `feat/model-monitoring`
  - `fix/data-validation`
  - `docs/update-readme`

## 3. Code Quality

- Follow PEP 8 conventions.
- Use type hints where appropriate.
- Keep functions modular and testable.
- Run `ruff check .` before submitting.

## 4. Testing

- Add tests for new functionality.
- Run `pytest` before opening a pull request.
- Never use production data containing sensitive information in tests.

## 5. Machine Learning

- Prevent data leakage.
- Document important changes to features and preprocessing.
- Record relevant model evaluation metrics.
- Never claim improved model performance without evidence.

## 6. Pull Requests

- Explain what changed and why.
- Include relevant tests and results.
- Update documentation when necessary.
- Do not include secrets, credentials, or unintended data files.

## 7. Changelog

- Document significant user-facing changes in `CHANGELOG.md`.
