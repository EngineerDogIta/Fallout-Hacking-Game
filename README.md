## Istruzioni per l'Installazione e l'Esecuzione del Gioco

### Prerequisiti
Assicurati di avere installato Python 3.x sul tuo sistema. Puoi scaricarlo e installarlo dal sito ufficiale di [Python](https://www.python.org/).

### Installazione
1. Clona questo repository sul tuo computer:
    ```sh
    git clone https://github.com/tuo-username/Fallout-Hacking-Game.git
    ```
2. Naviga nella directory del progetto:
    ```sh
    cd Fallout-Hacking-Game
    ```

### Configurazione
Puoi personalizzare il gioco modificando i seguenti parametri nel file config.json:
```python
NAME_FILE = "wordListItaliano.txt"
EFFECT_WAIT_SEC = 0.1
MAX_NUM_WORD = 10
MIN_NUM_WORD = 4
LENGHT_PER_WORD = 5
DIFFICULTY = 2 # NEVER MAKE THIS VALUE 0 I REPEAT NEVER!!!
```
- `NAME_FILE`: Nome del file contenente la lista delle parole da utilizzare nel gioco.
- `EFFECT_WAIT_SEC`: Tempo di attesa per la stampa di ogni linea nella console. Imposta a 0 per visualizzare immediatamente tutte le parole.
- `MAX_NUM_WORD`: Numero massimo di parole che il gioco può prendere casualmente.
- `MIN_NUM_WORD`: Numero minimo di parole che il gioco può prendere casualmente.
- `LENGHT_PER_WORD`: Lunghezza di ogni parola generata.
- `DIFFICULTY`: Difficoltà del gioco, che determina il numero di tentativi disponibili. 1 è il più facile e corrisponde al numero di parole generate, 2 dimezza il numero di tentativi, e così via.

### Esecuzione del Gioco
Per avviare il gioco, esegui il seguente comando nella console:
```sh
python main.py
```

### Cambiare Lingua
Per cambiare la lingua del gioco, crea un file di testo con una lista di parole nella lingua desiderata e aggiorna il parametro `NAME_FILE` nel file main.py con il nome del nuovo file.

### Note Legali
Non possiedo il marchio della serie Fallout, questo è solo un fan-game che riproduce quella parte del gioco. Tutto il codice all'interno è stato scritto a mano.
```

Aggiungi questa sezione al tuo `README.md` per fornire istruzioni più dettagliate su come configurare e giocare al gioco.
Aggiungi questa sezione al tuo `README.md` per fornire istruzioni più dettagliate su come configurare e giocare al gioco.