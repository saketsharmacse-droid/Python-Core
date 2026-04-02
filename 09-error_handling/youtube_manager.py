import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            #print(type(test))
            return test
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)
        
    #finally

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    
    
    for index, video in enumerate(videos, start=1):
        
        print(f"{index}. {video['name']}, Duration: {video['time']} ")
        
    print("\n")
    print("*" * 70)
        
    


def add_video(videos):
    name = input("Enter Video Name: ")
    time = input("Enter Video Length: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)



def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter a video number to update: "))
    
    if 1<= index <= len(videos):
        name = input("Enter the new video Name: ")
        time = input("Enter the new video Time: ")
        videos[index-1] = {'name': name, 'time':time}
        save_data_helper(videos)
    else:
        print("Invalid Video Index Selected")
        


def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))
    
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("Successfully deleted!")
    else:
        print("Invalid Video Index Selected.")
        


def main():
    videos = load_data()

    while True:
        print("\n Youtube Manager | Choose an Option")
        print("1. List all YouTube Videos")
        print("2. Add a YouTube Video")
        print("3. Update a YouTube Video detail")
        print("4. Delete the YouTube Video")
        print("5. Exit the App")
        Choice = input("Enter your Choice: ")
        #print(videos)

        match Choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_videos(videos)
            case '5':
                print("Exit initiated...............!!")
                break
            case _:
                print("Invalid Choice! Please try again.")


if __name__ == "__main__":
    main()
#"__"is called dunden



#>>> list = [{'name': 'chai', 'time': '2mins'},{'name': 'code', 'time': '3mins'}]
#>>> for i in enumerate(list, start = 1):
#...  print(i)
#... 
#(1, {'name': 'chai', 'time': '2mins'})
#(2, {'name': 'code', 'time': '3mins'})
#>>> for i, video in enumerate(list, start=1): 
#...  print(f"{i}, {video['name']}")
#... 
#1, chai
#2, code
#>>>