## Raw scoring (as in the paper)

| model | dataset | condition | n | acc % [95% CI] | figurative % (n) | literal % (n) | change vs baseline (pts) | McNemar p |
|---|---|---|---|---|---|---|---|---|
| mt0-large | bengali_test | baseline | 340 | 55.6 [50.6, 60.9] | 55.9 (272) | 54.4 (68) | - | - |
| mt0-large | kannada_en_reviewed | baseline | 305 | 60.7 [55.1, 66.2] | 57.4 (242) | 73.0 (63) | - | - |
| mt0-large | kannada_en_reviewed | gold_explanation | 305 | 86.2 [82.3, 90.2] | 87.6 (242) | 81.0 (63) | +25.6 | 0.000 |
| mt0-large | kannada_en_reviewed | self_explanation | 305 | 61.0 [55.4, 66.6] | 57.9 (242) | 73.0 (63) | +0.3 | 1.000 |
| mt0-large | kannada_test | baseline | 305 | 54.8 [49.2, 60.7] | 52.1 (242) | 65.1 (63) | - | - |
| mt0-large | kannada_test | gold_explanation | 305 | 75.1 [70.5, 79.7] | 74.0 (242) | 79.4 (63) | +20.3 | 0.000 |
| mt0-large | kannada_test | self_explanation | 305 | 53.8 [48.2, 59.3] | 50.8 (242) | 65.1 (63) | -1.0 | 0.549 |
| qwen3.5-2b | kannada_en_reviewed | baseline | 305 | 74.1 [69.2, 79.0] | 71.9 (242) | 82.5 (63) | - | - |
| qwen3.5-2b | kannada_en_reviewed | gold_explanation | 305 | 83.9 [79.7, 87.9] | 83.5 (242) | 85.7 (63) | +9.8 | 0.000 |
| qwen3.5-2b | kannada_en_reviewed | self_explanation | 305 | 76.4 [71.5, 81.0] | 73.6 (242) | 87.3 (63) | +2.3 | 0.167 |
| qwen3.5-2b | kannada_test | baseline | 305 | 64.3 [59.0, 69.5] | 62.4 (242) | 71.4 (63) | - | - |
| qwen3.5-2b | kannada_test | gold_explanation | 305 | 84.9 [81.0, 88.9] | 85.1 (242) | 84.1 (63) | +20.7 | 0.000 |
| qwen3.5-2b | kannada_test | self_explanation | 305 | 69.2 [64.3, 74.4] | 68.2 (242) | 73.0 (63) | +4.9 | 0.011 |
| random | kannada_en_reviewed | baseline | 305 | 48.9 [43.6, 54.4] | 47.9 (242) | 52.4 (63) | - | - |
| random | kannada_en_reviewed | gold_explanation | 305 | 47.5 [42.0, 53.4] | 47.1 (242) | 49.2 (63) | -1.3 | 0.805 |
| random | kannada_en_reviewed | self_explanation | 305 | 50.2 [44.6, 55.7] | 51.7 (242) | 44.4 (63) | +1.3 | 0.805 |
| random | kannada_test | baseline | 305 | 51.8 [45.9, 57.4] | 52.1 (242) | 50.8 (63) | - | - |
| random | kannada_test | gold_explanation | 305 | 52.5 [46.6, 58.0] | 54.1 (242) | 46.0 (63) | +0.7 | 0.939 |
| random | kannada_test | self_explanation | 305 | 48.5 [42.9, 54.1] | 46.7 (242) | 55.6 (63) | -3.3 | 0.477 |
| sarvam-1 | kannada_en_reviewed | baseline | 305 | 79.0 [74.4, 83.9] | 77.3 (242) | 85.7 (63) | - | - |
| sarvam-1 | kannada_en_reviewed | gold_explanation | 305 | 91.8 [88.5, 94.8] | 90.5 (242) | 96.8 (63) | +12.8 | 0.000 |
| sarvam-1 | kannada_en_reviewed | self_explanation | 305 | 83.3 [79.0, 87.2] | 81.8 (242) | 88.9 (63) | +4.3 | 0.029 |
| sarvam-1 | kannada_test | baseline | 305 | 83.0 [78.4, 86.9] | 81.4 (242) | 88.9 (63) | - | - |
| sarvam-1 | kannada_test | gold_explanation | 305 | 95.4 [93.1, 97.7] | 95.5 (242) | 95.2 (63) | +12.5 | 0.000 |
| sarvam-1 | kannada_test | self_explanation | 305 | 83.6 [79.3, 87.5] | 83.1 (242) | 85.7 (63) | +0.7 | 0.864 |

