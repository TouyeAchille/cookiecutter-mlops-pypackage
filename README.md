# MLOps Python package template


## Generate a project

Install uv, then run from the directory where you want the new project:

```bash
uvx cruft create https://github.com/TouyeAchille/cookiecutter-mlops-pypackage.git
```

Enter a project name when prompted. Cookiecutter converts it to a Python-safe package name. To render this local checkout, use:

```bash
uvx cookiecutter .
```

## Template maintenance

Update the files under `{{cookiecutter.package_name}}/` when changing the generated project structure. Update `cookiecutter.json` when adding or changing prompts.
