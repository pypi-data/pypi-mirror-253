| Name         | Input shape | Output shape |     MACs |   Params | Description        |
|:------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| features.0   |  3x224x224  |  64x224x224  |   0.77 % |   0.00 % | Conv2d k=3 p=1 s=1 |
| features.1   |  64x224x224 |  64x224x224  |   0.00 % |   0.00 % | ReLU               |
| features.2   |  64x224x224 |  64x224x224  |  16.36 % |   0.03 % | Conv2d k=3 p=1 s=1 |
| features.3   |  64x224x224 |  64x224x224  |   0.00 % |   0.00 % | ReLU               |
| features.4   |  64x224x224 |  64x112x112  |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.5   |  64x112x112 | 128x112x112  |   8.18 % |   0.06 % | Conv2d k=3 p=1 s=1 |
| features.6   | 128x112x112 | 128x112x112  |   0.00 % |   0.00 % | ReLU               |
| features.7   | 128x112x112 | 128x112x112  |  16.36 % |   0.11 % | Conv2d k=3 p=1 s=1 |
| features.8   | 128x112x112 | 128x112x112  |   0.00 % |   0.00 % | ReLU               |
| features.9   | 128x112x112 |  128x56x56   |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.10  |  128x56x56  |  256x56x56   |   8.18 % |   0.22 % | Conv2d k=3 p=1 s=1 |
| features.11  |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.12  |  256x56x56  |  256x56x56   |  16.36 % |   0.44 % | Conv2d k=3 p=1 s=1 |
| features.13  |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.14  |  256x56x56  |  256x28x28   |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.15  |  256x28x28  |  512x28x28   |   8.18 % |   0.89 % | Conv2d k=3 p=1 s=1 |
| features.16  |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.17  |  512x28x28  |  512x28x28   |  16.36 % |   1.77 % | Conv2d k=3 p=1 s=1 |
| features.18  |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.19  |  512x28x28  |  512x14x14   |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.20  |  512x14x14  |  512x14x14   |   4.09 % |   1.77 % | Conv2d k=3 p=1 s=1 |
| features.21  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.22  |  512x14x14  |  512x14x14   |   4.09 % |   1.77 % | Conv2d k=3 p=1 s=1 |
| features.23  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.24  |  512x14x14  |   512x7x7    |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| avgpool      |   512x7x7   |   512x7x7    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| classifier.0 |    25088    |     4096     |   0.91 % |  77.24 % | Linear             |
| classifier.1 |     4096    |     4096     |   0.00 % |   0.00 % | ReLU               |
| classifier.2 |     4096    |     4096     |   0.00 % |   0.00 % | Dropout            |
| classifier.3 |     4096    |     4096     |   0.15 % |  12.61 % | Linear             |
| classifier.4 |     4096    |     4096     |   0.00 % |   0.00 % | ReLU               |
| classifier.5 |     4096    |     4096     |   0.00 % |   0.00 % | Dropout            |
| classifier.6 |     4096    |     1000     |   0.04 % |   3.08 % | Linear             |
| Total        |  3x224x224  |     1000     |  11.31 G | 133.05 M | VGG                |