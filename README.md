# world development indicators

downloaded from https://data.world/worldbank/world-development-indicators

You need to log in and download the CSV. The CSV previously did not
require a login for download; one such historical CSV is archived at
https://web.archive.org/web/20171012171000/http://databank.worldbank.org/data/download/WDI_csv.zip

sha1 checksum:

```
6b70c2a727ed96a087629ccb0ab8e2005d26d9c4  WDIData.csv
```

For the database schema, see the
[one for the Maddison repo](https://github.com/riceissa/maddison-project-data/blob/master/schema.sql).

To generate the SQL files, the scripts in this repository require the
[`devec_sql_common`](https://github.com/riceissa/devec_sql_common)
Python package.  To install, run:

```bash
git clone https://github.com/riceissa/devec_sql_common
cd devec_sql_common
pip3 install -e .
```

## License

CC0

## See also

- [penn-world-table-data](https://github.com/riceissa/penn-world-table-data)
- [maddison-project-data](https://github.com/riceissa/maddison-project-data)
