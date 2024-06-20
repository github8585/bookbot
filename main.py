def count_words_in_file(path_to_file):
    try:
        with open(path_to_file) as f:
            content = f.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"File not found: {path_to_file}")
        return None
    except IOError as e:
        print(f"IOError: {e}")
        return None

def count_characters(text):
    char_count = {}
    text = text.lower()
    
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count

def generate_report(path_to_file):
    try:
        with open(path_to_file) as f:
            text = f.read()
    except FileNotFoundError:
        print(f"File not found: {path_to_file}")
        return None
    except IOError as e:
        print(f"IOError: {e}")
        return None
    
    word_count = count_words_in_file(path_to_file)
    if word_count is not None:
        print(f"--- Begin report of {path_to_file} ---")
        print(f"{word_count} words found in the document\n")

        # Count characters
        character_counts = count_characters(text)

        # Sort character counts by frequency
        sorted_characters = sorted(character_counts.items(), key=lambda x: x[1], reverse=True)

        # Print character counts
        for char, count in sorted_characters:
            print(f"The '{char}' character was found {count} times")
        
        print("--- End report ---")

# Example usage:
path_to_file = 'books/frankenstein.txt'
generate_report(path_to_file)
