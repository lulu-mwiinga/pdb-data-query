#!/usr/bin/env python

import requests
import os 

#creating a function that downloads a PDB file if its not available on your machine and if it is it will tell you 
def get_pdb_text(pdb_id):
   
  
    filename = f"{pdb_id}.pdb"
    
    #checking if the file is available locally 
    if os.path.isfile(filename):
        print("The PDB file is available locally.")
        
        # reading contents of the file
        with open(filename, 'r') as fobject:
            read_it = fobject.read()
        
        # remove newlines using split()
        content = ''.join(read_it)
        contents = content.split('\n')
        
        return contents
        
    #if its not available locally then it downloads the file     
    else:
        response = requests.get(f'https://files.rcsb.org/download/{pdb_id}.pdb')
        
        #creating a file and saving the downloaded file to it 
        with open(filename, 'w') as f:
            f.write(response.text)
        
        print("Your file is being downloaded")
        
        # remove newlines using split() and join()
        content = ''.join(response.text)
        contents = content.split('\n')
        
        return contents


def pdb_part_selection(pdb_id, choice):
    # get the contents of the PDB file. choice represents (HEADER,TITLE,SOURCE,KEYWDS,AUTHOR,JRNL TITLE)
	
	#geting the contents of the file
    pdb_text = get_pdb_text(pdb_id)    

    # create an empty string
    separate = ""
    
    
    # iterate through the lines of the PDB file,the pdb file is a list of strings
    for line in pdb_text:
    
        # if the line starts with the the user input(choice)
        if line.startswith(choice):
            #removing newline characters
            clean = line.strip()

            #iterating through the lines based on the choice given and has newline characters after 80 characters
            for i in range(0, len(clean), 80):
                separate += clean[i:i+80] + "\n"
        
    return separate
    
#gets the protein residues in a single string when given the pdb file and the chain id
def protein_residues(pdb_id, chain_ID):
	
    pdb_text = get_pdb_text(pdb_id)
    
    #creating an empty list to put the information obtained from below
    atom_list = []
    # a for loop to iterate through the the lines in the pdb files
    for line in pdb_text:
        #if the lines start with atom and the characters at index 13:15 is CA
        if line.startswith("ATOM") and line[13:15] == "CA" and line[21] == (f"{chain_ID}"):
            #it will then add to the list
            atom_list.append(line)
    #print(atom_list)

    
    #creating a dictionary that will be used to get the three letter residues present in the text and using them as keys
    dictionary = {"ALA":"A",          
    "ASX":"B",            
    "CYS":"C",            
    "ASP":"D",            
    "GLU":"E",            
    "PHE":"F",          
    "GLY":"G",            
    "HIS":"H",            
    "ILE":"I",            
    "LYS":"K",            
    "LEU":"L",            
    "MET":"M",            
    "ASN":"N",            
    "PRO":"P",            
    "GLN":"Q",            
    "ARG":"R",            
    "SER":"S",            
    "THR":"T",            
    "SEC":"U",            
    "VAL":"V",            
    "TRP":"W",            
    "XAA":"X",            
    "TYR":"Y",            
    "GLX":"Z"}  
    
    #creating an empty list to store the information below
    residue_list = []
    
    #iterating through the list atom_ca that only has the lines with atom and and ca 
    for line in atom_list:
        #getting the three letter residue found at index 17:20 and assigning it to the variable residue(these are the keys) 
        residue = line[17:20]
        #appending it to the empty list value with the keys from the dictionary
        residue_list.append(dictionary[residue])
        
    #taking the one letter residues that are in a list and joining them and making a string
    string_residue = ''.join(residue_list)
    
    #printing the information in fasta format
    return string_residue
    
#a function that creates a fasta formatted file 
def create_fasta(pdb_id, output_file, chain_ID=None):

    #creating a header with the part selecttion function
    header = pdb_part_selection(pdb_id, "HEADER")
    
    #getting the residues with the protein residues function 
    pro_res = protein_residues(pdb_id, chain_ID)
    
    #creating a file name and writting them in fasta format
    with open(output_file, "w") as fobject:
        if chain_ID is None:
            fobject.write(f">{header}\n{pro_res}\n")
        else:
            fobject.write(f">{header} chain_ID: {chain_ID}\n{pro_res}\n")
    print(f"Your fasta formatted content is in {output_file}")

