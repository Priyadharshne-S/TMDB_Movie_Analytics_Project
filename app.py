import streamlit as st
import pandas as pd
import mysql.connector
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns


# =====================================
# PREMIUM TMDB CHART THEME
# =====================================

def apply_movie_chart_theme(chart):
    return (
        chart.configure(
            background="#2B1D18",
            padding=20
        )
        .configure_view(
            stroke="#B89A72",
            strokeWidth=1.5
        )
        .configure_axis(
            labelColor="#E8D2A6",
            titleColor="#D6B878",
            gridColor="#654A3D",
            domainColor="#B89A72",
            tickColor="#B89A72",
            labelFontSize=12,
            titleFontSize=13
        )
        .configure_title(
            color="#FFD700",
            fontSize=18,
            fontWeight="bold"
        )
        .configure_legend(
            labelColor="#E8D2A6",
            titleColor="#D6B878"
        )
    )


# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="TMDB Movie Analytics",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------
# CUSTOM DASHBOARD THEME
# -----------------------------------

st.markdown("""


<style>

/* =====================================
   1. MAIN DASHBOARD THEME
===================================== */

.stApp {
    background: #2B1D18 !important;
    color: #F3E5C8 !important;
}

p, label {
    color: #E8D2A6;
}

h2, h3 {
    color: #D6B878 !important;
}

/* Main page spacing */
[data-testid="stMainBlockContainer"] {
    padding-top: 3rem !important;
    margin-top: 0 !important;
}

.main h1 {
    margin-top: 10px !important;
    padding-top: 10px !important;
    line-height: 1.4 !important;
}

/* =====================================
   2. PREMIUM GOLD MAIN TITLE
===================================== */

.main .block-container h1 {
    background: linear-gradient(
        120deg,
        #D6B878,
        #E8C6A0,
        #B76E79
    ) !important;

    color: #2B1D18 !important;
    padding: 22px 25px;
    border-radius: 14px;
    border: 2px solid #FFD700;
    text-align: center;
    font-size: 34px !important;
    font-weight: 800;
    letter-spacing: 1.5px;

    box-shadow:
        0 5px 16px rgba(0, 0, 0, 0.45),
        0 0 12px rgba(214, 184, 120, 0.25);
}

/* Subtitle */
.main .block-container [data-testid="stCaptionContainer"] {
    color: #E8D2A6 !important;
    text-align: center;
    font-size: 17px;
    font-weight: 600;
}

/* =====================================
   3. FLOATING MOCHA SIDEBAR
===================================== */

[data-testid="stSidebar"] {
    background: linear-gradient(
        145deg,
        #493329 0%,
        #3B2922 50%,
        #2B1D18 100%
    ) !important;

    border: none !important;
    border-radius: 0 !important;

    box-shadow:
        10px 0 25px rgba(0, 0, 0, 0.65),
        5px 0 18px rgba(183, 110, 121, 0.30),
        2px 0 10px rgba(214, 184, 120, 0.18) !important;
}

[data-testid="stSidebar"]::after {
    display: none !important;
    content: none !important;
}

[data-testid="stSidebarContent"] {
    padding: 18px 12px !important;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p {
    color: #D6B878 !important;
    font-weight: 600;
}

/* Sidebar dropdowns */
[data-testid="stSidebar"] div[data-baseweb="select"] > div {
    background-color: #E8D2A6 !important;
    border: 2px solid #B76E79 !important;
    border-radius: 8px !important;
}

[data-testid="stSidebar"] div[data-baseweb="select"] div,
[data-testid="stSidebar"] div[data-baseweb="select"] span {
    color: #2B1D18 !important;
}

/* Sidebar slider */
[data-testid="stSidebar"] [data-testid="stSlider"] [role="slider"] {
    background-color: #FFD700 !important;
}

/* =====================================
   4. PREMIUM NOTIFICATION BOXES
===================================== */

[data-testid="stAlert"] {
    background: linear-gradient(
        110deg,
        #E8D2A6 0%,
        #D6B878 30%,
        #B89A72 60%,
        #8B6B50 100%
    ) !important;

    border: 2px solid #E8D2A6 !important;
    border-left: 7px solid #B76E79 !important;
    border-radius: 12px !important;

    box-shadow:
        0 0 12px rgba(214, 184, 120, 0.35),
        inset 0 1px 5px rgba(255, 255, 255, 0.4) !important;
}

[data-testid="stAlert"] > div,
[data-testid="stAlert"] > div > div {
    background: transparent !important;
}

[data-testid="stAlert"] [data-testid="stMarkdownContainer"] {
    width: 100% !important;
    text-align: center !important;
}

[data-testid="stAlert"] p {
    color: #3B2922 !important;
    font-size: 18px !important;
    font-weight: 800 !important;
    text-align: center !important;
    padding: 8px 0 !important;
    letter-spacing: 0.5px;
    text-shadow: 0 1px 1px rgba(255, 255, 255, 0.35);
}

[data-testid="stAlert"] svg {
    color: #FFD700 !important;
    fill: #FFD700 !important;
    filter:
        drop-shadow(0 0 3px #FFF2A6)
        drop-shadow(0 0 6px #D6B878);
}

/* =====================================
   5. 3D KPI CARDS
===================================== */

[data-testid="stMetric"] {
    background: linear-gradient(
        145deg,
        #493329 0%,
        #3B2922 55%,
        #2B1D18 100%
    ) !important;

    border: 1px solid #B89A72 !important;
    border-radius: 14px !important;
    padding: 18px 14px !important;

    box-shadow:
        0 5px 12px rgba(0, 0, 0, 0.4),
        inset 0 1px 4px rgba(255, 255, 255, 0.08) !important;

    transition: all 0.3s ease !important;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-6px) scale(1.02) !important;
    border-color: #FFD700 !important;

    box-shadow:
        0 12px 22px rgba(0, 0, 0, 0.5),
        0 0 16px rgba(214, 184, 120, 0.45),
        inset 0 1px 5px rgba(255, 255, 255, 0.15) !important;
}

[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] p {
    color: #E8D2A6 !important;
    font-weight: 700 !important;
}

[data-testid="stMetricValue"],
[data-testid="stMetricValue"] div {
    color: #FFD700 !important;
    font-weight: 800 !important;
}

/* =====================================
   6. FOUR DASHBOARD TABS
===================================== */

.stTabs [role="tablist"] {
    display: grid !important;
    grid-template-columns: repeat(4, minmax(0, 1fr)) !important;
    width: 100% !important;
    gap: 3px !important;
    border-bottom: 2px solid #D6B878 !important;
    padding-bottom: 10px !important;
}

.stTabs [role="tab"] {
    width: 100% !important;
    min-height: 65px !important;
    justify-content: center !important;
    text-align: center !important;
    white-space: normal !important;
    padding: 12px 8px !important;

    background: linear-gradient(
        145deg,
        #493329,
        #3B2922
    ) !important;

    color: #E8D2A6 !important;
    border: 2px solid #D6B878 !important;
    border-radius: 10px !important;
    font-size: 18px !important;
    font-weight: 700 !important;

    box-shadow:
        0 4px 8px rgba(0, 0, 0, 0.35),
        inset 0 1px 3px rgba(255, 255, 255, 0.08) !important;
}

.stTabs [role="tab"][aria-selected="true"] {
    background: linear-gradient(
        135deg,
        #E8D2A6,
        #D6B878
    ) !important;

    color: #2B1D18 !important;
    border: 2px solid #FFD700 !important;

    box-shadow:
        0 5px 12px rgba(0, 0, 0, 0.4),
        0 0 12px rgba(255, 215, 0, 0.35) !important;
}

.stTabs [role="tab"][aria-selected="true"] * {
    color: #2B1D18 !important;
}

/* =====================================
   7. LIGHT CHAMPAGNE TABLE
===================================== */

[data-testid="stDataFrame"],
[data-testid="stTable"] {
    border: 2px solid #D6B878 !important;
    border-radius: 12px !important;
    overflow: hidden !important;

    box-shadow:
        0 5px 15px rgba(0, 0, 0, 0.4),
        0 0 10px rgba(214, 184, 120, 0.25) !important;
}

/* HTML table styling */
[data-testid="stTable"] th {
    background-color: #B89A72 !important;
    color: #2B1D18 !important;
    font-weight: 800 !important;
}

[data-testid="stTable"] td {
    background-color: #F3E5C8 !important;
    color: #3B2922 !important;
    border: 1px solid #D6B878 !important;
}

/* =====================================
   8. BUTTONS
===================================== */

.stButton > button {
    background: linear-gradient(
        135deg,
        #B76E79,
        #D6B878
    ) !important;

    color: #2B1D18 !important;
    border-radius: 8px !important;
    border: 1px solid #FFD700 !important;
    font-weight: bold !important;
}

.stButton > button:hover {
    background: #E8D2A6 !important;
    color: #2B1D18 !important;
    box-shadow: 0 0 12px rgba(255, 215, 0, 0.4);
}

/* =====================================
   9. DIVIDERS AND HEADER
===================================== */

hr {
    border-color: #D6B878 !important;
}

header[data-testid="stHeader"] {
    background-color: #2B1D18 !important;
}

.stDeployButton {
    display: none !important;
}


/* RESTORE FLOATING ROSE-GOLD SIDEBAR GLOW */

[data-testid="stSidebar"] {
    background: linear-gradient(
        145deg,
        #493329 0%,
        #3B2922 50%,
        #2B1D18 100%
    ) !important;

    box-shadow:
        8px 0 20px rgba(0, 0, 0, 0.65),
        4px 0 18px rgba(183, 110, 121, 0.45),
        2px 0 12px rgba(214, 184, 120, 0.25) !important;

    border-right: none !important;
}

/* Soft rose-gold glow inside the sidebar */
[data-testid="stSidebarContent"] {
    box-shadow:
        inset -5px 0 14px rgba(183, 110, 121, 0.12),
        inset -2px 0 8px rgba(214, 184, 120, 0.12) !important;
}


/* DASHBOARD TAB HOVER - 3D LIFT */
.stTabs [role="tablist"] {
    overflow: visible !important;
    padding-top: 12px !important;
    padding-bottom: 16px !important;
}

.stTabs [role="tab"] {
    position: relative !important;
    z-index: 1 !important;

    transition:
        transform 0.3s ease,
        box-shadow 0.3s ease,
        filter 0.3s ease !important;
}

.stTabs [role="tab"]:hover {
    transform: translateY(-6px) !important;
    z-index: 5 !important;

    filter: brightness(1.15) !important;

    box-shadow:
        0 12px 20px rgba(0, 0, 0, 0.65),
        0 0 18px rgba(255, 215, 0, 0.55),
        0 0 25px rgba(183, 110, 121, 0.3) !important;
}

/* PREMIUM CHART CONTAINER - GOLD GLOW */

div[data-testid="stVegaLiteChart"] {
    border: 1.5px solid rgba(214, 184, 120, 0.65) !important;
    border-radius: 16px !important;
    padding: 12px !important;
    background: linear-gradient(
        145deg,
        #3B2922,
        #2B1D18
    ) !important;

    box-shadow:
        0 5px 15px rgba(0, 0, 0, 0.55),
        0 0 10px rgba(214, 184, 120, 0.22),
        inset 0 0 8px rgba(183, 110, 121, 0.12) !important;

    transition: all 0.35s ease !important;
}

/* CHART HOVER - FLOATING EFFECT */

div[data-testid="stVegaLiteChart"]:hover {
    transform: translateY(-5px) !important;

    border-color: #FFD700 !important;

    box-shadow:
        0 14px 25px rgba(0, 0, 0, 0.65),
        0 0 18px rgba(255, 215, 0, 0.45),
        0 0 28px rgba(183, 110, 121, 0.30) !important;
}
/* FIX CHART WIDTH AND RIGHT-SIDE OVERFLOW */

div[data-testid="stVegaLiteChart"] {
    width: 100% !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
    overflow: hidden !important;
}

div[data-testid="stVegaLiteChart"] > div {
    width: 100% !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
}

div[data-testid="stVegaLiteChart"] canvas,
div[data-testid="stVegaLiteChart"] svg {
    max-width: 100% !important;
}

/* PREMIUM DATA TABLE DESIGN */

div[data-testid="stDataFrame"] {
    border: 1.5px solid #D6B878 !important;
    border-radius: 14px !important;
    overflow: hidden !important;

    box-shadow:
        0 6px 16px rgba(0, 0, 0, 0.55),
        0 0 12px rgba(214, 184, 120, 0.25) !important;

    transition: all 0.3s ease !important;
}

/* TABLE HOVER EFFECT */

div[data-testid="stDataFrame"]:hover {
    transform: translateY(-4px) !important;
    box-shadow:
        0 12px 24px rgba(0, 0, 0, 0.65),
        0 0 18px rgba(255, 215, 0, 0.4),
        0 0 25px rgba(183, 110, 121, 0.25) !important;
}

/* QUERY EXPLORER - PREMIUM BUTTON */

div[data-testid="stMainBlockContainer"] button {
    background: linear-gradient(
        135deg,
        #D6B878,
        #B89A72,
        #B76E79
    ) !important;

    color: #2B1D18 !important;
    font-weight: 800 !important;
    border: 1px solid #FFD700 !important;
    border-radius: 10px !important;

    box-shadow:
        0 4px 12px rgba(0, 0, 0, 0.45),
        0 0 10px rgba(214, 184, 120, 0.25) !important;

    transition: all 0.3s ease !important;
}

div[data-testid="stMainBlockContainer"] button:hover {
    transform: translateY(-3px) !important;
    filter: brightness(1.15) !important;

    box-shadow:
        0 8px 18px rgba(0, 0, 0, 0.55),
        0 0 18px rgba(255, 215, 0, 0.5) !important;
}
/* QUERY EXPLORER - PREMIUM DROPDOWN */

div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background: linear-gradient(
        135deg,
        #493329,
        #2B1D18
    ) !important;

    border: 1.5px solid #D6B878 !important;
    border-radius: 10px !important;

    box-shadow:
        0 4px 12px rgba(0, 0, 0, 0.4),
        0 0 8px rgba(214, 184, 120, 0.2) !important;
}

/* SELECTED DROPDOWN TEXT */

div[data-testid="stSelectbox"] div[data-baseweb="select"] span {
    color: #FFD700 !important;
    font-weight: 600 !important;
}

/* DROPDOWN HOVER */

div[data-testid="stSelectbox"] div[data-baseweb="select"]:hover > div {
    border-color: #FFD700 !important;
    box-shadow: 0 0 14px rgba(255, 215, 0, 0.4) !important;
}
</style>


""", unsafe_allow_html=True)


