# HoopsQuery

## Description

As an avid NBA fan, I’m passionate about exploring detailed shot statistics of NBA players. This project is a full-stack application designed to provide dynamic insights into NBA shot data. It leverages React.js, HTML, and CSS for a responsive and user-friendly frontend, while Flask and Python handle backend operations. PostgreSQL serves as the robust database for storing extensive datasets, and OpenAI's GPT-4o mini model powers the intelligent query processing.

The application works by allowing users to input queries related to NBA shot statistics. These queries are processed by GPT-4o mini to dynamically generate the appropriate SQL commands. The backend then executes these queries against the PostgreSQL database and returns the results, which are displayed on a separate page, providing users with precise and actionable data insights.

*NOTE: This data is strictly from the years 2004 to 2024 (some stats are not included such as playoffs, free-throws)*

### Prerequisites
- Python3 <br />
- PostGreSQL <br />
- React <br />
- OpenAI <br />
- Psycopg2-binary <br />
- Flask <br />
- react-router-dom <br />

### Setup

1. Install Prerequisites <br />
2. Insert NBA-Shots data in PostGreSQL Database
2. ```git clone https://github.com/lukezx3/HoopsQuery.git``` <br />
3. ```cd <your project directory>``` <br />
4. Run ```npm start``` from project directory to run react script <br />
5. From another terminal/cmd-line tab: ```cd server``` <br />
6. Run ```python3 app.py``` to start backend server <br />

### Demo

https://github.com/user-attachments/assets/87c40652-73a5-48cb-8308-c53cfda71b2c

### Acknowledgements

Credit to DomSamangy for datasets: https://github.com/DomSamangy/NBA_Shots_04_24

