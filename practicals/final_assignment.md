### FInal Assignment

... you are a phylogeneticist now! 

.... in these practical we are going to use the proteoms from 7 Mollusk species taken from public database plus one Annelidae as outgroup:

  - [*Biomphalaria glabrata*](https://imagens.ebc.com.br/PLQ4dlImF82bd1vjscHc2EjtVKo=/1600x800/https://agenciabrasil.ebc.com.br/sites/default/files/atoms/image/esquistossomose_artigo_fiomg_interno_0.jpg?itok=Y-6YUgCu) (Gasteropoda)
  - [*Acanthopleura granulata*](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Acanthopleura_granulata_%28West_Indian_fuzzy_chitons%29_%28San_Salvador_Island%2C_Bahamas%29_1_%2816131898481%29.jpg/1600px-Acanthopleura_granulata_%28West_Indian_fuzzy_chitons%29_%28San_Salvador_Island%2C_Bahamas%29_1_%2816131898481%29.jpg?20150503211646) (Poliplacophora)
  - [*Crassostrea virginica*](https://upload.wikimedia.org/wikipedia/commons/6/6d/Oyster_bed%2C_Brunswick%2C_GA%2C_US.jpg) (Bivalvia)
  - [*Lottia gigantea*](https://upload.wikimedia.org/wikipedia/commons/8/8e/Lottia_gigantea.jpg) (Gasteropoda)
  - [*Octopus bimaculoides*](https://www.flickr.com/photos/39365853@N07/7532895572/sizes/k/) (Cephalopoda)
  - [*Sinivicula constricta*](https://www.cabidigitallibrary.org/cms/10.1079/cabicompendium.63482/asset/b2492559-2c1b-4e14-bb98-06f1719d8dca/assets/graphic/63482_02.jpg) (Bivalvia)
  - [*Pinctada fucata*](https://cdn.britannica.com/49/9749-050-33C30CE5/European-flat-oyster.jpg) (Bivalvia)
  - [*Helobdella robusta*](https://upload.wikimedia.org/wikipedia/commons/9/98/Europ%C3%A4ischer-Platt-Egel_cropped.jpg) (Anellidae)


Let's start from their proteoms that you can find in the ```Data/Proteoms``` folder:

00 - perform an orthology inference using ```orthofinder``` - or you can use [mine](https://github.com/for-giobbe/MP25/blob/main/data/OrthoFinder.zip)

01 - align single copy orthogroups using ```mafft```

02 - trim multiple sequence alignement using ```Gblocks```

03 - concatenate them using ```AMAS```

04 - perform a ML inference using gene-partitions and merging using ```IQTREE```

05 - infer bracnhes support on the ML tree using 1000 ultrafast (parametric) replicates with ```IQTREE```

06 - perform BI - without any partition - then asses ESS with ```tracer``` and provide a MCC tree with ```treeannotator```

07 - as a check, perform ML inference using mixture models with ```IQTREE```

08 - as a further check, compare the ML inference using mixture models to the partitioned ML and the BI ones with ```IQTREE```

09 - perform a coalescence-based inference using ```astral```

10 - now that you are shure on the topology, infer a time treewith ```IQTREE```, knowing that bivalves diverged 465 MYA 

