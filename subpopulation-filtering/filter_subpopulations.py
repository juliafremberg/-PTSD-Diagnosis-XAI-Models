import json
import re
import csv

def load_patterns(patterns_file):
    with open(patterns_file, 'r') as f:
        return [line.strip() for line in f]

def filter_data(input_file, patterns):
    filtered_data = []
    pattern_counts = {pattern: 0 for pattern in patterns}  # Debugging: Track pattern matches
    with open(input_file, 'r') as f:
        for line in f:
            data = json.loads(line.strip())
            if 'control' in data.get('label', []):
                for post in data.get('posts', []):
                    if 'body' in post:
                        for pattern in patterns:
                            if re.search(pattern, post['body'], re.IGNORECASE):
                                filtered_data.append(data)
                                print(f'found {len(filtered_data)} matches')
                                pattern_counts[pattern] += 1  # Debugging: Increment pattern match count
                                if len(filtered_data) >= 300:  # Stop after 300 matches
                                    break
                        if len(filtered_data) >= 300:  # Stop after 300 matches
                            break
                if len(filtered_data) >= 300:  # Stop after 300 matches
                    break
    # Debugging: Log pattern match counts
    for pattern, count in pattern_counts.items():
        print(f"Pattern '{pattern}' matched {count} times")
    return filtered_data

def write_output_csv(output_file, data, max_users=1000):
    retained_users = min(len(data), max_users)
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['TID', 'text']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
       
        print(f'Retained Users: {retained_users}')
        writer.writeheader()
        user_count = 0  # Counter for the number of users written to the file
        for row in data:
            if user_count >= max_users:
                break
            for post in row.get('posts', []):
                if 'body' in post:
                    writer.writerow({'TID': row['id'], 'text': post['body']})
            user_count += 1
    return retained_users

def process_files(input_file, patterns_files, output_files):
    total_users = 0
    print("Starting process_files function")
    for patterns_file, output_file in zip(patterns_files, output_files):
        print(f"Loading patterns from {patterns_file}")
        patterns = load_patterns(patterns_file)
        print(f"{len(patterns)} patterns loaded")
        
        print(f"Filtering data from {input_file}")
        filtered_data = filter_data(input_file, patterns)
        retained_users = write_output_csv(output_file, filtered_data)
        
        print(f"{retained_users} rows matched the criteria for {patterns_file}")
        total_users += retained_users
    print(f"Total different users found: {total_users}")
    print("Finished process_files function")

def main():
    input_file = 'dev.jl'
    patterns_files = [
        'men_40_59_patterns.txt',
        'men_60_80_patterns.txt',
        'women_40_59_patterns.txt',
        'women_60_80_patterns.txt',
    ]
    output_files = [
        'controls_M_40_59.csv',
        'controls_M_60_80.csv',
        'controls_W_40_59.csv',
        'controls_W_60_80.csv',
    ]
    
    process_files(input_file, patterns_files, output_files)

if __name__ == "__main__":
    main()
