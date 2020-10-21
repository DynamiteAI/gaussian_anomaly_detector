A collection of anomaly detectors integrated with the [dynamite_analyzer_framework](https://github.com/DynamiteAI/dynamite-analyzer-framework).


### Install

Install this analyzer by pointing the `anomaly-analyzer` root (where the `setup.py` is located.)

```
sudo python3 dynamite-analyzer.py "<path-to-project-root>/" install
```

### Uninstall
```
sudo python3 dynamite-analyzer.py "<path-to-project-root>/" uninstall
```

### Show Parameters

Show the default parameters (and their datatypes) available for this analyzer.
```
sudo python3 dynamite-analyzer.py <path-to-project-root>/ info
```

```
{
 "domain": {
  "value": "main",
  "datatype": "<class 'str'>"
 },
 "include_fields": {
  "value": [
   "uid",
   "community_id",
   "duration",
   "orig_bytes",
   "resp_bytes"
  ],
  "datatype": "<class 'tuple'>"
 },
 "load_model": {
  "value": true,
  "datatype": "<class 'bool'>"
 },
 "train_fields": {
  "value": [
   "duration",
   "orig_bytes",
   "resp_bytes"
  ],
  "datatype": "<class 'tuple'>"
 }
}

```

### Run Analyzer

```
sudo python3 dynamite-analyzer.py <path-to-project-root>/ run -i file --file /etc/dynamite/replays/zeek/ee7bddec94ff4f6f06154c70107c05da/conn.log -o console
```

### Run Analyzer With Custom Parameters

```
sudo python3 dynamite-analyzer.py <path-to-project-root>/ run -i file --file /etc/dynamite/replays/zeek/ee7bddec94ff4f6f06154c70107c05da/conn.log -o console --params '{"domain": "conn_log_test", "load_model": true}'
```

#### Sample Output:

```
{"dataset_name": "conn_log_test", "score": 1, "msg": "resp_bytes", "data_extra": {"score": 1, "reason": "resp_bytes", "uid": "CHownb1QzyZuxEBRX3", "community_id": "1:QYQcS4DKQSpzeaPiufQmpMO+BXg=", "duration": 20.558900117874146, "orig_bytes": 1175.0, "resp_bytes": 1400.0}}
{"dataset_name": "conn_log_test", "score": 1, "msg": "resp_bytes", "data_extra": {"score": 1, "reason": "resp_bytes", "uid": "C0FDzF3v2XI3P8A794", "community_id": "1:vF9mDeWx9pJ04HsMWfFZowO+FLw=", "duration": 231.62419390678406, "orig_bytes": 64.0, "resp_bytes": 23616.0}}
{"dataset_name": "conn_log_test", "score": 1, "msg": "duration", "data_extra": {"score": 1, "reason": "duration", "uid": "C48YJk1pvIZi6DrqG7", "community_id": "1:oEzHTPoHIvaNOBQ8mQrcIp33m54=", "duration": 175.64575695991516, "orig_bytes": 36368.0, "resp_bytes": 4800.0}}
{"dataset_name": "conn_log_test", "score": 1, "msg": "duration", "data_extra": {"score": 1, "reason": "duration", "uid": "C4wSINbSt5R22e46h", "community_id": "1:ckeIK8fkTQKFvCfaboRSjeEv//Y=", "duration": 189.67514300346375, "orig_bytes": 1820.0, "resp_bytes": 0.0}}
```