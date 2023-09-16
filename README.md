Users of this module and script can execute a variety of operations on PDB files using various tools.
The choices are as follows: 

   1. Download a PDB file:
   This just downloads the file if it is not available yet 
   2. Print selected details:
   printing only lines that start with; HEADER, TITLE,SOURCE,KEYWDS,AUTHOR,JRNL TITL. Depending on your choice
   
   3. printing single-letter residues:
   prints single letter residues as a string wen give a pdb file and a chain id
 
   4. Creates a FASTA format file
   5. Print or write relevant lines:
   it can either print or write lines that start with ATOM,HETATM
   6. Print non-standard protein residues
   7. Plot the temperature factor of a protein:
   creates a plot of the temperature factor of residues when given the chain id
   

This is how to create a conda environment:

open the terminal and type:

– conda env list
This will show all the conda environments present
	
– conda create --name py38 python=3.8 requests
This will create a new conda environment called py38 with a python version of 3.8 and has the requests module installed

– conda activate py38
Then activating the new conda environment that was just created
	

Then, enter the following commands to execute the script:

 - chmod +x checkPDB.py
 -./checkPDB.py
 
Type "Q","q" or "quit" to exit the script.  
