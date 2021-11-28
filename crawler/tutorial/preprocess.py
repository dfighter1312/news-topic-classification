with open('links.txt','r') as textfile:
    lines = textfile.readlines()
    with open('filtered_links.txt','w') as writefile:
        for line in lines:
            if line[:5] != 'https' or len(line) < 30:
                continue
            html_pos = line.find('html')
            if html_pos == -1:
                continue
            writefile.write(f'{line[:html_pos]}html\n')