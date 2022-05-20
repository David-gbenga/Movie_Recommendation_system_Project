"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Introduction","Solution Overview", "About Company", "Explorative Data Analysis"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except Exception as e:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")
                    print(e, traceback.format_exc())


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection ==  "Introduction":
        st.title("Introduction")
        st.write("In today’s technology driven world, recommender systems are socially and economically critical to \
            ensure that individuals can make optimised choices surrounding the content they engage with on a daily \
            basis. One application where this is especially true is movie recommendations; where intelligent algorithms\
             can help viewers find great titles from tens of thousands of options.With this context, EDSA has consulted\
              EDKO Consultings(2110ACDS_T14) to construct a recommendation algorithm based on content or collaborative \
              filtering, capable of accurately predicting how a user will rate a movie they have not yet viewed, based\
               on their historical preferences.Providing an accurate and robust solution to this challenge has immense \
               economic potential, with users of the system being personalised recommendations - generating platform \
               affinity for the streaming services which best facilitates their audience's viewing.A recommender system \
               functions by predicting a user's rating or preference for an item. This allows a service provider to build\
                up a catalog of items which it believes the user will want to examine - thereby increasing their engagement with the service and allowing a wider array of content to be considered.")
    if page_selection == "About Company":
        st.title("About Us")
        st.write("EDKO Consulting is an Information Technology Company whose focus is on delivering superior value to our clients on Data Science services.")
        st.write("We provide a human and machine powered solution for extracting knowledge from data. Our solutions are used by our clients to uncover insights from their data and empower their business teams to make data driven decisions.")
    if page_selection == "Explorative Data Analysis":
        st.title("Explorative Data Analysis")
        st.info("Lets us explore the data used in training our model")
        # You can read a markdown file from supporting resources folder
        # looked at the classes
        st.write("Genre Distribution")
        st.image('resources/imgs/movie_genre_dist.jpg')

        st.write("Top 10 User Number of Ratings")
        st.image('resources/imgs/genre_dist.jpg')

        st.write("Top 10 Number of Ratings")
        st.image('resources/imgs/top_10_number_of_ratings.jpg')

        st.write("Top 10 Director Ratings")
        st.image('resources/imgs/top_ten_director_ratings.jpg')

        st.write("T Distributed Stochastic Graph")
        st.image('resources/imgs/T_distributed_stoch.jpg')

        st.write("Rating Analysis")
        st.image('resources/imgs/rating_analysis.jpg')

        st.write("PCA Analysis")
        st.image('resources/imgs/pca_analysis.jpg')

    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
