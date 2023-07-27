// C program to demonstrate shallow copy
# include <stdio.h>
# include <string.h>
# include <stdlib.h>

struct test
{
  char *str;
};

int main()
{
  struct test st1, st2;
  st1.str = (char *)malloc(sizeof(char) * 20);

  strcpy(st1.str, "GeeksforGeeks");

  st2 = st1;
  st1.str[0] = 'X';
  st1.str[1] = 'Y';

  /* Since copy was shallow, both strings are same */
  printf("st1's str = %s\n", st1.str);
  printf("st2's str = %s\n", st2.str);

  return 0;
}

Output:
st1's str = XYeksforGeeks
st2's str = XYeksforGeeks