#A function that allows you to print of or write relevant lines in a file
def print_or_write(pdb_id, chain_ID, output_option, record_type=None):
    
    pdb_text = get_pdb_text(pdb_id)
    #if atom or hetatm is  specified 
    if record_type is not None:
        #the file is used to append because of the forloop below so that it adds to it everytime
        with open("output.txt", "a") as file:
            for line in pdb_text:
                if line.startswith(record_type) and line[13:15] == "CA" and line[21] == (f"{chain_ID}"):
                    #checking if the user picked read or write 
                    if output_option == "print":
                        print(line)
                    elif output_option == "write":
                        file.write(line)
    #if record type is none
    elif record_type is None:
        
        with open("output.txt", "a") as file:
        #only filter out the lines with Ca and the chain label regarless of atom or hetatm 
            for line in pdb_text:
                if line[13:15] == "CA" and line[21] == (f"{chain_ID}"):
                    #printing or writting based on the user 
                    if output_option == "print":
                        print(line)
                    elif output_option == "write":
                        file.write(line)
                        
#A function that checks if there are none standard residues                       
def unusual_protein(pdb_id, chain_ID):
    
    pdb_text = get_pdb_text(pdb_id)
    
    dictionary = {"ALA":"A",
                  "ASX":"B",
                  "CYS":"C",
                  "ASP":"D",
                  "GLU":"E",
                  "PHE":"F",
                  "GLY":"G",
                  "HIS":"H",
                  "ILE":"I",
                  "LYS":"K",
                  "LEU":"L",
                  "MET":"M",
                  "ASN":"N",
                  "PRO":"P",
                  "GLN":"Q",
                  "ARG":"R",
                  "SER":"S",
                  "THR":"T",
                  "SEC":"U",
                  "VAL":"V",
                  "TRP":"W",
                  "XAA":"X",
                  "TYR":"Y",
                  "GLX":"Z"}
	#adding residues to lists to make them iterable
    residues = []
    not_standard = []
    for line in pdb_text:
        if line.startswith("ATOM") and line[13:15] == "CA" and line[21] == chain_ID:
            residue = line[17:20]
            residues.append(residue)
    #checking if the residue is not in the standar residue dictionary          
    for residue in residues:     
        if residue not in dictionary:
            not_standard.append(residue)
    #if non standard residues are found then they are printed out       
    if len(not_standard) > 0:
        print(f"The Non-standard residues are {not_standard}")
    else:
        print("All residues present are standard")
        
#A function that makes a plot for the temperature factor given a chain id        
def make_plot(pdb_id, chain_ID, dimensions,file_name):
    
    #creating lists for x and y values 
    temp_factor = []
    atom_serial_no = []
    
    #getting the text 
    pdb_text = get_pdb_text(pdb_id)
    

    # a for loop to iterate through the the lines in the pdb files
    for line in pdb_text:
        #if the lines start with atom and the characters at index 13:15 is CA
        if line.startswith("ATOM") and line[13:15] == "CA" and line[21] == (chain_ID):
            #the temperature factor which will be the y value of the plot
            temp_factor.append(float(line[60:66]))
            #the atom serial number will be the x value 
            atom_serial_no.append(int(line[6:11]))

    #creating  x and y values for the plot        
    xvalues = atom_serial_no
    yvalues = temp_factor


    #importing the matplotlib so i can plot graphs 
    from matplotlib import pyplot as plt
    
    fig = plt.figure(figsize = (dimensions))
    #plotting the graph 
    plt.plot(xvalues,yvalues, color = "red")
    plt.title(f"Temperature factor of {chain_ID} residues")
    plt.xlabel("residue number")
    plt.ylabel("Temperature factor")
    #saving the graph to the file 
    plt.savefig(file_name)
    
   
    

