# extracts data from a file
# file is filled with data from pdf
# returns a list of strings
# and uses xlsxwriter to write the data to an excel file
import data_class
# import regex
import re
import xlsx_writer

def prework_file(filename):
    # open file
    # opens a file to read and write
    file = open(filename, "r")
    # read file
    text = file.read()
    file.close() 

    #if line starts with "Geschäftsführer:", then remove the line
    text = re.sub(r'Gesch.*\n', '', text)
    # if line starts with "UST", then remove the line
    text = re.sub(r'UST.*\n', '', text)
    # if line starts with "Handelsregister", then remove the line
    text = re.sub(r'Handelsregister.*\n', '', text)
    # removes tripple newline to double newline
    text = re.sub(r'\n\s*\n\s*\n', '\n\n', text)
    file = open(filename, "w")
    file.write(text)
    file.close()
    # print text
    # print(text)


def create_excel_line():
    prework_file("text_from_image.txt")
    # get the file text_from_image.txt
    file = open("text_from_image.txt", "r", encoding="utf-8")
    # create a new object of the class data_class 
    data = data_class.excel_line()
    # fill the object with data from the text file
    besteller_line = -1
    product_data_line = -1
    for cnt, line in enumerate(file):
        # if the line starts with "Bestell-Nr.:"
        # the number between "Bestell-Nr.:" and "Versand:" is the data_class.bestellnummer
        if re.match(r'^Bestell-Nr.:\s', line):
            bestellnummer_plus = re.findall(r'\d+', line)
            # takes only the first number of the list and stores it in data_class.bestellnummer
            data.bestellnummer = bestellnummer_plus[0]
        # if the line starts with "Lieferschein"
        # the next numbers are the data_class.lieferschein
        if re.match(r'^Lieferschein\s', line):
            lieferschein_plus = re.findall(r'\d+', line)
            # takes only the first number of the list and stores it in data_class.lieferschein
            data.lieferschein = lieferschein_plus[0]
        
        # if line starts with "Grohe AG"
        # remember this line and store its number in tmp_line
        # if linenumber is tmp_line + 3 
        # then this line is the data_class.besteller
        if re.match(r'^Grohe AG', line):
            besteller_line = cnt
        # if tmp_line is not -1 and linenumber is tmp_line + 3
        # then this line is the data_class.besteller
        if besteller_line != -1 and cnt == besteller_line + 3 and data.besteller == -1:
            # if line ends with newline, then remove the newline
            if line[-1] == "\n":
                line = line[:-1]
            data.besteller = line
        # if line starts with "Pos. Menge Einheit Artikelnummer nachliefern:"
        # then the following text elements contains the product data
        # if the line starts with 001, 002, 003, ...
        # then the next number after 001, 002, 003, ... is the article quantity 
        # if the number is shorter then 3 digits
        if re.match(r'^\d{3}\s', line):
            product_data_line = cnt
            # line = line minus first 3 digits
            line = line[4:]
            # if first number is one or thwo digits long
            # then the next number is the article quantity
            if re.match(r'^\d{1,2}\s', line):
                data.product.menge = re.findall(r'\d+', line)[0]
            else:
                # take the last number of the line
                data.product.menge = re.findall(r'\d+', line)[-1]
            
        # if product_data_line is not -1 and linenumber is product_data_line + 1
        # then this line contains the product quantity
        if product_data_line != -1 and cnt == product_data_line + 1 and data.product.menge == -1:
            menge_plus = re.findall(r'\d+', line)
            # takes only the first number of the list and stores it in data_class.menge
            data.product.menge = menge_plus[-1]
        # and product_data_line + 3 is the product model
        if product_data_line != -1 and cnt == product_data_line + 2 and data.product.model == -1:
            # if line ends with newline, then remove the newline
            if line[-1] == "\n":
                line = line[:-1]
            data.product.model = line
            # append the product data to the list of products
            data.product_list.append(data.product)
            # clear the product data
            data.product = data_class.product_data()
            product_data_line = -1
    # close the file
    file.close()
    # prints all data from data_class.py
    print("Besteller:\t", data.besteller)
    print("Bestellnummer:\t", data.bestellnummer)
    print("Lieferschein:\t", data.lieferschein)
    # foreach product in the list of products
    # print model and menge
    for product_pos, product in enumerate(data.product_list):
        print("Position:\t", product_pos + 1)
        print("\tModel:\t", product.model)
        print("\tMenge:\t", product.menge)
    # prints the data from the text file
    print()

    # crete a list with Besteller, Bestellnummer, Lieferschein, Position, Model, Menge
    # and for each prduct in list create a new list 
    # with the previous besteller, bestellnummer, lieferschein but with the new model and menge
    # and append the new list to the list of products
    # and print the list of products
    collection_of_lines = []
    excel_line_list = []
    for product in data.product_list:
        excel_line_list.append(data.besteller)
        excel_line_list.append(data.bestellnummer)
        excel_line_list.append(data.lieferschein)
        excel_line_list.append(product.menge)
        excel_line_list.append(product.model)
        collection_of_lines.append(excel_line_list)
        excel_line_list = []

    return collection_of_lines


# test the function
this = create_excel_line()
for object_data in this:
    xlsx_writer.write_to_excel(object_data)


