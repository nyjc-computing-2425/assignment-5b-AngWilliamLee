# from pprint import pprint

# Part 1
def read_csv(filename):
    """
    Given a filename, reads the csv file and return a list of lists
  
    Parameter
    ---------
    filename: str
       The filename of the csv file to read
  
    Returns
    -------
    tuple
        a tuple consisting of a header list and a nested list containing the data
    """
  
    with open(filename, 'r') as csv_file:
        first_row = csv_file.readline()
        header = first_row.split(',')
        data = []
        for line in csv_file:
            row_list = line.strip().split(',')
            row_list[0] = int(row_list[0])
            row_list[3] = int(row_list[3])
            data.append(row_list)
            
        return header, data

# pprint(read_csv("pre-u-enrolment-by-age.csv"))
        
    

# Part 2
def filter_gender(enrolment_by_age, sex):
    """
    Given a nested list, filters by gender, returns a nested list

    Parameter
    ---------
    enrolment_by_age: list
      The list to be filtred

    Returns
    -------
    filtered_records: list
      nested list containing gender-filtered data
    """            
    filtered_records = []
    for record in enrolment_by_age:
        if record[2] == sex:
            filtered_records.append([record[0], record[1], record[3]])
            # filtered_records.append([record[0], record[3]])

    return filtered_records

# with open("pre-u-enrolment-by-age.csv", 'r') as csv_file:
#     first_row = csv_file.readline()
#     data = []
#     for line in csv_file:
#         row_list = line.strip().split(',')
#         row_list[0] = int(row_list[0])
#         row_list[3] = int(row_list[3])
#         data.append(row_list)
        
# mf_enrolment = filter_gender(data, 'MF')
# pprint(mf_enrolment)


# Part 3
def sum_by_year(enrolment_data):
    """
    Given a nested list, sums enrolment_data by year, returns a nested list
  
    Parameter
    ---------
    enrolment_data: list
      The list to be summed
  
    Returns
    -------
    total_enrolment : list
      nested list with each inner list comprising year and summed data
    """
  
    result = []

    for record in enrolment_data:
        year = record[0]
        enrolment = record[2]
    
        year_found = False
        for entry in result:
            if entry[0] == year:
                entry[1] += enrolment
                year_found = True

        if not year_found:
            result.append([year, enrolment])
    return result
    
# enrolment_by_year = sum_by_year(mf_enrolment)
# pprint(enrolment_by_year)



# Part 4
def write_csv(filename, header, data):
    """
    Given a filename, header and data, write them into a csv file and return csv file and number of lines in it
  
    Parameter
    ---------
    filename: str
      The filename for the csv file to be written
    header: list
      The headers for the csv file to be written
    data: list
      The data for the csv file to be written
  
    Returns
    -------
    length_of_file: str
      string containing the number of lines in the csv file to be written
    """
    with open(filename, 'w') as file:
        file.write(','.join(header) + '\n')

        count = 0
        for row in data:
            row[0] = str(row[0])
            row[1] = str(row[1])
            row_str = ','.join(row)
            file.write(row_str + '\n')
            count += 1
        return count
        # return (header, data, count)

# pprint(write_csv('total-enrolment-by-year.csv', ["year", "total_enrolment"], enrolment_by_year))


  

# TESTING
# You can write code below to call the above functions
# and test the output
