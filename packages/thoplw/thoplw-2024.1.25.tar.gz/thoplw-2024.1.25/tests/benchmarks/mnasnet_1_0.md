| Name                 | Input shape | Output shape |     MACs |   Params | Description        |
|:--------------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| layers.0             |  3x224x224  |  32x112x112  |   3.22 % |   0.02 % | Conv2d k=3 p=1 s=2 |
| layers.1             |  32x112x112 |  32x112x112  |   0.48 % |   0.00 % | BatchNorm2d        |
| layers.2             |  32x112x112 |  32x112x112  |   0.00 % |   0.00 % | ReLU               |
| layers.3             |  32x112x112 |  32x112x112  |   1.07 % |   0.01 % | Conv2d k=3 p=1 s=1 |
| layers.4             |  32x112x112 |  32x112x112  |   0.48 % |   0.00 % | BatchNorm2d        |
| layers.5             |  32x112x112 |  32x112x112  |   0.00 % |   0.00 % | ReLU               |
| layers.6             |  32x112x112 |  16x112x112  |   1.91 % |   0.01 % | Conv2d k=1 p=0 s=1 |
| layers.7             |  16x112x112 |  16x112x112  |   0.24 % |   0.00 % | BatchNorm2d        |
| layers.8.0.layers.0  |  16x112x112 |  48x112x112  |   2.87 % |   0.02 % | Conv2d k=1 p=0 s=1 |
| layers.8.0.layers.1  |  48x112x112 |  48x112x112  |   0.72 % |   0.00 % | BatchNorm2d        |
| layers.8.0.layers.2  |  48x112x112 |  48x112x112  |   0.00 % |   0.00 % | ReLU               |
| layers.8.0.layers.3  |  48x112x112 |   48x56x56   |   0.40 % |   0.01 % | Conv2d k=3 p=1 s=2 |
| layers.8.0.layers.4  |   48x56x56  |   48x56x56   |   0.18 % |   0.00 % | BatchNorm2d        |
| layers.8.0.layers.5  |   48x56x56  |   48x56x56   |   0.00 % |   0.00 % | ReLU               |
| layers.8.0.layers.6  |   48x56x56  |   24x56x56   |   1.07 % |   0.03 % | Conv2d k=1 p=0 s=1 |
| layers.8.0.layers.7  |   24x56x56  |   24x56x56   |   0.09 % |   0.00 % | BatchNorm2d        |
| layers.8.1.layers.0  |   24x56x56  |   72x56x56   |   1.61 % |   0.04 % | Conv2d k=1 p=0 s=1 |
| layers.8.1.layers.1  |   72x56x56  |   72x56x56   |   0.27 % |   0.01 % | BatchNorm2d        |
| layers.8.1.layers.2  |   72x56x56  |   72x56x56   |   0.00 % |   0.00 % | ReLU               |
| layers.8.1.layers.3  |   72x56x56  |   72x56x56   |   0.60 % |   0.01 % | Conv2d k=3 p=1 s=1 |
| layers.8.1.layers.4  |   72x56x56  |   72x56x56   |   0.27 % |   0.01 % | BatchNorm2d        |
| layers.8.1.layers.5  |   72x56x56  |   72x56x56   |   0.00 % |   0.00 % | ReLU               |
| layers.8.1.layers.6  |   72x56x56  |   24x56x56   |   1.61 % |   0.04 % | Conv2d k=1 p=0 s=1 |
| layers.8.1.layers.7  |   24x56x56  |   24x56x56   |   0.09 % |   0.00 % | BatchNorm2d        |
| layers.8.2.layers.0  |   24x56x56  |   72x56x56   |   1.61 % |   0.04 % | Conv2d k=1 p=0 s=1 |
| layers.8.2.layers.1  |   72x56x56  |   72x56x56   |   0.27 % |   0.01 % | BatchNorm2d        |
| layers.8.2.layers.2  |   72x56x56  |   72x56x56   |   0.00 % |   0.00 % | ReLU               |
| layers.8.2.layers.3  |   72x56x56  |   72x56x56   |   0.60 % |   0.01 % | Conv2d k=3 p=1 s=1 |
| layers.8.2.layers.4  |   72x56x56  |   72x56x56   |   0.27 % |   0.01 % | BatchNorm2d        |
| layers.8.2.layers.5  |   72x56x56  |   72x56x56   |   0.00 % |   0.00 % | ReLU               |
| layers.8.2.layers.6  |   72x56x56  |   24x56x56   |   1.61 % |   0.04 % | Conv2d k=1 p=0 s=1 |
| layers.8.2.layers.7  |   24x56x56  |   24x56x56   |   0.09 % |   0.00 % | BatchNorm2d        |
| layers.9.0.layers.0  |   24x56x56  |   72x56x56   |   1.61 % |   0.04 % | Conv2d k=1 p=0 s=1 |
| layers.9.0.layers.1  |   72x56x56  |   72x56x56   |   0.27 % |   0.01 % | BatchNorm2d        |
| layers.9.0.layers.2  |   72x56x56  |   72x56x56   |   0.00 % |   0.00 % | ReLU               |
| layers.9.0.layers.3  |   72x56x56  |   72x28x28   |   0.42 % |   0.04 % | Conv2d k=5 p=2 s=2 |
| layers.9.0.layers.4  |   72x28x28  |   72x28x28   |   0.07 % |   0.01 % | BatchNorm2d        |
| layers.9.0.layers.5  |   72x28x28  |   72x28x28   |   0.00 % |   0.00 % | ReLU               |
| layers.9.0.layers.6  |   72x28x28  |   40x28x28   |   0.67 % |   0.07 % | Conv2d k=1 p=0 s=1 |
| layers.9.0.layers.7  |   40x28x28  |   40x28x28   |   0.04 % |   0.00 % | BatchNorm2d        |
| layers.9.1.layers.0  |   40x28x28  |  120x28x28   |   1.12 % |   0.11 % | Conv2d k=1 p=0 s=1 |
| layers.9.1.layers.1  |  120x28x28  |  120x28x28   |   0.11 % |   0.01 % | BatchNorm2d        |
| layers.9.1.layers.2  |  120x28x28  |  120x28x28   |   0.00 % |   0.00 % | ReLU               |
| layers.9.1.layers.3  |  120x28x28  |  120x28x28   |   0.70 % |   0.07 % | Conv2d k=5 p=2 s=1 |
| layers.9.1.layers.4  |  120x28x28  |  120x28x28   |   0.11 % |   0.01 % | BatchNorm2d        |
| layers.9.1.layers.5  |  120x28x28  |  120x28x28   |   0.00 % |   0.00 % | ReLU               |
| layers.9.1.layers.6  |  120x28x28  |   40x28x28   |   1.12 % |   0.11 % | Conv2d k=1 p=0 s=1 |
| layers.9.1.layers.7  |   40x28x28  |   40x28x28   |   0.04 % |   0.00 % | BatchNorm2d        |
| layers.9.2.layers.0  |   40x28x28  |  120x28x28   |   1.12 % |   0.11 % | Conv2d k=1 p=0 s=1 |
| layers.9.2.layers.1  |  120x28x28  |  120x28x28   |   0.11 % |   0.01 % | BatchNorm2d        |
| layers.9.2.layers.2  |  120x28x28  |  120x28x28   |   0.00 % |   0.00 % | ReLU               |
| layers.9.2.layers.3  |  120x28x28  |  120x28x28   |   0.70 % |   0.07 % | Conv2d k=5 p=2 s=1 |
| layers.9.2.layers.4  |  120x28x28  |  120x28x28   |   0.11 % |   0.01 % | BatchNorm2d        |
| layers.9.2.layers.5  |  120x28x28  |  120x28x28   |   0.00 % |   0.00 % | ReLU               |
| layers.9.2.layers.6  |  120x28x28  |   40x28x28   |   1.12 % |   0.11 % | Conv2d k=1 p=0 s=1 |
| layers.9.2.layers.7  |   40x28x28  |   40x28x28   |   0.04 % |   0.00 % | BatchNorm2d        |
| layers.10.0.layers.0 |   40x28x28  |  240x28x28   |   2.24 % |   0.22 % | Conv2d k=1 p=0 s=1 |
| layers.10.0.layers.1 |  240x28x28  |  240x28x28   |   0.22 % |   0.02 % | BatchNorm2d        |
| layers.10.0.layers.2 |  240x28x28  |  240x28x28   |   0.00 % |   0.00 % | ReLU               |
| layers.10.0.layers.3 |  240x28x28  |  240x14x14   |   0.35 % |   0.14 % | Conv2d k=5 p=2 s=2 |
| layers.10.0.layers.4 |  240x14x14  |  240x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| layers.10.0.layers.5 |  240x14x14  |  240x14x14   |   0.00 % |   0.00 % | ReLU               |
| layers.10.0.layers.6 |  240x14x14  |   80x14x14   |   1.12 % |   0.43 % | Conv2d k=1 p=0 s=1 |
| layers.10.0.layers.7 |   80x14x14  |   80x14x14   |   0.02 % |   0.01 % | BatchNorm2d        |
| layers.10.1.layers.0 |   80x14x14  |  480x14x14   |   2.24 % |   0.87 % | Conv2d k=1 p=0 s=1 |
| layers.10.1.layers.1 |  480x14x14  |  480x14x14   |   0.11 % |   0.04 % | BatchNorm2d        |
| layers.10.1.layers.2 |  480x14x14  |  480x14x14   |   0.00 % |   0.00 % | ReLU               |
| layers.10.1.layers.3 |  480x14x14  |  480x14x14   |   0.70 % |   0.27 % | Conv2d k=5 p=2 s=1 |
| layers.10.1.layers.4 |  480x14x14  |  480x14x14   |   0.11 % |   0.04 % | BatchNorm2d        |
| layers.10.1.layers.5 |  480x14x14  |  480x14x14   |   0.00 % |   0.00 % | ReLU               |
| layers.10.1.layers.6 |  480x14x14  |   80x14x14   |   2.24 % |   0.87 % | Conv2d k=1 p=0 s=1 |
| layers.10.1.layers.7 |   80x14x14  |   80x14x14   |   0.02 % |   0.01 % | BatchNorm2d        |
| layers.10.2.layers.0 |   80x14x14  |  480x14x14   |   2.24 % |   0.87 % | Conv2d k=1 p=0 s=1 |
| layers.10.2.layers.1 |  480x14x14  |  480x14x14   |   0.11 % |   0.04 % | BatchNorm2d        |
| layers.10.2.layers.2 |  480x14x14  |  480x14x14   |   0.00 % |   0.00 % | ReLU               |
| layers.10.2.layers.3 |  480x14x14  |  480x14x14   |   0.70 % |   0.27 % | Conv2d k=5 p=2 s=1 |
| layers.10.2.layers.4 |  480x14x14  |  480x14x14   |   0.11 % |   0.04 % | BatchNorm2d        |
| layers.10.2.layers.5 |  480x14x14  |  480x14x14   |   0.00 % |   0.00 % | ReLU               |
| layers.10.2.layers.6 |  480x14x14  |   80x14x14   |   2.24 % |   0.87 % | Conv2d k=1 p=0 s=1 |
| layers.10.2.layers.7 |   80x14x14  |   80x14x14   |   0.02 % |   0.01 % | BatchNorm2d        |
| layers.11.0.layers.0 |   80x14x14  |  480x14x14   |   2.24 % |   0.87 % | Conv2d k=1 p=0 s=1 |
| layers.11.0.layers.1 |  480x14x14  |  480x14x14   |   0.11 % |   0.04 % | BatchNorm2d        |
| layers.11.0.layers.2 |  480x14x14  |  480x14x14   |   0.00 % |   0.00 % | ReLU               |
| layers.11.0.layers.3 |  480x14x14  |  480x14x14   |   0.25 % |   0.10 % | Conv2d k=3 p=1 s=1 |
| layers.11.0.layers.4 |  480x14x14  |  480x14x14   |   0.11 % |   0.04 % | BatchNorm2d        |
| layers.11.0.layers.5 |  480x14x14  |  480x14x14   |   0.00 % |   0.00 % | ReLU               |
| layers.11.0.layers.6 |  480x14x14  |   96x14x14   |   2.69 % |   1.04 % | Conv2d k=1 p=0 s=1 |
| layers.11.0.layers.7 |   96x14x14  |   96x14x14   |   0.02 % |   0.01 % | BatchNorm2d        |
| layers.11.1.layers.0 |   96x14x14  |  576x14x14   |   3.22 % |   1.25 % | Conv2d k=1 p=0 s=1 |
| layers.11.1.layers.1 |  576x14x14  |  576x14x14   |   0.13 % |   0.05 % | BatchNorm2d        |
| layers.11.1.layers.2 |  576x14x14  |  576x14x14   |   0.00 % |   0.00 % | ReLU               |
| layers.11.1.layers.3 |  576x14x14  |  576x14x14   |   0.30 % |   0.12 % | Conv2d k=3 p=1 s=1 |
| layers.11.1.layers.4 |  576x14x14  |  576x14x14   |   0.13 % |   0.05 % | BatchNorm2d        |
| layers.11.1.layers.5 |  576x14x14  |  576x14x14   |   0.00 % |   0.00 % | ReLU               |
| layers.11.1.layers.6 |  576x14x14  |   96x14x14   |   3.22 % |   1.25 % | Conv2d k=1 p=0 s=1 |
| layers.11.1.layers.7 |   96x14x14  |   96x14x14   |   0.02 % |   0.01 % | BatchNorm2d        |
| layers.12.0.layers.0 |   96x14x14  |  576x14x14   |   3.22 % |   1.25 % | Conv2d k=1 p=0 s=1 |
| layers.12.0.layers.1 |  576x14x14  |  576x14x14   |   0.13 % |   0.05 % | BatchNorm2d        |
| layers.12.0.layers.2 |  576x14x14  |  576x14x14   |   0.00 % |   0.00 % | ReLU               |
| layers.12.0.layers.3 |  576x14x14  |   576x7x7    |   0.21 % |   0.33 % | Conv2d k=5 p=2 s=2 |
| layers.12.0.layers.4 |   576x7x7   |   576x7x7    |   0.03 % |   0.05 % | BatchNorm2d        |
| layers.12.0.layers.5 |   576x7x7   |   576x7x7    |   0.00 % |   0.00 % | ReLU               |
| layers.12.0.layers.6 |   576x7x7   |   192x7x7    |   1.61 % |   2.50 % | Conv2d k=1 p=0 s=1 |
| layers.12.0.layers.7 |   192x7x7   |   192x7x7    |   0.01 % |   0.02 % | BatchNorm2d        |
| layers.12.1.layers.0 |   192x7x7   |   1152x7x7   |   3.22 % |   5.00 % | Conv2d k=1 p=0 s=1 |
| layers.12.1.layers.1 |   1152x7x7  |   1152x7x7   |   0.07 % |   0.10 % | BatchNorm2d        |
| layers.12.1.layers.2 |   1152x7x7  |   1152x7x7   |   0.00 % |   0.00 % | ReLU               |
| layers.12.1.layers.3 |   1152x7x7  |   1152x7x7   |   0.42 % |   0.65 % | Conv2d k=5 p=2 s=1 |
| layers.12.1.layers.4 |   1152x7x7  |   1152x7x7   |   0.07 % |   0.10 % | BatchNorm2d        |
| layers.12.1.layers.5 |   1152x7x7  |   1152x7x7   |   0.00 % |   0.00 % | ReLU               |
| layers.12.1.layers.6 |   1152x7x7  |   192x7x7    |   3.22 % |   5.00 % | Conv2d k=1 p=0 s=1 |
| layers.12.1.layers.7 |   192x7x7   |   192x7x7    |   0.01 % |   0.02 % | BatchNorm2d        |
| layers.12.2.layers.0 |   192x7x7   |   1152x7x7   |   3.22 % |   5.00 % | Conv2d k=1 p=0 s=1 |
| layers.12.2.layers.1 |   1152x7x7  |   1152x7x7   |   0.07 % |   0.10 % | BatchNorm2d        |
| layers.12.2.layers.2 |   1152x7x7  |   1152x7x7   |   0.00 % |   0.00 % | ReLU               |
| layers.12.2.layers.3 |   1152x7x7  |   1152x7x7   |   0.42 % |   0.65 % | Conv2d k=5 p=2 s=1 |
| layers.12.2.layers.4 |   1152x7x7  |   1152x7x7   |   0.07 % |   0.10 % | BatchNorm2d        |
| layers.12.2.layers.5 |   1152x7x7  |   1152x7x7   |   0.00 % |   0.00 % | ReLU               |
| layers.12.2.layers.6 |   1152x7x7  |   192x7x7    |   3.22 % |   5.00 % | Conv2d k=1 p=0 s=1 |
| layers.12.2.layers.7 |   192x7x7   |   192x7x7    |   0.01 % |   0.02 % | BatchNorm2d        |
| layers.12.3.layers.0 |   192x7x7   |   1152x7x7   |   3.22 % |   5.00 % | Conv2d k=1 p=0 s=1 |
| layers.12.3.layers.1 |   1152x7x7  |   1152x7x7   |   0.07 % |   0.10 % | BatchNorm2d        |
| layers.12.3.layers.2 |   1152x7x7  |   1152x7x7   |   0.00 % |   0.00 % | ReLU               |
| layers.12.3.layers.3 |   1152x7x7  |   1152x7x7   |   0.42 % |   0.65 % | Conv2d k=5 p=2 s=1 |
| layers.12.3.layers.4 |   1152x7x7  |   1152x7x7   |   0.07 % |   0.10 % | BatchNorm2d        |
| layers.12.3.layers.5 |   1152x7x7  |   1152x7x7   |   0.00 % |   0.00 % | ReLU               |
| layers.12.3.layers.6 |   1152x7x7  |   192x7x7    |   3.22 % |   5.00 % | Conv2d k=1 p=0 s=1 |
| layers.12.3.layers.7 |   192x7x7   |   192x7x7    |   0.01 % |   0.02 % | BatchNorm2d        |
| layers.13.0.layers.0 |   192x7x7   |   1152x7x7   |   3.22 % |   5.00 % | Conv2d k=1 p=0 s=1 |
| layers.13.0.layers.1 |   1152x7x7  |   1152x7x7   |   0.07 % |   0.10 % | BatchNorm2d        |
| layers.13.0.layers.2 |   1152x7x7  |   1152x7x7   |   0.00 % |   0.00 % | ReLU               |
| layers.13.0.layers.3 |   1152x7x7  |   1152x7x7   |   0.15 % |   0.23 % | Conv2d k=3 p=1 s=1 |
| layers.13.0.layers.4 |   1152x7x7  |   1152x7x7   |   0.07 % |   0.10 % | BatchNorm2d        |
| layers.13.0.layers.5 |   1152x7x7  |   1152x7x7   |   0.00 % |   0.00 % | ReLU               |
| layers.13.0.layers.6 |   1152x7x7  |   320x7x7    |   5.37 % |   8.34 % | Conv2d k=1 p=0 s=1 |
| layers.13.0.layers.7 |   320x7x7   |   320x7x7    |   0.02 % |   0.03 % | BatchNorm2d        |
| layers.14            |   320x7x7   |   1280x7x7   |   5.97 % |   9.26 % | Conv2d k=1 p=0 s=1 |
| layers.15            |   1280x7x7  |   1280x7x7   |   0.07 % |   0.12 % | BatchNorm2d        |
| layers.16            |   1280x7x7  |   1280x7x7   |   0.00 % |   0.00 % | ReLU               |
| classifier.0         |     1280    |     1280     |   0.00 % |   0.00 % | Dropout            |
| classifier.1         |     1280    |     1000     |   0.38 % |  28.97 % | Linear             |
| Total                |  3x224x224  |     1000     | 336.24 M |   4.42 M | MNASNet            |