# Define a function, called get_movies_from_tastedive. It should take one input parameter, a string that is the name of a movie or music artist. The function should return the 5 TasteDive results that are associated with that string; be sure to only get movies, not other kinds of media. It will be a python dictionary with just one key, ‘Similar’.

# Try invoking your function with the input “Black Panther”.
1. 

import json
import requests_with_caching

def get_movies_from_tastedive(para):
    base='https://tastedive.com/api/similar'
    d={}
    d['q']=para
    d['limit']=5
    d['type']='movies'
    res=requests_with_caching.get(base,d,permanent_cache_file="permanent_cache.txt")
    js = res.json()
    print(res.url)
    print (js)
    return js
  
  
  2.

def extract_movie_titles(para):
    print(type(para))
    titles = []
    for x in para['Similar']['Results']:
        titles.append(x['Name'])
    print(titles)
    return titles    
            
para = get_movies_from_tastedive('Black Panther')

3.
         
def get_related_titles(l):
    one=[]
    for x in l:
        c=get_movies_from_tastedive(x)
        cc=extract_movie_titles(c)
        for b in cc:
            one.append(b)
    return list(set(one))

para = get_movies_from_tastedive('Black Panther')
l=extract_movie_titles(para)

4. 


import json
import requests_with_caching

def get_movie_data(o):
    d={}
    d['t']=o
    d['r']='json'
    base='http://www.omdbapi.com/'
    x=requests_with_caching.get(base,d,permanent_cache_file='permanent_cache.txt')
    c=x.json()
    print(c)
    return c
a=get_movie_data('Venom')

5.
import json
import requests_with_caching

def get_movie_data(o):
    d={}
    d['t']=o
    d['r']='json'
    base='http://www.omdbapi.com/'
    x=requests_with_caching.get(base,d,permanent_cache_file='permanent_cache.txt')
    c=x.json()
    return c
def get_movie_rating(r):
    rate=r['Ratings']
    for x in rate:
        if x['Source']=='Rotten Tomatoes':
            a=(x['Value'])
            return int(a[:2])
    else:
        return 0
      
