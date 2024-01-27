# NomanBot.py

import g4f as noman
import re
import time

def response(message):
    # Check if the message is empty or consists only of whitespace characters
    if not message.strip():
        return "Don't send an empty message"
    
    # Remove unnecessary symbols from the message
    cleaned_message = remove_unnecessary_symbols(message)
    
    # Check if the cleaned message is empty or consists only of whitespace characters
    if not cleaned_message.strip():
        return "Don't send an empty message"
    
    # Perform the response generation with the cleaned message and handle timeout
    try:
        start_time = time.time()
        response = noman.ChatCompletion.create(
            model=noman.models.default,
            messages=[{"role": "user", "content": cleaned_message}],
            proxy="http://host:port",
            timeout=120,
        )
        end_time = time.time()
        
        # Check if the response time exceeds a specified limit (e.g., 10 seconds)
        if end_time - start_time > 120:
            return "Sorry, I couldn't understand your message within the time limit."
        
        return response
    except Exception as e:
        # Handle exceptions, e.g., timeout or other errors
        print(f"Error: {e}")
        return "An error occurred during response generation."

def remove_unnecessary_symbols(message):
    # Define a regular expression pattern to match unnecessary symbols
    pattern = re.compile('[^a-zA-Z0-9\s]')
    
    # Use the pattern to replace unnecessary symbols with an empty string
    cleaned_message = re.sub(pattern, '', message)
    
    return cleaned_message
