# lichess Backup Utility

TL;DR The program ```backup_studies_as_pgn_files.py``` can be used to archive [Lichess](https://lichess.org/) studies.

## Why

[Lichess](https://lichess.org/) allows users to create studies. These studies are divided into chapters. These chapters
must be backed up periodically by the user to ensure in the event of a loss that they may be restored.

Example Study: [Rook And Pawn Endgames: Introduction](https://lichess.org/study/dqCpuvFS)

## What

This code is responsible for collecting all chapters of a study from a provided HTML input. The Lichess site leverages an infinite scroll class that makes pure web scraping not possible without a makeshift browser such as Selenium. Hence, the code uses FireFox via Selenium to launch a browser, login, scroll to the bottom of the study page, and then download for each study.

## How
* Create\Modify a config file as ```config.ini``` to include the necessary login credentials leveraging the template as an example.
* Execute the ```backup_studies_as_pgn_files.py``` with no arguments required.

# Running 
## Prerequisites
This is Python 3 code. Install Python and configure a virtual environment using the provided ```requirements.txt``` file. Have geckodriver available in the path. 
 
## Output
**CONSOLE**
```bash
(1/3): Capturing study D0eFd0RV... COMPLETE!
(2/3): Capturing study aJKP9TlR... COMPLETE!
(3/3): Capturing study PIO0uVsE... COMPLETE!
...
```

**./out/manifest.csv**
```csv
0,D0eFd0RV,todoperososTestStudy,todoperoso's Test Study
1,aJKP9TlR,Gamestudy,Game study
2,PIO0uVsE,FunGame,Fun Game
...
```

**./out/ac6JRqJk_JomegaStudiesTableofContents.pgn**
```text
[Event "Jomega Studies Table of Contents: Introduction"]
[Site "https://lichess.org/study/ac6JRqJk/26zl81Aq"]
[Result "*"]
[UTCDate "2020.04.10"]
[UTCTime "09:51:27"]
[Variant "Standard"]
[ECO "?"]
[Opening "?"]
[Annotator "https://lichess.org/@/jomega"]

{ This study is a table of contents for all my Lichess studies.

My studies are extensively cross linked. Usually a top level study exists for a topic. For example, the Beginner Course. Hence, only those top level studies will be listed here.

The course studies have their own table of contents. }
 *


[Event "Jomega Studies Table of Contents: Beginner Course Studies"]
[Site "https://lichess.org/study/ac6JRqJk/ljRHcph3"]
[Result "*"]
[UTCDate "2020.04.10"]
[UTCTime "09:54:19"]
[Variant "Standard"]
[ECO "?"]
[Opening "?"]
[Annotator "https://lichess.org/@/jomega"]
[FEN "8/8/8/8/8/8/8/8 w - - 0 1"]
[SetUp "1"]

{ The top level study for the Beginner Course is here
https://lichess.org/study/Ztgx3vJq

Table of Contents is here
https://lichess.org/study/otqEtXkg }
 *

...
```