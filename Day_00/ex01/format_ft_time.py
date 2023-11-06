from datetime import datetime

# Define a function to format current time and date
def format_time_date():
    # Get the current timestamp
    current_timestamp = datetime.now().timestamp()
    
    # Formatting timestamp
    formatted_timestamp = f"Seconds since January 1, 1970: {current_timestamp:,.4f} or {current_timestamp:.2e} in scientific notation"
    
    # Formatting current date
    formatted_date = datetime.now().strftime("%b %d %Y")
    
    return formatted_timestamp, formatted_date

# Call the function and print formatted time and date
formatted_timestamp, formatted_date = format_time_date()
print(formatted_timestamp)
print(formatted_date)