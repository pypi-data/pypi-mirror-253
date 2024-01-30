#include <omp.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/time.h>
#include <stdlib.h>

int rnd_int();
void rand_fill(int *x, int n);
long usecs ();
double secs ();
void do_stuff(double sec);
int compute_one(double sec);
int f_a();
int f_b();
int f_c();
int f_x(int b, int c);
int f_y(int a, int x);
void use_resource();