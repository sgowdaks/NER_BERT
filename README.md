# Named Entity Recognition Using Transfer Learning
NER is a sequence tagging task, detecting entity names such as person, location, organization names, etc in a sequence of text. Real-world applications like efficient search, content recommendation, etc. uses NER. 
We chose these three applications, NER on
1. LPSC (Lunar and Planetary Science Conference)
2. BC2GM (BioCreative II Gene Mention Recognition)

For accessing the free GPU's that google provides, Edit --> Notebook settings --> GPU


## Instructions for LPSC Dataset

1. If you want to start from scratch, then the orginal LPSC dataset is located inside LPSC_and_BC2GM/LPSC-annotated/ folder, which is in brat annotaion format. 

## step1:
First convert it into IOB fomat, for that run the script nerToIOB.py, the input file to this should contain the path of the .txt and .ann file next to eachother. For that inside LPSC-16 and LPSC-15 use the commands
```
1. ls $PWD/*.txt > 1.list    (all the .txt file paths are in 1.list file)
2. ls $PWD/*.ann > 2.list    (all the .ann file paths are in 2.list file) 
3. paste  -d "," 1.list  2.list  > input.list   (combines the path of both .txt,.ann file with comma seperated)
```
Pass the input.list as input to the nertoIOB.py, which replaces the orginal annotaions with IOB format. 

## step2:
Convert the Brat annotation to NER format, for this download stanford core NLP package 2015-04-20 3.5.2 version from https://stanfordnlp.github.io/CoreNLP/history.html, unzip the file and after getting inside that folder run the command 
```
java -Xmx5g edu.stanford.nlp.pipeline.StanfordCoreNLP -file input.txt
```

which will start the server. Now run the brat2ner.py command with input as input.list, this outputs the NER format, once the NER format is avaible, you cal close the core NLP server.

2. If you want to directly access the LPSC dataset in NER format it is avaible in LPSC_and_BC2GM/LPSC_dataset.

The source code for NER with LPSC is located in LPSC_and_BC2GM/ folder. Download the Jupyter notebook NER_BERT.ipynb file, upload it to your google drive and don't forget to access GPU. Now download the test.txt and train.txt dataset from LPSC_and_BC2GM/LPSC_dataset and upload it google colab and run all the cells.

## Instructions for BC2GM Dataset

The source code for NER with BC2GM is located in LPSC_and_BC2GM/ folder. Download the Jupyter notebook NER_BERT.ipynb file, upload it to your google drive and don't forget to access GPU. Now download the BC_test.tsv and BC_train.tsv dataset from LPSC_and_BC2GM/BC2GM_dataset and upload it google colab before running all the cells make sure to uncomment 4 lines and comment 4 lines, the line details are provided in the colab file. Since we are using same source code for both LPSC and BC2GM datset, it is necessary. Now run all the cells.

We sincerely Thank Prof. Mandy for all the guidance. We Thanks Dr. Thamme Gowda for Brat2ner.py code, Neils Rogge for tutorials on [NER with BERT](https://github.com/NielsRogge/Transformers-Tutorials/tree/master/BERT), Google for providing free GPU’s, HuggingFace for free API’s with documentation. 



