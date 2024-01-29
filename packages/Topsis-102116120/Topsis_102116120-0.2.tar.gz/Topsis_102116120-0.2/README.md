Project description
Topsis
Topsis( Technique for order for preference by similarity to Ideal solution ) for MCDM (Multiple criteria decision making) in Python compiled by Priyanshu Singh, 102116120, TIET, Patiala.

Installation
Use the package manager pip to install Topsis pip install topsis_102116120

Usage
Enter Data = 'CSV FILE' , then enter Weights = 'WEIGHTS VECTOR' and the Impacts = 'IMPACTS VECTOR' with comma separated signs (+,-) .

python [Data as .csv] [Weights as a integer vector] [Impacts as a string]

Example of Data
topsis(Data = pd.read_csv('FILE PATH') , Weights = [1,1,1,1] , Impacts = ['+','-','-','+'])

Please Note That"
The first column should be the Items name and all other columns should only contains numeric values before processing. If any non-numeric data is present then please remove it or do some encoding before processing. So the csv MUST follow the format as shown in the Example section. The input data file MUST contain three or more columns. The second to last columns of the data file MUST contain NUMERIC values. The number of weights, impacts and columns (second to last) MUST be SAME. Impacts MUST either be '+' or '-'. Impacts and Weights MUST be separated by , (comma).

Example of CSV

Mobile Price Storage Camera Looks
M1 250 16 12 Excellent
M2 200 16 8 Average
M3 300 32 16 Good
M4 275 32 8 Good
M5 225 16 16 Below Average

    	TO

Mobile Price Storage Camera Looks
M1 250 16 12 5
M2 200 16 8 3
M3 300 32 16 4
M4 275 32 8 4
M5 225 16 16 2
