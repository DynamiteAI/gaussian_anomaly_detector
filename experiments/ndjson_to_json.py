import json
with open('detections_001.ndjson') as f:
    parsed = []
    for line in f.readlines():
        parsed.append(json.loads(line)['data_extra'])

print(parsed)