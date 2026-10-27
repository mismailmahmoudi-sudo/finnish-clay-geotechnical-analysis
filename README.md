
# Finnish Clay Geotechnical Analysis

## Project Description

This project aims to analyze and compare the geotechnical properties of four Finnish clay deposits: Haarajoki, Suurpelto, Tolsa, and POKO.

## Research Question

How do the geotechnical properties vary among the four Finnish clay deposits?

## Objectives

- Compare the geotechnical properties of the four Finnish clay deposits.
- Calculate relevant statistical indicators.
- Generate comparative visualizations.
- Ensure that the data analysis can be reproduced using Python.

## Dataset

The dataset contains laboratory measurements of geotechnical properties collected from four Finnish clay deposits.

- **Source:** Borealis Demo
- **Dataset DOI:** https://doi.org/10.80240/FK2/DZGAMU
- **Original authors:** Löfman and Korkiala-Tanttu
- **Dataset license:** CC BY 4.0
- **Main dataset:** 375 observations and 50 variables
- **Data formats:** XLSX and CSV

The dataset includes soil classification, water content, Atterberg limits, undrained shear strength, and consolidation properties.

The data are retrieved from Borealis rather than stored directly in this GitHub repository.

## Methodology

The project follows five main steps:

1. Automatically download the dataset from Borealis using Python.
2. Preprocess the data by handling missing values and checking variable formats.
3. Calculate descriptive statistical indicators.
4. Generate comparative figures using Python.
5. Interpret the results and document the analysis.

## Statistical Indicators

The analysis is planned to include:

1. Mean water content for each clay deposit.
2. Mean plasticity index for each clay deposit.
3. Mean undrained shear strength for each clay deposit.

The final indicators will depend on the available variables and their data quality.

## Visualizations

The project aims to generate:

1. A bar chart comparing mean water content across the four deposits.
2. A box plot comparing the distribution of undrained shear strength.

Each figure will include a title, axis labels, units, and a description.

## Project Structure

```text
finnish-clay-geotechnical-analysis/
├── README.md
├── LICENSE
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── AI_Prompts.md
├── environment.yml
├── .gitignore
├── report.md
├── data/
│   ├── raw/
│   └── processed/
├── scripts/
│   ├── download_data.py
│   ├── preprocess.py
│   └── analyze.py
├── notebooks/
├── figures/
└── results/
```

This structure represents the intended organization of the project and will be completed during the laboratory.

## Reproducibility

Python will be used for data downloading, preprocessing, statistical analysis, and visualization.

The project will use the following Python libraries:

- Pandas
- NumPy
- Matplotlib

A Conda environment configuration file (`environment.yml`) will be provided to reproduce the computational environment.

The instructions for installing dependencies and executing the scripts will be added as the project develops.

## Collaboration

Development will follow a GitHub workflow based on:

1. Creating GitHub Issues to organize project tasks.
2. Developing changes on dedicated branches.
3. Writing meaningful commit messages.
4. Opening Pull Requests for review.
5. Merging reviewed contributions into the main branch.

## License

The project code is released under the MIT License.

The original Borealis dataset is distributed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license.

## Acknowledgements

The dataset is based on the work of Löfman and Korkiala-Tanttu (2021).

  
