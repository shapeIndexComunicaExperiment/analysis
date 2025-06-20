    
# Comparison of shape index absent in 20% of the network against an ideal shape index
    
| Query template         | relation execution time   | p-value       |   avg ratio HTTP request |
|------------------------|---------------------------|---------------|--------------------------|
| interactive-discover-1 | greater                   | 8.73E-36      |                     2.36 |
| interactive-discover-2 | greater                   | 2.16E-02      |                     0.97 |
| interactive-discover-3 | similar                   | 2.28E-01 (RH) |                     1    |
| interactive-discover-4 | greater                   | 6.38E-17      |                     1.49 |
| interactive-discover-5 | similar                   | 7.28E-02 (RH) |                     0.97 |
| interactive-discover-6 | lesser                    | 9.28E-06      |                     0.71 |
| interactive-discover-7 | lesser                    | 1.97E-04      |                     0.71 |
| interactive-short-1    | greater                   | 1.12E-83      |                     6.02 |
| interactive-short-4    | lesser                    | 1.30E-13      |                     0.31 |
| interactive-short-5    | greater                   | 1.01E-09      |                     2.36 |

RH, indicate that the p-value is associated to the rejected hypothesis.
