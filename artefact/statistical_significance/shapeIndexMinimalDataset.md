    
# Comparison of shape index with shapes with minimal information against an ideal shape index
    
| Query template         | relation execution time   | p-value       |   avg ratio HTTP request |
|------------------------|---------------------------|---------------|--------------------------|
| interactive-discover-1 | lesser                    | 3.08E-05      |                     0.67 |
| interactive-discover-2 | similar                   | 5.18E-01 (RH) |                     0.75 |
| interactive-discover-3 | similar                   | 3.90E-01 (RH) |                     0.95 |
| interactive-discover-4 | similar                   | 9.17E-01 (RH) |                     0.74 |
| interactive-discover-5 | similar                   | 7.27E-01 (RH) |                     0.75 |
| interactive-discover-6 | lesser                    | 8.12E-04      |                     0.74 |
| interactive-discover-7 | lesser                    | 8.50E-04      |                     0.74 |
| interactive-short-1    | greater                   | 9.52E-80      |                     5.47 |
| interactive-short-4    | lesser                    | 3.05E-13      |                     0.39 |
| interactive-short-5    | lesser                    | 1.41E-02      |                     0.52 |
| interactive-short-7    | lesser                    | 3.53E-18      |                     0.7  |

RH, indicate that the p-value is associated to the rejected hypothesis.
