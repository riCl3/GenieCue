import pickle
import streamlit as st
import requests
from PIL import Image
import io

# Page configuration
st.set_page_config(
    page_title="GeniCue | Movie Recommender",
    page_icon="🎬",
    layout="wide",
)

# Custom CSS for a modern UI
st.markdown("""
<style>
    /* Modern color scheme */
    :root {
        --primary: #6366F1;
        --primary-hover: #818CF8;
        --secondary: #2DD4BF;
        --dark: #1E293B;
        --light: #F8FAFC;
        --card-bg: rgba(255, 255, 255, 0.05);
        --card-border: rgba(255, 255, 255, 0.1);
    }

    .main {
        background-color: var(--dark);
        color: var(--light);
    }

    /* Header styles */
    .title-container {
        text-align: center;
        margin-bottom: 2rem;
        padding: 1.5rem 0;
        background: linear-gradient(90deg, var(--primary), var(--secondary));
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
        position: relative;
        overflow: hidden;
    }

    .title-container h1 {
        font-weight: 800;
        font-size: 3rem;
        margin: 0;
        background: linear-gradient(to right, #FFFFFF, #E2E8F0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline-block;
    }

    .title-container p {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.1rem;
        margin-top: 0.5rem;
    }

    /* Movie card styles */
    .movie-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(170px, 1fr));
        gap: 20px;
    }

    .movie-card {
        background: var(--card-bg);
        border: 1px solid var(--card-border);
        border-radius: 12px;
        overflow: hidden;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        height: 100%;
        display: flex;
        flex-direction: column;
    }

    .movie-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 25px rgba(0, 0, 0, 0.2);
        border-color: var(--primary);
    }

    .movie-poster {
        width: 100%;
        aspect-ratio: 2/3;
        object-fit: cover;
        border-bottom: 1px solid var(--card-border);
    }

    .movie-info {
        padding: 12px;
        flex-grow: 1;
        display: flex;
        flex-direction: column;
    }

    .movie-title {
        font-size: 1rem;
        font-weight: 600;
        margin-bottom: 8px;
        overflow: hidden;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        color: white;
    }

    .movie-meta {
        font-size: 0.8rem;
        color: rgba(255, 255, 255, 0.7);
        display: flex;
        align-items: center;
        gap: 8px;
        margin-top: auto;
    }

    .rating {
        display: flex;
        align-items: center;
        gap: 4px;
        color: #FFD700;
    }

    /* Button styles */
    .custom-button {
        background: linear-gradient(90deg, var(--primary), var(--secondary));
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 8px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        width: 100%;
        text-align: center;
    }

    .custom-button:hover {
        opacity: 0.9;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
    }

    /* Search box styles */
    .search-container {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 2rem;
        border: 1px solid var(--card-border);
    }

    /* Section styles */
    .section-title {
        font-size: 1.5rem;
        font-weight: 700;
        margin: 2rem 0 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid var(--primary);
        display: inline-block;
    }

    /* Footer style */
    .footer {
        margin-top: 4rem;
        text-align: center;
        padding: 2rem 0;
        border-top: 1px solid var(--card-border);
        color: rgba(255, 255, 255, 0.6);
    }

    /* Updated creator attribution */
    .creator-info {
        font-size: 1.1rem;
        margin: 0 0 10px 0;
        padding: 8px 16px;
        display: inline-block;
        background: linear-gradient(90deg, rgba(99, 102, 241, 0.15), rgba(45, 212, 191, 0.15));
        border-radius: 8px;
        border-left: 4px solid var(--primary);
    }

    .creator-info strong {
        background: linear-gradient(90deg, var(--primary), var(--secondary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
    }

    .footer a {
        color: var(--primary);
        text-decoration: none;
    }

    .footer a:hover {
        text-decoration: underline;
    }

    /* Selectbox styling */
    div[data-baseweb="select"] {
        background-color: rgba(255, 255, 255, 0.1) !important;
        border-radius: 8px !important;
    }

    div[data-baseweb="select"] > div {
        background-color: transparent !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        color: white !important;
    }

    /* Updated feature box with margin */
    .feature-box {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 30px;
        display: flex;
        align-items: center;
        gap: 15px;
        border: 1px solid var(--card-border);
        flex: 1;
        max-width: 48%;
    }

    /* Feature box container with space between */
    .feature-container {
        display: flex;
        justify-content: space-between;
        gap: 35px;
        margin-bottom: 30px;
    }

    .feature-icon {
        font-size: 24px;
        color: var(--primary);
    }

    .selected-movie {
        background: linear-gradient(to right, rgba(99, 102, 241, 0.1), rgba(45, 212, 191, 0.1));
        border-radius: 12px;
        padding: 20px;
        margin: 20px 0;
        border: 1px solid var(--card-border);
    }

    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .animate-in {
        animation: fadeIn 0.6s ease forwards;
    }
</style>
""", unsafe_allow_html=True)


