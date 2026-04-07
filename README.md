# whichgame
Building a personal data engineering project that ingests daily game data to help a small group of friends discover new games based on their preferences. The pipeline will track player activity trends, ratings, and game metadata to surface personalized recommendations. Data will be stored and analyzed locally for learning purposes only.

# Why
There is one major problem my friends and I have which led to the creation of this project. And that is *What game do we play?!*

We constantly are getting bored of a game and looking for new one's to play. Out of this problem spawned 5 major questions that RAWG's data can help us figure out.

1. What games are people actively playing right now?
2. Which new releases are worth paying attention to?
3. What games will me and my friends most likely enjoy?
4. How is a game's reception trending over time? 
5. How long of a time commitment is a game? 

## Data Source
I am relying on the **RAWG** Free tier API for my data source. All my insights are gathered through the data available here, specifically with the *games* endpoint.

> You can explore the RAWG API and even grab your own API Key here: https://rawg.io/apidocs

## Data Modeling
I went with a star schema because I need to query and aggregate data fast to answer these questions my friends and I have.

So I will have a fact table consisting of the measureable and quantitive data I'll use to analyze. And the dimension tables that will contain the descriptive context for the games.

> More information on the data model found here: 

## Data Flow & Tech Stack
The flow is simple. RAWG API &rarr; Google BigQuery (Data Warehouse) &rarr; Streamlit

> Architecture Diagram found here: [Design](/doc/whichgame_architecture.png)

But, behind the scenes a lot will be happening to transform the data, hand pick out only the important data for my use case, and aggregating for visualization.

I will use a medallion architecture to have a clear separation of the raw, cleaned, and business ready data. Each layers serves a distinct purpose and I never lose my original data.

**Tech Stack:**
- Python for grabbing raw api data in JSON format and loading into Google BigQuery
- Google BigQuery for Data Warehouse
- DBT for data transformations using SQL
- Streamlit for visualizations
- Github Actions for Daily Incremental Load Batch Jobs
- Google Service Account needed for authentication to BigQuery