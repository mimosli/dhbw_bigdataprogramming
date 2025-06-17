# Python Course Exercise: Open Beer Database

## 1. Prepare the data

1. download the openbeer database from https://openbeerdb.com/, "openbeerdb_csv.zip". (You may assemble the link before. But the idea is that after publishing a notebook/code it works as a standalone solution and no further interactions are needed from the user)
1. unzip the csv in Python

## 2. Read the data into a class that allows data processing

1. Which package is well suited and why?
1. Read the data into this package
1. Create a "Qualitative Summary" of the data.
1. Access the column "brewery_id" from beers dataframe
1. Access first row of beers and its corresponding brewery row
1. Join beers data with brewery data and print result of first beer row from 5.

## 3. Reading the data into a local database

1. Which database is well suited and why?
1. Read the data into this database

## 4. Questions related to the data (use database from 3. to answer)

1. What is the average alcohol content of the beers produced by country of production?
1. How many breweries are there per country/city?
1. How many beer styles does a brewery brew on average? How many are there per country?
1. What is the median of the alcohol content?
1. Which beer style is mainly found in which country?

## 4. Visualization of the data

1. Use map to visualize brewery locations on a world map
1. Use a heatmap to display number of beers per country and per alcohol content (to simplify: only use whole numbers of alcohol)

Hint for libraries:

- Map: https://basemaptutorial.readthedocs.io/en/latest/plotting_data.html, https://anaconda.org/conda-forge/basemap
- Heatmap: https://cmdlinetips.com/2019/01/how-to-make-heatmap-with-seaborn-in-python/
