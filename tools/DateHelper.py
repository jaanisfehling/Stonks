def oneMonthEarlier(date):
    # Datum für einen Monat früher zurückgeben
    # Format: "2020-12-31"
    date = date.split("-")
    # Falls es nicht Januar ist
    if date[1] != "01":
        date[1] = str(int(date[1]) - 1)
    else:
        date[0] = str(int(date[0]) - 1)
        date[1] = "12"
    new_date = date[0] + "-" + date[1] + "-" + date[2]
    return new_date

def oneDayEarlier(date):
    # Einen Tag früher zurückgeben
    # Format: "2020-12-31"
    date = date.split("-")
    # Falls es der erste Tag im Monat ist
    if date[2] == "01":
        date[2] = "31"
        # Falls es nicht Januar ist
        if date[1] != "01":
            date[1] = str(int(date[1]) - 1)
        else:
            date[0] = str(int(date[0]) - 1)
            date[1] = "12"
    else:
        date[2] = str(int(date[2])-1)
    new_date = date[0] + "-" + date[1] + "-" + date[2]
    return new_date
