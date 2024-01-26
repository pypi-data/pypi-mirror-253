| Name                             | Input shape | Output shape |     MACs |   Params | Description        |
|:--------------------------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| features.0                       |  3x224x224  |  64x111x111  |   6.10 % |   0.15 % | Conv2d k=3 p=0 s=2 |
| features.1                       |  64x111x111 |  64x111x111  |   0.00 % |   0.00 % | ReLU               |
| features.2                       |  64x111x111 |   64x55x55   |   0.00 % |   0.00 % | MaxPool2d k=3 s=2  |
| features.3.squeeze               |   64x55x55  |   16x55x55   |   0.89 % |   0.08 % | Conv2d k=1 p=0 s=1 |
| features.3.squeeze_activation    |   16x55x55  |   16x55x55   |   0.00 % |   0.00 % | ReLU               |
| features.3.expand1x1             |   16x55x55  |   64x55x55   |   0.89 % |   0.09 % | Conv2d k=1 p=0 s=1 |
| features.3.expand1x1_activation  |   64x55x55  |   64x55x55   |   0.00 % |   0.00 % | ReLU               |
| features.3.expand3x3             |   16x55x55  |   64x55x55   |   7.98 % |   0.75 % | Conv2d k=3 p=1 s=1 |
| features.3.expand3x3_activation  |   64x55x55  |   64x55x55   |   0.00 % |   0.00 % | ReLU               |
| features.4.squeeze               |  128x55x55  |   16x55x55   |   1.77 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| features.4.squeeze_activation    |   16x55x55  |   16x55x55   |   0.00 % |   0.00 % | ReLU               |
| features.4.expand1x1             |   16x55x55  |   64x55x55   |   0.89 % |   0.09 % | Conv2d k=1 p=0 s=1 |
| features.4.expand1x1_activation  |   64x55x55  |   64x55x55   |   0.00 % |   0.00 % | ReLU               |
| features.4.expand3x3             |   16x55x55  |   64x55x55   |   7.98 % |   0.75 % | Conv2d k=3 p=1 s=1 |
| features.4.expand3x3_activation  |   64x55x55  |   64x55x55   |   0.00 % |   0.00 % | ReLU               |
| features.5                       |  128x55x55  |  128x27x27   |   0.00 % |   0.00 % | MaxPool2d k=3 s=2  |
| features.6.squeeze               |  128x27x27  |   32x27x27   |   0.86 % |   0.33 % | Conv2d k=1 p=0 s=1 |
| features.6.squeeze_activation    |   32x27x27  |   32x27x27   |   0.00 % |   0.00 % | ReLU               |
| features.6.expand1x1             |   32x27x27  |  128x27x27   |   0.86 % |   0.34 % | Conv2d k=1 p=0 s=1 |
| features.6.expand1x1_activation  |  128x27x27  |  128x27x27   |   0.00 % |   0.00 % | ReLU               |
| features.6.expand3x3             |   32x27x27  |  128x27x27   |   7.70 % |   2.99 % | Conv2d k=3 p=1 s=1 |
| features.6.expand3x3_activation  |  128x27x27  |  128x27x27   |   0.00 % |   0.00 % | ReLU               |
| features.7.squeeze               |  256x27x27  |   32x27x27   |   1.71 % |   0.67 % | Conv2d k=1 p=0 s=1 |
| features.7.squeeze_activation    |   32x27x27  |   32x27x27   |   0.00 % |   0.00 % | ReLU               |
| features.7.expand1x1             |   32x27x27  |  128x27x27   |   0.86 % |   0.34 % | Conv2d k=1 p=0 s=1 |
| features.7.expand1x1_activation  |  128x27x27  |  128x27x27   |   0.00 % |   0.00 % | ReLU               |
| features.7.expand3x3             |   32x27x27  |  128x27x27   |   7.70 % |   2.99 % | Conv2d k=3 p=1 s=1 |
| features.7.expand3x3_activation  |  128x27x27  |  128x27x27   |   0.00 % |   0.00 % | ReLU               |
| features.8                       |  256x27x27  |  256x13x13   |   0.00 % |   0.00 % | MaxPool2d k=3 s=2  |
| features.9.squeeze               |  256x13x13  |   48x13x13   |   0.59 % |   1.00 % | Conv2d k=1 p=0 s=1 |
| features.9.squeeze_activation    |   48x13x13  |   48x13x13   |   0.00 % |   0.00 % | ReLU               |
| features.9.expand1x1             |   48x13x13  |  192x13x13   |   0.45 % |   0.76 % | Conv2d k=1 p=0 s=1 |
| features.9.expand1x1_activation  |  192x13x13  |  192x13x13   |   0.00 % |   0.00 % | ReLU               |
| features.9.expand3x3             |   48x13x13  |  192x13x13   |   4.01 % |   6.73 % | Conv2d k=3 p=1 s=1 |
| features.9.expand3x3_activation  |  192x13x13  |  192x13x13   |   0.00 % |   0.00 % | ReLU               |
| features.10.squeeze              |  384x13x13  |   48x13x13   |   0.89 % |   1.50 % | Conv2d k=1 p=0 s=1 |
| features.10.squeeze_activation   |   48x13x13  |   48x13x13   |   0.00 % |   0.00 % | ReLU               |
| features.10.expand1x1            |   48x13x13  |  192x13x13   |   0.45 % |   0.76 % | Conv2d k=1 p=0 s=1 |
| features.10.expand1x1_activation |  192x13x13  |  192x13x13   |   0.00 % |   0.00 % | ReLU               |
| features.10.expand3x3            |   48x13x13  |  192x13x13   |   4.01 % |   6.73 % | Conv2d k=3 p=1 s=1 |
| features.10.expand3x3_activation |  192x13x13  |  192x13x13   |   0.00 % |   0.00 % | ReLU               |
| features.11.squeeze              |  384x13x13  |   64x13x13   |   1.19 % |   1.99 % | Conv2d k=1 p=0 s=1 |
| features.11.squeeze_activation   |   64x13x13  |   64x13x13   |   0.00 % |   0.00 % | ReLU               |
| features.11.expand1x1            |   64x13x13  |  256x13x13   |   0.79 % |   1.35 % | Conv2d k=1 p=0 s=1 |
| features.11.expand1x1_activation |  256x13x13  |  256x13x13   |   0.00 % |   0.00 % | ReLU               |
| features.11.expand3x3            |   64x13x13  |  256x13x13   |   7.14 % |  11.96 % | Conv2d k=3 p=1 s=1 |
| features.11.expand3x3_activation |  256x13x13  |  256x13x13   |   0.00 % |   0.00 % | ReLU               |
| features.12.squeeze              |  512x13x13  |   64x13x13   |   1.59 % |   2.66 % | Conv2d k=1 p=0 s=1 |
| features.12.squeeze_activation   |   64x13x13  |   64x13x13   |   0.00 % |   0.00 % | ReLU               |
| features.12.expand1x1            |   64x13x13  |  256x13x13   |   0.79 % |   1.35 % | Conv2d k=1 p=0 s=1 |
| features.12.expand1x1_activation |  256x13x13  |  256x13x13   |   0.00 % |   0.00 % | ReLU               |
| features.12.expand3x3            |   64x13x13  |  256x13x13   |   7.14 % |  11.96 % | Conv2d k=3 p=1 s=1 |
| features.12.expand3x3_activation |  256x13x13  |  256x13x13   |   0.00 % |   0.00 % | ReLU               |
| classifier.0                     |  512x13x13  |  512x13x13   |   0.00 % |   0.00 % | Dropout            |
| classifier.1                     |  512x13x13  |  1000x13x13  |  24.78 % |  41.52 % | Conv2d k=1 p=0 s=1 |
| classifier.2                     |  1000x13x13 |  1000x13x13  |   0.00 % |   0.00 % | ReLU               |
| classifier.3                     |  1000x13x13 |   1000x1x1   |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| Total                            |  3x224x224  |   1000x1x1   | 349.16 M |   1.24 M | SqueezeNet         |