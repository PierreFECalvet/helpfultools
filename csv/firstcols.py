{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN0oTC0IwaweRGBSTTq55kz"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "sNmjUk9I63-v"
      },
      "outputs": [],
      "source": [
        "import csv\n",
        "\n",
        "def main(input_file, output_file, num_col):\n",
        "    # Specify encoding as 'utf-8' when opening the file\n",
        "    with open(input_file, 'r', encoding='utf-8') as file_in, open(output_file, 'w', newline='', encoding='utf-8') as file_out:\n",
        "        reader = csv.reader(file_in)\n",
        "        writer = csv.writer(file_out)\n",
        "        for row in reader:\n",
        "            new_row = row[:num_col]  # Keep only the first 28 columns\n",
        "            writer.writerow(new_row)\n",
        "\n",
        "def input_file():\n",
        "    input_file = input(\"Enter the name of the input file: \")\n",
        "    while True:\n",
        "        if input_file == '':\n",
        "            print(\"You must enter a file name.\")\n",
        "            input_file = input(\"Enter the name of the input file: \")\n",
        "        elif not input_file.endswith('.csv'):\n",
        "            print(\"Input file must be a CSV file.\")\n",
        "            input_file = input(\"Enter the name of the input file: \")\n",
        "        else:\n",
        "            return input_file\n",
        "\n",
        "def output_file():\n",
        "    output_file = input(\"Enter the name of the output file: \")\n",
        "    while True:\n",
        "        if output_file == '':\n",
        "            print(\"You must enter a file name.\")\n",
        "            output_file = input(\"Enter the name of the output file: \")\n",
        "        elif not output_file.endswith('.csv'):\n",
        "            print(\"Output file must be a CSV file.\")\n",
        "            output_file = input(\"Enter the name of the output file: \")\n",
        "        else:\n",
        "            return output_file\n",
        "\n",
        "def col_num():\n",
        "    number_of_columns = input(\"number of columns?: \")\n",
        "    while True:\n",
        "        if number_of_columns > 0:\n",
        "            return number_of_columns\n",
        "        else:\n",
        "            print(\"must be a number above 0\")\n",
        "            number_of_columns = input(\"number of columns?: \")\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    input_file_path = input_file()\n",
        "    output_file_path = output_file()\n",
        "    number_of_columns = input(\"number of columns?: \")\n",
        "    main(input_file_path, output_file_path, number_of_columns)\n"
      ]
    }
  ]
}