class Coach():
    """
    This class is a coach which allows you to query a database of 
    old questions you've had to answer for yourself. It's a way of
    outsourcing decision-making to a wiser you.

    The process goes as follows: I instantiate coach, and it asks me

    "What do you need advice on?"

    At this point, I provide a question, and the coach class runs 
    a query on my local database of former questions asked. If I've 
    asked the question before, then a match will be given. 
    """
    def __init__(self):
        print("Hi, I'm coach!")

    def ask_question(self):
        """
        This method is for users to ask coach a question
        """
        val = input('What is your question?')
        print(val)



if __name__=="__main__":
    
    c = Coach()
    c.ask_question()
    