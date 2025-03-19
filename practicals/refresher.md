
To cut the long story short, if can remember and use all comands listed subsequently, you can say you are a shell professional!

---

### move around!

```bash
whoami # username
pwd # print working directory
cd # change directory (relative or absolute path)
cd .. # bring you back one directory up
cd ~ # cd to your home
ls # print list of elements in directory
ls –lh # print sizes in human readable format
man list # (or any command, gives the manual for that command)
history # dispay last commands
ls *.fasta #list all fasta files
```

---

### write fast!

```
Ctrl+d # close session
Ctrl+l # clean the command line
Ctrl+c # kills a process
Ctrl+a # goes to the beginning of the line
Ctrl+e # goes to the endo of the line
Ctrl+arrows # moves faster
Ctrl+w # deletes the last folder
Ctrl+r # recursively search the history of commands
```

---

### special characters :-P

```bash
~ # home directory
. # current directory
.. # up one folder
/ # path directory separator
* # any character
; # shell commands separator
\> # redirect output to new file
\t # tab
\n # end of line in bash
\r # end of line in mac
\n\r # end of line in windows
\^ # starting with ; grep "^>" file #print lines starting with ">"
\$ # ending with ; grep ">\$" file #print lines ending with ">"
# many others (& | < ? []{} etc..)
```

