| Name                             | Input shape | Output shape |     MACs |   Params | Description        |
|:--------------------------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| features.0                       |  3x224x224  |  96x109x109  |  20.47 % |   1.14 % | Conv2d k=7 p=0 s=2 |
| features.1                       |  96x109x109 |  96x109x109  |   0.00 % |   0.00 % | ReLU               |
| features.2                       |  96x109x109 |   96x54x54   |   0.00 % |   0.00 % | MaxPool2d k=3 s=2  |
| features.3.squeeze               |   96x54x54  |   16x54x54   |   0.55 % |   0.12 % | Conv2d k=1 p=0 s=1 |
| features.3.squeeze_activation    |   16x54x54  |   16x54x54   |   0.00 % |   0.00 % | ReLU               |
| features.3.expand1x1             |   16x54x54  |   64x54x54   |   0.36 % |   0.09 % | Conv2d k=1 p=0 s=1 |
| features.3.expand1x1_activation  |   64x54x54  |   64x54x54   |   0.00 % |   0.00 % | ReLU               |
| features.3.expand3x3             |   16x54x54  |   64x54x54   |   3.28 % |   0.74 % | Conv2d k=3 p=1 s=1 |
| features.3.expand3x3_activation  |   64x54x54  |   64x54x54   |   0.00 % |   0.00 % | ReLU               |
| features.4.squeeze               |  128x54x54  |   16x54x54   |   0.73 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| features.4.squeeze_activation    |   16x54x54  |   16x54x54   |   0.00 % |   0.00 % | ReLU               |
| features.4.expand1x1             |   16x54x54  |   64x54x54   |   0.36 % |   0.09 % | Conv2d k=1 p=0 s=1 |
| features.4.expand1x1_activation  |   64x54x54  |   64x54x54   |   0.00 % |   0.00 % | ReLU               |
| features.4.expand3x3             |   16x54x54  |   64x54x54   |   3.28 % |   0.74 % | Conv2d k=3 p=1 s=1 |
| features.4.expand3x3_activation  |   64x54x54  |   64x54x54   |   0.00 % |   0.00 % | ReLU               |
| features.5.squeeze               |  128x54x54  |   32x54x54   |   1.46 % |   0.33 % | Conv2d k=1 p=0 s=1 |
| features.5.squeeze_activation    |   32x54x54  |   32x54x54   |   0.00 % |   0.00 % | ReLU               |
| features.5.expand1x1             |   32x54x54  |  128x54x54   |   1.46 % |   0.34 % | Conv2d k=1 p=0 s=1 |
| features.5.expand1x1_activation  |  128x54x54  |  128x54x54   |   0.00 % |   0.00 % | ReLU               |
| features.5.expand3x3             |   32x54x54  |  128x54x54   |  13.13 % |   2.96 % | Conv2d k=3 p=1 s=1 |
| features.5.expand3x3_activation  |  128x54x54  |  128x54x54   |   0.00 % |   0.00 % | ReLU               |
| features.6                       |  256x54x54  |  256x27x27   |   0.00 % |   0.00 % | MaxPool2d k=3 s=2  |
| features.7.squeeze               |  256x27x27  |   32x27x27   |   0.73 % |   0.66 % | Conv2d k=1 p=0 s=1 |
| features.7.squeeze_activation    |   32x27x27  |   32x27x27   |   0.00 % |   0.00 % | ReLU               |
| features.7.expand1x1             |   32x27x27  |  128x27x27   |   0.36 % |   0.34 % | Conv2d k=1 p=0 s=1 |
| features.7.expand1x1_activation  |  128x27x27  |  128x27x27   |   0.00 % |   0.00 % | ReLU               |
| features.7.expand3x3             |   32x27x27  |  128x27x27   |   3.28 % |   2.96 % | Conv2d k=3 p=1 s=1 |
| features.7.expand3x3_activation  |  128x27x27  |  128x27x27   |   0.00 % |   0.00 % | ReLU               |
| features.8.squeeze               |  256x27x27  |   48x27x27   |   1.09 % |   0.99 % | Conv2d k=1 p=0 s=1 |
| features.8.squeeze_activation    |   48x27x27  |   48x27x27   |   0.00 % |   0.00 % | ReLU               |
| features.8.expand1x1             |   48x27x27  |  192x27x27   |   0.82 % |   0.75 % | Conv2d k=1 p=0 s=1 |
| features.8.expand1x1_activation  |  192x27x27  |  192x27x27   |   0.00 % |   0.00 % | ReLU               |
| features.8.expand3x3             |   48x27x27  |  192x27x27   |   7.38 % |   6.66 % | Conv2d k=3 p=1 s=1 |
| features.8.expand3x3_activation  |  192x27x27  |  192x27x27   |   0.00 % |   0.00 % | ReLU               |
| features.9.squeeze               |  384x27x27  |   48x27x27   |   1.64 % |   1.48 % | Conv2d k=1 p=0 s=1 |
| features.9.squeeze_activation    |   48x27x27  |   48x27x27   |   0.00 % |   0.00 % | ReLU               |
| features.9.expand1x1             |   48x27x27  |  192x27x27   |   0.82 % |   0.75 % | Conv2d k=1 p=0 s=1 |
| features.9.expand1x1_activation  |  192x27x27  |  192x27x27   |   0.00 % |   0.00 % | ReLU               |
| features.9.expand3x3             |   48x27x27  |  192x27x27   |   7.38 % |   6.66 % | Conv2d k=3 p=1 s=1 |
| features.9.expand3x3_activation  |  192x27x27  |  192x27x27   |   0.00 % |   0.00 % | ReLU               |
| features.10.squeeze              |  384x27x27  |   64x27x27   |   2.19 % |   1.97 % | Conv2d k=1 p=0 s=1 |
| features.10.squeeze_activation   |   64x27x27  |   64x27x27   |   0.00 % |   0.00 % | ReLU               |
| features.10.expand1x1            |   64x27x27  |  256x27x27   |   1.46 % |   1.33 % | Conv2d k=1 p=0 s=1 |
| features.10.expand1x1_activation |  256x27x27  |  256x27x27   |   0.00 % |   0.00 % | ReLU               |
| features.10.expand3x3            |   64x27x27  |  256x27x27   |  13.13 % |  11.83 % | Conv2d k=3 p=1 s=1 |
| features.10.expand3x3_activation |  256x27x27  |  256x27x27   |   0.00 % |   0.00 % | ReLU               |
| features.11                      |  512x27x27  |  512x13x13   |   0.00 % |   0.00 % | MaxPool2d k=3 s=2  |
| features.12.squeeze              |  512x13x13  |   64x13x13   |   0.68 % |   2.63 % | Conv2d k=1 p=0 s=1 |
| features.12.squeeze_activation   |   64x13x13  |   64x13x13   |   0.00 % |   0.00 % | ReLU               |
| features.12.expand1x1            |   64x13x13  |  256x13x13   |   0.34 % |   1.33 % | Conv2d k=1 p=0 s=1 |
| features.12.expand1x1_activation |  256x13x13  |  256x13x13   |   0.00 % |   0.00 % | ReLU               |
| features.12.expand3x3            |   64x13x13  |  256x13x13   |   3.04 % |  11.83 % | Conv2d k=3 p=1 s=1 |
| features.12.expand3x3_activation |  256x13x13  |  256x13x13   |   0.00 % |   0.00 % | ReLU               |
| classifier.0                     |  512x13x13  |  512x13x13   |   0.00 % |   0.00 % | Dropout            |
| classifier.1                     |  512x13x13  |  1000x13x13  |  10.57 % |  41.09 % | Conv2d k=1 p=0 s=1 |
| classifier.2                     |  1000x13x13 |  1000x13x13  |   0.00 % |   0.00 % | ReLU               |
| classifier.3                     |  1000x13x13 |   1000x1x1   |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| Total                            |  3x224x224  |   1000x1x1   | 818.93 M |   1.25 M | SqueezeNet         |