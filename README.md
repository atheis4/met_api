# PyMet (WIP)
A Python API for consuming the Metropolitan Museum of Art's publicly available dataset.

## Introduction
Finding sources for working with images of paintings is very difficult. The quality of Google image search results are highly variable.

### The Met
Thankfully, the Metropolitan Museum of Art in New York City has graciously made their works avaiable for download and free use via their [openaccess](https://github.com/metmuseum/openaccess) repo.

Unfortunately, they only provide a massive CSV (256 MB) without any instructions on how to download or use the collection.

### How to download
Because of the size of the data file, you'll need to use [git's Large File Storage](https://git-lfs.github.com/) extension to properly download the full collection.

### Update the CsvPaths constants
Once you have the dataset on your local machine, you'll need to update the file paths located in the [constants module](https://github.com/atheis4/pymet/blob/master/pymet/utils/constants.py#L56-L59).

MetObjects.csv represents the full collection.
MetPaintings.csv represent only those rows where `Object Name == 'Painting'`.

## The Collection
The full collection contains almost 500,000 rows of unique works. The data is not clean or uniform. Be wary of encoding issues if using Python 2. Columns were named to be human readable and are not easily accessed by data science libraries (pandas).

A list of all the columns (after transformation) in the dataset can be found [here](https://github.com/atheis4/pymet/blob/master/pymet/utils/constants.py#L4-L47).

### MetPaintings
`MetPaintings` is an object intended to make all the paintings in the collection more accessible for study. For this reason I have limited the columns that are contained in this dataset. This represents 6100 individual works in 750 mediums.

This is the primary object I will be developing and working with.
