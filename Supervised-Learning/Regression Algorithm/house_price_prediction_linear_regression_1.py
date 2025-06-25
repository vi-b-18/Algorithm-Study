"""
Algorithm 1: linear regression
keypoint:
 1. use to understand relationship between variables
 2. relationship between independent variable X and dependent variable Y
 3. goal is to find an optimal linear function, that is, to determine a set of coefficients (weights) so that the function can predict the value of the dependent variable as accurately as possible.
"""
from random import random

# linear regression to predict house price based on several factors
"""
identify variables 
        dependent variable : (Y) = price of house (hp)
        independent variables: { number of room(nr), house size (hs), has pool (p), location score(ls), garage capacity (gc)}
"""
# as usual set up the required library
from google import genai

# create your gemini client (* important)
client = genai.Client(api_key='AIzaSyCXoJST2quGI7rqfQbSgKZ6KpIzCjXOoKw')


# build your response model
def askQuest(userQuestion):  # method should take user prompt to process it as the content of the chat
    response = client.models.generate_content(
        model="gemini-2.5-flash",  # Specify you model as usual (each time you change model, change api key)
        contents=userQuestion  # user prompt/question passed to model to get the appropriate response
    )
    return response  # make the method return the response


# set a while loop to True so it runs indefinitely
while True:
    print(" To Exit the chat, type bye.")  # display your initial prompt message as if you are the bot, indicate user how to exit (type bye)
    query = input("ask me something: " + " ")  # let user input their question
    if query.lower() == "bye":   # verify if you want to exit the program
        break                   # if user has typed in bye, exit program
    else:                       # else display the response as indicated below
        print(askQuest(query).text)  # the .text return the text content of Bot response, and it is printed in your terminal
