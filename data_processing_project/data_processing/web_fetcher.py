import requests

def fetch_user_data():
  
    api_url = "https://jsonplaceholder.typicode.com/users"
    
    try:
      
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()  
        
       
        users = response.json()
        
        user_names = []
        for user in users:
            if 'name' in user:
                user_names.append(user['name'])
            else:
                print(f"Warning: User missing 'name' field: {user}")
        
        return user_names
        
    except requests.exceptions.Timeout:
        raise requests.RequestException("Request timed out while fetching user data")
    except requests.exceptions.ConnectionError:
        raise requests.RequestException("Connection error while fetching user data")
    except requests.exceptions.HTTPError as e:
        raise requests.RequestException(f"HTTP error while fetching user data: {e}")
    except requests.exceptions.RequestException as e:
        raise requests.RequestException(f"Error fetching user data: {e}")
    except ValueError as e:
        raise ValueError(f"Error parsing API response: {e}")
    except Exception as e:
        raise ValueError(f"Unexpected error while fetching user data: {e}")
