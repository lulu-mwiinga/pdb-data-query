#!/usr/bin/env python

import pdblib
import sys

#creating a function that lists all the possible functionalities of the script
def functionality_options():
    print("Please select an option:")
    print("1. Download a pdb file")
    print("2. Print selected details")
    print("3. Single letter residue")
    print("4. Fasta Format File ")
    print("5. Print or write relevant lines  ")
    print("6. Print non-standard protein residues ")
    print("7. Plot of temperature factor of a protein ")


# checking if there is no argument given to the script
if len(sys.argv) == 1:
    functionality_options()

    # while loop to ask for continuous user input
    while True:
        option = input("Pick an option (1-7) and q to quit): ")
        # if any of these is the user input then the while loop will break
        quitting = ["quit", "q", "Q"]
        # using break to exit the while loop
        if option in quitting:
            break
      	#using elif statements to have numbers that correspond with the functionalities listen above.
      	#if a value error would occur or a filenot found error would occur, no traceback error would be shown but a helpful message
        elif option == "1":
            try:
                pdblib.get_pdb_text(input("Enter a PDB ID: "))
            except FileNotFoundError:
                print("The file is not found, check if the PDB ID is correct")

        elif option == "2":
            try:
                pdb_id = input("Enter PDB ID: ")
                choice = input('Enter your choice to filter out lines eg "HEADER": ')
                result = pdblib.pdb_part_selection(pdb_id, choice)
                print(result)
            except ValueError:
                print("This is an invalid input. Enter a valid input.")

        elif option == "3":
            try:
                pdb_id = input("Enter PDB ID: ")
                chain_ID = input("Enter a chain ID: ")
                result = pdblib.protein_residues(pdb_id, chain_ID)
                print(result)
            except ValueError:
                print("This is an invalid input. Enter a valid input.")

        elif option == "4":
            try:
                pdb_id = input("Enter PDB ID: ")
                output_file = input("Enter an output file name: ")
                chain_ID = input("Enter a chain ID: ")
                result = pdblib.create_fasta(pdb_id, output_file, chain_ID)
                print(result)
            except ValueError:
                print("This is an invalid input. Enter a valid input.")

        elif option == "5":
            try:
                pdb_id = input("Enter PDB ID: ")
                chain_ID = input("Enter a chain ID: ")
                output_option = input("Select an output option(print/write): ")
                record_type = input("filtering text with ATOM/HETATM: ")
                result = pdblib.print_or_write(pdb_id, chain_ID, output_option, record_type)
                print(result)
            except ValueError:
                print("Invalid input. Please try again.")

        elif option == "6":
            try:
                pdb_id = input("Enter PDB ID: ")
                chain_ID = input("Enter a chain ID: ")
                result = pdblib.unusual_protein(pdb_id, chain_ID)
                print(result)
            except ValueError:
                print("Invalid input. Please try again.")

        elif option == "7":
            try:
                pdb_id = input("Enter PDB ID: ")
                chain_ID = input("Enter a chain ID: ")
                dimension1 = int(input("Enter the dimension of the length of your plots eg 21: "))
                dimension2 = int(input("Enter your width for the plot second: "))
                file_name = input("Enter a file name, in which the plot will be saved: ")
                pdblib.make_plot(pdb_id, chain_ID, (dimension1,dimension2), file_name)

            except ValueError:
                print("Invalid input. Please try again")

