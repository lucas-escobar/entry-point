# entry-point
Python program used to create, organize, and manage daily digital journal 
entries. Designed to be a minimalist, command-line focused program.

## Motivation

Writing thoughts down in an unstructured, non-goal oriented way before starting 
computer-related work can increase focus. Allowing your computer to hold
what is in your mind can help unload. Archiving thoughts in text format is
also valuable for analysis at a later date if desired.

## Usage
1. Clone repository
2. Edit `data_path` in `config/config.ini` to point to where journal entries 
are to be stored
3. `cd` to project directory
5. Call `python main.py -w` to create a new journal entry for the current day

## Arguments
`python main.py --help` outputs:
```buildoutcfg
usage: entry-point [-h] [-w] [-r [READ ...]] [-d DIRECTORY]

Command line program that creates, organizes, and manages daily journal entries.

optional arguments:
  -h, --help            show this help message and exit
  -w, --write           Create and open a new entry file with the current date. 
                        If an entry for the current date exists, the file is 
                        opened.
  -r [READ ...], --read [READ ...]
                        Read entries in specified date range. Range can be 
                        relative to current date (read past 3 entries: [3]) or 
                        absolute (read entries from 2022-01-01 to 2023-01-01: 
                        ['2022-01-01', '2023-01-01'])
  -d DIRECTORY, --directory DIRECTORY
                        Specify directory in which to store journal entries
```

## Development
For notes relating to development, see [dev docs](./docs/dev.md)


