with open('task2.txt', 'r') as f:
    file_content = f.readlines()
    print(f'Count of words: {[len(a.split()) for a in file_content]}\n'
          f'Total number of lines: {len(file_content)}')
