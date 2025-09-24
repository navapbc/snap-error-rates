# Preliminary Models of SNAP Error Rates

This repository contains data and code to reproduce a preliminary analysis for
how well state policies can explain SNAP error rates. A full description of the
methodology and preliminary results are available in:
[SNAP Error Rate Modeling](https://docs.google.com/document/d/1zNUsgYA81ChnMRFV03Elat1qz8kdMfGiLd08wDqRo5I/edit?tab=t.0#heading=h.mtc4swvlio8d)

## Running

To run the analysis, install the required python packages in a virtual environment
and execute the runner script with:

    python3.12 -m venv ~/envs/snap-error-rates
    source ~/envs/snap-error-rates/bin/activate
    pip install -r requirements.txt
    bash run.sh

## Data Sources

[SNAP Payment Error Rates](https://www.fns.usda.gov/snap/qc/per)

[SNAP Policy Data Sets](https://www.ers.usda.gov/data-products/snap-policy-data-sets)

Supplemental Nutrition Assistance Program COVID-19 Policy and Enrollment Data, United States, 1987-2024
(ICPSR [39331](https://www.icpsr.umich.edu/web/sbeccc/studies/39331)).

[United States Governors 1775-2020](https://doi.org/10.3886/E102000V3)

[The Book of the States, The Governors: 2022](https://bookofthestates.org/tables/2022-4-1/)

[The Book of the States, The Governors: 2023](https://bookofthestates.org/tables/2023-4-1/)

Copyright © 2025 Nava PBC. All rights reserved.
