# Correct a sample sheet

## Background


For some parts of our pipelines at Clinical Genomics (CG) we use sample sheets. 
The sample sheet is a comma separated file `csv` file where each line holds information about a sample.
Each sample line have multiple columns with different types of information such as the sample id, the person who created the sample sheet etc.

### Barcodes
When sequencing a sample the molecules are uniquely identified using a barcode. 
The barcode is a random combination of letters `A`, `C`, `G` or `T`, example: `ACCATTTGGAGAGA`. 
For this example we will be using dual indexes which means that there are two columns in the sample sheet, one named `index1` and one `index2`.
The problem is that the sample sheet that we are given have both indexes in one string in the first index column where indexes are separated by the `+`-symbol.
Example `ATTA+CGGC`.
We need to covert the barcode from the first column and create a new sample sheet where, for each sample, the correct index is in the correct column.

### Reverse Complement

Moreover there are some situations where the second index needs to be converted into its reverse complement. 
The reverse complement means that each nucleotide is replaced by it's complementary nucleotide and the string is reversed.
We want to convert our second index with it's reverse complement when both indexes have length 10.

#### Reverse complements

| A | C | G | T |
| - | - | - | - |
| T | G | C | A |

In our case we need to replace the second index of the dual indexes with its reverse complement.

## Summary of tasks

- Read a sample sheet file
- Convert the index string from the index1-column into the two indexes
- Replace the second index with its reverse complement when both indexes have length of 10 bases
- Rest of information in sample sheet should be intact
