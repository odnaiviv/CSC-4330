#include <stdio.h>
#include <string.h>

int q2() {
  // initalizing variables
  char wordCount[] = "had";
  char word[6066];
  int count = 0;

  // opening file
  FILE *file = fopen("HarryPotter.txt", "r");
  if (file == NULL) {
    perror("Error opening file!");
    return 1;
  }
  // checking through each word in text file
  while (fscanf(file, "%s", word) == 1) {
    // increment if the word is present
    if (strcmp(word, wordCount) == 0) {
      count++;
    }
  }

  fclose(file);

  // output results
  printf("''%s' Count: %d\n", wordCount, count);
}
