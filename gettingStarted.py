def welcome_assignment_answers(question):
    # Students do not have to follow the skeleton for this assignment.
    # Another way to implement is using a "case" statements similar to C.
    
    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "pcap"
        
    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
        
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
        
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
        
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
        
    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        # IMPORTANT: Replace the string below with your actual SHA256 hash!
        answer = "5be8afabf868b693bd7ab32b33d1ab6de75886328edb5ad4febec59b61122db0" 
        
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
        
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        # In the 5-layer TCP/IP model, Application is Layer 5. 
        # (Note: If your course specifically uses the OSI model for layer numbers, this would be 7).
        answer = 5 
        
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        # In both the 5-layer TCP/IP model and OSI model, the Network/Internet layer is Layer 3.
        answer = 3
        
    else: 
        ### you should understand why this else case should be included
        ### what happens if there is a typo in one of the questions?
        ### maybe put something here to flag an issue and catch errors
        answer = "This is not my beautiful wife! This is not my beautiful car! How did I get here?"
        
    return answer

# Complete all the questions.

if __name__ == "__main__":
    # use this space to debug and verify that the program works
    debug_question = "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number"
    print(welcome_assignment_answers(debug_question))
