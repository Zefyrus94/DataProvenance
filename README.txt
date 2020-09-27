Eseguendo
- jupyter notebook PowerConsumption.ipynb
	si utilizza mlflow per registrare le informazioni di provenienza per le operazioni di pre-processing (artefatti),
	training (metriche e parametri). Esse vengono salvate nella cartella mlruns (all'interno di questa cartella) e sono visualizzabili tramite web browser dopo aver eseguito su command line: mlflow ui
- jupyter notebook Census_withMLFlow.ipynb viene utilizzato mlflow per registrare la provenienza delle op. di
	preprocessing sul dataset Census (Giulia Simonelli)
- jupyter notebook IBM_space_removal.ipynb testa la registrazione della provenienza per l'operazione "rimozione degli
	spazi" utilizzando ProvLake di IBM Brasile, sul dataset Census di cui vengono presi in esame 5 record. Crea un log di workflow. Per testarlo online, lanciare tramite command line: python api.py, un servizio web per memorizzare le informazioni su mongoDB (mongodb deve essere in esecuzione)
- python client.py: crea 10 task di provenienza con una coda di 5 elementi per il calcolo del fattoriale. IBM Brasile ha
	reso il compito molto flessibile, molto dipenderà poi dalle query (es. quelle riportata da Giulia) per riuscire ad estrarre la giusta informazione sulla provenienza di un certo dato che ha subito numerose trasformazioni
