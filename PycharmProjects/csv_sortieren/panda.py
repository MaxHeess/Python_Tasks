import pandas

data = pandas.read_csv("aufgabe50.csv")
sorted_data = data.sort_values(by=["last_name"], ascending = True)
sorted_data.to_csv("aufgabe_sortiert.csv", index = False)