from data_processing import read_data, fetch_user_data

def main():
    print("=" * 60)
    print("Data Processing Project")
    print("=" * 60)
    
    data_file = "data.txt"
    
    try:
        print("\n1. Reading data from file...")
        print(f"Reading from: {data_file}")
        
        file_data = read_data(data_file)
        
        print(f"\nData from file ({len(file_data)} records):")
        print("-" * 30)
        for name, age in file_data:
            print(f"{name}: {age} years old")
       
        if file_data:
            ages = [age for name, age in file_data]
            avg_age = sum(ages) / len(ages)
            min_age = min(ages)
            max_age = max(ages)
            
            print(f"\nFile Data Statistics:")
            print(f"Average age: {avg_age:.1f}")
            print(f"Age range: {min_age} - {max_age}")
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please make sure 'data.txt' exists in the current directory.")
        return
    except Exception as e:
        print(f"Error reading file data: {e}")
        return
    
    try:
        print("\n2. Fetching data from web API...")
        print("Connecting to JSONPlaceholder API...")
        
        web_data = fetch_user_data()
        
        print(f"\nData from web API ({len(web_data)} users):")
        print("-" * 40)
        for i, user_name in enumerate(web_data, 1):
            print(f"{i}. {user_name}")
    
    except Exception as e:
        print(f"Error fetching web data: {e}")
        print("Please check your internet connection and try again.")
        return
    
    print("\n3. Data Comparison:")
    print("-" * 30)
    print(f"File data: {len(file_data)} records")
    print(f"Web API data: {len(web_data)} records")
    
    file_names = [name for name, age in file_data]
    matching_names = set(file_names) & set(web_data)
    
    if matching_names:
        print(f"Matching names found: {', '.join(matching_names)}")
    else:
        print("No matching names found between file and API data")
    
    print("\n" + "=" * 60)
    print("Project completed successfully!")

if __name__ == "__main__":
    main()
