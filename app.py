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



if __name__ == "__main__":
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