# Part 1
def read_csv(filename):
  """
  1) Takes a string filename
  2) Reads CSV data stored in filename
  3) Returns two values, (header, data):
  - header is a list containing the column labels (from the first row)
  - data is a nested list containing the data.
    Data should be converted to appropriate types, i.e. int, float, or str.
  """
  with open(filename, 'r') as csv_file:
    data = []
    for line in csv_file:
        row_list = line.strip().split(',')
        data.append(row_list)
    first_row = csv_file.readline()
    header = first_row.split(',')
    return header, data
    

# Part 2
def filter_gender(enrolment_by_age, sex):
  """
  1) Takes a list of records enrolment_by_age and a string sex
  2) Return a list of records where the value in the "sex" column matches string sex (We are only keeping data for total enrolment, not split by gender.)
  3) Exclude the sex column from the returned records.
  You should end up with data for three columns: year, age, and enrolment_jc.
  """
  filtered_records = []
  for record in enrolment_by_age:
      if record[-1] == sex:
          filtered_records.append([record[0], record[1], record[2]])
  return filtered_records


# Part 3
def sum_by_year(enrolment_data):
  """
  1) Add up the total enrolment for each year, regardless of age
  2) Return the result as a list of lists. Each inner list comprises two integers, year and total_enrolment.
  """
  enrolment_by_year = {} #making dictionary
  for record in enrolment_data:
      year = record[0]
      enrolment = record[-1]
    
      if year in enrolment_by_year:
          enrolment_by_year[year] += enrolment
      else:
          enrolment_by_year[year] = enrolment
  return [[year, total_enrolment] for year, total_enrolment in enrolment_by_year.items()]


# Part 4
def write_csv(filename, header, data):
  """
   write header and data to filename in CSV format and return the number of lines written. Any existing data in filename should be ignored and overwritten.
  """
  with open(filename, 'w') as file:
      file.write(','.join(header) + '\n')

      for row in data:
          row_str = ','.join(str(x) for x in row)
          file.write(row_str + '\n')
        
  with open(filename, 'r') as file:
      return len(file.readlines()) - 1

  

# TESTING
# You can write code below to call the above functions
# and test the output
# enrolment_by_age = [[1984, '17 YRS', 8710, 'girl'], [1984, '18 YRS', 3927, 'boy']]
# print(filter_gender(enrolment_by_age, 'girl'))
# enrolment_data = [
#     [1984, "poo", 1000],
#     [1984, 2000],
#     [1985, 1500],
#     [1985, 2000],
#     [1985, 500]
# ]
# enrolment_by_year = sum_by_year(enrolment_data)
# print(enrolment_by_year)
# filename = 'total-enrolment-by-year.csv'
# header = ["year", "total_enrolment"]
# enrolment_by_year = [[2020, 1500],
#     [2021, 1800],
#     [2022, 2000],
#     [2023, 2100],
#     [2024, 2200], [2022, 1022]]

# num_lines_written = write_csv(filename, header, enrolment_by_year)
# print(num_lines_written)
