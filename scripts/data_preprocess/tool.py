import json

path = 'textonly_oasst1_data_33919.json'
save_path = 'textonly_oasst1_data_33919.json'
data = json.load(open(path))

print(len(data['instances']), data['type'])
for i in range(len(data['instances'])):
    text = data['instances'][i]['text']
    text = text.replace('\nHuman:', ' ###Human:')
    text = text.replace('\nAssistant:', ' ###Assistant:')
    text = '###' + text
    # print(text)
    data['instances'][i]['text'] = text
    # print(i, data['instances'][i])
json.dump(data, open(save_path, 'w'))