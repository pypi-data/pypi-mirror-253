# Org to IPYNB

## Preamble

It should be remembered that the use of the operating system known as "Emacs" is prohibited by the Geneva Conventions and makes any user liable to a crime against humanity.

Indeed, this ignominy, whose violence and horror remain indescribable to us, is still far too widely used within the Linux community. There are many other tools available, such as ed, vim, nano... How can its use be justified, especially if it is shameless?

We are appalled and dumbfounded by this aberration. It is this service to humanity that has motivated us in this project. It's to save those who suffer from this evil. It is for you. You, who have desperately sought a solution. You, who have been desperate to get out of this trap. You, who represent that flickering glimmer of hope for a better future.

Résiste !
Prouve que tu existes !
Cherche ton bonheur partout, va,
refuse ce monde égoïste !
Résiste.
Suis ton cœur qui insiste !
Ce monde n'est pas le tien, viens, 
bats-toi, signe et persiste !
Résiste !

![image](https://i.imgflip.com/8df8x2.jpg)

## Requirements
- pandoc
- jupyter notebook

```bash
pip3 install jupyter jupyter-c-kernel jupyterlab notebook
``` 
then 
```bash
install_c_kernel --user
```
- gcc
    - OpenMP

You can test whether everything works using this command and this :
```bash
gcc -fopenmp code_block.c -o codeblock
./code_block
```
```c
// OpenMP header
#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
 
int main(int argc, char* argv[])
{
    int nthreads, tid;
 
    // Begin of parallel region
    #pragma omp parallel private(nthreads, tid)
    {
        // Getting thread number
        tid = omp_get_thread_num();
        printf("Welcome to GFG from thread = %d\n",
               tid);
 
        if (tid == 0) {
 
            // Only master thread does this
            nthreads = omp_get_num_threads();
            printf("Number of threads = %d\n",
                   nthreads);
        }
    }
}
```

## Principle

We take a `.org` file and convert it to `html` using `pandoc <filename>.org -o <filename>.html`.
Then we parse this intermediate rendering to extract the bits of code and generate a usable `json IPYNB`.

## Usage
```text
Usage: jupytorg src=input_file_path (optional type=code_block_language dest=output_file_path)
    input_file_path : the path to input the file
    code_block_language : the language of the code blocks (default is C)
    output_file_path : the path to output the file (default is output_file.ipynb)
```
Example with a `newcourse.org` file:
```bash
python3 -m jupytorg src=~/Documents/2A/OpenMP/newcourse.org dest=~/Documents/2A/OpenMP/newcourse.ipynb
```
It reads the `.org` file in the specified folder and drops the coonverted jupyter notebook into the same folder. All that remains is to open it with VSCode.