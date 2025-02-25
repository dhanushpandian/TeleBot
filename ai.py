from dotenv import load_dotenv
import requests
import json
import os
import re 
from db import get_db_connection

with open("Q_data.json", "r") as file:
    Q = json.load(file)
    Q={int(k):v for k,v in Q.items()}

load_dotenv()

file_path = os.path.join(os.path.dirname(__file__), "sql\sql.txt")

def ai_bot(choice, user):
    print(user, Q[choice])
    x = input("Describe your query: ")

    with open(file_path, "r") as f:
        schema = f.read()

    user_message = f"""
    Generate an optimized SQL query that retrieves all relevant details to answer:
    '{x} for the user name like {user} for the query about {Q[choice]}' based only on the telecom database schema and not cooking new values or tables on ur own : {schema}.
    Ensure the query correctly joins tables across multiple linked databases only if its necessary.
    Only return the SQL query in plain text (without any markdown formatting).
    """

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

    payload = {"contents": [{"parts": [{"text": user_message}]}]}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        response_data = response.json()
        try:
            sql_query = response_data["candidates"][0]["content"]["parts"][0]["text"].strip()

            # 🔹 Remove markdown formatting (```sql ... ```)
            sql_query = re.sub(r"```(sql)?", "", sql_query).strip()

            print("\n🔹 **Generated SQL Query:** \n")
            print(sql_query)
            try:
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute(sql_query)
                results = cursor.fetchall()
            except Exception as e:
                print(f"❌ Database query execution failed: {e}")
                results = None
            finally:
                if 'conn' in locals() and conn:
                    conn.close()


            if results:
                # **📌 Neatly format & display results**
                # print("\n🔹 **Database Response:**\n")
                # headers = results[0].keys()  # Column names
                # rows = [list(row.values()) for row in results]
                # print(tabulate(rows, headers=headers, tablefmt="grid"))

                formatted_data = json.dumps(results, default=str)  

                ai_response_payload = {
                    "contents": [{
                        "parts": [{"text": f"Given this database result: {formatted_data}, provide a response to the user's query: '{x}'from user {user} in the matter {Q[choice]} in a clear, concise, and professional manner."}]
                    }]
                }
                
                ai_response = requests.post(url, headers=headers, json=ai_response_payload)

                if ai_response.status_code == 200:
                    ai_response_data = ai_response.json()
                    ai_message = ai_response_data["candidates"][0]["content"]["parts"][0]["text"].strip()
                    print("\n🗣️ **AI Response:** \n")
                    print(ai_message)
                else:
                    print("\n⚠️ **Error: Failed to fetch AI-generated response.**")

            return results

        except KeyError:
            print("\n❌ **Error: Invalid response from Gemini API**")
            return "Error: Unable to generate SQL query"

    else:
        print("\n❌ **Error: Failed to fetch response from Gemini API**")
        return "Error: Failed to generate SQL query"

if __name__ == "__main__":
    print(ai_bot(1, "john"))