# -----------------------------------
# DASHBOARD HEADER
# -----------------------------------
@st.cache_resource
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=st.secrets["mysql"]["password"],
        database="tmdb_movie_analytics"
    )
st.title("🎬 TMDB MOVIE ANALYTICS")

st.caption(
    "Explore the Global Movie Industry Through Data"
)




st.success(
    "Welcome to the TMDB Movie Analytics Dashboard!"
)



try:
    connection = create_connection()

    if connection.is_connected():
        st.success("MySQL Database Connected Successfully!")

        # -----------------------------------
        # SIDEBAR FILTERS
        # -----------------------------------

        st.sidebar.title("🎯 MOVIE FILTERS")

        cursor = connection.cursor()

        cursor.execute(
            "SELECT genre_name FROM genres ORDER BY genre_name"
        )

        genre_options = [
            row[0] for row in cursor.fetchall()
            if row[0] is not None
        ]

        selected_genre = st.sidebar.selectbox(
            "Select Genre",
            ["All Genres"] + genre_options
        )

        cursor.execute("""
            SELECT DISTINCT YEAR(release_date)
            FROM movies
            WHERE release_date IS NOT NULL
            ORDER BY YEAR(release_date)
        """)

        year_options = [
            int(row[0]) for row in cursor.fetchall()
            if row[0] is not None
        ]

        cursor.close()

        selected_year = st.sidebar.selectbox(
            "Select Release Year",
            ["All Years"] + year_options
        )

        selected_rating = st.sidebar.slider(
            "Minimum Movie Rating",
            min_value=0.0,
            max_value=10.0,
            value=0.0,
            step=0.5
        )

        # -----------------------------------
        # FILTER CONDITIONS
        # -----------------------------------

        filter_conditions = " WHERE 1=1"
        params = []

        if selected_genre != "All Genres":
            filter_conditions += """
                AND EXISTS (
                    SELECT 1
                    FROM movie_genres mg
                    JOIN genres g ON mg.genre_id = g.genre_id
                    WHERE mg.movie_id = m.movie_id
                    AND g.genre_name = %s
                )
            """
            params.append(selected_genre)

        if selected_year != "All Years":
            filter_conditions += " AND YEAR(m.release_date) = %s"
            params.append(selected_year)

        filter_conditions += " AND m.vote_average >= %s"
        params.append(selected_rating)

        # -----------------------------------
        # FILTERED MOVIE QUERY
        # -----------------------------------

        query = """
            SELECT DISTINCT m.*
            FROM movies m
        """ + filter_conditions + """
            ORDER BY m.popularity DESC
            LIMIT 10
        """

        movie_data = pd.read_sql(
            query, connection, params=params
        )

        

        # -----------------------------------
        # MOVIE INDUSTRY OVERVIEW
        # -----------------------------------

        st.subheader("📊 MOVIE INDUSTRY OVERVIEW")

        # Total movies matching filters
        total_movies = pd.read_sql(
            "SELECT COUNT(*) AS total FROM movies m" + filter_conditions,
            connection,
            params=params
        ).iloc[0, 0]

        # Number of genres in filtered movies
        total_genres = pd.read_sql(
            """
            SELECT COUNT(DISTINCT g.genre_id) AS total
            FROM movies m
            JOIN movie_genres mg ON m.movie_id = mg.movie_id
            JOIN genres g ON mg.genre_id = g.genre_id
            """ + filter_conditions,
            connection,
            params=params
        ).iloc[0, 0]

        # Average rating of filtered movies
        avg_rating = pd.read_sql(
            "SELECT AVG(m.vote_average) AS average FROM movies m" + filter_conditions,
            connection,
            params=params
        ).iloc[0, 0]

        # Number of release years in filtered movies
        release_years = pd.read_sql(
            """
            SELECT COUNT(DISTINCT YEAR(m.release_date)) AS total
            FROM movies m
            """ + filter_conditions,
            connection,
            params=params
        ).iloc[0, 0]

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Movies", f"{total_movies:,}")
        col2.metric("Total Genres", f"{total_genres:,}")
        col3.metric("Average Rating", f"{avg_rating:.2f}/10")
        col4.metric("Release Years", f"{release_years:,}")

        # -----------------------------------
        # MOVIE DATASET PREVIEW
        # -----------------------------------

        st.subheader("Movie Dataset Preview")
        st.dataframe(movie_data, use_container_width=True)
        # -----------------------------------
        # TOP 10 MOVIE GENRES CHART
        # -----------------------------------

       
        genre_chart_query = """
        SELECT g.genre_name, COUNT(DISTINCT m.movie_id) AS movie_count
        FROM movies m
        JOIN movie_genres mg ON m.movie_id = mg.movie_id
        JOIN genres g ON mg.genre_id = g.genre_id
        """ + filter_conditions + """
        GROUP BY g.genre_name
        ORDER BY movie_count DESC
        LIMIT 10
        """

        genre_chart_data = pd.read_sql(
        genre_chart_query, connection, params=params
        )

        genre_chart = alt.Chart(genre_chart_data).mark_bar(
         color="#B76E79"
        ).encode(
        x=alt.X("movie_count:Q", title="Number of Movies"),
        y=alt.Y("genre_name:N", sort="-x", title="Genre"),
        tooltip=["genre_name", "movie_count"]
        ).properties(
        height=350
        ).configure(
        background="#FFF6FFFF"
        ).configure_view(
        fill="#E5E7EB",
        stroke="#B76E79",
        strokeWidth=3,
        strokeOpacity=1
        ).configure_axis(
        labelColor="#252A30",
        titleColor="#252A30",
        gridColor="#E2AB73",
        domainColor="#D6B878",
        domainWidth=2,
        tickColor="#D6B878",
        tickWidth=2
        )

        

