# Final Project

Our team in Trello is *Group D*.
 
This repository contains the following contents;
 
* Source code - *fp.py, marker.py, verb.py*
* Test code - *test.py* (sample test code)
* Data set - *gutenberg*

## What the program does

This program takes two *known text* and one *questioned text*. Then, it computes the log-likelihood function and decides which of two text is near to questioned text. Then, it makes a decision if it is written by the same author or not.

 
## Execution Step

**Step1:** Make sure that the source code and data set are in the same directory.

**Step2:** Run the following command in terminal with any file name in the data set;
```
python3 fp.py filename1 filename2 filename3 RUN
```

Note: The `filename1` and `filename2` correspond to the *known text* and `filename3` corresponds to the *questioned text*.

For example,
```
python3 fp.py austen-emma.txt shakespeare-caesar.txt austen-sense.txt RUN
```

In this case, the known texts are *austen-emma.txt* and *shakespeare-caesar.txt*, the questioned text is *austen-sense.txt*.

**Step3:** The result is shown in the command line with the name of the most likely text and the value of average difference of type token ratio for each feature.

For example, running the command in the previous example produces the following results;

```
The most likely text is austen-emma.txt.
The ratio difference of IN is 0.09860772357723586 %.
The ratio difference of VB is 0.04171488400488353 %.
The ratio difference of JJR is 0.7419450000000004 %.
The ratio difference of JJS is 1.1213952727272738 %.
The ratio difference of RB is 0.059242662942272005 %.
The ratio difference of VBD is 0.045348647416413486 %.
The ratio difference of UH is 2.8515679999999994 %.
The ratio difference of FW is 14.102565000000004 %.
The ratio difference of Will and Going is 14.102565000000004 %.
The questioned text "austen-sense.txt" is considered as written by the author of the text "austen-emma.txt".
```

In this case, it is concluded that the questioned text is written by the same author as most likely text.


