methly_diff: methyl_diff.c
	gcc -Wall -static -O3 -o methyl_diff $< -lm
