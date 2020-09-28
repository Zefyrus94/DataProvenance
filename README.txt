Per i test ho utilizzato Python 3.7
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
- python neo4j <folderToUpload>: dopo aver modificato all'interno del file la password per il graph db (per Neo4j Desktop per Windows 10) e tgtdir l'esecuzione di questo script carica entità, attività e relazioni contenute nei file json per la cartella <folderToUpload> specificata. Sul calco del file per caricare i dati su MongoDB ad opera di Giulia Simonelli, anche questa deve essere del tipo results/Censusprov (una cartella di file json contenuta in un'altra cartella)




The ProvLake's code is Renan Souza and IBM's property.
Some other experiments on data provenance required the use of code of Giulia Simonelli and the authors of Scorpion, Titian and Databricks AI Summit 2020.
