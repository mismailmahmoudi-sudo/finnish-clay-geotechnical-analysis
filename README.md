
# Finnish Clay Geotechnical Analysis

## 1. GENERAL INFORMATION

### 1.1 Title of Dataset

Geotechnical Properties of Four Finnish Clay Deposits (Haarajoki, Suurpelto, Tolsa, POKO) — Reorganized Version of the Löfman and Korkiala-Tanttu (2021) Dataset.

### 1.2 Project Description

This project aims to analyze and compare the geotechnical properties of four Finnish clay deposits: Haarajoki, Suurpelto, Tolsa, and POKO.

The dataset contains laboratory measurements related to soil classification, water content, Atterberg limits, undrained shear strength, compressibility, and consolidation characteristics.

The project is developed as part of Laboratory 3 — Open and Reproducible Science (ING8100) at Polytechnique Montréal.

The main objective is to establish a reproducible data analysis workflow using Python, Git, and GitHub.

### 1.3 Author Information

**Original dataset authors:**

- Monica Susanne Löfman
- Leena Korkiala-Tanttu

**Project contributors:**

- Main contributor: Mohamed Ismail Mahmoudi
- Second contributor: Yassine Mougli
- Institution: Polytechnique Montréal
- Course: ING8100 — Open and Reproducible Science

### 1.4 Geographic Coverage

The dataset covers four Finnish clay deposits:

- Haarajoki
- Suurpelto
- Tolsa
- POKO

### 1.5 Date of Data Collection

- Original data collection period: To be verified from the original publication.
- Original dataset publication: 2021.
- Reorganized dataset publication: 2026.

### 1.6 Funding Sources

Funding information is not specified in the available dataset metadata.

### 1.7 Keywords

Geotechnical engineering, Finnish clay, soil properties, laboratory testing, water content, Atterberg limits, undrained shear strength, oedometer tests, consolidation, reproducible research, Python.

---

## 2. SHARING AND ACCESS INFORMATION

### 2.1 Dataset Availability

The dataset is publicly accessible through Borealis Demo.

**Dataset DOI:**

https://doi.org/10.80240/FK2/DZGAMU

**Borealis repository:**

https://demo.borealisdata.ca/dataset.xhtml?persistentId=doi:10.80240/FK2/DZGAMU

The project is designed to retrieve data automatically from Borealis instead of storing the original dataset directly in the GitHub repository.

### 2.2 Data License

The original dataset is distributed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license.

The original authors must be appropriately acknowledged when the data are reused.

The GitHub project's original code is licensed separately under the MIT License.

### 2.3 Related Publication

Löfman, M. S., and Korkiala-Tanttu, L. (2021).

*Transformation models for the compressibility properties of Finnish clays using a multivariate database.*

Georisk.

DOI: https://doi.org/10.1080/17499518.2020.1864410

### 2.4 Original Data Source

The reorganized dataset is based on the original dataset published by Löfman and Korkiala-Tanttu (2021), available through Zenodo.

DOI: https://doi.org/10.5281/zenodo.4709003

### 2.5 Recommended Dataset Citation

Löfman, Monica Susanne; Korkiala-Tanttu, Leena (2026).

*Propriétés géotechniques de quatre dépôts d'argile finlandais (Haarajoki, Suurpelto, Tolsa, POKO) — version réorganisée du jeu de Löfman et Korkiala-Tanttu (2021).*

Borealis.

https://doi.org/10.80240/FK2/DZGAMU

---

## 3. DATA AND FILE OVERVIEW

### 3.1 Dataset Description

The main laboratory dataset contains:

- 375 observations
- 50 variables
- Geotechnical measurements from four Finnish clay deposits
- Laboratory test results related to physical, mechanical, and consolidation properties

### 3.2 Main Data Files

| Filename | Format | Description |
|---|---|---|
| Laboratory_data.xlsx | XLSX | Original laboratory measurements |
| laboratory_data.csv | CSV | Converted laboratory dataset |
| layer_statistics.csv | CSV | Statistical information organized by soil layer |
| oedometer_increments_creep_cv.csv | CSV | Oedometer consolidation and creep information |
| convert_xlsx_to_csv.py | Python | Conversion script from Excel to CSV |
| compute_layer_statistics.py | Python | Script for calculating layer statistics |
| requirements.txt | TXT | Python dependencies provided with the Borealis dataset |
| README.md | Markdown | Original dataset documentation |
| LICENSE.txt | TXT | Data license information |
| MD5SUMS.txt | TXT | File integrity checksums |

The complete list of Borealis files will be verified and documented as the project develops.

### 3.3 Dataset Dimensions

| Dataset | Observations | Variables |
|---|---:|---:|
| laboratory_data.csv | 375 | 50 |
| layer_statistics.csv | 79 | 11 |
| oedometer_increments_creep_cv.csv | 113 | 17 |

### 3.4 Project Directory Structure

The project will follow the directory structure below:

```text
finnish-clay-geotechnical-analysis/
│
├── README.md
├── LICENSE
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── AI_Prompts.md
├── environment.yml
├── .gitignore
├── report.md
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│   ├── download_data.py
│   ├── preprocess.py
│   └── analyze.py
│
├── notebooks/
├── figures/
└── results/
```

The structure separates raw data, processed data, Python scripts, figures, and analysis results.

The data directories will be populated through the project's scripts.

### 3.5 Dataset Versions

The Borealis dataset currently displays version 2.1.

Detailed changes between versions will be verified using the Borealis version history.

---

## 4. DATA COLLECTION AND PROCESSING METHODOLOGY

### 4.1 Original Data Collection

