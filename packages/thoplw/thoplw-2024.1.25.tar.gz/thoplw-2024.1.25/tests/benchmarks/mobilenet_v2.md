| Name                 | Input shape | Output shape |     MACs |   Params | Description        |
|:--------------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| features.0.0         |  3x224x224  |  32x112x112  |   3.31 % |   0.02 % | Conv2d k=3 p=1 s=2 |
| features.0.1         |  32x112x112 |  32x112x112  |   0.49 % |   0.00 % | BatchNorm2d        |
| features.0.2         |  32x112x112 |  32x112x112  |   0.00 % |   0.00 % | ReLU6              |
| features.1.conv.0.0  |  32x112x112 |  32x112x112  |   1.10 % |   0.01 % | Conv2d k=3 p=1 s=1 |
| features.1.conv.0.1  |  32x112x112 |  32x112x112  |   0.49 % |   0.00 % | BatchNorm2d        |
| features.1.conv.0.2  |  32x112x112 |  32x112x112  |   0.00 % |   0.00 % | ReLU6              |
| features.1.conv.1    |  32x112x112 |  16x112x112  |   1.96 % |   0.01 % | Conv2d k=1 p=0 s=1 |
| features.1.conv.2    |  16x112x112 |  16x112x112  |   0.25 % |   0.00 % | BatchNorm2d        |
| features.2.conv.0.0  |  16x112x112 |  96x112x112  |   5.88 % |   0.04 % | Conv2d k=1 p=0 s=1 |
| features.2.conv.0.1  |  96x112x112 |  96x112x112  |   1.47 % |   0.01 % | BatchNorm2d        |
| features.2.conv.0.2  |  96x112x112 |  96x112x112  |   0.00 % |   0.00 % | ReLU6              |
| features.2.conv.1.0  |  96x112x112 |   96x56x56   |   0.83 % |   0.02 % | Conv2d k=3 p=1 s=2 |
| features.2.conv.1.1  |   96x56x56  |   96x56x56   |   0.37 % |   0.01 % | BatchNorm2d        |
| features.2.conv.1.2  |   96x56x56  |   96x56x56   |   0.00 % |   0.00 % | ReLU6              |
| features.2.conv.2    |   96x56x56  |   24x56x56   |   2.21 % |   0.07 % | Conv2d k=1 p=0 s=1 |
| features.2.conv.3    |   24x56x56  |   24x56x56   |   0.09 % |   0.00 % | BatchNorm2d        |
| features.3.conv.0.0  |   24x56x56  |  144x56x56   |   3.31 % |   0.10 % | Conv2d k=1 p=0 s=1 |
| features.3.conv.0.1  |  144x56x56  |  144x56x56   |   0.55 % |   0.02 % | BatchNorm2d        |
| features.3.conv.0.2  |  144x56x56  |  144x56x56   |   0.00 % |   0.00 % | ReLU6              |
| features.3.conv.1.0  |  144x56x56  |  144x56x56   |   1.24 % |   0.04 % | Conv2d k=3 p=1 s=1 |
| features.3.conv.1.1  |  144x56x56  |  144x56x56   |   0.55 % |   0.02 % | BatchNorm2d        |
| features.3.conv.1.2  |  144x56x56  |  144x56x56   |   0.00 % |   0.00 % | ReLU6              |
| features.3.conv.2    |  144x56x56  |   24x56x56   |   3.31 % |   0.10 % | Conv2d k=1 p=0 s=1 |
| features.3.conv.3    |   24x56x56  |   24x56x56   |   0.09 % |   0.00 % | BatchNorm2d        |
| features.4.conv.0.0  |   24x56x56  |  144x56x56   |   3.31 % |   0.10 % | Conv2d k=1 p=0 s=1 |
| features.4.conv.0.1  |  144x56x56  |  144x56x56   |   0.55 % |   0.02 % | BatchNorm2d        |
| features.4.conv.0.2  |  144x56x56  |  144x56x56   |   0.00 % |   0.00 % | ReLU6              |
| features.4.conv.1.0  |  144x56x56  |  144x28x28   |   0.31 % |   0.04 % | Conv2d k=3 p=1 s=2 |
| features.4.conv.1.1  |  144x28x28  |  144x28x28   |   0.14 % |   0.02 % | BatchNorm2d        |
| features.4.conv.1.2  |  144x28x28  |  144x28x28   |   0.00 % |   0.00 % | ReLU6              |
| features.4.conv.2    |  144x28x28  |   32x28x28   |   1.10 % |   0.13 % | Conv2d k=1 p=0 s=1 |
| features.4.conv.3    |   32x28x28  |   32x28x28   |   0.03 % |   0.00 % | BatchNorm2d        |
| features.5.conv.0.0  |   32x28x28  |  192x28x28   |   1.47 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| features.5.conv.0.1  |  192x28x28  |  192x28x28   |   0.18 % |   0.02 % | BatchNorm2d        |
| features.5.conv.0.2  |  192x28x28  |  192x28x28   |   0.00 % |   0.00 % | ReLU6              |
| features.5.conv.1.0  |  192x28x28  |  192x28x28   |   0.41 % |   0.05 % | Conv2d k=3 p=1 s=1 |
| features.5.conv.1.1  |  192x28x28  |  192x28x28   |   0.18 % |   0.02 % | BatchNorm2d        |
| features.5.conv.1.2  |  192x28x28  |  192x28x28   |   0.00 % |   0.00 % | ReLU6              |
| features.5.conv.2    |  192x28x28  |   32x28x28   |   1.47 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| features.5.conv.3    |   32x28x28  |   32x28x28   |   0.03 % |   0.00 % | BatchNorm2d        |
| features.6.conv.0.0  |   32x28x28  |  192x28x28   |   1.47 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| features.6.conv.0.1  |  192x28x28  |  192x28x28   |   0.18 % |   0.02 % | BatchNorm2d        |
| features.6.conv.0.2  |  192x28x28  |  192x28x28   |   0.00 % |   0.00 % | ReLU6              |
| features.6.conv.1.0  |  192x28x28  |  192x28x28   |   0.41 % |   0.05 % | Conv2d k=3 p=1 s=1 |
| features.6.conv.1.1  |  192x28x28  |  192x28x28   |   0.18 % |   0.02 % | BatchNorm2d        |
| features.6.conv.1.2  |  192x28x28  |  192x28x28   |   0.00 % |   0.00 % | ReLU6              |
| features.6.conv.2    |  192x28x28  |   32x28x28   |   1.47 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| features.6.conv.3    |   32x28x28  |   32x28x28   |   0.03 % |   0.00 % | BatchNorm2d        |
| features.7.conv.0.0  |   32x28x28  |  192x28x28   |   1.47 % |   0.17 % | Conv2d k=1 p=0 s=1 |
| features.7.conv.0.1  |  192x28x28  |  192x28x28   |   0.18 % |   0.02 % | BatchNorm2d        |
| features.7.conv.0.2  |  192x28x28  |  192x28x28   |   0.00 % |   0.00 % | ReLU6              |
| features.7.conv.1.0  |  192x28x28  |  192x14x14   |   0.10 % |   0.05 % | Conv2d k=3 p=1 s=2 |
| features.7.conv.1.1  |  192x14x14  |  192x14x14   |   0.05 % |   0.02 % | BatchNorm2d        |
| features.7.conv.1.2  |  192x14x14  |  192x14x14   |   0.00 % |   0.00 % | ReLU6              |
| features.7.conv.2    |  192x14x14  |   64x14x14   |   0.74 % |   0.35 % | Conv2d k=1 p=0 s=1 |
| features.7.conv.3    |   64x14x14  |   64x14x14   |   0.02 % |   0.01 % | BatchNorm2d        |
| features.8.conv.0.0  |   64x14x14  |  384x14x14   |   1.47 % |   0.69 % | Conv2d k=1 p=0 s=1 |
| features.8.conv.0.1  |  384x14x14  |  384x14x14   |   0.09 % |   0.04 % | BatchNorm2d        |
| features.8.conv.0.2  |  384x14x14  |  384x14x14   |   0.00 % |   0.00 % | ReLU6              |
| features.8.conv.1.0  |  384x14x14  |  384x14x14   |   0.21 % |   0.10 % | Conv2d k=3 p=1 s=1 |
| features.8.conv.1.1  |  384x14x14  |  384x14x14   |   0.09 % |   0.04 % | BatchNorm2d        |
| features.8.conv.1.2  |  384x14x14  |  384x14x14   |   0.00 % |   0.00 % | ReLU6              |
| features.8.conv.2    |  384x14x14  |   64x14x14   |   1.47 % |   0.69 % | Conv2d k=1 p=0 s=1 |
| features.8.conv.3    |   64x14x14  |   64x14x14   |   0.02 % |   0.01 % | BatchNorm2d        |
| features.9.conv.0.0  |   64x14x14  |  384x14x14   |   1.47 % |   0.69 % | Conv2d k=1 p=0 s=1 |
| features.9.conv.0.1  |  384x14x14  |  384x14x14   |   0.09 % |   0.04 % | BatchNorm2d        |
| features.9.conv.0.2  |  384x14x14  |  384x14x14   |   0.00 % |   0.00 % | ReLU6              |
| features.9.conv.1.0  |  384x14x14  |  384x14x14   |   0.21 % |   0.10 % | Conv2d k=3 p=1 s=1 |
| features.9.conv.1.1  |  384x14x14  |  384x14x14   |   0.09 % |   0.04 % | BatchNorm2d        |
| features.9.conv.1.2  |  384x14x14  |  384x14x14   |   0.00 % |   0.00 % | ReLU6              |
| features.9.conv.2    |  384x14x14  |   64x14x14   |   1.47 % |   0.69 % | Conv2d k=1 p=0 s=1 |
| features.9.conv.3    |   64x14x14  |   64x14x14   |   0.02 % |   0.01 % | BatchNorm2d        |
| features.10.conv.0.0 |   64x14x14  |  384x14x14   |   1.47 % |   0.69 % | Conv2d k=1 p=0 s=1 |
| features.10.conv.0.1 |  384x14x14  |  384x14x14   |   0.09 % |   0.04 % | BatchNorm2d        |
| features.10.conv.0.2 |  384x14x14  |  384x14x14   |   0.00 % |   0.00 % | ReLU6              |
| features.10.conv.1.0 |  384x14x14  |  384x14x14   |   0.21 % |   0.10 % | Conv2d k=3 p=1 s=1 |
| features.10.conv.1.1 |  384x14x14  |  384x14x14   |   0.09 % |   0.04 % | BatchNorm2d        |
| features.10.conv.1.2 |  384x14x14  |  384x14x14   |   0.00 % |   0.00 % | ReLU6              |
| features.10.conv.2   |  384x14x14  |   64x14x14   |   1.47 % |   0.69 % | Conv2d k=1 p=0 s=1 |
| features.10.conv.3   |   64x14x14  |   64x14x14   |   0.02 % |   0.01 % | BatchNorm2d        |
| features.11.conv.0.0 |   64x14x14  |  384x14x14   |   1.47 % |   0.69 % | Conv2d k=1 p=0 s=1 |
| features.11.conv.0.1 |  384x14x14  |  384x14x14   |   0.09 % |   0.04 % | BatchNorm2d        |
| features.11.conv.0.2 |  384x14x14  |  384x14x14   |   0.00 % |   0.00 % | ReLU6              |
| features.11.conv.1.0 |  384x14x14  |  384x14x14   |   0.21 % |   0.10 % | Conv2d k=3 p=1 s=1 |
| features.11.conv.1.1 |  384x14x14  |  384x14x14   |   0.09 % |   0.04 % | BatchNorm2d        |
| features.11.conv.1.2 |  384x14x14  |  384x14x14   |   0.00 % |   0.00 % | ReLU6              |
| features.11.conv.2   |  384x14x14  |   96x14x14   |   2.21 % |   1.04 % | Conv2d k=1 p=0 s=1 |
| features.11.conv.3   |   96x14x14  |   96x14x14   |   0.02 % |   0.01 % | BatchNorm2d        |
| features.12.conv.0.0 |   96x14x14  |  576x14x14   |   3.31 % |   1.56 % | Conv2d k=1 p=0 s=1 |
| features.12.conv.0.1 |  576x14x14  |  576x14x14   |   0.14 % |   0.07 % | BatchNorm2d        |
| features.12.conv.0.2 |  576x14x14  |  576x14x14   |   0.00 % |   0.00 % | ReLU6              |
| features.12.conv.1.0 |  576x14x14  |  576x14x14   |   0.31 % |   0.15 % | Conv2d k=3 p=1 s=1 |
| features.12.conv.1.1 |  576x14x14  |  576x14x14   |   0.14 % |   0.07 % | BatchNorm2d        |
| features.12.conv.1.2 |  576x14x14  |  576x14x14   |   0.00 % |   0.00 % | ReLU6              |
| features.12.conv.2   |  576x14x14  |   96x14x14   |   3.31 % |   1.56 % | Conv2d k=1 p=0 s=1 |
| features.12.conv.3   |   96x14x14  |   96x14x14   |   0.02 % |   0.01 % | BatchNorm2d        |
| features.13.conv.0.0 |   96x14x14  |  576x14x14   |   3.31 % |   1.56 % | Conv2d k=1 p=0 s=1 |
| features.13.conv.0.1 |  576x14x14  |  576x14x14   |   0.14 % |   0.07 % | BatchNorm2d        |
| features.13.conv.0.2 |  576x14x14  |  576x14x14   |   0.00 % |   0.00 % | ReLU6              |
| features.13.conv.1.0 |  576x14x14  |  576x14x14   |   0.31 % |   0.15 % | Conv2d k=3 p=1 s=1 |
| features.13.conv.1.1 |  576x14x14  |  576x14x14   |   0.14 % |   0.07 % | BatchNorm2d        |
| features.13.conv.1.2 |  576x14x14  |  576x14x14   |   0.00 % |   0.00 % | ReLU6              |
| features.13.conv.2   |  576x14x14  |   96x14x14   |   3.31 % |   1.56 % | Conv2d k=1 p=0 s=1 |
| features.13.conv.3   |   96x14x14  |   96x14x14   |   0.02 % |   0.01 % | BatchNorm2d        |
| features.14.conv.0.0 |   96x14x14  |  576x14x14   |   3.31 % |   1.56 % | Conv2d k=1 p=0 s=1 |
| features.14.conv.0.1 |  576x14x14  |  576x14x14   |   0.14 % |   0.07 % | BatchNorm2d        |
| features.14.conv.0.2 |  576x14x14  |  576x14x14   |   0.00 % |   0.00 % | ReLU6              |
| features.14.conv.1.0 |  576x14x14  |   576x7x7    |   0.08 % |   0.15 % | Conv2d k=3 p=1 s=2 |
| features.14.conv.1.1 |   576x7x7   |   576x7x7    |   0.03 % |   0.07 % | BatchNorm2d        |
| features.14.conv.1.2 |   576x7x7   |   576x7x7    |   0.00 % |   0.00 % | ReLU6              |
| features.14.conv.2   |   576x7x7   |   160x7x7    |   1.38 % |   2.60 % | Conv2d k=1 p=0 s=1 |
| features.14.conv.3   |   160x7x7   |   160x7x7    |   0.01 % |   0.02 % | BatchNorm2d        |
| features.15.conv.0.0 |   160x7x7   |   960x7x7    |   2.30 % |   4.34 % | Conv2d k=1 p=0 s=1 |
| features.15.conv.0.1 |   960x7x7   |   960x7x7    |   0.06 % |   0.11 % | BatchNorm2d        |
| features.15.conv.0.2 |   960x7x7   |   960x7x7    |   0.00 % |   0.00 % | ReLU6              |
| features.15.conv.1.0 |   960x7x7   |   960x7x7    |   0.13 % |   0.24 % | Conv2d k=3 p=1 s=1 |
| features.15.conv.1.1 |   960x7x7   |   960x7x7    |   0.06 % |   0.11 % | BatchNorm2d        |
| features.15.conv.1.2 |   960x7x7   |   960x7x7    |   0.00 % |   0.00 % | ReLU6              |
| features.15.conv.2   |   960x7x7   |   160x7x7    |   2.30 % |   4.34 % | Conv2d k=1 p=0 s=1 |
| features.15.conv.3   |   160x7x7   |   160x7x7    |   0.01 % |   0.02 % | BatchNorm2d        |
| features.16.conv.0.0 |   160x7x7   |   960x7x7    |   2.30 % |   4.34 % | Conv2d k=1 p=0 s=1 |
| features.16.conv.0.1 |   960x7x7   |   960x7x7    |   0.06 % |   0.11 % | BatchNorm2d        |
| features.16.conv.0.2 |   960x7x7   |   960x7x7    |   0.00 % |   0.00 % | ReLU6              |
| features.16.conv.1.0 |   960x7x7   |   960x7x7    |   0.13 % |   0.24 % | Conv2d k=3 p=1 s=1 |
| features.16.conv.1.1 |   960x7x7   |   960x7x7    |   0.06 % |   0.11 % | BatchNorm2d        |
| features.16.conv.1.2 |   960x7x7   |   960x7x7    |   0.00 % |   0.00 % | ReLU6              |
| features.16.conv.2   |   960x7x7   |   160x7x7    |   2.30 % |   4.34 % | Conv2d k=1 p=0 s=1 |
| features.16.conv.3   |   160x7x7   |   160x7x7    |   0.01 % |   0.02 % | BatchNorm2d        |
| features.17.conv.0.0 |   160x7x7   |   960x7x7    |   2.30 % |   4.34 % | Conv2d k=1 p=0 s=1 |
| features.17.conv.0.1 |   960x7x7   |   960x7x7    |   0.06 % |   0.11 % | BatchNorm2d        |
| features.17.conv.0.2 |   960x7x7   |   960x7x7    |   0.00 % |   0.00 % | ReLU6              |
| features.17.conv.1.0 |   960x7x7   |   960x7x7    |   0.13 % |   0.24 % | Conv2d k=3 p=1 s=1 |
| features.17.conv.1.1 |   960x7x7   |   960x7x7    |   0.06 % |   0.11 % | BatchNorm2d        |
| features.17.conv.1.2 |   960x7x7   |   960x7x7    |   0.00 % |   0.00 % | ReLU6              |
| features.17.conv.2   |   960x7x7   |   320x7x7    |   4.60 % |   8.68 % | Conv2d k=1 p=0 s=1 |
| features.17.conv.3   |   320x7x7   |   320x7x7    |   0.02 % |   0.04 % | BatchNorm2d        |
| features.18.0        |   320x7x7   |   1280x7x7   |   6.13 % |  11.57 % | Conv2d k=1 p=0 s=1 |
| features.18.1        |   1280x7x7  |   1280x7x7   |   0.08 % |   0.14 % | BatchNorm2d        |
| features.18.2        |   1280x7x7  |   1280x7x7   |   0.00 % |   0.00 % | ReLU6              |
| classifier.0         |     1280    |     1280     |   0.00 % |   0.00 % | Dropout            |
| classifier.1         |     1280    |     1000     |   0.39 % |  36.20 % | Linear             |
| Total                |  3x224x224  |     1000     | 327.49 M |   3.54 M | MobileNetV2        |