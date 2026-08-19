import pandas as pd
import matplotlib.pyplot  as plt

dataset=pd.read_csv('C:\\Users\\Ayush\\OneDrive\\Desktop\\python\\project\\netflix_dataset_data_analysis.csv')
dataset.dropna(inplace=True) # handling  missing data

#Q1 bar graph of tv show vs movie
type_counts=dataset['type'].value_counts()

plt.figure(figsize=(6,8))
plt.bar(type_counts.index,type_counts.values,color=['blue','orange'])

plt.title('Numer of Tv shows vs Movies')
plt.ylabel('Counts')
plt.xlabel('Type')
plt.savefig('q1.png',dpi=300,bbox_inches='tight')



#Q2 ratings chart
rating_count=dataset['rating'].value_counts()
plt.figure(figsize=(8,10))
plt.pie(rating_count.values,labels=rating_count.index,autopct='%1.1f%%',colors=['red','yellow','orange','grey','pink','coral','purple'])
plt.legend()
plt.title('Rating chart')
plt.savefig('q2.png',dpi=300,bbox_inches='tight')

#Q3 no of releases changed over the year
year_count=dataset['release_year'].value_counts()
year_count=year_count.sort_index(ascending=True)
plt.figure(figsize=(8,9))
plt.plot(year_count.index,year_count.values)
plt.grid()
plt.xlabel('Year')
plt.ylabel('Number of releases')
plt.title('Number of releases every year')
plt.savefig('q3.png',dpi=300,bbox_inches='tight')


#Q4 distribution of duration histogram
plt.figure(figsize=(8,9))
duration_count=dataset['duration']
plt.hist(duration_count,bins=20,edgecolor='black')
plt.title('Distribution of duration')
plt.xlabel('Duration')
plt.ylabel('Counts')
plt.savefig('q4.png',dpi=300,bbox_inches='tight')


#Q5 relationship between release year and number of shows
release_count=dataset['release_year'].value_counts()
release_count=year_count.sort_index(ascending=True)
plt.figure(figsize=(8,9))
plt.scatter(release_count.index,release_count.values)
plt.grid()
plt.xlabel('Year')
plt.ylabel('Number of releases')
plt.title('Number of releases every year')
plt.savefig('q5.png',dpi=300,bbox_inches='tight')


#q6 top 5 countries with the highest number of  shows
country_count=dataset['country'].value_counts()
country_count=country_count.sort_values(ascending=False)
country_count=country_count.head(5)
plt.figure(figsize=(8,9))
plt.title('Top 5 countries with the highest number of shows')
plt.barh(country_count.index,country_count.values,color='orange')
plt.ylabel('Country')
plt.xlabel('Number of shows')
plt.savefig('q6.png',dpi=300,bbox_inches='tight')


#q7 compare tv shows and movies with years

tvshow=dataset[dataset['type']=='TV Show']['release_year'].value_counts().sort_index()
movies=dataset[dataset['type']=='Movie']['release_year'].value_counts().sort_index()


plt.figure(figsize=(8,9))
plt.plot(tvshow.index,tvshow.values,color='red',label='TV Shows')
plt.plot(movies.index,movies.values,color='orange',label='Movies')
plt.title('Comparision of TV Show vs Movies over years')
plt.xlabel('Year')
plt.ylabel('Number of Shows released')
plt.legend()
plt.savefig('q7.png',dpi=300,bbox_inches='tight')



