# Session 2 Notes

## Plan for Today
> 1. Parse context annotations, entities
> 2. Parse public metrics
> 3. Merge Data & Includes
> 4. Convert created_at
> 5. Convert referenced_tweet
> 6. Filter data by condition

## Explore
> Read csv file with ```pd.read_csv```
>    - ```dtype=object```, so the long id number is kept in full
>    - the default ```sep``` is comma
>
> Summarize data with:
>    - ```raw_data.describe()```
>
> Pay attention to the datatypes:
>    - ```raw_data.dtypes```
>    - Ideally, all columns should be object
>
> Glimpse the data with the first five rows
>    - ```raw_data.head()```
>    - It is often useful to check a few rows so we have an idea what the data look like
>
> Further checking out by indexing
>    - ```raw_data.loc[0,"context_annotations"]```
>    - ```raw_data.iloc[0,1]```

## Parse
> **When parsing data, or any data wrangling, keep in mind what the data type is, and which type to convert to.**
> ### Understanding **json** data ###
>     - A common use of JSON is to exchange data to/from a web server.
>     - When receiving data from a web server, the data is always a string.
>     - use ```ast.literal_eval()``` to convert the string first
>     - ideally the converted data type should be **dict**, which can be easily flattened
>     - use ```pd.json_normalize()``` to flatten the
>
> ### Define Function ###
>     - Define function that can parse each of the entries and return the parsed data
>     - The function will process data explained above
>
> ### Vectorize Function ###
>     - Vectorization could simplify the code
>     - Vectorization will take array as the input instead of single entry
>     - use ```np.vectorize()```
>
> ### Apply Function to raw data ###
>
>
