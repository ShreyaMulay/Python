import pandas as pd
import time


def load_responses_from_csv(file_path):
    df = pd.read_csv(file_path)
    responses = dict(zip(df['user_input'].str.lower(), df['bot_response']))
    # Load whole csv data initialyy as a dictionary format
    # print("responses",responses)
    return responses

def chatbot_response(user_input, responses):
    user_input = user_input.lower()
    # print(":user_input",user_input)
    return responses.get(user_input, "I'm sorry, I don't understand that. Can you rephrase?")

def chat_with_bot(responses):
    print("Hello! I'm a pandas-based chatbot. Type 'quit' to exit.")
    fp = open('chatBot.txt', "a")
    separator = "_"* 70
    fp.write(separator + "\n")
    fp.write("Chat log" + "\n")
    fp.write("LOG file created as "+ time.ctime() + "\n")
    fp.write(separator + "\n")
    
    fp.write("CONTENT OF FILE ARE :" +"\n")
    fp.write(separator + "\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            fp.write("You :quit")
            fp.write("\nChatbot :Goodbye")
            break

        response = chatbot_response(user_input, responses)
        print(f"Chatbot: {response}")
      
        fp.write("You :")
        fp.write("%s \n" %user_input)

        fp.write("Chatbot :")
        fp.write("%s \n" %response)

        fp.write(separator + "\n")
    fp.close()


# Load responses from the CSV file using pandas
responses = load_responses_from_csv('response.csv')

# Start the chat
chat_with_bot(responses)
