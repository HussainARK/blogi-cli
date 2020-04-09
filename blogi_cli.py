import requests
import os
import getpass

api_url = 'https://blogi-backend.herokuapp.com'

def connect():
    global key
    key = getpass.getpass("Enter the API Key: ", stream=None)

    response = requests.get(api_url + "/posts?key={}".format(key)).text

    if response == "Error: API Key is missing":
        print("The API Key is Wrong\n")
        return False
    else:
        print("Authenticated Successfuly\n")
        return True

try:
    command = ''

    print("""\
Welcome to the Blogi CLI Program!

This Python Program is used to interact aith the Blogi API

You just need to type some Commands to get Started!

Type "help" for Help.
        """)

    while command.lower() != "quit":
        command = input("Blogi> ")

        if command.lower() == 'getposts':
            if connect():
                response = requests.get(api_url + "/posts?key={}".format(key)).json()
                print("Connecting...\n")

                if response != []:
                    print("______________________________________________")
                    print("|  Post ID  |  Title  |  Author  |  Content  |")
                    print("|--------------------------------------------|")
                    for post in response:
                        print("|  " + str(post.get('bid')) + "  |  " + post.get("title") + "  |  " + post.get("author") + "  |  " + post.get("content") + "  |")
                    
                    print("|--------------------------------------------|")
                    print("")
                else:
                    print("There are no Posts Right Now.\n")
            else:
                continue
        
        elif command.lower() == "createpost":
            if connect():
                post_title = input("Post Title: ")
                post_author = input("Post Author: ")
                post_content = input("Post Content: ")
                print("Connecting...\n")

                response = requests.post(url=(api_url + "/posts?key={}".format(key)), json={'title': post_title, 'author': post_author, 'content': post_content}).text
                print(response)
            else:
                continue

        elif command.lower() == "editpost":
            if connect():
                selected_post_id = int(input("Enter the Post ID of the Post: "))
                
                post_new_title = input("Post new Title: ")
                post_new_author = input("Post new Author: ")
                post_new_content = input("Post new Content: ")
                print("Connecting...\n")

                response = requests.put(url=(api_url + "/posts/{}?key={}".format(str(selected_post_id), key)), json={'title': post_new_title, 'author': post_new_author, 'content': post_new_content}).text
                print(response)
            else:
                continue

        elif command.lower() == "deletepost":
            if connect():
                selected_post_id = int(input("Enter the Post ID of the Post: "))
                print("Connecting...\n")

                response = requests.delete(url=(api_url + "/posts/{}?key={}".format(str(selected_post_id), key))).text
                print(response)
            else:
                continue

        # Other commands

        elif command.lower() == 'whatisthis':
            print("This is Blogi CLI!")

        elif command.lower() == "help":
            print("""\
This is the Windows Command Line Tool for Interacting with the Blogi RESTful API,

Playing with the API:
    getposts - returns all the Blog Posts as a Table
    createpost - creates a Blog Post
    editpost - edits a Specific Blog Post
    deletepost - deletes a Specific Blog Post

Other:
    help - prints this Message
    whatisthis - *Try Yourself :)*
    clear - clears the Screen
    quit - exits the Program
            """)

        elif command.lower() == "clear":
            os.system("cls")

        elif command.lower() == "quit":
            break

        elif command.lower() == "":
            continue

        else:
            print(f'"{command}" is not a Valid Command')
except:
    print("Error!")
    quit()
