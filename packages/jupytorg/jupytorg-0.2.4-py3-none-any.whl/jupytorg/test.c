#include "aux.h"

int iam;
	
int main(int argc, char* argv[]){
  #pragma omp parallel private(iam)
    {
      iam = omp_get_thread_num();
  
  #pragma omp master
      {
        do_stuff(0.1);
        printf(" ---> This is only done by: %2d\n",iam);
      }
      printf("      This is also done by: %2d.\n",iam);
    }
}
