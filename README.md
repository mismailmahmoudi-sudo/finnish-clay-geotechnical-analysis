# Finnish Clay Geotechnical Analysis

**Course:** ING8100 — Open and Reproducible Science, Polytechnique Montréal  
**Project status:** Analysis completed

## 1. General Information

### Dataset and Project Description

**Dataset:** *Geotechnical Properties of Four Finnish Clay Deposits (Haarajoki, Suurpelto, Tolsa, POKO) — Reorganized Version of the Löfman and Korkiala-Tanttu (2021) Dataset.*

This project compares selected geotechnical properties of four Finnish clay deposits using publicly available laboratory measurements. Developed for Laboratory 3 of ING8100, it demonstrates a reproducible workflow combining automated data acquisition, preprocessing, statistical analysis, visualization, and collaborative development through GitHub.

**Project contributors:**
- [mismailmahmoudi-sudo](https://github.com/mismailmahmoudi-sudo)
- [yassinemougli02](https://github.com/yassinemougli02)

**Source dataset authors:** Monica Susanne Löfman and Leena Korkiala-Tanttu.

**Institution:** Polytechnique Montréal, Canada.

**Geographic coverage:** Haarajoki, Suurpelto, Tolsa, and POKO, Finland.

**Original research:** 2021.  
**Reorganized Borealis dataset:** 2026 (version 2.1 at the time of initial documentation).

The original data collection dates and funding sources were not established from the metadata consulted.

**Keywords:** Geotechnical engineering, Finnish clay, water content, undrained shear strength, unit weight, reproducible research.

## 2. Sharing and Access Information

The dataset is publicly available through the Borealis demonstration repository.

- **Borealis dataset:** https://demo.borealisdata.ca/dataset.xhtml?persistentId=doi:10.80240/FK2/DZGAMU
- **Dataset DOI:** https://doi.org/10.80240/FK2/DZGAMU
- **Original dataset:** https://doi.org/10.5281/zenodo.4709003
- **Source data license:** Creative Commons Attribution 4.0 International (CC BY 4.0).
- **Project code license:** MIT License (see `LICENSE`).

The original data are retrieved programmatically from Borealis and are not committed directly to GitHub. The Borealis demonstration instance is intended for testing and may not provide permanent availability.

**Related publication:**

Löfman, M. S., & Korkiala-Tanttu, L. (2021). *Transformation models for the compressibility properties of Finnish clays using a multivariate database*. Georisk. https://doi.org/10.1080/17499518.2020.1864410

## 3. Data and File Overview

The main laboratory dataset contains **375 observations and 50 variables**. The source collection includes additional soil-layer and oedometer measurements, but this project analyzes the main laboratory dataset.

### Repository Structure

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
│   ├── mean_water_content.png
│   └── undrained_strength_boxplot.png
└── results/
    └── geotechnical_statistics.csv
```

The `data/raw/` and `data/processed/` directories contain locally generated data files, which are excluded from version control. Empty directories may be represented by `.gitkeep` files.

## 4. Data Collection and Processing Methodology

The source dataset includes laboratory measurements from soil classification, fall cone, and oedometer tests. Detailed experimental procedures are available in the original research documentation.

The project implements three Python scripts:

1. **Data download — `scripts/download_data.py`:** Retrieves the laboratory dataset from the Borealis API and saves it as `data/raw/Laboratory_data.xlsx`.
2. **Preprocessing — `scripts/preprocess.py`:** Standardizes column names, removes unnecessary whitespace, identifies missing-value markers, and exports `data/processed/laboratory_data_clean.csv` while preserving the original 375 observations.
3. **Analysis — `scripts/analyze.py`:** Calculates descriptive statistics and generates comparative figures, saving outputs in `results/` and `figures/`.

The analysis uses Python 3.11, Pandas, NumPy, Matplotlib, OpenPyXL, and Requests. Dependencies are defined in `environment.yml`.

## 5. Data-Specific Information

Three geotechnical parameters were selected for analysis:

| Variable | Description | Unit | Available measurements |
|---|---|---|---:|
| `w0` | Natural water content | % | 369 |
| `su` | Undrained shear strength (fall cone test) | kPa | 189 |
| `gamma` | Unit weight | kN/m³ | 275 |

Variable definitions and units were verified using the Borealis data dictionary.

Missing measurements are excluded from the relevant statistical calculations without removing entire observations from the dataset. Consequently, sample sizes differ between variables and deposits.

## 6. Research Question and Analysis

**Research question:** How do the geotechnical properties vary among the four Finnish clay deposits?

For each deposit, the analysis calculates three descriptive statistics: the number of valid measurements, arithmetic mean, and standard deviation.

Two figures are generated:

- **Figure 1:** Mean natural water content (%) by clay deposit.
- **Figure 2:** Distribution of undrained shear strength (kPa) by clay deposit.

The analysis shows differences between the deposits. Suurpelto exhibits the highest mean natural water content and lowest mean unit weight, while Tolsa shows the opposite pattern. Haarajoki has the highest mean undrained shear strength.

The detailed results, figures, scientific interpretation, and limitations are presented in the [scientific report](report.md).

## 7. Reproducibility and Usage

### Requirements

Install Git and Anaconda or Miniconda. An internet connection is required to download the original dataset.

### Installation and Execution

Open Anaconda Prompt or a terminal, then execute:

```bash
# Clone the repository
git clone https://github.com/mismailmahmoudi-sudo/finnish-clay-geotechnical-analysis.git
cd finnish-clay-geotechnical-analysis

# Create and activate the environment
conda env create -f environment.yml
conda activate finnish-clay-env

# Run the reproducible workflow
python scripts/download_data.py
python scripts/preprocess.py
python scripts/analyze.py
```

All Python commands must be executed from the project root directory. If the Conda environment already exists, skip the environment creation command.

### Generated Outputs

| Output file | Description |
|---|---|
| `data/raw/Laboratory_data.xlsx` | Original dataset downloaded from Borealis |
| `data/processed/laboratory_data_clean.csv` | Cleaned laboratory dataset |
| `results/geotechnical_statistics.csv` | Descriptive statistics |
| `figures/mean_water_content.png` | Mean natural water content comparison |
| `figures/undrained_strength_boxplot.png` | Undrained shear strength distribution |

The figures and interpretation are also available in [report.md](report.md).

## 8. Collaboration and Contributions

The project follows a collaborative GitHub workflow based on Issues, feature branches, descriptive commits, Pull Requests, and peer reviews.

The main development tasks were organized through:

- **Issue #3:** Automated Borealis data download.
- **Issue #4:** Data preprocessing.
- **Issue #5:** Statistical analysis and figure generation.

Changes were reviewed before being merged into the protected `main` branch. The repository's commit and Pull Request history records contributions and approvals.

Additional documentation:

- [CONTRIBUTING.md](CONTRIBUTING.md) — Contribution guidelines.
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — Collaboration and conduct expectations.
- [AI_Prompts.md](AI_Prompts.md) — Documentation of generative AI assistance.

## 9. Reuse Limitations and Acknowledgements

This project is a secondary analysis of previously collected laboratory data. The results are descriptive and should not be used directly as engineering design parameters.

Differences in sample sizes, sampling depths, soil layers, and testing conditions may influence comparisons between deposits.

The original research and dataset are credited to **Löfman and Korkiala-Tanttu**. Source data reuse is governed by CC BY 4.0, while the repository code is distributed under the MIT License.

The project acknowledges Borealis for research data sharing and GitHub for supporting collaborative and reproducible development.

---

**Last updated:** November 2026.
