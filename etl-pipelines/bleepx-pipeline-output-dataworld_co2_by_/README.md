# ETL Pipeline: bleepx-pipeline-output-dataworld_co2_by_

A full browser-based ETL pipeline by **Landrykb**.

## Medallion flow

- **Bronze (Extract):** raw CSV from https://data.world/worldbank/co2-emissions (12 data rows)
- **Silver (SQL):** exploration and aggregation in `query.sql` (4 data rows)
- **Gold (Python):** transformation in `transform.py` (2 data rows)
- **Load (S3):** uploaded to `bleepx-pipeline-output/dataworld/co2_by_country.csv`

## Files

- `raw.csv` — Bronze source data
- `query.sql` — Silver SQL
- `sql_result.csv` — Silver output
- `transform.py` — Gold Python
- `output.csv` — Gold output ready for S3
- `s3_manifest.txt` — S3 destination
- `pipeline.json` — run metadata

---
*Pushed by **Landrykb** — *bleep* approved.*
