import sqlite3

conn = sqlite3.connect("SmartRestaurant.db")
cursor = conn.cursor()

file = open("data.txt", "r", encoding="utf-8")
lines = []
while True:
    line = file.readline()

    if line == "\n":
        continue
    elif not line:
        break
    else:
        line = line.strip('\n"')
        lines.append(tuple(line.split("|")))


tables = [
    ["PELATIS", 5],
    ["KRATISI", 4],
    ["TRAPEZI", 4],
    ["KRITIKI", 5],
    ["PARAGGELIA", 4],
    ["MAGEIRAS", 6],
    ["SERVITOROS", 6],
    ["PROMITHEYTIS", 4],
    ["YLIKA", 4],
    ["FAGITO", 5],
    ["POTO", 4],
    ["PARASKEYAZEI", 2],
    ["APOTELEITAI", 2],
    ["PERILAMBANEI", 2],
    ["ANALAMBANEI", 2],
    ["EFODIAZEI", 2],
    ["PROMITHEVEI", 3],
]

orismata = {
    1: "?",
    2: "?, ?",
    3: "?, ?, ?",
    4: "?, ?, ?, ?",
    5: "?, ?, ?, ?, ?",
    6: "?, ?, ?, ?, ?, ?",
}

for i in range(len(tables)):
    globals()[tables[i][0] + "_DATA"] = lines[i * 10 : (i + 1) * 10]
    # print(FAGITO_DATA)


for i in range(len(tables)):
    cursor.executemany(
        "INSERT INTO {} VALUES ({})".format(
            tables[i][0], ",".join(["?" for _ in range(tables[i][1])])
        ),
        lines[i * 10 : (i + 1) * 10],
    )


conn.commit()
conn.close()
