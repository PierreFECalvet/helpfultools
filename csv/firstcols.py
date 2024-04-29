import csv

def main(input_file, output_file, num_col):
    # Specify encoding as 'utf-8' when opening the file
    with open(input_file, 'r', encoding='utf-8') as file_in, open(output_file, 'w', newline='', encoding='utf-8') as file_out:
        reader = csv.reader(file_in)
        writer = csv.writer(file_out)
        for row in reader:
            new_row = row[:num_col]  # Keep only the first 28 columns
            writer.writerow(new_row)

def input_file():
    input_file = input("Enter the name of the input file: ")
    while True:
        if input_file == '':
            print("You must enter a file name.")
            input_file = input("Enter the name of the input file: ")
        elif not input_file.endswith('.csv'):
            print("Input file must be a CSV file.")
            input_file = input("Enter the name of the input file: ")
        else:
            return input_file

def output_file():
    output_file = input("Enter the name of the output file: ")
    while True:
        if output_file == '':
            print("You must enter a file name.")
            output_file = input("Enter the name of the output file: ")
        elif not output_file.endswith('.csv'):
            print("Output file must be a CSV file.")
            output_file = input("Enter the name of the output file: ")
        else:
            return output_file

def col_num():
    number_of_columns = input("number of columns?: ")
    while True:
        if number_of_columns > 0:
            return number_of_columns
        else:
            print("must be a number above 0")
            number_of_columns = input("number of columns?: ")

if __name__ == '__main__':
    input_file_path = input_file()
    output_file_path = output_file()
    number_of_columns = input("number of columns?: ")
    main(input_file_path, output_file_path, number_of_columns)
