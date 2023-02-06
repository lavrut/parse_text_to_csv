import csv

def parse_text_to_csv(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        data = [line.strip().split() for line in lines]

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
        
    return data

def extract_column(data, column_index):
    return [row[column_index] for row in data]

input_file = 'input.txt'
output_file = 'output.csv'
data = parse_text_to_csv(input_file, output_file)
column = extract_column(data, column_index=0)
print(column)
