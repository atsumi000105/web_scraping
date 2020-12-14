# Project
> Scraping a Real Estate Website

### Mission
The real estate company "ImmoEliza" wants to create a machine learning model to make price predictions on real estate sales in Belgium. We must therefore create a dataset that holds the following columns :

- Locality
- Type of property (House/apartment)
- Subtype of property (Bungalow, Chalet, Mansion, ...)
- Price
- Type of sale (Exclusion of life sales)
- Number of rooms
- Area
- Fully equipped kitchen (Yes/No)
- Furnished (Yes/No)
- Open fire (Yes/No)
- Terrace (Yes/No) 
    - If yes: Area
- Garden (Yes/No)
   - If yes: Area
- Surface of the land
- Surface area of the plot of land
- Number of facades
- Swimming pool (Yes/No)
- State of the building (New, to be renovated, ...)

**Collaboration tool used**: GitHub

**Environment**: Linux

**Editors** : Visual Code, Jupyter Notebook

**Programming Language**: Python

**Collaborators**: [Orhan Nurkan](https://github.com/orhannurkan) , [Christophe Schellinck](https://github.com/christopheschellinck) and [Davy Nimbona](https://github.com/davymariko)

### Installation
- Clone the repo
- To have the environment requirements, run:
```
pip install -r requirements.txt
```
### Execution
Execute the application by running:
```
scrap.py
```
### Steps
- The first step is to iterate through the 334 search pages and get every link to unique property description and save the links in the file `links_list.txt`
- We used the selenium package and we retrieved every link through X-Paths
- The source code can be found in `scrap.py`
- The second step was to get every link from the links list file and retrieve every data from every page and save the information in a database (davy.db, find it in Database folder)

### Work Repartition
- Christophe working on Building a dataframe
- Orhan is working on accessing all the records through the right X-Path
- Davy working getting all the page records and filter all the links (in order to get the right ones)
- Davy working on saving scrapped data in SQLite database
- Iterate through all the search pages
- Use the X-Path for next button (Stop the loop if not present)
