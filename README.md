# Redis active-passive test

Tests active passive replication between two redis clusters.
Write 1-100 values in source DB and read them backwards from destination DB.

## Usage

Install dependencies (just redis):

```sh
pip install -r requirements.txt
```

then

```sh
python3 redislabs_script.py --source_host SOURCE_HOST --source_port SOURCE_POST --dest_host DEST_HOST --dest_port DEST_PORT
```

For further information about usage run:

```sh
python3 redislabs_script.py -h
```
