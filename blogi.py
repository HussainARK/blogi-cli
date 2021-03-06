import urllib.request, getpass, os, json

# api_url is the API URL :)
api_url = "https://blogi-backend.herokuapp.com"

# ANSIColors which is the ANSI Color Codes for Coloring Terminal Text
class ANSIColors:
    CEND      = '\33[0m'
    CBOLD     = '\33[1m'
    CITALIC   = '\33[3m'
    CURL      = '\33[4m'
    CBLINK    = '\33[5m'
    CBLINK2   = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK  = '\33[30m'
    CRED    = '\33[31m'
    CGREEN  = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE   = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE  = '\33[36m'
    CWHITE  = '\33[37m'

    CBLACKBG  = '\33[40m'
    CREDBG    = '\33[41m'
    CGREENBG  = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG   = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG  = '\33[46m'
    CWHITEBG  = '\33[47m'

    CGREY    = '\33[90m'
    CRED2    = '\33[91m'
    CGREEN2  = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2   = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2  = '\33[96m'
    CWHITE2  = '\33[97m'

    CGREYBG    = '\33[100m'
    CREDBG2    = '\33[101m'
    CGREENBG2  = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2   = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2  = '\33[106m'
    CWHITEBG2  = '\33[107m'

# connect() function for connecting and Authenticating the User.
def connect():
    global key
    key = getpass.getpass("Enter the API Key: ", stream=None)

    print(f"{ANSIColors.CYELLOW}Fetching the API...{ANSIColors.CEND}\n")
    
    response = urllib.request.urlopen(f'{api_url}/posts?key={key}').read().decode()
    
    if response == "Error: API Key is missing":
        print(f"{ANSIColors.CRED}The API Key is Wrong{ANSIColors.CEND}\n")
        return False
    else:
        print(f"{ANSIColors.CGREEN}Authenticated Successfuly{ANSIColors.CEND}\n")
        return True

try:
    os.system('cls')

    command = ''

    print("""\
Welcome to the Blogi CLI Program!

This Python Program is used to interact with the Blogi API

You just need to type some Commands to get Started!

Type "help" to get Started.
        """)

    while command.lower() != "quit":
        command = input("Blogi> ")

        if command.lower() == 'getposts':
            if connect():
                print(f"{ANSIColors.CYELLOW}Connecting to the API...{ANSIColors.CEND}\n")
                
                response = urllib.request.urlopen(f'{api_url}/posts?key={key}').read().decode()
                
                dict_response = json.loads(response)

                print(f"{ANSIColors.CGREEN}Connected!{ANSIColors.CEND}\n")

                if dict_response != []:
                    print("______________________________________________")
                    print("|  Post ID  |  Title  |  Author  |  Content  |")
                    print("|--------------------------------------------|")
                    for post in dict_response:
                        print("|  " + str(post.get('bid')) + "  |  " + post.get("title") + "  |  " + post.get("author") + "  |  " + post.get("content") + "  |")
                    
                    print("|--------------------------------------------|\n")
                else:
                    print(f"There are no Posts Right Now.\n")
            else:
                continue
        
        elif command.lower() == "createpost":
            if connect():
                post_title = input("Post Title: ")
                post_author = input("Post Author: ")
                post_content = input("Post Content: ")
                print(f"{ANSIColors.CYELLOW}Connecting to the API...{ANSIColors.CEND}\n")

                data = {"title": post_title, "author": post_author, "content": post_content}
                headers = {"Content-Type": "application/json"}
                
                dict_data = json.dumps(data)

                request = urllib.request.Request(
                    f'{api_url}/posts?key={key}', 
                    data=bytes(dict_data.encode('utf-8')), 
                    headers=headers, 
                    method="POST"
                )
                
                response = urllib.request.urlopen(request).read().decode()
                
                print(f"{ANSIColors.CGREEN}Connected!{ANSIColors.CEND}\n")
                print(f"{response}\n")
            else:
                continue

        elif command.lower() == "editpost":
            if connect():
                selected_post_id = int(input("Enter the Post ID of the Post: "))
                
                new_post_title = input("Post new Title: ")
                new_post_author = input("Post new Author: ")
                new_post_content = input("Post new Content: ")
                print(f"{ANSIColors.CYELLOW}Connecting to the API...{ANSIColors.CEND}\n")

                data = {"title": new_post_title, "author": new_post_author, "content": new_post_content}
                headers = {"Content-Type": "application/json"}
                
                dict_data = json.dumps(data)

                request = urllib.request.Request(
                    f'{api_url}/posts/{str(selected_post_id)}?key={key}', 
                    data=bytes(dict_data.encode('utf-8')), 
                    headers=headers, 
                    method="PUT"
                )

                response = urllib.request.urlopen(request).read().decode()

                print(f"{ANSIColors.CGREEN}Connected!{ANSIColors.CEND}\n")
                print(f"{response}\n")
            else:
                continue

        elif command.lower() == "deletepost":
            if connect():
                selected_post_id = int(input("Enter the Post ID of the Post: "))
                print(f"{ANSIColors.CYELLOW}Connecting to the API...{ANSIColors.CEND}\n")
                request = urllib.request.Request(
                    f'{api_url}/posts/{str(selected_post_id)}?key={key}', 
                    method="DELETE"
                )

                response = urllib.request.urlopen(request).read().decode()

                print(f"{ANSIColors.CGREEN}Connected!{ANSIColors.CEND}\n")
                print(f"{response}\n")
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
            print(f'{ANSIColors.CRED}"{command}" is not a Valid Command{ANSIColors.CEND}')
except:
    print(f"{ANSIColors.CRED}Error!{ANSIColors.CEND}")
    quit()
