# Development docs
Document to facilitate ongoing or frequently updated notes relating to 
development.

## Functional requirements

### Core
* create and open (with text editor) new markdown file with current date in 
title or header
* calling entry-point will cd to journal directory
* organize folders by year > month > week > day
* view combination of entries from a specified date range (in full form 
or header-only format)
* search entries for strings (fuzzy?)

### Stretch
* integration with todo list subsystem
* sentiment analysis on each journal entry to assess mood
* implement topic identifier (classifier)
* display visual representation of stoic calendar

## TODO
* create functionality to view entries in absolute mode
* restructure `tests` directory. This dir is currently experimental and not
used.