The dataset contains results from geotechnical laboratory investigations conducted on Finnish clay deposits.

The available laboratory measurements include:

- Soil classification
- Water content
- Atterberg limits
- Unit weight
- Grain-size distribution
- Undrained shear strength
- Oedometer compression
- Consolidation properties
- Creep-related parameters

Detailed experimental procedures can be consulted in the original scientific publications.

### 4.2 Automated Data Download

The dataset will be downloaded from Borealis using the Python script:

`scripts/download_data.py`

Downloaded files will be stored in:

`data/raw/`

This procedure aims to make data acquisition reproducible.

### 4.3 Data Preprocessing

The script:

`scripts/preprocess.py`

will perform the following operations when appropriate:

1. Identify and handle missing values.
2. Verify and correct data types.
3. Standardize column names.
4. Detect inconsistent measurements.
5. Prepare the dataset for statistical analysis.

Processed files will be saved in:

`data/processed/`

### 4.4 Statistical Analysis

The script:

`scripts/analyze.py`

will calculate statistical indicators and generate figures based on the research question.

The analysis will use Python libraries including:

- Pandas
- NumPy
- Matplotlib

### 4.5 Data Quality Assurance

Quality control will include:

- Verification of dataset dimensions.
- Identification of missing values.
- Validation of numerical variables.
- Documentation of preprocessing procedures.
- Verification of generated results.

### 4.6 Software Requirements

The computational environment will use:

- Python
- Pandas
- NumPy
- Matplotlib
- Conda
- Git
- GitHub

Exact package versions will be specified in `environment.yml`.

### 4.7 Data Limitations

The analysis is limited to the geotechnical measurements available in the dataset.

Differences in testing conditions, sample characteristics, and available measurements may affect comparisons between the clay deposits.

---

## 5. DATA-SPECIFIC INFORMATION

### 5.1 Main Laboratory Dataset

**Filename:** `laboratory_data.csv`

**Number of observations:** 375

**Number of variables:** 50

The dataset contains geotechnical laboratory measurements from the four Finnish clay deposits.

The exact variable names, units, and missing-value conventions will be documented after inspection of the CSV file.

### 5.2 Layer Statistics Dataset

**Filename:** `layer_statistics.csv`

**Number of observations:** 79

**Number of variables:** 11

This dataset provides statistical information associated with soil layers.

### 5.3 Oedometer Dataset

**Filename:** `oedometer_increments_creep_cv.csv`

**Number of observations:** 113

**Number of variables:** 17

This dataset contains oedometer-related information, including consolidation and creep parameters.

### 5.4 Missing Values and Units

Missing-value codes, engineering units, and variable definitions will be verified before conducting the statistical analysis.

---

## 6. RESEARCH QUESTION AND OBJECTIVES

### 6.1 Research Question

**How do the geotechnical properties vary among the four Finnish clay deposits?**

### 6.2 Research Objectives

1. Compare the geotechnical properties of the four deposits.
2. Calculate relevant statistical indicators.
3. Identify differences and variability between deposits.
4. Generate comparative visualizations.
5. Document the workflow to ensure reproducibility.

### 6.3 Statistical Indicators

The proposed indicators are:

1. Mean water content for each clay deposit.
2. Mean plasticity index for each clay deposit.
3. Mean undrained shear strength for each clay deposit.

The final selection will depend on the variables available in the dataset.

### 6.4 Visualizations

The analysis aims to generate:

**Figure 1:** Bar chart comparing mean water content across the four clay deposits.

**Figure 2:** Box plot comparing the distribution of undrained shear strength.

Each figure will include appropriate titles, axis labels, units, and interpretations.

---

## 7. REPRODUCIBILITY

### 7.1 Computational Environment

A reproducible Python environment will be created using Conda.

The required dependencies will be documented in:

`environment.yml`

### 7.2 Reproducing the Analysis

Once implementation is complete, users will be able to reproduce the workflow by:

1. Cloning the GitHub repository.
2. Creating the Python environment.
3. Downloading the data from Borealis.
4. Executing the preprocessing script.
5. Executing the analysis script.
6. Examining the generated results and figures.

Exact installation and execution commands will be added after the scripts have been implemented and tested.

### 7.3 Expected Outputs

The project is expected to generate:

- Processed datasets.
- Statistical indicators.
- Comparative figures.
- A Markdown report presenting and interpreting the results.

---

## 8. COLLABORATIVE DEVELOPMENT

The project follows a collaborative GitHub workflow.

Team members will:

1. Create GitHub Issues to organize tasks.
2. Assign tasks to project contributors.
3. Develop modifications on separate branches.
4. Use descriptive commit messages.
5. Submit Pull Requests.
6. Review changes before merging into the `main` branch.

At least three Issues will be created, with at least one assigned to each team member.

At least one Issue will be closed through a Pull Request.

Each Pull Request will require at least one review before merging.

Contribution guidelines will be provided in:

`CONTRIBUTING.md`

---

## 9. LICENSE AND ACKNOWLEDGEMENTS

The original code developed for this GitHub project is released under the MIT License.

The original Borealis dataset is distributed under the CC BY 4.0 license.

The project acknowledges Löfman and Korkiala-Tanttu for making the geotechnical dataset available for research.

This project is developed for educational purposes as part of ING8100 at Polytechnique Montréal.

---

## 10. DOCUMENTATION AND PROJECT STATUS

Project documentation will be updated progressively as scripts, analyses, and results become available.

The use of artificial intelligence tools during project development will be documented in:

`AI_Prompts.md`

**Project status:** In development.

**Last documentation update:** To be completed.
