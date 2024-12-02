# Project Name: STEAK N STAKE

This application is designed to collect and analyze data from multiple stock files. It provides users with the option to explore the data from some preselected stocks or input their own JSON files to run various statistical operations and study trends in stock prices through generated graphs and console outputs. Users have the option to view the latest data, explore stock prices on a specific day, or examine the stock's information and chart over a specified time period.

### Packages to install:
  - pip install python-docx
  - pip install matploplib
  - pip install humanize

## How does it work?

To run the script normally, enter python ./main.py into your cli <br />
To run the script with a specific JSON data file, run python .\main.py --filePath stock-data\{name_of_your_stock}.json  <br />
To run the script with a specific file and to automatically store the data for the MOST CURRENT DAY run: python .\main.py --filePath stock-data\AAL.json --defaultInput 1 <br />


1. Once main.py is ran the user will be prompted to select one of the 5 included stocks.
2. Once a stock is selected the a second menu will open that will give the user one of the 6 options for statistical analysis.
3. The user will be able to see a statistical output as well as a graph displaying data on the current stock using matplolib.
4. The output will be stored in both a txt file as well as a word document using the python-docx library.


### Group Members:
- Emanuel Rivas
- Jeffrey Mai
- Romeo Ashkar