# -----------------------------------
# TOP 10 HIGHEST-GROSSING MOVIES
# -----------------------------------

    
    revenue_query = """
    SELECT m.title, m.revenue
    FROM movies m
    """ + filter_conditions + """
    AND m.revenue > 0
    ORDER BY m.revenue DESC
    LIMIT 10
    """

    revenue_data = pd.read_sql(
    revenue_query, connection, params=params
    )

    revenue_chart = alt.Chart(revenue_data).mark_bar(
    color="#D6B878"
    ).encode(
    x=alt.X("revenue:Q", title="Revenue ($)"),
    y=alt.Y("title:N", sort="-x", title="Movie"),
    tooltip=["title", "revenue"]
    ).properties(
    height=350
    ).configure(
    background="#FFF6FFFF"
        ).configure_view(
        fill="#E8EAEC",
        stroke="#E9D165",
        strokeWidth=3,
        strokeOpacity=1
    ).configure_axis(
    labelColor="#252A30",
    titleColor="#252A30",
    gridColor="#C5BDB5",
    domainColor="#D6B878",
    domainWidth=2,
    tickColor="#D6B878",
    tickWidth=2
    )

    
    # -----------------------------------
    # MOVIES RELEASED EACH YEAR
    # -----------------------------------

  
    yearly_query = """
        SELECT YEAR(m.release_date) AS release_year,
               COUNT(*) AS movie_count
        FROM movies m
    """ + filter_conditions + """
        AND m.release_date IS NOT NULL
        GROUP BY YEAR(m.release_date)
        ORDER BY release_year
    """

    yearly_data = pd.read_sql(
        yearly_query, connection, params=params
    )
    yearly_chart = alt.Chart(yearly_data).mark_line(
        color="#B76E79",
        strokeWidth=4,
        point=alt.OverlayMarkDef(
            filled=True,
            color="#D6B878",
            size=90,
            stroke="#B76E79",
            strokeWidth=2
        )
    ).encode(
        x=alt.X(
            "release_year:O",
            title="Release Year",
            axis=alt.Axis(labelAngle=-45)
        ),
        y=alt.Y(
            "movie_count:Q",
            title="Number of Movies"
        ),
        tooltip=["release_year", "movie_count"]
    ).properties(
        height=380
    ).configure(
        background="#FFF6FFFF"
    ).configure_view(
        fill="#E8EAEC",
        stroke="#E9D165",
        strokeWidth=3
    ).configure_axis(
        labelColor="#252A30",
        titleColor="#252A30",
        gridColor="#E2AB73",
        domainColor="#D6B878",
        domainWidth=2,
        tickColor="#D6B878",
        tickWidth=2
    )

    
    # -----------------------------------
    # MOVIE BUDGET VS REVENUE
    # -----------------------------------

  
    budget_revenue_query = """
        SELECT m.title, m.budget, m.revenue, m.vote_average
        FROM movies m
    """ + filter_conditions + """
        AND m.budget > 0
        AND m.revenue > 0
    """

    budget_revenue_data = pd.read_sql(
        budget_revenue_query, connection, params=params
    )

    budget_revenue_chart = alt.Chart(budget_revenue_data).mark_circle(
        opacity=0.8,
        size=110,
        stroke="#B76E79",
        strokeWidth=1.2
    ).encode(
        x=alt.X("budget:Q", title="Movie Budget ($)"),
        y=alt.Y("revenue:Q", title="Movie Revenue ($)"),
        color=alt.Color(
            "vote_average:Q",
            title="Movie Rating",
            scale=alt.Scale(
                range=["#B76E79", "#D6B878", "#E9D165"]
            )
        ),
        tooltip=["title", "budget", "revenue", "vote_average"]
    ).properties(
        height=420
    ).configure(
        background="#FFF6FFFF"
    ).configure_view(
        fill="#E8EAEC",
        stroke="#E9D165",
        strokeWidth=3
    ).configure_axis(
        labelColor="#252A30",
        titleColor="#252A30",
        gridColor="#E2AB73",
        domainColor="#D6B878",
        domainWidth=2,
        tickColor="#D6B878",
        tickWidth=2
    ).configure_legend(
        labelColor="#252A30",
        titleColor="#252A30"
    )

    
    # -----------------------------------
    # DISTRIBUTION OF MOVIE RATINGS
    # -----------------------------------


    rating_query = """
        SELECT m.vote_average
        FROM movies m
    """ + filter_conditions + """
        AND m.vote_average > 0
    """

    rating_data = pd.read_sql(
        rating_query, connection, params=params
    )
    rating_chart = alt.Chart(rating_data).mark_bar(
        color="#D6B878",
        opacity=0.9,
        stroke="#B76E79",
        strokeWidth=1.5,
        cornerRadiusTopLeft=5,
        cornerRadiusTopRight=5
    ).encode(
        x=alt.X(
            "vote_average:Q",
            bin=alt.Bin(maxbins=20),
            title="Movie Rating",
            axis=alt.Axis(tickMinStep=1)
        ),
        y=alt.Y(
            "count():Q",
            title="Number of Movies"
        ),
        tooltip=[
            alt.Tooltip("count():Q", title="Movie Count")
        ]
    ).properties(
        height=400
    ).configure(
        background="#FFF6FFFF"
    ).configure_view(
        fill="#E8EAEC",
        stroke="#E9D165",
        strokeWidth=3
    ).configure_axis(
        labelColor="#252A30",
        titleColor="#252A30",
        gridColor="#E2AB73",
        domainColor="#D6B878",
        domainWidth=2,
        tickColor="#D6B878",
        tickWidth=2
    )

    
    # -----------------------------------
    # TOP 10 ACTORS BY NUMBER OF MOVIES
    # -----------------------------------

    

    actor_query = """
        SELECT c.actor_name, COUNT(DISTINCT c.movie_id) AS movie_count
        FROM cast c
        JOIN movies m ON c.movie_id = m.movie_id
    """ + filter_conditions + """
        GROUP BY c.actor_name
        ORDER BY movie_count DESC
        LIMIT 10
    """

    actor_data = pd.read_sql(
        actor_query, connection, params=params
    )
    actor_chart = alt.Chart(actor_data).mark_bar(
        cornerRadiusEnd=8,
        stroke="#B76E79",
        strokeWidth=1.5
    ).encode(
        x=alt.X(
            "movie_count:Q",
            title="Number of Movies"
        ),
        y=alt.Y(
            "actor_name:N",
            sort="-x",
            title="Actor"
        ),
        color=alt.Color(
            "movie_count:Q",
            scale=alt.Scale(
                range=["#B76E79", "#D6B878", "#E9D165"]
            ),
            legend=None
        ),
        tooltip=["actor_name", "movie_count"]
    ).properties(
        height=420
    ).configure(
        background="#FFF6FFFF"
    ).configure_view(
        fill="#E8EAEC",
        stroke="#E9D165",
        strokeWidth=3
    ).configure_axis(
        labelColor="#252A30",
        titleColor="#252A30",
        gridColor="#E2AB73",
        domainColor="#D6B878",
        domainWidth=2,
        tickColor="#D6B878",
        tickWidth=2
    )

    
    # -----------------------------------
    # AVERAGE POPULARITY BY GENRE
    # -----------------------------------

    

    popularity_query = """
        SELECT g.genre_name,
               AVG(m.popularity) AS average_popularity
        FROM movies m
        JOIN movie_genres mg ON m.movie_id = mg.movie_id
        JOIN genres g ON mg.genre_id = g.genre_id
    """ + filter_conditions + """
        GROUP BY g.genre_name
        ORDER BY average_popularity DESC
    """

    popularity_data = pd.read_sql(
        popularity_query, connection, params=params
    )
    popularity_chart = alt.Chart(popularity_data).mark_bar(
        cornerRadiusEnd=10,
        stroke="#B76E79",
        strokeWidth=1.5
    ).encode(
        x=alt.X(
            "average_popularity:Q",
            title="Average Popularity"
        ),
        y=alt.Y(
            "genre_name:N",
            sort="-x",
            title="Movie Genre"
        ),
        color=alt.Color(
            "average_popularity:Q",
            scale=alt.Scale(
                range=["#B76E79", "#D6B878", "#E9D165"]
            ),
            legend=None
        ),
        tooltip=[
            "genre_name",
            alt.Tooltip(
                "average_popularity:Q",
                format=".2f",
                title="Average Popularity"
            )
        ]
    ).properties(
        height=420
    ).configure(
        background="#FFF6FFFF"
    ).configure_view(
        fill="#E8EAEC",
        stroke="#E9D165",
        strokeWidth=3
    ).configure_axis(
        labelColor="#252A30",
        titleColor="#252A30",
        gridColor="#E2AB73",
        domainColor="#D6B878",
        domainWidth=2,
        tickColor="#D6B878",
        tickWidth=2
    )

    
    # -----------------------------------
    # TOP 10 MOST COMMON MOVIE KEYWORDS
    # -----------------------------------


    keyword_query = """
        SELECT mk.keyword_name,
               COUNT(DISTINCT mk.movie_id) AS movie_count
        FROM movie_keywords mk
        JOIN movies m ON mk.movie_id = m.movie_id
    """ + filter_conditions + """
        GROUP BY mk.keyword_name
        ORDER BY movie_count DESC
        LIMIT 10
    """

    keyword_data = pd.read_sql(
        keyword_query, connection, params=params
    )
    keyword_chart = alt.Chart(keyword_data).mark_bar(
        cornerRadiusEnd=9,
        stroke="#B76E79",
        strokeWidth=1.5
    ).encode(
        x=alt.X(
            "movie_count:Q",
            title="Number of Movies"
        ),
        y=alt.Y(
            "keyword_name:N",
            sort="-x",
            title="Movie Keywords"
        ),
        color=alt.Color(
            "movie_count:Q",
            scale=alt.Scale(
                range=["#B76E79", "#D6B878", "#E9D165"]
            ),
            legend=None
        ),
        tooltip=["keyword_name", "movie_count"]
    ).properties(
        height=420
    ).configure(
        background="#FFF6FFFF"
    ).configure_view(
        fill="#E8EAEC",
        stroke="#E9D165",
        strokeWidth=3
    ).configure_axis(
        labelColor="#252A30",
        titleColor="#252A30",
        gridColor="#E2AB73",
        domainColor="#D6B878",
        domainWidth=2,
        tickColor="#D6B878",
        tickWidth=2
    )

    
    # -----------------------------------
    # MOVIE RUNTIME DISTRIBUTION
    # -----------------------------------

    

    runtime_query = """
        SELECT m.runtime
        FROM movies m
    """ + filter_conditions + """
        AND m.runtime > 0
    """

    runtime_data = pd.read_sql(
        runtime_query, connection, params=params
    )
    runtime_chart = alt.Chart(runtime_data).mark_bar(
        color="#B76E79",
        opacity=0.85,
        stroke="#D6B878",
        strokeWidth=2,
        cornerRadiusTopLeft=5,
        cornerRadiusTopRight=5
    ).encode(
        x=alt.X(
            "runtime:Q",
            bin=alt.Bin(maxbins=25),
            title="Movie Runtime (Minutes)"
        ),
        y=alt.Y(
            "count():Q",
            title="Number of Movies"
        ),
        tooltip=[
            alt.Tooltip("count():Q", title="Movie Count")
        ]
    ).properties(
        height=400
    ).configure(
        background="#FFF6FFFF"
    ).configure_view(
        fill="#E8EAEC",
        stroke="#E9D165",
        strokeWidth=3
    ).configure_axis(
        labelColor="#252A30",
        titleColor="#252A30",
        gridColor="#E2AB73",
        domainColor="#D6B878",
        domainWidth=2,
        tickColor="#D6B878",
        tickWidth=2
    )

    
    # -----------------------------------
    # AVERAGE MOVIE RATING BY GENRE
    # -----------------------------------


    genre_rating_query = """
        SELECT g.genre_name,
               AVG(m.vote_average) AS average_rating
        FROM movies m
        JOIN movie_genres mg ON m.movie_id = mg.movie_id
        JOIN genres g ON mg.genre_id = g.genre_id
    """ + filter_conditions + """
        GROUP BY g.genre_name
        ORDER BY average_rating DESC
    """

    genre_rating_data = pd.read_sql(
        genre_rating_query, connection, params=params
    )
    genre_rating_chart = alt.Chart(genre_rating_data).mark_bar(
        cornerRadiusEnd=10,
        stroke="#B76E79",
        strokeWidth=1.5
    ).encode(
        x=alt.X(
            "average_rating:Q",
            title="Average Movie Rating",
            scale=alt.Scale(domain=[0, 10])
        ),
        y=alt.Y(
            "genre_name:N",
            sort="-x",
            title="Movie Genre"
        ),
        color=alt.Color(
            "average_rating:Q",
            scale=alt.Scale(
                domain=[0, 10],
                range=["#B76E79", "#D6B878", "#E9D165"]
            ),
            legend=None
        ),
        tooltip=[
            "genre_name",
            alt.Tooltip(
                "average_rating:Q",
                format=".2f",
                title="Average Rating"
            )
        ]
    ).properties(
        height=420
    ).configure(
        background="#FFF6FFFF"
    ).configure_view(
        fill="#E8EAEC",
        stroke="#E9D165",
        strokeWidth=3
    ).configure_axis(
        labelColor="#252A30",
        titleColor="#252A30",
        gridColor="#E2AB73",
        domainColor="#D6B878",
        domainWidth=2,
        tickColor="#D6B878",
        tickWidth=2
    )


    # -----------------------------------
    # ORGANIZE CHARTS INTO FOUR TABS
    # -----------------------------------

    overview_tab, finance_tab, audience_tab, insights_tab = st.tabs([
        "📊 Overview",
        "💰 Financial Analysis",
        "⭐ Audience & Popularity",
        "🎬 Movie Insights"
    ])

    # TAB 1: OVERVIEW
    with overview_tab:
        st.subheader("TOP 10 MOVIE GENRES")
        st.altair_chart(
            apply_movie_chart_theme(genre_chart),
            use_container_width=True
            )

        st.subheader("MOVIE RELEASE TRENDS")
        st.altair_chart(
            apply_movie_chart_theme(yearly_chart),
            use_container_width=True
            )

    # TAB 2: FINANCIAL ANALYSIS
    with finance_tab:
        st.subheader("TOP 10 HIGHEST-GROSSING MOVIES")
        st.altair_chart(
            apply_movie_chart_theme(revenue_chart),
            use_container_width=True
            )
        st.subheader("MOVIE BUDGET VS REVENUE")
        st.altair_chart(
            apply_movie_chart_theme(budget_revenue_chart),
            use_container_width=True
            )

    # TAB 3: AUDIENCE & POPULARITY
    with audience_tab:
        st.subheader("DISTRIBUTION OF MOVIE RATINGS")
        st.altair_chart(
        apply_movie_chart_theme(rating_chart),
        use_container_width=True
        )
        st.subheader("TOP 10 ACTORS")
        st.altair_chart(
        apply_movie_chart_theme(actor_chart),
        use_container_width=True
        )
        st.subheader("AVERAGE POPULARITY BY GENRE")
        st.altair_chart(
        apply_movie_chart_theme(popularity_chart),
        use_container_width=True
        )   
       
    # TAB 4: MOVIE INSIGHTS
    with insights_tab:
        st.subheader("TOP 10 MOST COMMON KEYWORDS")
        st.altair_chart(
        apply_movie_chart_theme(keyword_chart),
        use_container_width=True
        )
        
        st.subheader("MOVIE RUNTIME DISTRIBUTION")
        st.altair_chart(
        apply_movie_chart_theme(runtime_chart),
        use_container_width=True
        )
        st.subheader("AVERAGE MOVIE RATING BY GENRE")
        st.altair_chart(
        apply_movie_chart_theme(genre_rating_chart),
        use_container_width=True
        )      
        
    # -----------------------------------
    # QUERY EXPLORER
    # -----------------------------------

    st.divider()
    st.header("🔎 QUERY EXPLORER")
    st.caption("Explore movie data through interactive database queries.")
    query_choice = st.selectbox(
        "SELECT AN ANALYSIS",
        [
            "Top 10 Highest-Rated Movies",
            "Top 10 Most Popular Movies",
            "Movies Released by Year",
            "Top 10 Highest-Grossing Movies",
            "Top 10 Longest Movies",
            "Movie Count by Genre"
        ]
    )
    if st.button("🚀 RUN ANALYSIS"):
        if query_choice == "Top 10 Highest-Rated Movies":
            explorer_query = """
                SELECT title, vote_average, vote_count
                FROM movies
                WHERE vote_count > 0
                ORDER BY vote_average DESC
                LIMIT 10
            """

        elif query_choice == "Top 10 Most Popular Movies":
            explorer_query = """
                SELECT title, popularity, vote_average
                FROM movies
                ORDER BY popularity DESC
                LIMIT 10
            """

        elif query_choice == "Movies Released by Year":
            explorer_query = """
                SELECT YEAR(release_date) AS release_year,
                       COUNT(*) AS movie_count
                FROM movies
                WHERE release_date IS NOT NULL
                GROUP BY YEAR(release_date)
                ORDER BY release_year
            """

        elif query_choice == "Top 10 Highest-Grossing Movies":
            explorer_query = """
                SELECT title, revenue
                FROM movies
                WHERE revenue > 0
                ORDER BY revenue DESC
                LIMIT 10
            """

        elif query_choice == "Top 10 Longest Movies":
            explorer_query = """
                SELECT title, runtime
                FROM movies
                WHERE runtime > 0
                ORDER BY runtime DESC
                LIMIT 10
            """

        elif query_choice == "Movie Count by Genre":
            explorer_query = """
                SELECT g.genre_name,
                       COUNT(DISTINCT m.movie_id) AS movie_count
                FROM movies m
                JOIN movie_genres mg ON m.movie_id = mg.movie_id
                JOIN genres g ON mg.genre_id = g.genre_id
                GROUP BY g.genre_name
                ORDER BY movie_count DESC
            """

    explorer_data = pd.read_sql(explorer_query, connection)

    st.success("Analysis completed successfully!")

    st.metric(
    label="TOTAL RECORDS FOUND",
    value=f"{len(explorer_data):,}"
    )

    st.dataframe(
    explorer_data,
    use_container_width=True
    )
except Exception as e:
    st.error(f"Database Connection Failed: {e}")

  

