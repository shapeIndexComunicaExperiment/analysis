
# Comparison execution time shape index approach against the type index

| Query template         | relation execution time   | p-value       |   avg ratio HTTP request |
|------------------------|---------------------------|---------------|--------------------------|
| interactive-discover-1 | lesser                    | 1.14E-36      |                     0.57 |
| interactive-discover-2 | lesser                    | 4.42E-04      |                     0.88 |
| interactive-discover-3 | similar                   | 7.47E-01 (RH) |                     0.97 |
| interactive-discover-4 | lesser                    | 2.07E-17      |                     0.65 |
| interactive-discover-5 | lesser                    | 5.58E-03      |                     0.88 |
| interactive-discover-6 | similar                   | 2.56E-01 (RH) |                     1.12 |
| interactive-discover-7 | similar                   | 7.83E-01 (RH) |                     1.12 |
| interactive-short-1    | lesser                    | 1.12E-83      |                     0.33 |
| interactive-short-4    | greater                   | 3.76E-22      |                    13    |
| interactive-short-5    | lesser                    | 3.12E-17      |                     0.44 |

RH, indicate that the p-value is associated to the rejected hypothesis.
