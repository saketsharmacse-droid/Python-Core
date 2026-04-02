#we will use an opensource project called freeapi.app for free predefined api's
import requests

def fetch_random_user():
    url_chai = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url_chai)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch user data")
    
    
    
def main():
    try:
        username, country = fetch_random_user()
        print(f"Username:{username} \nCountry: {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
        
#read about post get methods