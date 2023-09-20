## Write your code here
from re import M
## Write your code here

def print_every_movie_title():
    movie_list = []
    for i in range(0, len(movies)):
      movie = (list(movies)[i]["title"])
      movie_list.append(movie)

    return movie_list
    
def get_movie_description_length(movie_index):
  desc = (list(movie_index["description"]))
  desc_len = len(desc)
  return desc_len

def get_avg_movie_description_length():
  avg_len = 0
  for i in range(0, len(movies)):
    desc_len = len(list(movies[i]["description"]))
    avg_len = avg_len + desc_len

  avg_len = avg_len/len(movies)
  return avg_len

def get_max_movie_name_length():
  name_len_dict = {}
  for i in range(0, len(movies)):
    name_length = len(movies[i]["title"])
    movie_name = (movies[i]["title"])
    
       
    name_len_dict.update({movie_name:name_length})
    max_name = max(name_len_dict, key=name_len_dict.get)
    
  

  max_name_len = name_len_dict[max_name]

  

  return max_name_len, max_name

movie_names = print_every_movie_title()
movie_desc = get_movie_description_length(movies[1])
desc_avg_len = get_avg_movie_description_length()
get_max_movie_name_length()
