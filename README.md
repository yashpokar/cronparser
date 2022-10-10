# Cron Parser

Simple cron parser

## Requirements

- Python 3.6+ is required.
- `pip` command should be available.

## Installation

```bash
git clone git@github.com:yashpokar/cronparser.git
```

```bash
cd cronparser
```

```bash
pip install .
```


## Usage

```bash
parsecron "*/15 0 1,15 * 1-5 /usr/bin/find"
```

Sample output
```
minute         0 15 30 45
hour           0
month          1 2 3 4 5 6 7 8 9 10 11 12
day of week    1 15
command        /usr/bin/find
```
