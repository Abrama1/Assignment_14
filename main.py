import csv
import pandas

# Task_1


def filter_and_create_survived_csv(input_file, output_file):

    with open(input_file, "r") as input_csv, open(output_file, "w", newline="") as output_csv:

        reader = csv.DictReader(input_csv)
        fieldnames = reader.fieldnames

        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:

            if row["Survived"] == "1":

                writer.writerow(row)


filter_and_create_survived_csv("titanic.csv", "survived.csv")

print(f"The 'survived.csv' file has been created with only the survivor information.")

# Task_2


def filter_and_create_ssl_companies_csv(input_file, output_file):
    ssl_companies = []

    with open(input_file, "r") as input_csv:
        reader = csv.DictReader(input_csv)

        fieldnames = ["Index", "Organization Id", "Name", "Website", "Industry", "Number of employees"]

        with open(output_file, "w", newline='') as output_csv:

            writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:

                website = row["Website"].lower()

                if website.startswith("https://"):

                    ssl_companies.append({
                        "Index": row["Index"],
                        "Organization Id": row["Organization Id"],
                        "Name": row["Name"],
                        "Website": row["Website"],
                        "Industry": row["Industry"],
                        "Number of employees": row["Number of employees"],
                    })

                    writer.writerow({
                        "Index": row["Index"],
                        "Organization Id": row["Organization Id"],
                        "Name": row["Name"],
                        "Website": row["Website"],
                        "Industry": row["Industry"],
                        "Number of employees": row["Number of employees"],
                    })

    return ssl_companies


ssl_companies_data = filter_and_create_ssl_companies_csv("organizations-100.csv", "ssl_companies.csv")

print(f"The 'ssl_companies.csv' file has been created with SSL protected companies.")

# Task_3


df = pandas.read_csv("organizations-100.csv")

df_sorted = df.sort_values(by="Number of employees")

df_sorted.to_csv("sorted_csv.csv", index=False)

print("Sorting and writing to sorted_csv.csv completed successfully.")
