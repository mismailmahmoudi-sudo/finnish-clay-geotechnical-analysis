
# Contributing Guidelines

## 1. Introduction

This project, Finnish Clay Geotechnical Analysis, is developed as part of Laboratory 3 — Open and Reproducible Science (ING8100) at Polytechnique Montréal.

The objective is to develop a reproducible workflow for analyzing geotechnical properties of four Finnish clay deposits using Python and GitHub.

Contributions should follow the guidelines below to ensure collaboration, code quality, and reproducibility.

## 2. Project Contributors

The project is developed by two team members:

- Contributor 1: Mohamed Ismail Mahmoudi / mismailmahmoudi-sudo
- Contributor 2: Yassine Mougli / yassinemougli02

Both contributors are responsible for completing assigned tasks, documenting their work, and reviewing each other's contributions.

All contributors must follow the rules described in `CODE_OF_CONDUCT.md`.

## 3. GitHub Issues

GitHub Issues are used to organize and track project tasks.

Each Issue must include:
- A clear title and description.
- An expected outcome.
- An assigned team member.

Project requirements:
- Create at least 3 Issues.
- Assign at least one Issue to each contributor.
- Close at least one Issue through a Pull Request.

## 4. Branching Strategy

The `main` branch must remain stable and protected from direct modifications.

All changes should be developed on dedicated branches.

Branch naming conventions:

- `feature/description` — New functionality.
- `fix/description` — Bug fixes.
- `docs/description` — Documentation.
- `data/description` — Data processing.
- `analysis/description` — Statistical analysis.

Examples:
- `docs/update-readme`
- `feature/download-data`
- `data/preprocessing`
- `analysis/statistical-indicators`

## 5. Commits and Pull Requests

Contributors should follow this workflow:

1. Create or select a GitHub Issue.
2. Create a working branch from `main`.
3. Implement and test the required changes.
4. Commit changes with descriptive messages.
5. Open a Pull Request targeting `main`.
6. Request a review from the other team member.
7. Address review comments before merging.

Commit message examples:

- `docs: update project documentation`
- `feat: add Borealis download script`
- `data: implement preprocessing`
- `analysis: calculate statistical indicators`
- `fix: correct missing values`

Each Pull Request must receive at least one review from another contributor before merging.

Contributors must not approve their own Pull Requests.

To automatically close an Issue, include a reference such as `Closes #3` in the Pull Request description.

## 6. Code Quality and Reproducibility

All Python scripts should be readable, documented, and reproducible.

Contributors should:

- Use clear variable and function names.
- Add meaningful comments.
- Avoid duplicated code and absolute file paths.
- Handle missing or invalid data appropriately.
- Test scripts before submitting a Pull Request.
- Document dependencies in `environment.yml`.
- Update the README when necessary.

The main scripts are:

- `scripts/download_data.py`
- `scripts/preprocess.py`
- `scripts/analyze.py`

## 7. Data Management

The dataset is hosted on Borealis:

https://doi.org/10.80240/FK2/DZGAMU

Original data files must not be committed directly to GitHub.

Data should be downloaded automatically using the project script and organized into:

- `data/raw/` — Downloaded data.
- `data/processed/` — Processed data.

Temporary files, caches, virtual environments, and unnecessary generated files must be excluded using `.gitignore`.

The original dataset is licensed under CC BY 4.0.

## 8. Documentation and Academic Integrity

Documentation must be updated as the project develops.

Relevant files include:

- `README.md`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `AI_Prompts.md`
- `report.md`

Any use of artificial intelligence must comply with the course's academic integrity requirements and be documented in `AI_Prompts.md`.

All external scientific sources must be appropriately acknowledged.

Contributors are expected to maintain transparency, respect the applicable licenses, and ensure that the project can be reproduced by other researchers.
