# entry-point
Command line Python program used to create, organize, and manage daily digital 
journal entries in markdown format. 

## Motivation
I've found that writing thoughts down in an unstructured, non-goal oriented way 
before starting work increases my focus. Allowing a computer to store thoughts 
as they arise keeps me on track. Archiving thoughts in txt/md format is
also valuable for analysis at a later date if desired. This program was created
to allow me to quickly access my digital journal from any terminal.

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


