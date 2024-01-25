#include <stdio.h>
#include <string.h>

int q1b() {
  // initalizing variables
  char wordCount[] = "Harry";
  char line[6066];
  int count = 0;

  // opening file
  FILE *file = fopen("HarryPotter.txt", "r");
  if (file == NULL) {
    perror("Error opening file!");
    return 1;
  }

  // checking through each line in text file
  while (fgets(line, sizeof(line), file)) {
    // increment count if line has word
    if (strstr(line, wordCount) != NULL) {
      count++;
    }
  }

  fclose(file);

  // output results
  printf("Lines with '%s': %d\n", wordCount, count);
}
