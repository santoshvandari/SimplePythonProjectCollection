import requests

def getdata(url:str):
    htmldata= requests.get(url)
    if htmldata.status_code == 200:
        htmldata= htmldata.text
        try:
            title= (htmldata.split('<title>')[1].split('</title>')[0]).strip()
        except:
            title= "No Title Found"
        try: 
            description=(htmldata.split('<meta name="description" content="')[1].split('">')[0]).strip()
        except:
            description= "No Description Found"
        try: 
            htmlcontent= (htmldata.split('<body>')[1].split('</body>')[0]).strip()
        except:
            htmlcontent= "No HTML Content Found"
        return [title, description, htmlcontent]

def main():
    url = (str(input("Enter a URL(Leave Empty for Quit): "))).strip()
    if url:
        if url.__contains__("http://") or url.__contains__("https://") and url.__contains__(".com"):
            [title,description,htmlcontent]= getdata(url)
            print("Title: ", title)
            print("Description: ", description)
            print("HTML Content: ", htmlcontent)
        else:
            print("Invalid URL")
    else:
        exit(0)


if __name__ == "__main__":
    while(True):
        main()