Regular Expressions (__ReExp__): a sequence of characters that specifies a pattern. [Study them!](https://en.wikipedia.org/wiki/Regular_expression)

---

### grep!

```bash
grep "word" file # print all rows that contains "word"
grep -w "word" file # print all rows that contains exactly the pattern "word"
grep -V "word" file # inverted match, print all rows that not contain the patter "word"
grep -i "word" file # ignore case distinctions, grep both "word" and "WORD"
grep -c "word" file # count how many rows contain the patter "word"
grep –A10 "word" file # print rows containing pattern "word" and the 10 rows after
grep –B10 "word" file # print rows containing pattern "word" and the 10 rows before
grep –C10 "word" file # print rows containing pattern "word" and the 10 rows after and before
grep "Locus10[12]" file # print Locus101 and Locus102 
greo -E "(Locus101|Locus102)" file # print Locus101 and Locus102 
```

---

### sed!

```bash
sed 's/Locus/Transcript/' file # for each line subtitute "Locus" with "Transcripts" at first occurrance
sed 's/Locus/Transcript/g' file # for each line subtitute "Locus" with "Transcripts" at first occurrance
sed -i 's/Locus/Transcript/g' file # overwrite input with the output
sed '/Locus/d' file # delete any row containing "Locus"
```

---

### awk!

```bash
awk '{print $1}' file # print first column
awk '{print $0}' file # print all columns
awk '{print $NF}' file # print last column
awk '{print $4"\t"$1}' file # change orders of column and use tab as field separator in the output
awk -F";" '{print $3,$4}' file # fiels separator is ";"
awk '$1==$2 {print}' file # if first column = second column, print all columns
awk '$1 ~ /chr1/ && $3 - $2 > 10 {print}' file # if both the first column  contain "chr1" AND $3-$2>0 , print all columns
awk '{if ($1~">") print $0; else print length}' fasta_file # print length instead of sequence in fasta file
```

---

### comparisons ... 

```bash
a==b # a equal to b
a!=b # a different from b
a>=b # a greater or equal than b
a>b # a greater or equal than b
a<=b # a less or equal than b
a<b # a less than b
a || b # logical AND
a && b # logical OR
!a # not a
```

---

### edit files and folders ...

```bash
touch file_name #create new empty file
cp filename pathwheretocopy # copy file somewhere using absolute or relative path of where to copy
mv filename pathwheretocopy # moves file somewhere using absolute or relative path of where to copy
mv filename new_filename # rename file
less filename # see file
cat filename # similar to less
head filename # see first 10 rows of the file
tail filename # see last 10 rows of the file
head –n5 filename #(or tail –n 5) see only first 5 (or last) 5 rows
wc filename # outputs the number of words, lines, and characters
wc –l filename # outputs the number of lines
rm file # remove file
rm * # remove every file in that directory
mkdir newfoldername# make new directory
mkdir -p zmays-snps/{data/seqs,scripts,analysis} # create directory and subdirectories with one command
cp –r foldername # copy folder
mv foldername pathwheretomove # move folder
rm –r foldername # remove folder
```

---

### concatenate commands and programs <3

- the pipe ```|``` connects the standard output of one process to the standard input of another.

```bash
grep "word" file1 | sed 's/ /\t/g' | program1 > file2
```

- the semicolon ```;``` concatenate different commands or programs sequentially.

```bash
grep ">" file1.fasta >output1 ; grep "_" file2.fasta output2
```

- the ```&&``` concatenates two programs so that the second one run only if program1 completed successfully.

```bash
program1 input.txt > intermediate-results.txt && program2 intermediate-results.txt > results.txt
```

---

### variables <3

A variable in bash can be anything, a number, a character, a string of characters, a file, a folder. Variables are in bash are indicated with $

```bash
var="ciao"
echo $var # prints ciao
echo "$var" # prints ciao
echo '$var' # prints ciao
echo var # prints var
```

---

### for loop <3

```bash
for i in *.fasta; do echo $i; done
for i in *.fasta; do mv $i ${i::-5}”_for_trimming”; done
for i in *.fasta; do mv $i ${i:1:3}”.fasta” ; done
for i in *fasta; do sed ‘s/>Locus/>/’ > $i”_editname” ; done
for i in *fasta; do grep –c”>” $i ; done > counts
for i in *fasta; do program1 $i > “output_”$i; done
for i in */ ; do cd $i; cp *.fasta ../; cd ..; done
```

---

### if statement <3

```bash
if [ -f "file.fasta" ]; then echo "file.fasta exists"; fi
if [ -d "directory" ]; then echo "directory exists"; fi
if [ -s "file.fasta" ]; then echo "file.fasta is not empty"; fi
if [ ! -f "file.fasta" ]; then echo "file.fasta does not exist"; fi
if [ "$(wc -l < file.fasta)" -gt 10 ]; then echo "file.fasta has more than 10 lines"; fi
if grep -q ">Locus" file.fasta; then echo "Locus found"; fi
if command -v program1 >/dev/null; then echo "program1 is installed"; fi
```

---

### standard output and standard error :-O

Many programs use a "standard output" for outputting data, we usually redirected the standard output in an output file using ">". A separate file, called "standard error" is needed for errors, warnings, and messages. We can redirect the standard error with "2>"

```bash
program1 file 2> program1.stderr > results.txt
```

---

### merge and sort files ...

```bash
cat file1 file2 file3 … #merge multiple files in 1  
cat file1 file2 file3 > newfilename #redirect output to new file
sort file #sort the file, careful to computational sorting of file
sort –h file #human numeric sort
sort -t file #specify field separator (e.g., -t",")
sort -k1,1 -k2,2n file #sort by first column adn then numerically by second column
sort -k1,1 -k2,2nr file #sort by first column adn then numerically by second column in reversed order
sort -k1,1V -k2,2n file #as before but human sorted
join -1 1 -2 1 sorted_file1 sorted_file2 #join two files according to first column of each file
join -1 1 -2 1 -a 1 sorted_file1 sorted_file2 #keep also non joined rows
paste file1 file2 #merge lines of files
```

---

### compare sorted files ...

```bash
diff -y file1 file2 #Compare FILES line by line and show side by side
comm file1 file2 #compare two sorted files line by line
comm -1 file1 file2 #lines unique to file1
comm -2 file1 file2 #lines unique to file2
comm -12 file1 file2 #print only lines present in both file1 and file2
comm -3 file1 file2 #print lines in file1 not in file2, and vice versa
```

---

### download and transfer data!

`wget` can handle HTTP and FTP links

```bash
wget link
```

`curl` can transfer files using more protocols than wget.

```bash
curl –O link 
```

`scp` (secure copy): transfer data from local computer to remote host, or from two remote hosts. `scp` works just like cp, except we need to specify both host and path.

---

### compress and decompress data ...

```bash
gzip file # compress file file.gz
bzip2 file # slower than gzip but higher compression ratio
gzip –k file # keep also the not compressed file
gunzip file.gz # uncompress file
zless file.gz # less compressed file
zgrep "word" file.gz # use grep in compressed file
```

With **gzip** you don't get compression across files, each file is compressed independent of the others in the archive, advantage: you can access any of the files contained within.

With **tar** the only gain you can expect using tar alone would be by avoiding the space wasted by the file system as most of them allocate space at some granularity.

In **tar.gz** compression: create an archieve and extra step that compresses the entire archive, you cannot access single files without decompressing them.

```bash
tar -zcvf myfolder.tar.gz myfolder # c create archive; z gzip archive; f specify new output; v verbose
tar xvfz ./nome_archivio.tgz #decompress archive
```


---

### some tips on the terminal!

> tip: be **VERY careful with `rm`**, once you removed something there is no way to undo it; remember bash is case sensitive, the file, folder or scritp "Data" is different from "data".

> tip: **avoid special characters**; once created new file press “i" to write, after editing press Ctrl+c or esc and type `:wq` to save and exit from file or ':q!' to exit without saving.

---

### conda <3

```bash
conda init bash # initialize conda
conda env list # see list of environments
conda activate "environment_name" # activate environment_name
conda list # see packages installed in that environment_name
conda install -c channel program_name # install a package
conda deactivate # close environment 
```

---

## Git and GitHub <3

```bash
git add <file> # add file to the stagin area
git commit -m "commit message" # creates a new a commit 
git push # push any new commit
git pull # pull any changes from online repositories
git mv <file> # mv any file automatically adding this change to the staging area
git rm <file> # remove any file from the disk and from the staging area
git rm --cached <FILENAME> # remove a file from those that are synchronised
git status # display the current state of the git repository
```

---

#### [main](https://github.com/for-giobbe/MP25)