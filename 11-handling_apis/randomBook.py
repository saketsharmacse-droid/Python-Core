import requests

def get_random_books():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        get_data = data["data"]
        data_title = get_data["volumeInfo"]["title"]
        data_id = get_data["etag"]
        data_cat = get_data["volumeInfo"]["categories"]
        data_description = get_data["volumeInfo"]["description"]
        data_link = get_data.get("buyLink", "not Available")
    else:
        raise Exception("Failed to fetch your random book!!")
    
    return data_title, data_id, data_cat, data_description, data_link

def main():
    try:
        data_title, data_id, data_cat, data_description, data_link = get_random_books()
        if data_link == "not Available":
            print(f"Your Random Book Has Been Fetched!! \n**********************************\nBook Title: {data_title} \nBook id: {data_id} \nBook Category: {data_cat} \n\nBook Description: {data_description} \n\nPurchase Link: Not Available \n*********************************")
        else:
            print(f"Your Random Book Has Been Fetched!! \n\nBook Title: {data_title} \nBook id: {data_id} \nBook Category: {data_cat} \n\nBook Description: {data_description} \n\nPurchase Link: {data_link} \n*********************************")
    except Exception as e:
        print(str(e))
        
if __name__ == "__main__":
    main()