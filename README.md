# Linkify
![](https://github.com/IntelliTect/Linkify/actions/workflows/main.yml/badge.svg)

## Setup dev environment

### Install package dependencies
`powershell`
```powershell
python -m virtualenv env
.\env\Scripts\activate.ps1
pip install -r requirements.txt
```

`bash`
```bash
python -m virtualenv env
source ./env/Scripts/activate
pip install -r requirements.txt
```

### Setup environment variables
```
cp sample.env .env
```

Replace `.env` values with your own database values.

## To run

```
python -m linkify
```
Module will perform a dry-run by default (not make any changes). To commit changes to the database, run with `--commit`.
```
python -m linkify --commit
```

Logs are output to `/logs`.
