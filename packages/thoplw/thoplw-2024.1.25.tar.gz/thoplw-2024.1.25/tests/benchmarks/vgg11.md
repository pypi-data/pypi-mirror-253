| Name         | Input shape | Output shape |     MACs |   Params | Description        |
|:------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| features.0   |  3x224x224  |  64x224x224  |   1.14 % |   0.00 % | Conv2d k=3 p=1 s=1 |
| features.1   |  64x224x224 |  64x224x224  |   0.00 % |   0.00 % | ReLU               |
| features.2   |  64x224x224 |  64x112x112  |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.3   |  64x112x112 | 128x112x112  |  12.15 % |   0.06 % | Conv2d k=3 p=1 s=1 |
| features.4   | 128x112x112 | 128x112x112  |   0.00 % |   0.00 % | ReLU               |
| features.5   | 128x112x112 |  128x56x56   |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.6   |  128x56x56  |  256x56x56   |  12.15 % |   0.22 % | Conv2d k=3 p=1 s=1 |
| features.7   |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.8   |  256x56x56  |  256x56x56   |  24.31 % |   0.44 % | Conv2d k=3 p=1 s=1 |
| features.9   |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.10  |  256x56x56  |  256x28x28   |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.11  |  256x28x28  |  512x28x28   |  12.15 % |   0.89 % | Conv2d k=3 p=1 s=1 |
| features.12  |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.13  |  512x28x28  |  512x28x28   |  24.31 % |   1.78 % | Conv2d k=3 p=1 s=1 |
| features.14  |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.15  |  512x28x28  |  512x14x14   |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.16  |  512x14x14  |  512x14x14   |   6.08 % |   1.78 % | Conv2d k=3 p=1 s=1 |
| features.17  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.18  |  512x14x14  |  512x14x14   |   6.08 % |   1.78 % | Conv2d k=3 p=1 s=1 |
| features.19  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.20  |  512x14x14  |   512x7x7    |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| avgpool      |   512x7x7   |   512x7x7    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| classifier.0 |    25088    |     4096     |   1.35 % |  77.35 % | Linear             |
| classifier.1 |     4096    |     4096     |   0.00 % |   0.00 % | ReLU               |
| classifier.2 |     4096    |     4096     |   0.00 % |   0.00 % | Dropout            |
| classifier.3 |     4096    |     4096     |   0.22 % |  12.63 % | Linear             |
| classifier.4 |     4096    |     4096     |   0.00 % |   0.00 % | ReLU               |
| classifier.5 |     4096    |     4096     |   0.00 % |   0.00 % | Dropout            |
| classifier.6 |     4096    |     1000     |   0.05 % |   3.08 % | Linear             |
| Total        |  3x224x224  |     1000     |   7.61 G | 132.86 M | VGG                |