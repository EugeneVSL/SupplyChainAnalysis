import pandas as pd

# define columns of interest
relevant_columns = ['code', 'lc', 'product_name_en', 'quantity', 'serving_size', 'packaging_tags', 'brands', 'brands_tags', 'categories_tags', 'labels_tags', 'countries', 'countries_tags', 'origins', 'origins_tags']

# import the data in a data frame
oliveoil_data = pd.read_csv("data/olive_oil.csv", sep = '\t')

# filter for the columns of interest
oliveoil_data = oliveoil_data[relevant_columns]

#read the categories from the text file
with open("data/relevant_olive_oil_categories.txt", "r") as file:
    relevant_oliveoil_categories = file.read().splitlines()
    file.close()

# since the data in the 'categories_tags' is comma separated we turn it into a list
oliveoil_data['categories_tags'] = oliveoil_data['categories_tags'].str.split(",")

# drop rows with null values in the categories_tags
oliveoil_data = oliveoil_data.dropna(subset='categories_tags')

# filter the data in the DataFrame for column "categories_tags" based on the categories in txt file 
oliveoil_data = oliveoil_data[oliveoil_data['categories_tags'].apply(lambda x: any([i for i in x if i in relevant_oliveoil_categories]))]

# filter again for UK
oliveoil_data = oliveoil_data[(oliveoil_data['countries'] == 'United Kingdom')]

# group and count by origin country 
oliveoil_countries = oliveoil_data['origins'].value_counts()

# select the top country
top_olive_oil_origin = oliveoil_countries.index[0]
# print(top_olive_oil_origin)