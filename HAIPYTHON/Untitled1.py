#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello")


# In[6]:


#Part1
import pandas as pd
# Câu 1:
movies = pd.read_csv('./movies_data/movies.csv', sep=',')
movies.head(10)


# print(type(movies))
# print(movies.shape)

# In[7]:


print(type(movies))
print(movies.shape)


# In[13]:


# Câu 2:
tags = pd.read_csv('./movies_data/tags.csv', sep=',')
(type(tags))
(tags.shape)
(tags.head())


# In[12]:


# Câu 3:
ratings = pd.read_csv('./movies_data/ratings.csv', sep=',', parse_dates=['timestamp'])
(type(ratings))
(ratings.shape)
(ratings.head())


# In[14]:


#Part 2: Data Structures
# Câu 1:
row_0 = tags.iloc[0]
type(row_0)


# In[16]:


print(row_0)


# In[19]:


# Câu 2:
print(row_0.index)


# In[20]:


# Câu 3:
print(row_0['userId'])


# In[21]:


# Câu 4:
print('rating' in row_0)


# In[22]:


# Câu 5:
print(row_0.name)


# In[23]:


# Câu 6:
row_0 = row_0.rename('first_row')
print(row_0.name)


# In[25]:


#Part 3: DataFrames
# Câu 1:
(tags.head())


# In[26]:


print(tags.index)


# In[27]:


# Câu 2:
print(tags.columns)


# In[29]:


# Câu 3:
tags_sub = tags.iloc[[0, 10, 100, 1000]]
(tags_sub)


# In[31]:


#Part 4: Thống kê dữ liệu
# Câu 1:
(ratings.describe())


# In[33]:


# Câu 2:
print(ratings['rating'].describe())


# In[34]:


# Câu 3:
print(ratings['rating'].mean())


# In[36]:


(ratings.mean())


# In[37]:


print(ratings['rating'].min())


# In[38]:


print(ratings['rating'].max())


# In[39]:


print(ratings['rating'].std())


# In[40]:


print(ratings['rating'].mode())


# In[41]:


(ratings.corr())


# In[44]:


# Câu 4:
filter_1 = ratings['rating'] > 5
print(filter_1.head())
print(filter_1.tail())
print(filter_1.any())


# In[45]:


# Câu 5:
filter_2 = ratings['rating'] > 0
print(filter_2.all())


# In[46]:


#Part 5: Làm sạch dữ liệu: Xử lý dữ liệu bị thiếu
movies.shape


# In[47]:


#is any row NULL ?
movies.isnull().any()


# In[48]:


ratings.shape


# In[49]:


#is any row NULL ?
ratings.isnull().any()


# In[50]:


tags.shape


# In[51]:


#is any row NULL ?
tags.isnull().any()


# In[52]:


tags = tags.dropna()


# In[53]:


#Check again: is any row NULL ?
tags.isnull().any()


# In[54]:


tags.shape


# In[59]:


#Part 6: Trực quan hóa dữ liệu
# Câu 1
ratings['rating'].plot.hist()


# In[60]:


# Câu 2
ratings['rating'].plot.box()


# In[63]:


# Câu 3:
print(ratings['rating'].describe())


# In[64]:


#Part 7: Lấy dữ liệu trên cột
# Câu 1:
tag = tags['tag'].head()
print(type(tag))
print(tag)


# In[65]:


# Câu 2:
title_genres = movies[['title','genres']].head()
print(type(title_genres))
print(title_genres)


# In[67]:


# Câu 3:
print('Số dòng của ratings:', ratings.shape[0])
ratings_10_end = ratings[-10:]
(ratings_10_end)


# In[68]:


# Câu 4:
print(tags['tag'].head())
tag_counts = tags['tag'].value_counts()
print(type(tag_counts))
print(tag_counts.shape)
tag_counts_end = tag_counts[-10:]
print(tag_counts_end)


# In[69]:


# Câu 5:
tag_counts_end.plot.bar()


# In[71]:


#Part 8: Lọc dữ liệu trên dòng
# Câu 1:
is_highly_rated = ratings['rating'] >= 4
(is_highly_rated.head())
(ratings[is_highly_rated][30:50])


# In[73]:


