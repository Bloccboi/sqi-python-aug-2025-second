def read_data(file_path):
    
    data = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                line = line.strip()
            
                if not line:
                    continue
                    
                parts = line.split(',')
                
                if len(parts) != 2:
                    print(f"Warning: Skipping line {line_number} - invalid format: {line}")
                    continue
                
                name = parts[0].strip()
                age_str = parts[1].strip()
                
                try:
                    age = int(age_str)
                    data.append((name, age))
                except ValueError:
                    print(f"Warning: Skipping line      {line_number} - invalid age: {age_str}")
                    continue
                    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    except Exception as e:
        raise ValueError(f"Error reading file '{file_path}': {str(e)}")
    
    return data