import requests
import json

statementTypes = dict(
    income = "income",
    balancesheet = "balancesheet",
    cashflow = "cashflow"
)

def getStatement(ttName, statementType):
    """Returns records of the requested statement"""
    ttID = ttName.split("-")[-1]
    statement = dict()
    url_string = "https://api.tickertape.in/stocks/financials/{}/{}/annual/normal?count=10"
    url = url_string.format(statementType, ttID)
    records = json.loads(requests.get(url).content)["data"]
    for record in records:
        if record["displayPeriod"] == "TTM":
            continue
        
        for key in record:
            try:
                record[key] = round(record[key], 2)
            except:
                pass
        statement[record["displayPeriod"].split("FY")[1].strip()] = record
    return statement

def getYearsAndValues(statement, key):
    "Returns yearly values of the requested key"
    yearsAndValues = {}
    for fy in sorted(statement.keys()):
        year = fy.split("FY")[-1].strip()
        value = statement[fy][key]
        if not value:
            value = 0
        yearsAndValues[year] = value
    return yearsAndValues