# Câu 2:
is_animation = movies['genres'].str.contains('Animation')
(is_animation.head())
(movies[is_animation][5:15])


# In[74]:


# Câu 5:
movies[is_animation].head(15)


# In[76]:


#Part 9: Nhóm dữ liệu và tổng hợp
# Câu 1:
ratings_count = ratings[['movieId','rating']].groupby('rating').count()
(ratings_count)


# In[77]:


# Câu 2
average_rating = ratings[['movieId','rating']].groupby('movieId').mean()
print(average_rating.shape)
average_rating.head()


# In[78]:


# Câu 3
movie_count = ratings[['movieId','rating']].groupby('movieId').count()
movie_count.head()


# In[79]:


movie_count.tail()


# In[80]:


#Part 10: Gộp DataFrame
tags.head()


# In[81]:


movies.head()


# In[82]:


t = movies.merge(tags, on='movieId', how='inner')
t.head()


# In[83]:


t.tail()


# In[84]:


#Part 11: Kết hợp giữa nhóm, gộp, lọc dữ liệu
# Câu 1
avg_ratings = ratings.groupby('movieId', as_index=False).mean()
del avg_ratings['userId']
avg_ratings.head()


# In[85]:


# Câu 2
box_office = movies.merge(avg_ratings, on='movieId', how='inner')
box_office.tail()


# In[87]:


# Câu 3:
is_highly_rated = box_office['rating'] >= 4.0
(is_highly_rated[-5:])
box_office[is_highly_rated][-5:]


# In[88]:


# Câu 4:
is_comedy = box_office['genres'].str.contains('Comedy')
box_office[is_comedy][:5]


# In[89]:


# Câu 5:
box_office[is_comedy & is_highly_rated][-5:]


# In[90]:


#Part 12: Thao tác trên dữ liệu chuỗi
# Câu 1
movies.head()


# In[93]:


# Câu 2: Cắt 'genres' thành nhiều cột với split('|')
movie_genres = movies['genres'].str.split('|', expand=True)


# In[94]:


movie_genres[:10]


# In[95]:


# Câu 4: Thêm cột
movie_genres['isComedy'] = movies['genres'].str.contains('Comedy')


# In[96]:


movie_genres[:10]


# In[97]:


# Câu 4:
movies['year'] = movies['title'].str.extract('.*\((.*)\).*', expand=True)


# In[98]:


movies.head()


# In[99]:


movies.tail()


# In[100]:


#Part 13: Parsing Timestamps
tags = pd.read_csv('./movies_data/tags.csv', sep=',')


# In[101]:


# Câu 1:
tags.dtypes


# In[102]:


tags.head()


# In[104]:


# Câu 2
tags['parsed_time'] = pd.to_datetime(tags['timestamp'], unit='s')


# In[105]:


tags['parsed_time'].dtype


# In[106]:


tags.head()


# In[107]:


# Câu 3
greater_than_t = tags['parsed_time'] > '2015-02-01'
selected_rows = tags[greater_than_t]
print(tags.shape)
print(selected_rows.shape)


# In[108]:


# Câu 4: Sắp xếp dữ liệu tags tăng dần theo cột parsed_time. In 10 dòng dữ liệu đầu tiên củ
tags.sort_values(by='parsed_time', ascending=True)[:10]


# In[109]:


#Part 14: Tính trung bình của Movie Ratings theo thời gian
# Câu 1:
average_rating = ratings[['movieId','rating']].groupby('movieId', as_index=False).mean()
average_rating.tail()


# In[110]:


# Câu 2
joined = movies.merge(average_rating, on='movieId', how='inner')
joined.head()


# In[111]:


joined.corr()


# In[112]:


# Câu 3:
yearly_average = joined[['year','rating']].groupby('year', as_index=False).mean()
print(yearly_average.shape)
yearly_average[:10]


# In[113]:


# Câu 4:
yearly_average_asc = yearly_average.sort_values(by ='year', ascending=True)
yearly_average_asc[-20:]


# In[114]:


# yearly_average_asc[-20:].plot(x='year', y='rating', figsize=(15,10), grid=True)
yearly_average_asc[-20:].plot(x='year', y='rating')


# In[ ]:




