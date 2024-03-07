import requests

# Function to check the status of a website
def check_website_status(url):
    try:
        # Attempt to get the URL, with a timeout of 10 seconds to avoid hanging
        response = requests.get(url, timeout=10)
        # If the status code is 200, the site is up
        if response.status_code == 200:
            return True, ""
        else:
            # If the status code is not 200, return False and the status code
            return False, f"with status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        # If an exception occurs (like a connection error), return False and the error
        return False, f"with error: {e}"

# The main function where we check the status of Instagram and Facebook
def main():
    # Dictionary of the websites we want to check
    websites = {
        "Instagram": "https://www.instagram.com/",
        "Facebook": "https://www.facebook.com/",
        "Youtube": "https://www.youtube.com/"       
    }
    
    # Loop through the websites and check their status
    for name, url in websites.items():
        is_up, message = check_website_status(url)
        # Print a clean status message, adding the error message if there is one
        status = "is up and running!" if is_up else f"is down {message}"
        print(f"{name} {status}")

# Standard boilerplate to run the main function
if __name__ == "__main__":
    main()
