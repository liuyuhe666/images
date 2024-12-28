import json

with open('package.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
current_version = data['version']
major, minor, patch = map(int, current_version.split('.'))
patch += 1
new_version = f'{major}.{minor}.{patch}'
data['version'] = new_version
with open('package.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f'version: {current_version}')
