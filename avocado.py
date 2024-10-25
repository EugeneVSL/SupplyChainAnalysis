import pandas as pd

# define columns of interest
relevant_columns = ['code', 'lc', 'product_name_en', 'quantity', 'serving_size', 'packaging_tags', 'brands', 'brands_tags', 'categories_tags', 'labels_tags', 'countries', 'countries_tags', 'origins', 'origins_tags']

# import the data in a data frame
avocado_data = pd.read_csv("data/avocado.csv", sep = '\t')

# filter for the columns of interest
avocado_data = avocado_data[relevant_columns]

#read the categories from the text file
with open("data/relevant_avocado_categories.txt", "r") as file:
    relevant_avocado_categories = file.read().splitlines()
    file.close()

# since the data in the 'categories_tags' is comma separated we turn it into a list
avocado_data['categories_tags'] = avocado_data['categories_tags'].str.split(",")

# drop rows with null values in the categories_tags
avocado_data = avocado_data.dropna(subset='categories_tags')

# filter the data in the DataFrame for column "categories_tags" based on the categories in txt file 
avocado_data = avocado_data[avocado_data['categories_tags'].apply(lambda x: any([i for i in x if i in relevant_avocado_categories]))]

# filter again for UK
avocado_country_origin = avocado_data[(avocado_data['countries'] == 'United Kingdom')]

# group and count by origin country 
countries_list = avocado_country_origin['origins'].value_counts()

# select the top country
top_avocado_origin = countries_list.index[0]
# print(countries_list.index[0])