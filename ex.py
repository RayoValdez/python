def count_characters(word):
    return len(word)

def main():
    words = ["codeing", "python", "I know what I do and I enjoy", "hire me and you won't regret"]

    for word in words:
        char_count = count_characters(word)
        print(f'The word "{word}" has {char_count} characters.')

if __name__ == "__main__":
    main()

