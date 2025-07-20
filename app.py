import streamlit as st
import pickle
import requests
def fetch_poster(movie_id):
    #api_key="a9b83a138b613ea38644efb2dd544d0b"
    url="https://api.themoviedb.org/3/movie/{movie_id}?api_key={40d3fbb753bc4bb9ae7928dfe505b4f6}&language=en-US".format(movies)
    data=requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    full_path="a9b83a138b613ea38644efb2dd544d0b"+poster_path
    return full_path
movies=pickle.load(open("movies_list.pkl","rb"))
similarity=pickle.load(open("similarity.pkl","rb"))
movies_list=movies['title'].values
st.header("Movie Recommander System")
#create a dropdown to select the movie
selected_movie=st.selectbox("Select a movie",movies_list)
import streamlit.components.v1 as components
def recommand(movie):
    index=movies[movies['title']==movie].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda vector: vector[1])
    recommand_movie=[]
    recommand_poster=[]
    for i in distance[1:6]:
        movies_id=movies.iloc[i[0]].id

        recommand_movie.append(movies.iloc[i[0]].title)
        recommand_poster.append(fetch_poster(movie_id))
    return  recommand_movie, recommand_poster
if  st.button("Recommand"):
    movie_name,movie_poster=recommand(selected_movie)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])