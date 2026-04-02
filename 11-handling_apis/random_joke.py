import requests

def random_jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        joke = user_data["content"]
        joke_id = user_data["id"]
        return joke, joke_id
    else:
        raise Exception("Failed to fetch a Random Joke")
    
def main():
    try:
        joke, joke_id = random_jokes()
        print(f"Your Random Joke is: \n{joke} \nJoke id is: {joke_id}  \n***Laugh out Loud***")
    except Exception as e:
        print(str(e))
        

if __name__ == "__main__":
    main()
    