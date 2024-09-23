from datetime import datetime

AUTHOR = 'thiagoauler'
GITHUB = 'https://github.com/thiagoauler/MiSTer-Collections/raw/main/'

def process_record(output, record):
    global category
    global system
    if record.startswith('/'):
        record = record.removeprefix('/').split('/')
        category = record[0]
        if (len(record) > 1):
            system = record[1]
    else:
        output.write(f'[{category}/{record}]\n')
        output.write(f'system = {system}\n')
        output.write(f'match = {record}\n\n')

def process_collection(filename: str):
    # Open the collection file
    input = open(filename, 'r')
    # Create the sync conllection file
    sync = filename.replace('.txt', '.sync')
    output = open(sync, 'w')
    
    # Process the header
    name = input.readline().strip()
    url = f'{GITHUB}{sync}'
    updated = datetime.now().strftime('%Y-%m-%d %H:%M')

    output.write(f'name = {name}\n')
    output.write(f'author = {AUTHOR}\n')
    output.write(f'url = {url}\n')
    output.write(f'updated = {updated}\n\n')

    # Read all of its lines
    for record in input:
        if (record != '\n'):
            process_record(output, record.strip())
    
    # Close files
    input.close()
    output.close()

process_collection('my-favorites.txt')