
#include <python2.7/Python.h>
#include <sys/wait.h>
#include <stdlib.h>
#include <unistd.h>
#include<stdio.h>

void print_memory(void)
{

static char buf[128] = {'\0'};
long vmsize, vmrss;
int rc;
FILE *fp;
fp = fopen("/proc/self/statm", "r");
if (!fp)
return;
  
/* Only fetch the first two entries. */
rc = fscanf(fp, "%ld%ld", &vmsize, &vmrss);
fclose(fp);

if (rc != 2)
return;
  
/* Convert to KB. */
vmsize *= 4;
vmrss *= 4;
snprintf(buf, sizeof(buf), "VmSize=%ldkB, VmRSS=%ldkB", vmsize, vmrss);
printf("VmSize=%ldkB, VmRSS=%ldkB\n", vmsize, vmrss);
return;

}

void start_interpreter(){

Py_Initialize();
return;
}

void close_interpreter(){

Py_Finalize();
return;
}





int main() {
printf("The memory being used before this program starts is : \n");
print_memory();

printf("\n");
printf("\n");
printf("\n");
int i;

for(i=0;i<10;i++){

   start_interpreter();
  PyRun_SimpleString("from time import time,ctime\n"
                     "print 'Today is',ctime(time())\n");
  PyRun_SimpleString("from time import time,ctime\n"
                     "print 'Today is',ctime(time())\n");
  PyRun_SimpleString("from time import time,ctime\n"
                     "print 'Today is',ctime(time())\n");
                     
                     printf("\n");
  close_interpreter();
  
  printf("\n");
  sleep(6);
  }
  printf("\n");
  printf("\n");
  printf("\n");
  printf("The memory being used now at the end of the process is: \n");
  print_memory();
  
  return 0;
  
}
