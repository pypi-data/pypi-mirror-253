| Name                          | Input shape | Output shape |     MACs |   Params | Description                  |
|:-----------------------------:|:-----------:|:------------:|:--------:|:--------:|:----------------------------:|
| Conv2d_1a_3x3.conv            |  3x299x299  |  32x149x149  |   0.33 % |   0.00 % | Conv2d k=3 p=0 s=2           |
| Conv2d_1a_3x3.bn              |  32x149x149 |  32x149x149  |   0.05 % |   0.00 % | BatchNorm2d                  |
| Conv2d_2a_3x3.conv            |  32x149x149 |  32x147x147  |   3.46 % |   0.04 % | Conv2d k=3 p=0 s=1           |
| Conv2d_2a_3x3.bn              |  32x147x147 |  32x147x147  |   0.05 % |   0.00 % | BatchNorm2d                  |
| Conv2d_2b_3x3.conv            |  32x147x147 |  64x147x147  |   6.93 % |   0.08 % | Conv2d k=3 p=1 s=1           |
| Conv2d_2b_3x3.bn              |  64x147x147 |  64x147x147  |   0.10 % |   0.00 % | BatchNorm2d                  |
| maxpool1                      |  64x147x147 |   64x73x73   |   0.00 % |   0.00 % | MaxPool2d k=3 s=2            |
| Conv2d_3b_1x1.conv            |   64x73x73  |   80x73x73   |   0.47 % |   0.02 % | Conv2d k=1 p=0 s=1           |
| Conv2d_3b_1x1.bn              |   80x73x73  |   80x73x73   |   0.03 % |   0.00 % | BatchNorm2d                  |
| Conv2d_4a_3x3.conv            |   80x73x73  |  192x71x71   |  12.12 % |   0.58 % | Conv2d k=3 p=0 s=1           |
| Conv2d_4a_3x3.bn              |  192x71x71  |  192x71x71   |   0.07 % |   0.00 % | BatchNorm2d                  |
| maxpool2                      |  192x71x71  |  192x35x35   |   0.00 % |   0.00 % | MaxPool2d k=3 s=2            |
| Mixed_5b.branch1x1.conv       |  192x35x35  |   64x35x35   |   0.26 % |   0.05 % | Conv2d k=1 p=0 s=1           |
| Mixed_5b.branch1x1.bn         |   64x35x35  |   64x35x35   |   0.01 % |   0.00 % | BatchNorm2d                  |
| Mixed_5b.branch5x5_1.conv     |  192x35x35  |   48x35x35   |   0.20 % |   0.04 % | Conv2d k=1 p=0 s=1           |
| Mixed_5b.branch5x5_1.bn       |   48x35x35  |   48x35x35   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_5b.branch5x5_2.conv     |   48x35x35  |   64x35x35   |   1.64 % |   0.32 % | Conv2d k=5 p=2 s=1           |
| Mixed_5b.branch5x5_2.bn       |   64x35x35  |   64x35x35   |   0.01 % |   0.00 % | BatchNorm2d                  |
| Mixed_5b.branch3x3dbl_1.conv  |  192x35x35  |   64x35x35   |   0.26 % |   0.05 % | Conv2d k=1 p=0 s=1           |
| Mixed_5b.branch3x3dbl_1.bn    |   64x35x35  |   64x35x35   |   0.01 % |   0.00 % | BatchNorm2d                  |
| Mixed_5b.branch3x3dbl_2.conv  |   64x35x35  |   96x35x35   |   1.18 % |   0.23 % | Conv2d k=3 p=1 s=1           |
| Mixed_5b.branch3x3dbl_2.bn    |   96x35x35  |   96x35x35   |   0.01 % |   0.00 % | BatchNorm2d                  |
| Mixed_5b.branch3x3dbl_3.conv  |   96x35x35  |   96x35x35   |   1.77 % |   0.35 % | Conv2d k=3 p=1 s=1           |
| Mixed_5b.branch3x3dbl_3.bn    |   96x35x35  |   96x35x35   |   0.01 % |   0.00 % | BatchNorm2d                  |
| Mixed_5b.branch_pool.conv     |  192x35x35  |   32x35x35   |   0.13 % |   0.03 % | Conv2d k=1 p=0 s=1           |
| Mixed_5b.branch_pool.bn       |   32x35x35  |   32x35x35   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_5c.branch1x1.conv       |  256x35x35  |   64x35x35   |   0.35 % |   0.07 % | Conv2d k=1 p=0 s=1           |
| Mixed_5c.branch1x1.bn         |   64x35x35  |   64x35x35   |   0.01 % |   0.00 % | BatchNorm2d                  |
| Mixed_5c.branch5x5_1.conv     |  256x35x35  |   48x35x35   |   0.26 % |   0.05 % | Conv2d k=1 p=0 s=1           |
| Mixed_5c.branch5x5_1.bn       |   48x35x35  |   48x35x35   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_5c.branch5x5_2.conv     |   48x35x35  |   64x35x35   |   1.64 % |   0.32 % | Conv2d k=5 p=2 s=1           |
| Mixed_5c.branch5x5_2.bn       |   64x35x35  |   64x35x35   |   0.01 % |   0.00 % | BatchNorm2d                  |
| Mixed_5c.branch3x3dbl_1.conv  |  256x35x35  |   64x35x35   |   0.35 % |   0.07 % | Conv2d k=1 p=0 s=1           |
| Mixed_5c.branch3x3dbl_1.bn    |   64x35x35  |   64x35x35   |   0.01 % |   0.00 % | BatchNorm2d                  |
| Mixed_5c.branch3x3dbl_2.conv  |   64x35x35  |   96x35x35   |   1.18 % |   0.23 % | Conv2d k=3 p=1 s=1           |
| Mixed_5c.branch3x3dbl_2.bn    |   96x35x35  |   96x35x35   |   0.01 % |   0.00 % | BatchNorm2d                  |
| Mixed_5c.branch3x3dbl_3.conv  |   96x35x35  |   96x35x35   |   1.77 % |   0.35 % | Conv2d k=3 p=1 s=1           |
| Mixed_5c.branch3x3dbl_3.bn    |   96x35x35  |   96x35x35   |   0.01 % |   0.00 % | BatchNorm2d                  |
| Mixed_5c.branch_pool.conv     |  256x35x35  |   64x35x35   |   0.35 % |   0.07 % | Conv2d k=1 p=0 s=1           |
| Mixed_5c.branch_pool.bn       |   64x35x35  |   64x35x35   |   0.01 % |   0.00 % | BatchNorm2d                  |
| Mixed_5d.branch1x1.conv       |  288x35x35  |   64x35x35   |   0.39 % |   0.08 % | Conv2d k=1 p=0 s=1           |
| Mixed_5d.branch1x1.bn         |   64x35x35  |   64x35x35   |   0.01 % |   0.00 % | BatchNorm2d                  |
| Mixed_5d.branch5x5_1.conv     |  288x35x35  |   48x35x35   |   0.29 % |   0.06 % | Conv2d k=1 p=0 s=1           |
| Mixed_5d.branch5x5_1.bn       |   48x35x35  |   48x35x35   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_5d.branch5x5_2.conv     |   48x35x35  |   64x35x35   |   1.64 % |   0.32 % | Conv2d k=5 p=2 s=1           |
| Mixed_5d.branch5x5_2.bn       |   64x35x35  |   64x35x35   |   0.01 % |   0.00 % | BatchNorm2d                  |
| Mixed_5d.branch3x3dbl_1.conv  |  288x35x35  |   64x35x35   |   0.39 % |   0.08 % | Conv2d k=1 p=0 s=1           |
| Mixed_5d.branch3x3dbl_1.bn    |   64x35x35  |   64x35x35   |   0.01 % |   0.00 % | BatchNorm2d                  |
| Mixed_5d.branch3x3dbl_2.conv  |   64x35x35  |   96x35x35   |   1.18 % |   0.23 % | Conv2d k=3 p=1 s=1           |
| Mixed_5d.branch3x3dbl_2.bn    |   96x35x35  |   96x35x35   |   0.01 % |   0.00 % | BatchNorm2d                  |
| Mixed_5d.branch3x3dbl_3.conv  |   96x35x35  |   96x35x35   |   1.77 % |   0.35 % | Conv2d k=3 p=1 s=1           |
| Mixed_5d.branch3x3dbl_3.bn    |   96x35x35  |   96x35x35   |   0.01 % |   0.00 % | BatchNorm2d                  |
| Mixed_5d.branch_pool.conv     |  288x35x35  |   64x35x35   |   0.39 % |   0.08 % | Conv2d k=1 p=0 s=1           |
| Mixed_5d.branch_pool.bn       |   64x35x35  |   64x35x35   |   0.01 % |   0.00 % | BatchNorm2d                  |
| Mixed_6a.branch3x3.conv       |  288x35x35  |  384x17x17   |   5.00 % |   4.17 % | Conv2d k=3 p=0 s=2           |
| Mixed_6a.branch3x3.bn         |  384x17x17  |  384x17x17   |   0.01 % |   0.01 % | BatchNorm2d                  |
| Mixed_6a.branch3x3dbl_1.conv  |  288x35x35  |   64x35x35   |   0.39 % |   0.08 % | Conv2d k=1 p=0 s=1           |
| Mixed_6a.branch3x3dbl_1.bn    |   64x35x35  |   64x35x35   |   0.01 % |   0.00 % | BatchNorm2d                  |
| Mixed_6a.branch3x3dbl_2.conv  |   64x35x35  |   96x35x35   |   1.18 % |   0.23 % | Conv2d k=3 p=1 s=1           |
| Mixed_6a.branch3x3dbl_2.bn    |   96x35x35  |   96x35x35   |   0.01 % |   0.00 % | BatchNorm2d                  |
| Mixed_6a.branch3x3dbl_3.conv  |   96x35x35  |   96x17x17   |   0.42 % |   0.35 % | Conv2d k=3 p=0 s=2           |
| Mixed_6a.branch3x3dbl_3.bn    |   96x17x17  |   96x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6b.branch1x1.conv       |  768x17x17  |  192x17x17   |   0.74 % |   0.62 % | Conv2d k=1 p=0 s=1           |
| Mixed_6b.branch1x1.bn         |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6b.branch7x7_1.conv     |  768x17x17  |  128x17x17   |   0.49 % |   0.41 % | Conv2d k=1 p=0 s=1           |
| Mixed_6b.branch7x7_1.bn       |  128x17x17  |  128x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6b.branch7x7_2.conv     |  128x17x17  |  128x17x17   |   0.58 % |   0.48 % | Conv2d k=(1, 7) p=(0, 3) s=1 |
| Mixed_6b.branch7x7_2.bn       |  128x17x17  |  128x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6b.branch7x7_3.conv     |  128x17x17  |  192x17x17   |   0.86 % |   0.72 % | Conv2d k=(7, 1) p=(3, 0) s=1 |
| Mixed_6b.branch7x7_3.bn       |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6b.branch7x7dbl_1.conv  |  768x17x17  |  128x17x17   |   0.49 % |   0.41 % | Conv2d k=1 p=0 s=1           |
| Mixed_6b.branch7x7dbl_1.bn    |  128x17x17  |  128x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6b.branch7x7dbl_2.conv  |  128x17x17  |  128x17x17   |   0.58 % |   0.48 % | Conv2d k=(7, 1) p=(3, 0) s=1 |
| Mixed_6b.branch7x7dbl_2.bn    |  128x17x17  |  128x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6b.branch7x7dbl_3.conv  |  128x17x17  |  128x17x17   |   0.58 % |   0.48 % | Conv2d k=(1, 7) p=(0, 3) s=1 |
| Mixed_6b.branch7x7dbl_3.bn    |  128x17x17  |  128x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6b.branch7x7dbl_4.conv  |  128x17x17  |  128x17x17   |   0.58 % |   0.48 % | Conv2d k=(7, 1) p=(3, 0) s=1 |
| Mixed_6b.branch7x7dbl_4.bn    |  128x17x17  |  128x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6b.branch7x7dbl_5.conv  |  128x17x17  |  192x17x17   |   0.86 % |   0.72 % | Conv2d k=(1, 7) p=(0, 3) s=1 |
| Mixed_6b.branch7x7dbl_5.bn    |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6b.branch_pool.conv     |  768x17x17  |  192x17x17   |   0.74 % |   0.62 % | Conv2d k=1 p=0 s=1           |
| Mixed_6b.branch_pool.bn       |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6c.branch1x1.conv       |  768x17x17  |  192x17x17   |   0.74 % |   0.62 % | Conv2d k=1 p=0 s=1           |
| Mixed_6c.branch1x1.bn         |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6c.branch7x7_1.conv     |  768x17x17  |  160x17x17   |   0.62 % |   0.51 % | Conv2d k=1 p=0 s=1           |
| Mixed_6c.branch7x7_1.bn       |  160x17x17  |  160x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6c.branch7x7_2.conv     |  160x17x17  |  160x17x17   |   0.90 % |   0.75 % | Conv2d k=(1, 7) p=(0, 3) s=1 |
| Mixed_6c.branch7x7_2.bn       |  160x17x17  |  160x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6c.branch7x7_3.conv     |  160x17x17  |  192x17x17   |   1.08 % |   0.90 % | Conv2d k=(7, 1) p=(3, 0) s=1 |
| Mixed_6c.branch7x7_3.bn       |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6c.branch7x7dbl_1.conv  |  768x17x17  |  160x17x17   |   0.62 % |   0.51 % | Conv2d k=1 p=0 s=1           |
| Mixed_6c.branch7x7dbl_1.bn    |  160x17x17  |  160x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6c.branch7x7dbl_2.conv  |  160x17x17  |  160x17x17   |   0.90 % |   0.75 % | Conv2d k=(7, 1) p=(3, 0) s=1 |
| Mixed_6c.branch7x7dbl_2.bn    |  160x17x17  |  160x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6c.branch7x7dbl_3.conv  |  160x17x17  |  160x17x17   |   0.90 % |   0.75 % | Conv2d k=(1, 7) p=(0, 3) s=1 |
| Mixed_6c.branch7x7dbl_3.bn    |  160x17x17  |  160x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6c.branch7x7dbl_4.conv  |  160x17x17  |  160x17x17   |   0.90 % |   0.75 % | Conv2d k=(7, 1) p=(3, 0) s=1 |
| Mixed_6c.branch7x7dbl_4.bn    |  160x17x17  |  160x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6c.branch7x7dbl_5.conv  |  160x17x17  |  192x17x17   |   1.08 % |   0.90 % | Conv2d k=(1, 7) p=(0, 3) s=1 |
| Mixed_6c.branch7x7dbl_5.bn    |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6c.branch_pool.conv     |  768x17x17  |  192x17x17   |   0.74 % |   0.62 % | Conv2d k=1 p=0 s=1           |
| Mixed_6c.branch_pool.bn       |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6d.branch1x1.conv       |  768x17x17  |  192x17x17   |   0.74 % |   0.62 % | Conv2d k=1 p=0 s=1           |
| Mixed_6d.branch1x1.bn         |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6d.branch7x7_1.conv     |  768x17x17  |  160x17x17   |   0.62 % |   0.51 % | Conv2d k=1 p=0 s=1           |
| Mixed_6d.branch7x7_1.bn       |  160x17x17  |  160x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6d.branch7x7_2.conv     |  160x17x17  |  160x17x17   |   0.90 % |   0.75 % | Conv2d k=(1, 7) p=(0, 3) s=1 |
| Mixed_6d.branch7x7_2.bn       |  160x17x17  |  160x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6d.branch7x7_3.conv     |  160x17x17  |  192x17x17   |   1.08 % |   0.90 % | Conv2d k=(7, 1) p=(3, 0) s=1 |
| Mixed_6d.branch7x7_3.bn       |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6d.branch7x7dbl_1.conv  |  768x17x17  |  160x17x17   |   0.62 % |   0.51 % | Conv2d k=1 p=0 s=1           |
| Mixed_6d.branch7x7dbl_1.bn    |  160x17x17  |  160x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6d.branch7x7dbl_2.conv  |  160x17x17  |  160x17x17   |   0.90 % |   0.75 % | Conv2d k=(7, 1) p=(3, 0) s=1 |
| Mixed_6d.branch7x7dbl_2.bn    |  160x17x17  |  160x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6d.branch7x7dbl_3.conv  |  160x17x17  |  160x17x17   |   0.90 % |   0.75 % | Conv2d k=(1, 7) p=(0, 3) s=1 |
| Mixed_6d.branch7x7dbl_3.bn    |  160x17x17  |  160x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6d.branch7x7dbl_4.conv  |  160x17x17  |  160x17x17   |   0.90 % |   0.75 % | Conv2d k=(7, 1) p=(3, 0) s=1 |
| Mixed_6d.branch7x7dbl_4.bn    |  160x17x17  |  160x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6d.branch7x7dbl_5.conv  |  160x17x17  |  192x17x17   |   1.08 % |   0.90 % | Conv2d k=(1, 7) p=(0, 3) s=1 |
| Mixed_6d.branch7x7dbl_5.bn    |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6d.branch_pool.conv     |  768x17x17  |  192x17x17   |   0.74 % |   0.62 % | Conv2d k=1 p=0 s=1           |
| Mixed_6d.branch_pool.bn       |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6e.branch1x1.conv       |  768x17x17  |  192x17x17   |   0.74 % |   0.62 % | Conv2d k=1 p=0 s=1           |
| Mixed_6e.branch1x1.bn         |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6e.branch7x7_1.conv     |  768x17x17  |  192x17x17   |   0.74 % |   0.62 % | Conv2d k=1 p=0 s=1           |
| Mixed_6e.branch7x7_1.bn       |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6e.branch7x7_2.conv     |  192x17x17  |  192x17x17   |   1.30 % |   1.08 % | Conv2d k=(1, 7) p=(0, 3) s=1 |
| Mixed_6e.branch7x7_2.bn       |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6e.branch7x7_3.conv     |  192x17x17  |  192x17x17   |   1.30 % |   1.08 % | Conv2d k=(7, 1) p=(3, 0) s=1 |
| Mixed_6e.branch7x7_3.bn       |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6e.branch7x7dbl_1.conv  |  768x17x17  |  192x17x17   |   0.74 % |   0.62 % | Conv2d k=1 p=0 s=1           |
| Mixed_6e.branch7x7dbl_1.bn    |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6e.branch7x7dbl_2.conv  |  192x17x17  |  192x17x17   |   1.30 % |   1.08 % | Conv2d k=(7, 1) p=(3, 0) s=1 |
| Mixed_6e.branch7x7dbl_2.bn    |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6e.branch7x7dbl_3.conv  |  192x17x17  |  192x17x17   |   1.30 % |   1.08 % | Conv2d k=(1, 7) p=(0, 3) s=1 |
| Mixed_6e.branch7x7dbl_3.bn    |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6e.branch7x7dbl_4.conv  |  192x17x17  |  192x17x17   |   1.30 % |   1.08 % | Conv2d k=(7, 1) p=(3, 0) s=1 |
| Mixed_6e.branch7x7dbl_4.bn    |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6e.branch7x7dbl_5.conv  |  192x17x17  |  192x17x17   |   1.30 % |   1.08 % | Conv2d k=(1, 7) p=(0, 3) s=1 |
| Mixed_6e.branch7x7dbl_5.bn    |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_6e.branch_pool.conv     |  768x17x17  |  192x17x17   |   0.74 % |   0.62 % | Conv2d k=1 p=0 s=1           |
| Mixed_6e.branch_pool.bn       |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_7a.branch3x3_1.conv     |  768x17x17  |  192x17x17   |   0.74 % |   0.62 % | Conv2d k=1 p=0 s=1           |
| Mixed_7a.branch3x3_1.bn       |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_7a.branch3x3_2.conv     |  192x17x17  |   320x8x8    |   0.62 % |   2.32 % | Conv2d k=3 p=0 s=2           |
| Mixed_7a.branch3x3_2.bn       |   320x8x8   |   320x8x8    |   0.00 % |   0.01 % | BatchNorm2d                  |
| Mixed_7a.branch7x7x3_1.conv   |  768x17x17  |  192x17x17   |   0.74 % |   0.62 % | Conv2d k=1 p=0 s=1           |
| Mixed_7a.branch7x7x3_1.bn     |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_7a.branch7x7x3_2.conv   |  192x17x17  |  192x17x17   |   1.30 % |   1.08 % | Conv2d k=(1, 7) p=(0, 3) s=1 |
| Mixed_7a.branch7x7x3_2.bn     |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_7a.branch7x7x3_3.conv   |  192x17x17  |  192x17x17   |   1.30 % |   1.08 % | Conv2d k=(7, 1) p=(3, 0) s=1 |
| Mixed_7a.branch7x7x3_3.bn     |  192x17x17  |  192x17x17   |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_7a.branch7x7x3_4.conv   |  192x17x17  |   192x8x8    |   0.37 % |   1.39 % | Conv2d k=3 p=0 s=2           |
| Mixed_7a.branch7x7x3_4.bn     |   192x8x8   |   192x8x8    |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_7b.branch1x1.conv       |   1280x8x8  |   320x8x8    |   0.46 % |   1.72 % | Conv2d k=1 p=0 s=1           |
| Mixed_7b.branch1x1.bn         |   320x8x8   |   320x8x8    |   0.00 % |   0.01 % | BatchNorm2d                  |
| Mixed_7b.branch3x3_1.conv     |   1280x8x8  |   384x8x8    |   0.55 % |   2.06 % | Conv2d k=1 p=0 s=1           |
| Mixed_7b.branch3x3_1.bn       |   384x8x8   |   384x8x8    |   0.00 % |   0.01 % | BatchNorm2d                  |
| Mixed_7b.branch3x3_2a.conv    |   384x8x8   |   384x8x8    |   0.49 % |   1.85 % | Conv2d k=(1, 3) p=(0, 1) s=1 |
| Mixed_7b.branch3x3_2a.bn      |   384x8x8   |   384x8x8    |   0.00 % |   0.01 % | BatchNorm2d                  |
| Mixed_7b.branch3x3_2b.conv    |   384x8x8   |   384x8x8    |   0.49 % |   1.85 % | Conv2d k=(3, 1) p=(1, 0) s=1 |
| Mixed_7b.branch3x3_2b.bn      |   384x8x8   |   384x8x8    |   0.00 % |   0.01 % | BatchNorm2d                  |
| Mixed_7b.branch3x3dbl_1.conv  |   1280x8x8  |   448x8x8    |   0.64 % |   2.40 % | Conv2d k=1 p=0 s=1           |
| Mixed_7b.branch3x3dbl_1.bn    |   448x8x8   |   448x8x8    |   0.00 % |   0.01 % | BatchNorm2d                  |
| Mixed_7b.branch3x3dbl_2.conv  |   448x8x8   |   384x8x8    |   1.72 % |   6.49 % | Conv2d k=3 p=1 s=1           |
| Mixed_7b.branch3x3dbl_2.bn    |   384x8x8   |   384x8x8    |   0.00 % |   0.01 % | BatchNorm2d                  |
| Mixed_7b.branch3x3dbl_3a.conv |   384x8x8   |   384x8x8    |   0.49 % |   1.85 % | Conv2d k=(1, 3) p=(0, 1) s=1 |
| Mixed_7b.branch3x3dbl_3a.bn   |   384x8x8   |   384x8x8    |   0.00 % |   0.01 % | BatchNorm2d                  |
| Mixed_7b.branch3x3dbl_3b.conv |   384x8x8   |   384x8x8    |   0.49 % |   1.85 % | Conv2d k=(3, 1) p=(1, 0) s=1 |
| Mixed_7b.branch3x3dbl_3b.bn   |   384x8x8   |   384x8x8    |   0.00 % |   0.01 % | BatchNorm2d                  |
| Mixed_7b.branch_pool.conv     |   1280x8x8  |   192x8x8    |   0.27 % |   1.03 % | Conv2d k=1 p=0 s=1           |
| Mixed_7b.branch_pool.bn       |   192x8x8   |   192x8x8    |   0.00 % |   0.00 % | BatchNorm2d                  |
| Mixed_7c.branch1x1.conv       |   2048x8x8  |   320x8x8    |   0.73 % |   2.75 % | Conv2d k=1 p=0 s=1           |
| Mixed_7c.branch1x1.bn         |   320x8x8   |   320x8x8    |   0.00 % |   0.01 % | BatchNorm2d                  |
| Mixed_7c.branch3x3_1.conv     |   2048x8x8  |   384x8x8    |   0.88 % |   3.29 % | Conv2d k=1 p=0 s=1           |
| Mixed_7c.branch3x3_1.bn       |   384x8x8   |   384x8x8    |   0.00 % |   0.01 % | BatchNorm2d                  |
| Mixed_7c.branch3x3_2a.conv    |   384x8x8   |   384x8x8    |   0.49 % |   1.85 % | Conv2d k=(1, 3) p=(0, 1) s=1 |
| Mixed_7c.branch3x3_2a.bn      |   384x8x8   |   384x8x8    |   0.00 % |   0.01 % | BatchNorm2d                  |
| Mixed_7c.branch3x3_2b.conv    |   384x8x8   |   384x8x8    |   0.49 % |   1.85 % | Conv2d k=(3, 1) p=(1, 0) s=1 |
| Mixed_7c.branch3x3_2b.bn      |   384x8x8   |   384x8x8    |   0.00 % |   0.01 % | BatchNorm2d                  |
| Mixed_7c.branch3x3dbl_1.conv  |   2048x8x8  |   448x8x8    |   1.02 % |   3.84 % | Conv2d k=1 p=0 s=1           |
| Mixed_7c.branch3x3dbl_1.bn    |   448x8x8   |   448x8x8    |   0.00 % |   0.01 % | BatchNorm2d                  |
| Mixed_7c.branch3x3dbl_2.conv  |   448x8x8   |   384x8x8    |   1.72 % |   6.49 % | Conv2d k=3 p=1 s=1           |
| Mixed_7c.branch3x3dbl_2.bn    |   384x8x8   |   384x8x8    |   0.00 % |   0.01 % | BatchNorm2d                  |
| Mixed_7c.branch3x3dbl_3a.conv |   384x8x8   |   384x8x8    |   0.49 % |   1.85 % | Conv2d k=(1, 3) p=(0, 1) s=1 |
| Mixed_7c.branch3x3dbl_3a.bn   |   384x8x8   |   384x8x8    |   0.00 % |   0.01 % | BatchNorm2d                  |
| Mixed_7c.branch3x3dbl_3b.conv |   384x8x8   |   384x8x8    |   0.49 % |   1.85 % | Conv2d k=(3, 1) p=(1, 0) s=1 |
| Mixed_7c.branch3x3dbl_3b.bn   |   384x8x8   |   384x8x8    |   0.00 % |   0.01 % | BatchNorm2d                  |
| Mixed_7c.branch_pool.conv     |   2048x8x8  |   192x8x8    |   0.44 % |   1.65 % | Conv2d k=1 p=0 s=1           |
| Mixed_7c.branch_pool.bn       |   192x8x8   |   192x8x8    |   0.00 % |   0.00 % | BatchNorm2d                  |
| avgpool                       |   2048x8x8  |   2048x1x1   |   0.00 % |   0.00 % | AdaptiveAvgPool2d            |
| dropout                       |   2048x1x1  |   2048x1x1   |   0.00 % |   0.00 % | Dropout                      |
| fc                            |     2048    |     1000     |   0.04 % |   8.58 % | Linear                       |
| Total                         |  3x299x299  |     1000     |   5.75 G |  23.87 M | Inception3                   |