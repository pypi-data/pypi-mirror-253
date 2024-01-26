| Name         | Input shape | Output shape |     MACs |   Params | Description        |
|:------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| features.0   |  3x224x224  |  64x224x224  |   0.56 % |   0.00 % | Conv2d k=3 p=1 s=1 |
| features.1   |  64x224x224 |  64x224x224  |   0.00 % |   0.00 % | ReLU               |
| features.2   |  64x224x224 |  64x224x224  |  11.96 % |   0.03 % | Conv2d k=3 p=1 s=1 |
| features.3   |  64x224x224 |  64x224x224  |   0.00 % |   0.00 % | ReLU               |
| features.4   |  64x224x224 |  64x112x112  |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.5   |  64x112x112 | 128x112x112  |   5.98 % |   0.05 % | Conv2d k=3 p=1 s=1 |
| features.6   | 128x112x112 | 128x112x112  |   0.00 % |   0.00 % | ReLU               |
| features.7   | 128x112x112 | 128x112x112  |  11.96 % |   0.11 % | Conv2d k=3 p=1 s=1 |
| features.8   | 128x112x112 | 128x112x112  |   0.00 % |   0.00 % | ReLU               |
| features.9   | 128x112x112 |  128x56x56   |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.10  |  128x56x56  |  256x56x56   |   5.98 % |   0.21 % | Conv2d k=3 p=1 s=1 |
| features.11  |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.12  |  256x56x56  |  256x56x56   |  11.96 % |   0.43 % | Conv2d k=3 p=1 s=1 |
| features.13  |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.14  |  256x56x56  |  256x56x56   |  11.96 % |   0.43 % | Conv2d k=3 p=1 s=1 |
| features.15  |  256x56x56  |  256x56x56   |   0.00 % |   0.00 % | ReLU               |
| features.16  |  256x56x56  |  256x28x28   |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.17  |  256x28x28  |  512x28x28   |   5.98 % |   0.85 % | Conv2d k=3 p=1 s=1 |
| features.18  |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.19  |  512x28x28  |  512x28x28   |  11.96 % |   1.71 % | Conv2d k=3 p=1 s=1 |
| features.20  |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.21  |  512x28x28  |  512x28x28   |  11.96 % |   1.71 % | Conv2d k=3 p=1 s=1 |
| features.22  |  512x28x28  |  512x28x28   |   0.00 % |   0.00 % | ReLU               |
| features.23  |  512x28x28  |  512x14x14   |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| features.24  |  512x14x14  |  512x14x14   |   2.99 % |   1.71 % | Conv2d k=3 p=1 s=1 |
| features.25  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.26  |  512x14x14  |  512x14x14   |   2.99 % |   1.71 % | Conv2d k=3 p=1 s=1 |
| features.27  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.28  |  512x14x14  |  512x14x14   |   2.99 % |   1.71 % | Conv2d k=3 p=1 s=1 |
| features.29  |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | ReLU               |
| features.30  |  512x14x14  |   512x7x7    |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| avgpool      |   512x7x7   |   512x7x7    |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| classifier.0 |    25088    |     4096     |   0.66 % |  74.27 % | Linear             |
| classifier.1 |     4096    |     4096     |   0.00 % |   0.00 % | ReLU               |
| classifier.2 |     4096    |     4096     |   0.00 % |   0.00 % | Dropout            |
| classifier.3 |     4096    |     4096     |   0.11 % |  12.13 % | Linear             |
| classifier.4 |     4096    |     4096     |   0.00 % |   0.00 % | ReLU               |
| classifier.5 |     4096    |     4096     |   0.00 % |   0.00 % | Dropout            |
| classifier.6 |     4096    |     1000     |   0.03 % |   2.96 % | Linear             |
| Total        |  3x224x224  |     1000     |  15.47 G | 138.36 M | VGG                |