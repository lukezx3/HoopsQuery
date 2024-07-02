#import necessary libraries
import os
import openai
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import psycopg2.pool

#bypass CORS conflict
app = Flask(__name__)
CORS(app)

#create db pool
pool = psycopg2.pool.SimpleConnectionPool( 
    1, 20, user='postgres', password='', 
    host='localhost', port='5432', database='nbashooting')

#single db connection 
# try:
#     conn = psycopg2.connect(database="nbashooting", 
#         user="postgres", 
#         password="", 
#         host="localhost", port="5432")
# except Exception as err:
#     print(err)

#get openapi key
openai_api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = openai_api_key

#description for gpt query to match DB fields
schemaDescription = """
                The table 'nba_combined_all' has the following schema:
                -season_1: INTEGER (ex: 2004, 2005, 2006,...2024)
                -season_2: VARCHAR(100) (ex: 2004-05, 2005-06, 2006-07,...2023-24)
                -team_id: INTEGER (ex: 1610612747, 1610612757, ...)
                -team_name: VARCHAR(100) (ex: Golden State Warriors, Washington Wizards, etc (NBA teams from 2004-2024)
                -player_id: INTEGER, NOT NULL (ex: 977, 4-byte integer or less)
                -player_name: VARCHAR(100) (ex: NBA basketball players since 2004 to 2024)
                -position_group: VARCHAR(5) (ex: G, F, C which stand for Guard, Forward, Center)
                -position: VARCHAR(10) (ex: PG, SG, SF, PF, C which stand for Point Guard, Shooting Guard, Small Forward, Power Forward, and Center)
                -game_date: VARCHAR(100) (ex: 04-01-03, 04-13-03, etc_
                -game_id: INTEGER (ex: 4-byte integers)             
                -home_team: VARCHAR(100) (POR, LAL, GSW, etc... standard NBA team abbreviations)
                -away_team: VARCHAR(100) (POR, LAL, GSW, etc... standard NBA team abbreviations)
                -event_type: VARCHAR(100) (Made Shot, Missed Shot)  
                -shot_made: BOOLEAN (TRUE or FALSE)             
                -action_type: VARCHAR(100) (Layup Shot, Jump Shot, Hook Shot, etc... just make sure to search with LIKE %*user-inputted type of shot*%)
                -shot_type: VARCHAR(100) (Exact Names: 2PT Field Goal, 3PT Field Goal)
                -basic_zone: VARCHAR(100) (Restricted Area, In the Paint (non-RA), Midrange, Left Corner 3, Right Corner 3, Above the Break, Backcourt)
                -zone_name: VARCHAR(50) (Name of the side of court the shot took place in: left, left side center, center, right side center, right)
                -zone_abb: VARCHAR(10) (Abbreivation of the side of court: L, LC, C, RC, R)
                -zone_range: VARCHAR(50) (These are the specific possible values: Less than 8 ft., 8-16 ft. 16-24 ft. 24+ ft)
                -loc_x: REAL (X coordinate of the shot in the x, y plane of the court (0, 50))
                -loc_y: REAL (Y coordinate of the shot in the x, y plane of the court (0, 50))
                -shot_distance: INTEGER (Distance of the shot with respect to the center of the hoop, in feet)
                -quarter: INTEGER (1,2,3,4 which represent the quarter of the game)
                -mins_left: INTEGER (Minutes remaining in the quarter)
                -secs_left: INTEGER (Seconds remaining in minute of the quarter)
                -shot_id: INTEGER, NOT NULL (auto-incremented 1,2,3....xxx)
                *******************************
                -PRIMARY KEY (shot_id, player_id)
                -Indexes: indexes on player_id, player_name, season_1, team_id, team_name
              """

#query route
@app.route('/query', methods=['POST'])
def generateSQL():
    #app.logger.info('Triggered /query route')
    if request.method == 'POST':

        #store user query as userInput
        reqJSON = request.get_json()
        userInput = reqJSON['input']
        app.logger.info(userInput)

        attempts = 0
        maxAttempts = 20
        flag = True

        #make connection to pool
        conn = pool.getconn()
        curr = conn.cursor()

        #requery if gpt generated query is invalid
        while attempts < maxAttempts:
            try:
                if flag:
                    fprompt = f"{schemaDescription}\nGenerate an SQL query for the following request: {userInput}"
                else:
                    fprompt = f"{schemaDescription}\nQuery Failed. Regenerate an SQL query for the following request: {userInput}"


                #generate sql query through gpt
                gpt_response = openai.chat.completions.create(
                    model = 'gpt-3.5-turbo',
                    messages=[
                        {
                            "role": "user",
                            "content": fprompt,
                        },
                    ],
                    max_tokens=500,
                    temperature=0.7,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
            
                # #Get and run SQL query
                sql_query = gpt_response.choices[0].message.content
                sql_query = sql_query.lstrip().rstrip()
                print('Generated SQL query:', sql_query)
                curr.execute(sql_query)

                #obtain results from running query
                finalres = curr.fetchall()

                #close cursor and release db connection
                curr.close()
                pool.putconn(conn)

                #return query result
                response = jsonify(finalres)
                response.headers.add('Access-Control-Allow-Origin', '*')
                return response
            
            #if ran too many times, output failed
            except Exception as err:
                flag = False
                attempts += 1
                if attempts >= maxAttempts:
                    print(err)
                    pool.putconn(conn)
                    return jsonify({'success': False, 'error': "Failed to generate results."}), 500

if __name__ == '__main__':
    app.run(debug=True)