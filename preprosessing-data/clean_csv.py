import re
import csv

def preprocess_text(text):
    # Lowercasing Text
    text = text.lower()
    
    # Removing Hyperlinks
    text = re.sub(r'https?://\S+', '', text)
    
    # Removing HTML Tags
    text = re.sub(r'<.*?>', '', text)
    
    # Removing User Mentions
    text = re.sub(r'@\w+', '', text)
    
    # Removing HTML Entities
    text = re.sub(r'&\w+;', ' ', text)
    
    # Processing Hashtags
    text = re.sub(r'#(\w+)', r'\1', text)
    
    # Preserving Certain Characters and Whitespace
    text = re.sub(r'[^a-zA-Z0-9\s\.\'\!\?\,\;\-]', ' ', text)
    
    # Normalizing Spaces and Punctuation
    text = re.sub(r'(?<=[.,!?])(?=[^\s])', r' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'(\.|\!|\?|\,|\;)\1+', r'\1', text)  # Deduplicate sentence-ending symbols
    text = re.sub(r'\.{3,}', '.', text)  # Replace consecutive ellipsis with a single full stop
    text = text.strip()
    text = re.sub(r'(?<=\w)([.,;])(?=\S)', r'\1 ', text)
    
    # Ensure post ends with a full stop if it doesn't end with a sentence-ending symbol
    if not re.search(r'[.!?]$', text):
        text += '.'
    
    return text

def process_files(input_files, output_files):
    for input_file, output_file in zip(input_files, output_files):
        with open(input_file, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            # Skip the first row
            next(reader)
            # Read the actual column names from the second row
            fieldnames = next(reader)
            
            if 'TID' not in fieldnames or ('Text' not in fieldnames and 'text' not in fieldnames):
                print(f"Columns 'TID' or 'Text/text' not found in {input_file}. Available columns: {fieldnames}")
                continue

            tid_index = fieldnames.index('TID')
            text_index = fieldnames.index('Text') if 'Text' in fieldnames else fieldnames.index('text')

            rows = []
            for row in reader:
                if row:  # Ensure the row is not empty
                    cleaned_text = preprocess_text(row[text_index])
                    if cleaned_text:  # Ensure the cleaned text is not empty
                        rows.append({'TID': row[tid_index], 'text': cleaned_text})
            
            with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=['TID', 'text'])
                writer.writeheader()
                writer.writerows(rows)
                print(f"Cleaned data written to {output_file}")

def main():
    input_files = [
        'filtered_data_M_18_24.csv',
        'filtered_data_M_25_39.csv',
        'filtered_data_M_40_59.csv',
        'filtered_data_W_18_24.csv',
        'filtered_data_W_25_39.csv',
        'filtered_data_W_40_59.csv',
        'filtered_data_W_60_80.csv',
    ]
    
    output_files = [
        'cleaned_filtered_data_M_18_24.csv',
        'cleaned_filtered_data_M_25_39.csv',
        'cleaned_filtered_data_M_40_59.csv',
        'cleaned_filtered_data_W_18_24.csv',
        'cleaned_filtered_data_W_25_39.csv',
        'cleaned_filtered_data_W_40_59.csv',
        'cleaned_filtered_data_W_60_80.csv',
    ]
    
    process_files(input_files, output_files)

if __name__ == "__main__":
    main()
