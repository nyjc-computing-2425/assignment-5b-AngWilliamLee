# Part 1
def read_csv(filename):
  """
  Define a function, read_csv(filename), that:
  1) Takes a string filename
  2) Reads CSV data stored in filename
  3) Returns two values, (header, data):
  - header is a list containing the column labels (from the first row)
  - data is a nested list containing the data.
    Data should be converted to appropriate types, i.e. int, float, or str.
  """
  with open(filename, 'r') as csv_file:
    data = csv_file.read
    first_row = csv_file.readline()
    header = first_row.split(',')
    return (header, data)
    

# Part 2
def filter_gender(enrolment_by_age, sex):
    filtered_records = []
    for record in enrolment_by_age:
        if record[enrolment_by_age[0].index("sex")] == sex:
            filtered_records.append([record[0], record[1], record[2]])
    return filtered_records


# Part 3
def sum_by_year(enrolment):
  year_enrolment = {}  # Dictionary to store enrolment totals for each year
  for record in enrolment_data:
      year = record[0]
      enrolment = record[-1]  # Assuming enrolment is the last item in the record
      if year in year_enrolment:
          year_enrolment[year] += enrolment
      else:
          year_enrolment[year] = enrolment
  return [[year, total_enrolment] for year, total_enrolment in year_enrolment.items()]


# Part 4
def write_csv(filename, header, data):
  with open(filename, 'w', newline='') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(header)
      for row in data:
          writer.writerow(row)
  return len(data)


# TESTING
# You can write code below to call the above functions
# and test the output
