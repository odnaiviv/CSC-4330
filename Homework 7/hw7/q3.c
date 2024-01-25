#include <stdio.h>
#include <string.h>

int q3() {
  // initalizing variables
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
    if (oddCount(word)) {
      count++;
    }
  }

  fclose(file);

  // output results
  printf("Odd Numbers of A's/a's: %d\n", count);
}

// counting the odd number of A's/a's in the text file
int oddCount(const char *word) {
  // variables
  int count = 0;
  int length = strlen(word);

  // checking through each letter in the word
  for (int i = 0; i < length; i++) {
    // increment if the letter is A/a
    if (word[i] == 'A' || word[i] == 'a') {
      count++;
    }
  }
  return (count % 2 != 0);
}
