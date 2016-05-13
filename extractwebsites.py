import json
from sys import argv

if len(argv) != 3:
    print 'Please key in the necessary inputs'
else:
    args_input = argv

    try:
        selected_file = open(argv[2])
    except:
        raise ValueError('Please key in location of the selected startups file')

    try:
        data_file = open(argv[1])
    except:
        raise ValueError('Please key in valid data file location')

    selected = list()
    for line in selected_file:
        selected.append(line.replace('\n', ''))
    selected_file.close()

    results = list()
    for line in data_file:
        rows = line.split('\t')
        if rows[0] in selected:
            data = json.loads(rows[8])
            for site in data['entity']['sites']:
                if site['site']['name'] == 'Website':
                    results.append((rows[0].decode('utf-8'), site['url'].decode('utf-8')))
                    break

    with open(argv[2].split('.')[0] + '_websites.csv', 'w') as f:
        for result in results:
            f.write(result[0].encode('utf-8') + '\t' + result[1].encode('utf-8') + '\n')
