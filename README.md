# Linkify

## Setup dev environment

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

```
cp sample.env .env
```

Replace `.env` value with your own database values.

## To run

```
python -m linkify
```