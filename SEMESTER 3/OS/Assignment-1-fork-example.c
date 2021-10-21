
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

void child() {
  printf("In Child");
  printf("- | Parent PPID: %d Child PID: %d\n", getppid(), getpid());
  printf("Child task\n");
}

void parent() {
  printf("In Parent");
  printf("- | Parent PID: %d\n", getpid());
  printf("Parent task.\n");
}

int main(void) {
  pid_t pid = fork();

  if(pid == 0) {
    child();
    exit(EXIT_SUCCESS);
  }
  else if(pid > 0) {
    parent();
    printf("Waiting for child process to finish.\n");
    wait(NULL);
    printf("Child process finished.\n");

  }
  else {
    printf("Creating child process failed.");
  }

  return EXIT_SUCCESS;
}
