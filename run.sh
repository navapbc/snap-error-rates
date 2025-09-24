# Extract housholds from ACS
python scripts/data_households.py data/raw/ACSST1Y2017.S2201-2025-09-03T182341.csv
python scripts/data_households.py data/raw/ACSST1Y2018.S2201-2025-09-03T182328.csv
python scripts/data_households.py data/raw/ACSST1Y2019.S2201-2025-09-03T181950.csv
python scripts/data_households.py data/raw/ACSST1Y2022.S2201-2025-09-03T175501.csv
python scripts/data_households.py data/raw/ACSST1Y2023.S2201-2025-09-03T180918.csv

# Extract SNAP rate from ACS
python scripts/data_snap_rate.py data/raw/ACSST1Y2017.S2201-2025-09-03T182341.csv
python scripts/data_snap_rate.py data/raw/ACSST1Y2018.S2201-2025-09-03T182328.csv
python scripts/data_snap_rate.py data/raw/ACSST1Y2019.S2201-2025-09-03T181950.csv
python scripts/data_snap_rate.py data/raw/ACSST1Y2022.S2201-2025-09-03T175501.csv
python scripts/data_snap_rate.py data/raw/ACSST1Y2023.S2201-2025-09-03T180918.csv

# Build controls
python scripts/data_controls.py

# Extract pre-COVID policies
python scripts/data_policies_precovid.py

# Extract post-COVID policies
python scripts/data_policies_postcovid.py

# Model pre-COVID error rates
python scripts/model_precovid.py

# Model post-COVID error rates
python scripts/model_postcovid.py

# Plot pre-COVID error rates
python scripts/plot_precovid.py

# Plot post-COVID error rates
python scripts/plot_postcovid.py
