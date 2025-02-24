#from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from dotenv import load_dotenv
import pymysql
import os
import requests
from openai import OpenAI

load_dotenv()


def get_db_connection():
    return pymysql.connect(
        db=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        charset=os.getenv("DB_CHARSET"),
        connect_timeout=int(os.getenv("DB_TIMEOUT")),
        read_timeout=int(os.getenv("DB_TIMEOUT")),
        write_timeout=int(os.getenv("DB_TIMEOUT")),
        cursorclass=pymysql.cursors.DictCursor
    )

def show_tables():
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables=cursor.fetchall()
        return tables
    finally:
        connection.close()
    

def authenticate_user(user, pas):
    if user.lower() in ["john","jane","brown","emily","david"] and pas == "":
        return True
    else:
        return False

Q={
    1:"Show user details",
    2:"Billing Issues",
    3:"Network Problems",
    5:"Plan Recommendations",
    6:"Usage Insights",
}

def ai_bot(choice, user):
    print(user,Q[choice])
    x=input("Describe your query : ")
    f=open("schema.txt","r")
    schema=f.read()
    user_message = f"give me only the sql query for the data required for answering the question : {x} from the Schema to table: {schema}"
    f.close()
    client = OpenAI(
	base_url="https://router.huggingface.co/novita",
	api_key=os.getenv("API_KEY")
    )
    messages = [
	{
		"role": "user",
		"content": user_message
	}]
    completion = client.chat.completions.create(
	model="deepseek/deepseek-r1", 
	messages=messages, 
	max_tokens=500,
)
    print(completion.choices[0].message)


if __name__ == "__main__":
    #print(show_tables())
    print("\t\t\t\tTeleco AI bot")
    user=input("Enter your user name: ")
    pas=input("Enter your password: ")
    if authenticate_user(user, pas):
        print("\t\t\t\tWelcome to Teleco AI bot")
        while True:
            print("-"*100)
            choice = int(input("""Enter your choice:
        1.Show user details
        2.Billing Issues
        3.Network Problems
        5.Plan Recommendations
        6.Usage Insights
        0.Exit
        """))
            match choice:
                case 1:
                    print("User details:")
                case 2:
                    print("Billing Issues:")
                case 3:
                    print("Network Problems:")
                case 5:
                    print("Plan Recommendations:")
                case 6:
                    print("Usage Insights")
                case 0:
                    print("Exiting...")
                    exit()
                case _:
                    print("Invalid choice")
            ai_bot(choice, user)
    else:
        print("Invalid credentials")
        exit()