| Name         | Input shape | Output shape |     MACs |   Params | Description         |
|:------------:|:-----------:|:------------:|:--------:|:--------:|:-------------------:|
| features.0   |  3x224x224  |   64x55x55   |   9.84 % |   0.04 % | Conv2d k=11 p=2 s=4 |
| features.1   |   64x55x55  |   64x55x55   |   0.00 % |   0.00 % | ReLU                |
| features.2   |   64x55x55  |   64x27x27   |   0.00 % |   0.00 % | MaxPool2d k=3 s=2   |
| features.3   |   64x27x27  |  192x27x27   |  31.36 % |   0.50 % | Conv2d k=5 p=2 s=1  |
| features.4   |  192x27x27  |  192x27x27   |   0.00 % |   0.00 % | ReLU                |
| features.5   |  192x27x27  |  192x13x13   |   0.00 % |   0.00 % | MaxPool2d k=3 s=2   |
| features.6   |  192x13x13  |  384x13x13   |  15.70 % |   1.09 % | Conv2d k=3 p=1 s=1  |
| features.7   |  384x13x13  |  384x13x13   |   0.00 % |   0.00 % | ReLU                |
| features.8   |  384x13x13  |  256x13x13   |  20.93 % |   1.45 % | Conv2d k=3 p=1 s=1  |
| features.9   |  256x13x13  |  256x13x13   |   0.00 % |   0.00 % | ReLU                |
| features.10  |  256x13x13  |  256x13x13   |  13.96 % |   0.97 % | Conv2d k=3 p=1 s=1  |
| features.11  |  256x13x13  |  256x13x13   |   0.00 % |   0.00 % | ReLU                |
| features.12  |  256x13x13  |   256x6x6    |   0.00 % |   0.00 % | MaxPool2d k=3 s=2   |
| avgpool      |   256x6x6   |   256x6x6    |   0.00 % |   0.00 % | AdaptiveAvgPool2d   |
| classifier.0 |     9216    |     9216     |   0.00 % |   0.00 % | Dropout             |
| classifier.1 |     9216    |     4096     |   5.29 % |  61.79 % | Linear              |
| classifier.2 |     4096    |     4096     |   0.00 % |   0.00 % | ReLU                |
| classifier.3 |     4096    |     4096     |   0.00 % |   0.00 % | Dropout             |
| classifier.4 |     4096    |     4096     |   2.35 % |  27.46 % | Linear              |
| classifier.5 |     4096    |     4096     |   0.00 % |   0.00 % | ReLU                |
| classifier.6 |     4096    |     1000     |   0.57 % |   6.71 % | Linear              |
| Total        |  3x224x224  |     1000     | 714.22 M |  61.10 M | AlexNet             |