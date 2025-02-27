# Multiple Sequence Alignment & Filtering


---


## intro: 

All phylogenetic methods require a set of homologous characters thus the first step is to infer which nucleotides / codons / aminocid residues are homologous to each other, so that differences among these nucleotides result only from changes that convey descent information. This process is called  Multiple Sequence Alignment (MSA) and is often followed by an additional step of detection and exclusion of those alignment regions whose homology we are uncertain of.
Due to the large amount of data which we process nowadays, this step is often overlooked and as a result it's quite easy to find misaligned loci in modern datasets. Nonetheless this is a key step, which may affect downstream analyses (see further reading for more).

In this tutorial, we will use the most popular tools for multiple sequence alignment:

MAFFT [(Katoh and Standley 2013)](https://academic.oup.com/mbe/article/30/4/772/1073398)

T-Coffee [(Notredame et al., 2000)](https://www.ncbi.nlm.nih.gov/pubmed/10964570)

And subsequently filter the alignments using: 

Gblocks [(Talavera & Castresana, 2007)](https://academic.oup.com/sysbio/article/56/4/564/1682121)

At this stage you should have assembled your dataset into a multi-fasta file, which should look like [this](https://raw.githubusercontent.com/for-giobbe/phy/master/raw_genes/12S.fasta). It's very important that each one of you has it's own dastaset as this may provide natural examples of problems in analyses, but If you still do not have a dataset use [the one I am using](https://github.com/for-giobbe/phy/tree/master/raw_genes).

As we have a handfull of loci, we can use different approaches depending on their characteristics: some genes will be protein-coding (PCGs) and others will be non-coding (ncRNA).

Let's start with a look at the file with the ```cat``` command:

```
cat ND2.n.fasta
```

As you can see, in the [fasta format](https://en.wikipedia.org/wiki/FASTA_format) each record consists of an ID and a sequence, of which the ID is always on a single line that starts with the ">" symbol, followed by lines containing the sequence. 
The sequences are not aligned yet: this is the reason why they contain no gaps and differ in length.
The use of short and simple IDs is strongly recommended because many programs or scripts may not work if you use spaces or hyphens.


---


## aligning PCGs with MAFFT:

MAFFT is a very fast tool, which implements several different algorithms which makes it also very versatile.

Let's start with a PCG, using the code:

```
mafft --auto ND2.n.fasta > ND2_n_aligned.n.fasta
```

MAFFT contains many parameters, which you are encouraged to explore: an important one is the gap-opening penalty which by default is 1.53. Let's try a different value, using the code:

```
mafft --auto --op 7 ND2.n.fasta > ND2_op7_n_aligned.n.fasta
```

We can then inspect the outcome using Aliview: let's take some time to see if:

* there is any difference between the two gap-opening penalty values and

* if we can spot any stop codon, a task which can easily be done in Aliview using the sigma button (NB: adjust the genetic code and coding-frame).

Sometimes aligners which are not aware of the underlying structure of codons in PCGs can introduce some artificial stop codons, which are more often than not alignment errors.
Insertions and/or deletions ("indels") with lengths that are not multiples of three will disrupt the reading frame and cause large changes to the protein structure which are usually strongly selected against and rarely found in alignments of protein-coding sequences.
In cases where the placement of indels is ambiguous, information about the reading frame can be used to optimize the positioning of these indels, 
by translating the PCG from nucleotides into aminoacids, align the aminoacids and then retrotranslate the aminoacids alignment to nucleotides. 


Beware, your unaligned fasta file should have only sequence of multiple-three length of the retrotranslation step will not work. Here it is:

1. translation from nt to aa:

```
transeq -table 5 -sequence ND2.n.fasta -outseq ND2.p.fasta
```

2. aa alignment:

```
mafft --auto ND2.p.fasta > ND2_p_aligned.p.fasta
```

3. retrotranslation of the alignment from aa to nt:

```
pal2nal.pl ND2_p_aligned.p.fasta ND2.n.fasta -output fasta > ND2_p_aligned.n.fasta
```

Also it's important to notice that one can carry out phylogenetic inference on nucleotides and/or aminoacids: the first ones convey more information (due to the genetic code degeneracy) but that information can sometimes non suitable for inferring phylogenies (i.e. substitution saturation).


Last but not least: we leveraged the --auto flag of MAFFT, which automatically decides which is the best algorithm for carrying out the MSA, but several [algorithms](https://mafft.cbrc.jp/alignment/software/algorithms/algorithms.html) are implemented and the user can decide which one to rely on.


---


## aligning ncRNAs genes with MAFFT:

When dealing with non coding genes, we can not rely on the codon structure of the loci and it's generally more difficult to visually assess the quality of alignments. Luckily MAFFT implements specific [algorithms](https://mafft.cbrc.jp/alignment/software/source66.html) for the purpose:

* Q-INS-i - faster, less accurate.

* X-INS-i - slower, more accurate.

We can execute any of the two like this:

```mafft-qinsi 12S.fasta > 12S_qinsi_aligned.fasta```

```mafft-xinsi 12S.fasta > 12S_xinsi_aligned.fasta```

Is there any difference between the two?


```mafft-xinsi --op 1 12S.fasta > 12S_xinsi_op1_aligned.fasta```

```mafft-xinsi --op 7 12S.fasta > 12S_xinsi_op7_aligned.fasta```

How much is the gap opening penalty impacting on a ncRNA alignment?

---


## one aligner to rule them all: M-coffe.

T-Coffe is a popular aligner with an incredibly nice [server](http://tcoffee.crg.cat/) which I strongly encourage to explore. But today we are focusing on it's variant M-COFFEE: the idea behind M-COFFE is to combine many of the more popular aligners (including MAFFT).
If we type: ```t-coffee``` and scroll up a bit we can check wether the other aligners have been correctly installed (they should be, thanks to the magic behind conda installing). We should spot easily the popular ones as 
[Probcons](http://probcons.stanford.edu/), [Muscle](https://www.ebi.ac.uk/Tools/msa/muscle/), [Clustal](https://www.genome.jp/tools-bin/clustalw) and so on. We can give it a try using the default combination of aligners (Mkalign, Muscle & MAFFT) by typing:

```
t_coffee -seq 12S.fasta -mode fmcoffee
```

We should also take a look at the outputs:


* the ```.aln``` is the alignment file in the clustal format.
* the ```.dnd``` file is the guide tree generated in the process.
* the ```.html``` file mirrors the .aln file, it's just easyer to open by double clicking on it.

As you can see M-Coffee is combining multiple aligners into one and evaluating the uncertainty between their outcome. 


---


## the tradeoff between speed and accuracy: PSI-Coffe

The more accurate method (IMHO) is to rely on. This approach is quite useful when dealing with distantly related proteins and can be a game-changer when accurate alignments are necessary, for example for inferences on selection regimes.
We can easily use this method with the string:

```
t_coffee -seq 12S.fasta -mode psicoffee
```


---


## automating MSA:


In order to simplify our lessons and to gain a better understanding of the processes we restricted the number of genes to two / three. In real analyses usually hundreds or thousands of loci are used and thus the need to automate processes is quite strong. For loops are one possible solution:
 
```
mkdir aligned_genes;

for i in *fasta; do 
	gene_name=$(echo $i | awk -F “.” ‘{print $1}’); 
	mafft --auto $i > $name_aligned.fasta;
	done
```

I am also sharing an home-made [script](https://github.com/for-giobbe/phy/blob/master/scripts/msa.sh) for the purpose, you can test it and study its structure for the next lesson.


---


## alignment filtering:

The quality of multiple sequence alignments plays an important role in the accuracy of phylogenetic inference. It has been shown that removing certain positions (generally the ones which show an ambiguous homology and/or are highly variable) can improve the overall performance of many phylogenetic reconstruction methods. 
While dealing modern phylogenetic dataset, which consists of hundred to thousands of alignments is not possible to have a manual curation for each one, and thus it is necessary to automatically remove alignment errors.

In this tutorial we will use Gblocks:  this software will select blocks of conserved sites, which can be defined with many custom parameters, described in the [manual](http://molevol.cmima.csic.es/castresana/Gblocks/Gblocks_documentation.html)

We will use the susequent parameters and leave the rest to the default:

* -t= p (protein) d (DNA) c (codons) 
* -b4 Minimum Length Of A Block
* -b5 Allowed Gap Positions

Let's use this string one PCGs gene:

```
Gblocks ND2_p_aligned.n.fasta -t=d -b4=5 -b5=a
```

and this for ncRNAs:

```
Gblocks 12S_xinsi_op7_aligned.fasta -t=d -b4=5 -b5=a
```

The analyses will generate two kind of files:

* ```-gb```: filtered fasta files 
* ```-gb.htm```: for visualising which position got removed

We have to slightly reformat the Gblocks outputs, using a combination of ```tr``` and ```sed```:

```cat ND2_p_aligned.n.fasta-gb | tr -d " " | sed 's/_1//g'  > ND2_p_aligned.n.gb.fasta```

and

```cat 12S_xinsi_op7_aligned.fasta-gb | tr -d " " | sed 's/_1//g'  > 12S_xinsi_op7_aligned.gb.fasta```



Many other alternatives are possible, and all this tools can be extremely helpfull in removing noise and ameliorating certain characteristic of phylogenetic datasets which can affect subsequent inferences, such as substitution saturation & compositional heterogeneity. 
Here are the most popular:

[Aliscore](https://www.zfmk.de/de/forschung/forschungszentren-und-gruppen/aliscore) [(Kück et al., 2014)](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-15-294)

[BMGE](https://research.pasteur.fr/en/software/bmge-block-mapping-and-gathering-with-entropy/) [(Criscuolo & Gibaldo)](https://bmcevolbiol.biomedcentral.com/articles/10.1186/1471-2148-10-210)

Other approaches for filtering are possible and useful when dealing with a large number of loci. Positions, genes and entire alignment can be filtered out on several crietria, including:

* length
* occupancy
* dNdS
* ...

Consider also that a very stringent filtering can be a terrible approach in certain scenarios, for example when the phylogenetic signal and/or the amount of positions considered are scarce.

---


## conclusion

In the end you should have two aligned & filtered MSA, named something like [12S_xinsi_op7_aligned.gb.fasta](https://github.com/for-giobbe/phy/blob/master/examples/12S_xinsi_op7_aligned.gb.fasta) and [ND2_p_aligned.n.gb.fasta](https://github.com/for-giobbe/phy/blob/master/examples/ND2_p_aligned.n.gb.fasta).
An underlying theme of bioinformatics should start to become clear: every file should have a name which should convey most, if not all, the information regarding it.


---


## further reading: 

[very interesting paper on multiple sequence alignment uncertainty pt.1 ](https://academic.oup.com/gbe/article/7/8/2102/556628).

[very interesting paper on multiple sequence alignment uncertainty pt.2](https://science.sciencemag.org/content/319/5862/473?casa_token=t07ptffISm4AAAAA:j5l4US_y_GHOMduYw6R-MhyM7YUpa__08lw45l455DAU3tGFNKYlV40ZH0Si5w48Xl1gTEqsocLVvaE).

