

Tree search options:

 * ```-nstop``` = specify number of unsuccesfull iterations to stop (DEFAULT 100). If after 100 iterations it is not finding a new best tree, it will give up (usually increased).
 * ```-pers``` = specify perturbation strength (between 0 and 1) for randomized NNI, default is 0.5.

Moreover, is a good practice to run at least 10 IQ-TREE runs and chose the one with the bes logL values. It can be found in the ```.iqtree``` file. In this way you can be a little bit more sure that your tree is not stucked in a local optima.






Now let's open the tree (it should be called specie.tree.treefile) and compare it to:

  * The one obtained directly with Orthofinder.
  * The phylogenomic from [Kocot et al., 2020](https://www.nature.com/articles/s41598-019-56728-w).




If we had time, what could we do to improve our phylogeny? Well, a lot of things can be done.

  * **1.** Increase the taxon sampling.
  * **2.** Increase the sample of loci.
  * **3.** We can use softwares like Phylotreepruner to remove orthologs that does not follow a taxonomic constrain (imposed by strong bibliography knowledge, *e.g* monophyly of Bivalvia).
  * **4.** We can try to change the outgroup (very common).
  * **5.** We can check if there are some compositional biases in our dataset and in case remove them (*e.g.* Aliscore).
  * **6.** If we can confidentialy put some constrains on the tree (or we want just to test these hypotesis) we can build up a partially constrained tree and calculates the partition log-likelihoods on both the constrained and uncostrained trees. In this way we can indentify partitions that support more one topology or the other and take a deeper look at them. Another way to do a similar thing, is to calculate RF distances between each gene tree and the constrained/uncostrained trees.
  * **7.** We can check for saturation (*e.g* identifying faster evolving genes/sites).

...And **A LOT** of other stuff (*e.g* tree topology testing, likelihood mapping, site log-likelihoods ...), almost always inside IQ-TREE (take a look [here](http://www.iqtree.org/doc/Command-Reference)for a complete list of IQ-TREE functions).

However, remember that your results should be always presented, discussed and justified comparing them to bibliography!



