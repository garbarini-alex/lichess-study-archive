#lichess Backup Utility

TL;DR The program ```backup_studies_as_pgn_files.py``` can be used to archive [Lichess](https://lichess.org/) studies.

##Why

[Lichess](https://lichess.org/) allows users to create studies. These studies are divided into chapters. These chapters
must be backed up periodically by the user to ensure in the event of a loss that they may be restored.

Example Study: [Rook And Pawn Endgames: Introduction](https://lichess.org/study/dqCpuvFS)

##What

This code is responsible for calling their internal [API](https://lichess.org/api) to collect all chapters of a study from a provided HTML input. The HTML is extracted from a browser manually by a user before execution. The Lichess site leverages an infinite scroll class that makes pure web scraping not possible without a makeshift browser such as Selenium.

##How
* Go to the [Lichess Studies Section](https://lichess.org/study/by/jomega)
* Scroll to the bottom such that all studies available are displayed (click the ellipse at the bottom if it appears)
* Using your specific browser function, select all HTML code used to render the page.
* Convert the HTML into UTF-8 or ANSI encoding
* Replace the variable HTML_CODE_TO_REPLACE with the fresh HTML code
* Execute the ```backup_studies_as_pgn_files.py``` with no arguments required

# Running 
##Prerequisites
This is Python 3 code. Install Python and configure a virtual environment using the provided ```requirements.txt``` file. Try running the ```test.py``` to validate all requirements are met and execution is good to go. 
 
##Output
**CONSOLE**
```bash
(1/104): COMPLETED capture for study ac6JRqJk
(2/104): COMPLETED capture for study JZmdj8VM
...
```

**./out/manifest.csv**
```csv
0,ac6JRqJk,ac6JRqJk_JomegaStudiesTableofContents.pgn,Jomega Studies Table of Contents
1,JZmdj8VM,JZmdj8VM_Gamestudy.pgn,Game study
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

#TODO

* Implement Selenium to avoid HTML manual copy hassle