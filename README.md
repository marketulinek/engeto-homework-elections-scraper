# Elections Scraper
Homework for Python Academy - Elections Scraper

## Description
Scraping the results from parliamentary elections in Czech Republic (2017). Link [here](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).

## Installing
```
pip install -r requirements.txt
```

## Run the project
```
python main.py <target-url> <file-name-with-results>
```

## Example
First argument: ``` https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103 ```

Second argument: ``` vysledky_prostejov.csv ```

Running the command:
```
python main.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103' 'vysledky_prostejov.csv'
```

Download progress:
```
DOWNLOADING DATA FROM URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
SAVING TO FILE: vysledky_prostejov.csv
ENDING main.py
```

Partial output:
```
code, location, registered, envelopes, valid, ...
506761, Alojzov, 205, 145, 144, ...
589268, Bedihošť, 834, 527, 524, ...
```
