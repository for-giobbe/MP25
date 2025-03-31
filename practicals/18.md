# After Tree Building & Selection Regimes Inference



 
---




## intro: 

Phylogenetic systematics aims is to reconstruct the patterns of relationships among different organisms. 
And while phylogenetic trees can be considered by themselves the results of such investigations, they can also be
used to study evolutionary processes with a myriad of possibilities. This is not a comprensive list by any mean, 
just what I stumbled upon during my research:

* molecular evolution / selection regimes
* divergence time analyses
* mapping traits on phylogenies _i.e._ comparative methods

Due to the severe time constrains of the course, we just have time to deal with the analysis of selection regimes,
which may be the topic which is more fit for this course. But remember that the interaction of
molecular phylogenetics and paleontology & morphology is extremely exciting and
relies on very serious informatics skills as well. I have selected two papers (respectively on
[molecular dating](https://doi.org/10.1111/brv.12390) and [comparative methods](https://doi.org/10.1073/pnas.1817794116)), 
along with two excellent tutorials which you will find in the last section of this class.




---




## Inferring selection regimes: 

A powerful approach to molecular evolution comes from the comparison of 
the relative rates of synonymous and nonsynonymous substitutions: dN & dS (_a.k.a._ ω).
dN are the ratio of the number of nonsynonymous substitutions per non-synonymous site while
dS are the ratio of the number of synonymous substitutions per synonymous site.
Synonymous mutations do not change the amino acid sequence; hence their substitution rate (dS) is assumed to be neutral 
with respect to selective pressure on the protein product of a gene (_n.b._ this assumption is heavily contested).
Nonsynonymous mutations do change the amino acid sequence, so their substitution rate (dN) is a
function of selective pressure on the protein. 
The ratio of these rates (dN/dS) is a measure of selective regime which a gene underwent. 
It's generally accepted that nonsynonymous mutations which are deleterious will be counterselected for
(purifying selection) and dN/dS will be less than 1, whereas if nonsynonymous mutations
are advantageous they will be fixed at a higher rate than synonymous mutations, and dN/dS will
be greater than 1. A dN/dS ratio equal to one is consistent with neutral evolution.


Here we are going to carry out likelihood estimations of the dN/dS ratio [(Goldman and Yang 1994)](https://doi.org/10.1093/oxfordjournals.molbev.a040153) using
CODEML, which is part of the PAML package [(Ziheng Yang, 2007)](https://academic.oup.com/mbe/article/24/8/1586/1103731). 
PAML is an extremely versatile piece of software whose features include:

* estimating synonymous and nonsynonymous rates
* testing hypotheses concerning dN/dS rate ratios
* ancestral sequence reconstruction (DNA, codon, or AAs)
* various clock models
* simulating nucleotide, codon, or AA sequence data sets
* ...

Just an extensive reding of the [manual](http://abacus.gene.ucl.ac.uk/software/pamlDOC.pdf) will disclose all
of its possibilities! 


Several great and newer alternative exist, the most notable being HyPhy [(Pond et al., 2019)](https://doi.org/10.1093/molbev/msz197) which is also
implemented in the Datamonkey [web server](https://www.datamonkey.org/). The server is currently down because it's being fully used 
to study COVID-19: you can follow this effort [here](http://covid19.datamonkey.org/). It includes an almost real-time update on which sites 
are found to be undergoing postive selection, which is quite [impressive](https://observablehq.com/@spond/natural-selection-analysis-of-sars-cov-2-covid-19).
This is not just some super-cool bioinformatics but it can prove very useful to identify new strains of the virus.


Anyway, let's check what we need in order to run CODEML:

* a ```.fasta``` alignment
* a ```.nwk``` tree
* a ```.ctl``` file 

Since the last tree we calculated for our PCG contains bootstrap - and that can mess up with CODEML - we can quickly recalculate it using
```iqtree -s ND2_p_aligned.n.gb.fasta```. Anyway my [alignment](https://github.com/for-giobbe/phy/blob/master/examples/ND2_p_aligned.n.gb.fasta) and 
[tree](https://github.com/for-giobbe/phy/raw/master/examples/ND2_p_aligned.n.gb.fasta.treefile) are available.  
Another possible option could be to to use ```sed``` and a [regexp](https://en.wikipedia.org/wiki/Regular_expression) (something like ```sed "s/\)[0-9]/)/g"```)
on the command-line to remove bootstrap values.


Now we just miss the ```.ctl``` - which stads for control file - and has a similar role to the ```.cfg``` we've seen earlier.
Here is how it looks like:

```
seqfile = 								* sequence data filename
treefile = 								* tree structure file name
outfile = 								* main result file name
noisy = 								* 0,1,2,3,9: how much rubbish on the screen
verbose = 								* 1:detailed output
runmode = 								* 0:user defined tree
seqtype = 								* 1:codons
CodonFreq = 								* 0:equal, 1:F1X4, 2:F3X4, 3:F61
model = 								* 0:one omega ratio for all branches
NSsites = 								* 0:one omega ratio (M0 in Tables 2 and 4)
icode = 								* 0:universal code
fix_kappa = 								* 1:kappa fixed, 0:kappa to be estimated
kappa = 								* initial or fixed kappa
fix_omega = 								* 1:omega fixed, 0:omega to be estimated
omega =  								* initial omega
 ```


In the ```.ctl``` found right up here just few parameters are present and it's possible to customize analyses
even more deeply. 


In this analysis we are going to compare two models - one with omega = 0.1 and one with omega 2.0 - 
and subsequently compare their likelihoods, to asses which is the best fit for our data. 


First we need to modify a ```.ctl``` files to have ```omega = 0.1```, like this:

```
seqfile = ND2_p_aligned.n.gb.fasta					* sequence data filename
treefile = ND2_p_aligned.n.gb.fasta.treefile				* tree structure file name
outfile = ND2_omega_0.1.out						* main result file name
noisy = 9								* 0,1,2,3,9: how much rubbish on the screen
verbose = 1								* 1:detailed output
runmode = 0								* 0:user defined tree
seqtype = 1								* 1:codons
CodonFreq = 2								* 0:equal, 1:F1X4, 2:F3X4, 3:F61
model = 0								* 0:one omega ratio for all branches
NSsites = 0								* 0:one omega ratio (M0 in Tables 2 and 4)
icode = 4								* 0:universal code
fix_kappa = 0								* 1:kappa fixed, 0:kappa to be estimated
kappa = 2								* initial or fixed kappa
fix_omega = 1								* 1:omega fixed, 0:omega to be estimated
omega = 0.1 								* initial omega
```

which we can then save as ```ND2_omega_0.1.ctl```.


Then we need to have another ```.ctl``` with ```omega = 2```     
 
```
seqfile = ND2_p_aligned.n.gb.fasta					* sequence data filename
treefile = ND2_p_aligned.n.gb.fasta.treefile				* tree structure file name
outfile = ND2_omega_2.0.out						* main result file name
noisy = 9								* 0,1,2,3,9: how much rubbish on the screen
verbose = 1								* 1:detailed output
runmode = 0								* 0:user defined tree
seqtype = 1								* 1:codons
CodonFreq = 2								* 0:equal, 1:F1X4, 2:F3X4, 3:F61
model = 0								* 0:one omega ratio for all branches
NSsites = 0								* 0:one omega ratio (M0 in Tables 2 and 4)
icode = 4								* 0:universal code
fix_kappa = 0								* 1:kappa fixed, 0:kappa to be estimated
kappa = 2								* initial or fixed kappa
fix_omega = 1								* 1:omega fixed, 0:omega to be estimated
omega = 2 								* initial omega
```
 
and we can save it as ```ND2_omega_2.0.ctl```. 


Remember to give different names to the ```outfile``` parameter so that the outputs do not get overwritten. 
Also take care in selecting the correct gencode, otherwise it's likely that stop codons will be found and CODEML will give an error. 
I used 4 which is the correct one for the mitogenomes of arthropods but here is the full list:

* 0 for the universal code
* 1 for the mammalian mitochondrial code
* 3 for mold mt., 
* 4 for invertebrate mt.;
* 5 for ciliate nuclear code; 
* 6 for echinoderm mt.; 
* 7 for euplotid mt.;
* 8 for alternative yeast nuclear; 
* 9 for ascidian mt.; 
* 10 for blepharisma nuclear. 

You can also notice how we set ```fix_omega = 1``` in order to force an omega value; 
if you put it to 0 omega will be estimated with a ML search.

To run codeml all we need to do is type 'codeml' in the same folder that the codeml.ctl file is in;
all of the options are already in the codeml.ctl file, including all the other inputs required for the analysis. 
Let's type ```codeml ND2_omega_0.1.ctl``` and ```codeml ND2_omega_2.0.ctl```, 
you can finde the ones I used respectively [here](https://github.com/for-giobbe/phy/raw/master/examples/ND2_omega_0.1.ctl) 
and [here](https://github.com/for-giobbe/phy/raw/master/examples/ND2_omega_2.0.ctl).

Let's take a look at the outputs:

* the ```.out``` file which we specified is what we are really interested in.
* ```2NG.t```, ```2NG.dS```, ```2NG.dN``` subs rates, dN & dS distances
* ```4fold.nuc``` 4-fold [degenerate](https://en.wikipedia.org/wiki/Codon_degeneracy) sites
* ```rub```, ```rst```, ```rst1``` and ```lnf``` are some rather misterios intermediate files

The outputs contain many interesting informations, such as:

a summary of codon usage counts:
```
------------------------------------------------------------------------------
Phe F TTT     209 | Ser S TCT     105 | Tyr Y TAT     158 | Cys C TGT      14
      TTC      57 |       TCC      39 |       TAC      45 |       TGC       5
Leu L TTA     579 |       TCA     305 | *** * TAA       0 | Trp W TGA     154
      TTG      14 |       TCG       8 |       TAG       0 |       TGG       7
------------------------------------------------------------------------------
Leu L CTT      46 | Pro P CCT      49 | His H CAT      33 | Arg R CGT      16
      CTC       4 |       CCC      13 |       CAC       9 |       CGC       0
      CTA     102 |       CCA      90 | Gln Q CAA     106 |       CGA      20
      CTG       8 |       CCG       2 |       CAG       5 |       CGG       0
------------------------------------------------------------------------------
Ile I ATT     545 | Thr T ACT     113 | Asn N AAT     414 | Ser S AGT      21
      ATC      92 |       ACC      31 |       AAC      87 |       AGC       3
Met M ATA    1119 |       ACA     222 | Lys K AAA     304 |       AGA     147
      ATG      35 |       ACG       6 |       AAG      10 |       AGG       1
------------------------------------------------------------------------------
Val V GTT      37 | Ala A GCT      42 | Asp D GAT       4 | Gly G GGT      43
      GTC       2 |       GCC       9 |       GAC       2 |       GGC       4
      GTA     118 |       GCA     108 | Glu E GAA     143 |       GGA      97
      GTG       7 |       GCG       1 |       GAG       9 |       GGG      50
------------------------------------------------------------------------------
```

and a summary of base frequencies onthe different codon positions:
```
position  1:    T:0.28185    C:0.08344    A:0.52256    G:0.11214
position  2:    T:0.49336    C:0.18962    A:0.22047    G:0.09655
position  3:    T:0.30674    C:0.06669    A:0.59954    G:0.02704
Average         T:0.36065    C:0.11325    A:0.44752    G:0.07858
```

along with the statistics for each branch in the tree,
```
 branch          t       N       S   dN/dS      dN      dS  N*dN  S*dS

  19..1      2.991   917.2   105.8  0.1000  0.5164  5.1639 473.7 546.1
  19..20     0.528   917.2   105.8  0.1000  0.0913  0.9126  83.7  96.5
  20..2      1.037   917.2   105.8  0.1000  0.1791  1.7914 164.3 189.5
  20..21     0.095   917.2   105.8  0.1000  0.0163  0.1634  15.0  17.3
  21..22     0.125   917.2   105.8  0.1000  0.0216  0.2161  19.8  22.9
  22..23     0.100   917.2   105.8  0.1000  0.0173  0.1727  15.8  18.3
  23..24     0.280   917.2   105.8  0.1000  0.0483  0.4829  44.3  51.1
  24..4      0.512   917.2   105.8  0.1000  0.0885  0.8845  81.1  93.5
  24..25     0.276   917.2   105.8  0.1000  0.0477  0.4769  43.7  50.4
  25..26     0.173   917.2   105.8  0.1000  0.0299  0.2993  27.4  31.6
  26..27     0.102   917.2   105.8  0.1000  0.0175  0.1754  16.1  18.5
  27..28     0.057   917.2   105.8  0.1000  0.0098  0.0984   9.0  10.4
  28..29     0.362   917.2   105.8  0.1000  0.0625  0.6252  57.3  66.1
  29..5      0.139   917.2   105.8  0.1000  0.0240  0.2397  22.0  25.4
  29..6      0.170   917.2   105.8  0.1000  0.0293  0.2930  26.9  31.0
  28..9      0.197   917.2   105.8  0.1000  0.0340  0.3395  31.1  35.9
  27..30     0.027   917.2   105.8  0.1000  0.0046  0.0462   4.2   4.9
  30..31     0.083   917.2   105.8  0.1000  0.0144  0.1435  13.2  15.2
  31..8      0.296   917.2   105.8  0.1000  0.0511  0.5110  46.9  54.0
  31..14     0.351   917.2   105.8  0.1000  0.0606  0.6065  55.6  64.1
  30..32     0.056   917.2   105.8  0.1000  0.0096  0.0963   8.8  10.2
  32..33     0.034   917.2   105.8  0.1000  0.0059  0.0592   5.4   6.3
  33..11     0.235   917.2   105.8  0.1000  0.0406  0.4057  37.2  42.9
  33..12     0.192   917.2   105.8  0.1000  0.0332  0.3316  30.4  35.1
  32..13     0.187   917.2   105.8  0.1000  0.0322  0.3223  29.6  34.1
  26..10     0.148   917.2   105.8  0.1000  0.0255  0.2550  23.4  27.0
  25..7      0.320   917.2   105.8  0.1000  0.0553  0.5531  50.7  58.5
  23..34     0.389   917.2   105.8  0.1000  0.0672  0.6717  61.6  71.0
  34..15     0.636   917.2   105.8  0.1000  0.1098  1.0985 100.8 116.2
  34..16     0.598   917.2   105.8  0.1000  0.1033  1.0330  94.8 109.3
  22..17     1.084   917.2   105.8  0.1000  0.1872  1.8719 171.7 198.0
  21..18     1.176   917.2   105.8  0.1000  0.2031  2.0307 186.3 214.8
  19..3      0.633   917.2   105.8  0.1000  0.1094  1.0936 100.3 115.7

tree length for dN:       2.3465
tree length for dS:      23.4648
```
for a fixed omega of 0.1.


```
 branch          t       N       S   dN/dS      dN      dS  N*dN  S*dS

  19..1      2.187   908.8   114.2  2.0000  0.7721  0.3860 701.6  44.1
  19..20     0.332   908.8   114.2  2.0000  0.1174  0.0587 106.7   6.7
  20..2      0.802   908.8   114.2  2.0000  0.2833  0.1416 257.4  16.2
  20..21     0.066   908.8   114.2  2.0000  0.0234  0.0117  21.2   1.3
  21..22     0.052   908.8   114.2  2.0000  0.0184  0.0092  16.7   1.0
  22..23     0.096   908.8   114.2  2.0000  0.0338  0.0169  30.7   1.9
  23..24     0.143   908.8   114.2  2.0000  0.0504  0.0252  45.8   2.9
  24..4      0.362   908.8   114.2  2.0000  0.1276  0.0638 116.0   7.3
  24..25     0.167   908.8   114.2  2.0000  0.0590  0.0295  53.6   3.4
  25..26     0.115   908.8   114.2  2.0000  0.0406  0.0203  36.9   2.3
  26..27     0.050   908.8   114.2  2.0000  0.0175  0.0088  15.9   1.0
  27..28     0.039   908.8   114.2  2.0000  0.0139  0.0070  12.7   0.8
  28..29     0.241   908.8   114.2  2.0000  0.0852  0.0426  77.4   4.9
  29..5      0.130   908.8   114.2  2.0000  0.0459  0.0229  41.7   2.6
  29..6      0.133   908.8   114.2  2.0000  0.0469  0.0234  42.6   2.7
  28..9      0.157   908.8   114.2  2.0000  0.0554  0.0277  50.3   3.2
  27..30     0.020   908.8   114.2  2.0000  0.0072  0.0036   6.5   0.4
  30..31     0.048   908.8   114.2  2.0000  0.0170  0.0085  15.5   1.0
  31..8      0.232   908.8   114.2  2.0000  0.0820  0.0410  74.5   4.7
  31..14     0.259   908.8   114.2  2.0000  0.0913  0.0457  83.0   5.2
  30..32     0.031   908.8   114.2  2.0000  0.0111  0.0056  10.1   0.6
  32..33     0.033   908.8   114.2  2.0000  0.0117  0.0059  10.7   0.7
  33..11     0.175   908.8   114.2  2.0000  0.0618  0.0309  56.1   3.5
  33..12     0.150   908.8   114.2  2.0000  0.0531  0.0265  48.2   3.0
  32..13     0.142   908.8   114.2  2.0000  0.0502  0.0251  45.7   2.9
  26..10     0.134   908.8   114.2  2.0000  0.0474  0.0237  43.1   2.7
  25..7      0.227   908.8   114.2  2.0000  0.0801  0.0401  72.8   4.6
  23..34     0.208   908.8   114.2  2.0000  0.0734  0.0367  66.7   4.2
  34..15     0.447   908.8   114.2  2.0000  0.1580  0.0790 143.5   9.0
  34..16     0.399   908.8   114.2  2.0000  0.1409  0.0705 128.1   8.0
  22..17     0.785   908.8   114.2  2.0000  0.2771  0.1386 251.9  15.8
  21..18     0.856   908.8   114.2  2.0000  0.3023  0.1511 274.7  17.3
  19..3      0.453   908.8   114.2  2.0000  0.1601  0.0800 145.5   9.1

tree length for dN:       3.4156
tree length for dS:       1.7078
```
for a fixed omega of 2.0.


But we can extract the more important information using respectively:

```
cat ND2_omega_0.1.out | grep lnL
lnL(ntime: 33  np: 34):  -9504.175938      +0.000000
```

and

```
cat ND2_omega_0.1.out | grep lnL
lnL(ntime: 33  np: 34): -11041.325358      +0.000000
```

Of course this is just an example and if we are really interested in the dNdS value which better describes our data, 
we should definitively try more values. Anyway, in this analysis we can compare which was the best-fit model & assumption by just comparing the lnL values.
In this case the lnL associated to the model which assumes dN/dS = 0.1 is an absolute smaller number (less negative) than
the lnL associated to the model which assumes dN/dS = 2.0 (absolute bigger number / more negative) and thus the first
model is a better fit. This comparison is possible when the two models have the same number of parameters, as you can see from ```np: 34```;
when comparing nested model with different number of parameters a Likelihood Ratio Test (LRT) should be used.


The fact that 0.1 is a much better fit for our data compared to 2.0 implies that the gene selection regime 
is better described by a strong purifying selection regime - in which coding mutations are strongly counterselected -
and the gene do not appear to have experienced any positive selection throughout our clade. This result is
kind of expected when dealing with a mitochondrial PCG: ff tne NADH-coenzyme Q oxidoreductase was 
accumulating so many coding mutations it would hugely affect the [OXPHOS pathway](https://en.wikipedia.org/wiki/Oxidative_phosphorylation#NADH-coenzyme_Q_oxidoreductase_(complex_I))!
Nonetheless at the bottom of this page you'll find on interesting paper on mitogenomes selection regimes in electric fishes,
in which they used CODEML.

Finally, I wanna make you focus ono a couple things: 
in this kind of analysis dNdS values are averaged throughout all codons and all branches of our data
But we know that selection can differ widely between different functional domains of a protein & between different lineages
of a clade. 

In this perspective a value of 2 is highly unrealistic, as it would 
imply that most of the codons of the alignment and lineages of the tree are accumulating 2X coding mutations in respect to non-coding mutations. 
These values are very rarely associated to real positive selection events but can be instead used to detect 
fenomena as pseudogenization and misalignment, which can definitely negatively affect phylogenetic inferences.
The concept recalls our first lesson, where  we learned that among the many ways of filtering MSA dNdS was a possibility.

These assumption that every site and every branch are undergoing the same selection regime
can be relaxe independently - using branch and sites models - or at the same time - using the branch-site model.

---

<br/>
<br/>

## conclusions: 

* building a phylogeny is both a result by itself & the basis for other investigations
* we carried out a comparison of two model with different dN/dS in a ML framework
* we found which was the be best-fit model for our data
* analysing regimes of selection can have real applications!

---

<br/>
<br/>

## further reading: 

The free [book](https://lukejharmon.github.io/pcm/) "Learning from trees" By Luke J Harmon, on comparative methods.

The "Taming the BEAST" [platform](https://taming-the-beast.org/) which includes many tutorials on divergence times estimation using BEAST 2.

[Here](http://evomicsorg.wpengine.netdna-cdn.com/wp-content/uploads/2011/08/bielawski_paml_review.pdf) you'll find more on the theoretical background of dNdS calculations. 

[Convergent patterns of evolution of mitochondrial oxidative phosphorylation (OXPHOS) genes in electric fishes](https://doi.org/10.1098/rstb.2019.0179)