# Function to fetch movie poster with error handling
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        data = requests.get(url, timeout=5).json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path

        # Return a default image if no poster is available
        return "https://via.placeholder.com/500x750/1E293B/FFFFFF?text=No+Poster"
    except Exception:
        return "https://via.placeholder.com/500x750/1E293B/FFFFFF?text=No+Poster"


# Function to get extra movie details
def get_movie_details(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        data = requests.get(url, timeout=5).json()

        return {
            "rating": round(data.get('vote_average', 0), 1),
            "year": data.get('release_date', '')[:4] if data.get('release_date') else 'N/A',
            "genres": [genre['name'] for genre in data.get('genres', [])][:2],
            "overview": data.get('overview', 'No overview available.')[:200] + '...' if data.get('overview') and len(
                data.get('overview')) > 200 else data.get('overview', 'No overview available.')
        }
    except Exception:
        return {
            "rating": 0,
            "year": "N/A",
            "genres": [],
            "overview": "No overview available."
        }


def recommend(movie):
    with st.spinner("Finding the perfect movies for you..."):
        index = new_df[new_df['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movies = []

        for i in distances[1:7]:
            movie_id = new_df.iloc[i[0]].movie_id
            movie_title = new_df.iloc[i[0]].title
            poster_url = fetch_poster(movie_id)
            details = get_movie_details(movie_id)
            similarity_score = distances[i[0] - distances[1][0] + 1][1]

            recommended_movies.append({
                "title": movie_title,
                "poster": poster_url,
                "rating": details["rating"],
                "year": details["year"],
                "genres": details["genres"],
                "overview": details["overview"],
                "similarity": round(similarity_score * 100, 1)  # Convert to percentage
            })

        return recommended_movies


# Header with modern design
st.markdown("""
<div class="title-container animate-in">
    <h1>GeniCue</h1>
    <p>AI-Powered Movie Recommendation Engine</p>
</div>
""", unsafe_allow_html=True)

# Introduction
st.markdown("""
<div class="animate-in" style="opacity: 0; animation-delay: 0.2s;">
    <p style="font-size: 1.1rem; text-align: center; max-width: 800px; margin: 0 auto 2rem auto;">
        Discover your next favorite movie with GeniCue's intelligent recommendation engine. Based on your movie preferences, our AI system finds films with similar themes, styles, and appeal.
    </p>
</div>
""", unsafe_allow_html=True)

# Features section with improved spacing
st.markdown("""
<div class="animate-in" style="opacity: 0; animation-delay: 0.3s;">
    <div class="feature-container">
        <div class="feature-box">
            <div class="feature-icon">🎯</div>
            <div>
                <h3 style="margin: 0;">Personalized Recommendations</h3>
                <p style="margin: 5px 0 0 0;">Get movie suggestions tailored to your taste</p>
            </div>
        </div>
        <div class="feature-box">
            <div class="feature-icon">🔍</div>
            <div>
                <h3 style="margin: 0;">Content-Based Analysis</h3>
                <p style="margin: 5px 0 0 0;">Using advanced AI to match film characteristics</p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Load data
with st.spinner("Initializing movie database..."):
    try:
        new_df = pickle.load(open('movie_list.pkl', 'rb'))
        similarity = pickle.load(open('similarity.pkl', 'rb'))
        movie_list = new_df['title'].values
    except Exception as e:
        st.error(f"Error loading movie database: {e}")
        st.stop()

# Search container with styling
st.markdown("""
<div class="search-container animate-in" style="opacity: 0; animation-delay: 0.4s;">
    <h2 style="margin-top: 0; font-size: 1.3rem;">Find Movies Similar To Your Favorites</h2>
""", unsafe_allow_html=True)

selected_movie = st.selectbox(
    "Select a movie you enjoy",
    movie_list,
    index=0,
    placeholder="Type or select a movie...",
)

col1, col2 = st.columns([3, 1])
with col2:
    search_button = st.button('Get Recommendations', key='search_button')

st.markdown('</div>', unsafe_allow_html=True)

# Display selected movie details if a movie is selected
if selected_movie:
    try:
        movie_index = new_df[new_df['title'] == selected_movie].index[0]
        movie_id = new_df.iloc[movie_index].movie_id
        poster_url = fetch_poster(movie_id)
        details = get_movie_details(movie_id)

        st.markdown("""
        <div class="selected-movie animate-in" style="opacity: 0; animation-delay: 0.5s;">
            <h3 style="margin-top: 0;">Selected Movie</h3>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns([1, 3])

        with col1:
            # Fixed deprecated parameter
            st.image(poster_url, use_container_width=True)

        with col2:
            st.markdown(f"### {selected_movie}")

            if details["genres"]:
                st.markdown(f"**Genres:** {', '.join(details['genres'])}")

            if details["year"] != "N/A":
                st.markdown(f"**Year:** {details['year']}")

            if details["rating"] > 0:
                st.markdown(f"**Rating:** ⭐ {details['rating']}/10")

            st.markdown(f"**Overview:** {details['overview']}")

        st.markdown('</div>', unsafe_allow_html=True)
    except Exception as e:
        st.warning(f"Could not load details for {selected_movie}")

# Show recommendations when button is clicked
if search_button:
    recommended_movies = recommend(selected_movie)

    st.markdown("""
    <h2 class="section-title animate-in" style="opacity: 0; animation-delay: 0.6s;">
        Your Personalized Recommendations
    </h2>
    """, unsafe_allow_html=True)

    # Create a grid of movie cards
    st.markdown('<div class="movie-grid">', unsafe_allow_html=True)

    # Use Streamlit columns for responsive grid
    cols = st.columns(6)

    for i, movie in enumerate(recommended_movies):
        with cols[i]:
            st.markdown(f"""
            <div class="movie-card animate-in" style="opacity: 0; animation-delay: {0.7 + i * 0.1}s;">
                <img src="{movie['poster']}" class="movie-poster" alt="{movie['title']}">
                <div class="movie-info">
                    <div class="movie-title">{movie['title']}</div>
                    <div class="movie-meta">
                        <span>{movie['year']}</span>
                        <span class="rating">⭐ {movie['rating']}</span>
                    </div>
                    <div style="font-size: 0.8rem; margin-top: 8px; color: var(--primary);">
                        {movie['similarity']}% match
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# How it works section
st.markdown("""
<h2 class="section-title animate-in" style="opacity: 0; animation-delay: 0.8s;">
    How GeniCue Works
</h2>
<div class="animate-in" style="opacity: 0; animation-delay: 0.9s;">
    <p>GeniCue uses advanced machine learning algorithms to analyze movie features such as:</p>
    <ul>
        <li>Cast and crew</li>
        <li>Genre and themes</li>
        <li>Plot elements</li>
        <li>User ratings and reviews</li>
        <li>Visual style and tone</li>
    </ul>
    <p>By comparing these elements across thousands of films, GeniCue can identify movies with similar characteristics to your favorites, helping you discover new films you'll love.</p>
</div>
""", unsafe_allow_html=True)

# Footer with enhanced creator information
st.markdown("""
<div class="footer animate-in" style="opacity: 0; animation-delay: 1s;">
    <p class="creator-info">GeniCue was created by <strong>Soumya</strong>, NIT Allahabad Student</p>
    <p>Powered by TMDB API • Built with Streamlit • Copyright © 2025</p>
</div>
""", unsafe_allow_html=True)