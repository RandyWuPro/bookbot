import sys
from stats import get_num_words, get_num_char, sort_on, sort_char_counts

# Function to retrieve the filepath and read the content within the file
def get_book_text(filepath):
    with open(filepath) as f:
        # f is a file object
        file_contents = f.read()
        return file_contents
            
def main():
    # Checks if sys.argv have two entries or not. Provide guidance if not.
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    else:   
        filepath = sys.argv[1]
        retrieved_content = get_book_text(filepath)
        
        # word count
        num_words = get_num_words(retrieved_content)
        
        # Character counts in dictionary
        char_counts = get_num_char(retrieved_content)
        
        # Sort charcter counts by frequency
        sorted_chars = sort_char_counts(char_counts)
        
        # Print Bookbot title
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        
        # Print Word Count
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        
        # Print character frequency
        print("--------- Character Count -------")
        for item in sorted_chars:
            char = item["char"]
            count = item["num"]
            if char.isalpha():
                print(f"{char}: {count}")
        
        # Print End
        print("============= END ===============")
main() 
