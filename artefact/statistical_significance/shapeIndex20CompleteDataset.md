    
# Comparison shape index with 20% entries incomplete against an ideal shape index
    
| Query template         | relation execution time   | p-value       |   avg ratio HTTP request |
|------------------------|---------------------------|---------------|--------------------------|
| interactive-discover-1 | similar                   | 3.53E-01 (RH) |                     2.4  |
| interactive-discover-2 | lesser                    | 3.62E-23      |                     1.09 |
| interactive-discover-3 | lesser                    | 6.74E-05      |                     1.02 |
| interactive-discover-4 | similar                   | 7.71E-01 (RH) |                     1.29 |
| interactive-discover-5 | greater                   | 1.25E-02      |                     1.09 |
| interactive-discover-6 | lesser                    | 8.19E-16      |                     0.97 |
| interactive-discover-7 | lesser                    | 2.22E-16      |                     0.98 |
| interactive-short-1    | greater                   | 1.84E-31      |                     1.44 |
| interactive-short-4    | lesser                    | 1.17E-02      |                     0.93 |
| interactive-short-5    | similar                   | 7.75E-02 (RH) |                     1.61 |

RH, indicate that the p-value is associated to the rejected hypothesis.
