import requests 

def fetch_user_data():
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Check your internet connection?")
        print("More details:")
        print(e)
    else:
        status_code = response.status_code
        if status_code != 200:
            print(f"Status Code: {status_code}")
            print("Unexpected response:")
            print(response.text)
            return
        user_data = response.json()
        return [data['username'] for data in user_data]
    
if __name__ == "__main__":
    print(fetch_user_data())