## Swap-debiased scoring (answers also scored in swapped order)

| model | dataset | condition | n | acc % [95% CI] | figurative % (n) | literal % (n) | change vs baseline (pts) | McNemar p |
|---|---|---|---|---|---|---|---|---|
| mt0-large | bengali_test | baseline | 340 | 57.9 [52.6, 63.2] | 55.1 (272) | 69.1 (68) | - | - |
| mt0-large | kannada_en_reviewed | baseline | 305 | 65.2 [60.0, 70.5] | 60.7 (242) | 82.5 (63) | - | - |
| mt0-large | kannada_en_reviewed | gold_explanation | 305 | 91.5 [88.2, 94.4] | 91.7 (242) | 90.5 (63) | +26.2 | 0.000 |
| mt0-large | kannada_en_reviewed | self_explanation | 305 | 64.6 [59.3, 70.2] | 59.9 (242) | 82.5 (63) | -0.7 | 0.754 |
| mt0-large | kannada_test | baseline | 305 | 59.3 [53.8, 64.9] | 56.6 (242) | 69.8 (63) | - | - |
| mt0-large | kannada_test | gold_explanation | 305 | 92.5 [89.2, 95.4] | 93.8 (242) | 87.3 (63) | +33.1 | 0.000 |
| mt0-large | kannada_test | self_explanation | 305 | 57.7 [51.8, 63.0] | 54.1 (242) | 71.4 (63) | -1.6 | 0.332 |
| qwen3.5-2b | kannada_en_reviewed | baseline | 305 | 94.4 [91.8, 97.0] | 94.2 (242) | 95.2 (63) | - | - |
| qwen3.5-2b | kannada_en_reviewed | gold_explanation | 305 | 98.4 [96.7, 99.7] | 98.8 (242) | 96.8 (63) | +3.9 | 0.000 |
| qwen3.5-2b | kannada_en_reviewed | self_explanation | 305 | 94.1 [91.5, 96.7] | 93.8 (242) | 95.2 (63) | -0.3 | 1.000 |
| qwen3.5-2b | kannada_test | baseline | 305 | 79.0 [74.1, 83.3] | 78.1 (242) | 82.5 (63) | - | - |
| qwen3.5-2b | kannada_test | gold_explanation | 305 | 96.1 [93.8, 98.0] | 97.5 (242) | 90.5 (63) | +17.0 | 0.000 |
| qwen3.5-2b | kannada_test | self_explanation | 305 | 78.0 [73.1, 82.6] | 78.5 (242) | 76.2 (63) | -1.0 | 0.581 |
| random | kannada_en_reviewed | baseline | 305 | 42.3 [37.0, 47.9] | 40.5 (242) | 49.2 (63) | - | - |
| random | kannada_en_reviewed | gold_explanation | 305 | 50.8 [44.9, 56.7] | 50.0 (242) | 54.0 (63) | +8.5 | 0.042 |
| random | kannada_en_reviewed | self_explanation | 305 | 48.2 [43.0, 53.8] | 49.6 (242) | 42.9 (63) | +5.9 | 0.168 |
| random | kannada_test | baseline | 305 | 53.8 [47.9, 59.3] | 53.3 (242) | 55.6 (63) | - | - |
| random | kannada_test | gold_explanation | 305 | 50.8 [45.2, 56.4] | 48.3 (242) | 60.3 (63) | -3.0 | 0.504 |
| random | kannada_test | self_explanation | 305 | 48.9 [43.0, 54.4] | 47.1 (242) | 55.6 (63) | -4.9 | 0.251 |
| sarvam-1 | kannada_en_reviewed | baseline | 305 | 83.9 [79.7, 88.2] | 81.8 (242) | 92.1 (63) | - | - |
| sarvam-1 | kannada_en_reviewed | gold_explanation | 305 | 98.7 [97.4, 99.7] | 98.3 (242) | 100.0 (63) | +14.8 | 0.000 |
| sarvam-1 | kannada_en_reviewed | self_explanation | 305 | 85.9 [82.0, 89.8] | 84.3 (242) | 92.1 (63) | +2.0 | 0.327 |
| sarvam-1 | kannada_test | baseline | 305 | 87.9 [83.9, 91.5] | 86.4 (242) | 93.7 (63) | - | - |
| sarvam-1 | kannada_test | gold_explanation | 305 | 98.7 [97.4, 99.7] | 98.8 (242) | 98.4 (63) | +10.8 | 0.000 |
| sarvam-1 | kannada_test | self_explanation | 305 | 85.2 [80.7, 89.2] | 83.9 (242) | 90.5 (63) | -2.6 | 0.229 |
