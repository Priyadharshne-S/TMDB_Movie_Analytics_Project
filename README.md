# 🎬 REEL INSIGHTS
### Discovering the Stories Behind Movie Data

**An End-to-End TMDB Movie Analytics Project**

---

## 🌟 About the Project

Movies are more than entertainment—they are an industry driven by creativity, audience preferences, financial performance and changing trends.

**Reel Insights** explores these dimensions through data analytics. Using TMDB movie datasets, this project transforms raw movie records into meaningful insights through Python, SQL, data visualization and an interactive Streamlit dashboard.

The goal is to understand what the data reveals about movie genres, audience ratings, popularity, production costs and commercial success.

---

## 🎯 What This Project Explores

- Which genres dominate the movie dataset?
- How have movie releases changed over the years?
- Which movies achieved the highest revenue?
- Is movie popularity related to audience engagement?
- Which actors appear most frequently?
- How do ratings differ across genres?
- What patterns can be discovered from movie keywords and runtimes?

---

## 🧰 Technology Stack

| Tool | Application |
|---|---|
| Python | Core programming |
| Pandas & NumPy | Data preparation and analysis |
| MySQL | Relational database |
| SQL | Data extraction and querying |
| Matplotlib & Seaborn | Statistical visualization |
| Altair | Interactive charts |
| Streamlit | Dashboard development |
| Jupyter Notebook | Analytical workflow |

---

## 🔄 Project Workflow

**01 — Data Preparation**

Six related datasets were examined, cleaned and standardized. Missing values, duplicate records, inconsistent formats and date fields were handled.

**02 — Database Development**

Cleaned datasets were imported into MySQL, creating a structured database for further analysis.

**03 — SQL Exploration**

SQL queries were developed to investigate movie performance, genres, actors, ratings and revenue.

**04 — Python Analysis**

Pandas and NumPy were used to explore relationships, calculate performance measures and identify trends.

**05 — Visual Storytelling**

Ten visualizations were created to communicate important findings in an understandable way.

**06 — Interactive Dashboard**

A Streamlit application was developed to bring the analyses together in one interactive platform.

---

## 📁 Dataset Collection

The project works with six interconnected datasets:

| Dataset | Information |
|---|---|
| Movies | Titles, ratings, release dates, budget and revenue |
| Genres | Movie genre categories |
| Movie Genres | Movie-to-genre relationships |
| Cast | Actors and character details |
| Crew | Production team information |
| Movie Keywords | Descriptive movie keywords |

**Total cleaned records: 73,272**

---

## 📊 Analytical Highlights

Some interesting findings from the analysis:

| Finding | Result |
|---|---:|
| Movies with non-zero budget and revenue | 2,370 |
| Average movie profit | $164.89 million |
| Average ROI | 1,319.85% |
| Highest release year in the dataset | 2016 |
| Movies released in 2016 | 121 |
| Popularity and vote-count correlation | 0.361 |
| Repeated movie titles identified | 100 |

*These findings describe the analysed dataset and should not be interpreted as statistics for the entire global film industry.*

---

## 📈 Visualization Gallery

The project includes ten analytical visualizations:

1. Top 10 Movie Genres
2. Movie Release Trends
3. Top 10 Highest-Grossing Movies
4. Movie Budget vs Revenue
5. Distribution of Movie Ratings
6. Top 10 Actors
7. Average Popularity by Genre
8. Most Common Movie Keywords
9. Movie Runtime Distribution
10. Average Movie Rating by Genre

---

## 💻 Interactive Dashboard

The Streamlit dashboard is organized into four analytical sections and an additional Query Explorer.

**01. Overview**
- Genre distribution
- Movie release trends

**02. Financial Analysis**
- Highest-grossing movies
- Budget and revenue comparison

**03. Audience & Popularity**
- Rating distribution
- Top actors
- Genre popularity

**04. Movie Insights**
- Movie keywords
- Runtime distribution
- Average ratings by genre

**05. Query Explorer**

An interactive SQL-powered feature that allows users to explore six different movie analyses through a selection dropdown.

Additional features include dynamic KPI cards, interactive filters and a coordinated cinematic interface.

---

## 🎨 Design Philosophy

The dashboard follows a premium cinematic visual identity, combining:

- Deep chocolate and mocha backgrounds.
- Champagne-gold and rose-gold accents.
- Glowing chart borders.
- Floating hover effects.
- Elegant dashboard navigation.
- Interactive analytical components.

The design aims to make data exploration both informative and visually engaging.

---

## 🚀 Running the Project

### Requirements

Python, MySQL Server and the required Python libraries.

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Database Configuration

Create the MySQL database:

```sql
CREATE DATABASE tmdb_movie_analytics;
```

Import the cleaned datasets into their corresponding tables.

Configure your local database credentials in `.streamlit/secrets.toml`. Never publish your actual password.

### Launch the Dashboard

```bash
python -m streamlit run app.py
```

---

## 📚 Skills Demonstrated

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Python programming
- SQL querying and database management
- Data visualization and interpretation
- Interactive dashboard development
- Analytical problem-solving
- Data storytelling

---
---

## 🖼️ Dashboard Screenshots

Explore the dashboard interface and analytical results through the project screenshots.

All dashboard screenshots are available in the `project_screenshots` folder.

## 🏆 Project Outcome

Reel Insights brings together the complete data analytics process—from raw data preparation to interactive business intelligence.

It demonstrates how multiple analytical technologies can work together to uncover patterns, communicate findings and create a practical data exploration experience.

**REEL INSIGHTS | Turning Movie Data into Meaningful Discoveries**

*Python · Pandas · MySQL · SQL · Streamlit*
