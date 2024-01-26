| Name                 | Input shape | Output shape |     MACs |   Params | Description        |
|:--------------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| layers.0             |  3x224x224  |  16x112x112  |   4.64 % |   0.02 % | Conv2d k=3 p=1 s=2 |
| layers.1             |  16x112x112 |  16x112x112  |   0.69 % |   0.00 % | BatchNorm2d        |
| layers.2             |  16x112x112 |  16x112x112  |   0.00 % |   0.00 % | ReLU               |
| layers.3             |  16x112x112 |  16x112x112  |   1.55 % |   0.01 % | Conv2d k=3 p=1 s=1 |
| layers.4             |  16x112x112 |  16x112x112  |   0.69 % |   0.00 % | BatchNorm2d        |
| layers.5             |  16x112x112 |  16x112x112  |   0.00 % |   0.00 % | ReLU               |
| layers.6             |  16x112x112 |  8x112x112   |   1.38 % |   0.01 % | Conv2d k=1 p=0 s=1 |
| layers.7             |  8x112x112  |  8x112x112   |   0.34 % |   0.00 % | BatchNorm2d        |
| layers.8.0.layers.0  |  8x112x112  |  24x112x112  |   2.06 % |   0.01 % | Conv2d k=1 p=0 s=1 |
| layers.8.0.layers.1  |  24x112x112 |  24x112x112  |   1.03 % |   0.00 % | BatchNorm2d        |
| layers.8.0.layers.2  |  24x112x112 |  24x112x112  |   0.00 % |   0.00 % | ReLU               |
| layers.8.0.layers.3  |  24x112x112 |   24x56x56   |   0.58 % |   0.01 % | Conv2d k=3 p=1 s=2 |
| layers.8.0.layers.4  |   24x56x56  |   24x56x56   |   0.26 % |   0.00 % | BatchNorm2d        |
| layers.8.0.layers.5  |   24x56x56  |   24x56x56   |   0.00 % |   0.00 % | ReLU               |
| layers.8.0.layers.6  |   24x56x56  |   16x56x56   |   1.03 % |   0.02 % | Conv2d k=1 p=0 s=1 |
| layers.8.0.layers.7  |   16x56x56  |   16x56x56   |   0.17 % |   0.00 % | BatchNorm2d        |
| layers.8.1.layers.0  |   16x56x56  |   48x56x56   |   2.06 % |   0.03 % | Conv2d k=1 p=0 s=1 |
| layers.8.1.layers.1  |   48x56x56  |   48x56x56   |   0.52 % |   0.01 % | BatchNorm2d        |
| layers.8.1.layers.2  |   48x56x56  |   48x56x56   |   0.00 % |   0.00 % | ReLU               |
| layers.8.1.layers.3  |   48x56x56  |   48x56x56   |   1.16 % |   0.02 % | Conv2d k=3 p=1 s=1 |
| layers.8.1.layers.4  |   48x56x56  |   48x56x56   |   0.52 % |   0.01 % | BatchNorm2d        |
| layers.8.1.layers.5  |   48x56x56  |   48x56x56   |   0.00 % |   0.00 % | ReLU               |
| layers.8.1.layers.6  |   48x56x56  |   16x56x56   |   2.06 % |   0.03 % | Conv2d k=1 p=0 s=1 |
| layers.8.1.layers.7  |   16x56x56  |   16x56x56   |   0.17 % |   0.00 % | BatchNorm2d        |
| layers.8.2.layers.0  |   16x56x56  |   48x56x56   |   2.06 % |   0.03 % | Conv2d k=1 p=0 s=1 |
| layers.8.2.layers.1  |   48x56x56  |   48x56x56   |   0.52 % |   0.01 % | BatchNorm2d        |
| layers.8.2.layers.2  |   48x56x56  |   48x56x56   |   0.00 % |   0.00 % | ReLU               |
| layers.8.2.layers.3  |   48x56x56  |   48x56x56   |   1.16 % |   0.02 % | Conv2d k=3 p=1 s=1 |
| layers.8.2.layers.4  |   48x56x56  |   48x56x56   |   0.52 % |   0.01 % | BatchNorm2d        |
| layers.8.2.layers.5  |   48x56x56  |   48x56x56   |   0.00 % |   0.00 % | ReLU               |
| layers.8.2.layers.6  |   48x56x56  |   16x56x56   |   2.06 % |   0.03 % | Conv2d k=1 p=0 s=1 |
| layers.8.2.layers.7  |   16x56x56  |   16x56x56   |   0.17 % |   0.00 % | BatchNorm2d        |
| layers.9.0.layers.0  |   16x56x56  |   48x56x56   |   2.06 % |   0.03 % | Conv2d k=1 p=0 s=1 |
| layers.9.0.layers.1  |   48x56x56  |   48x56x56   |   0.52 % |   0.01 % | BatchNorm2d        |
| layers.9.0.layers.2  |   48x56x56  |   48x56x56   |   0.00 % |   0.00 % | ReLU               |
| layers.9.0.layers.3  |   48x56x56  |   48x28x28   |   0.81 % |   0.05 % | Conv2d k=5 p=2 s=2 |
| layers.9.0.layers.4  |   48x28x28  |   48x28x28   |   0.13 % |   0.01 % | BatchNorm2d        |
| layers.9.0.layers.5  |   48x28x28  |   48x28x28   |   0.00 % |   0.00 % | ReLU               |
| layers.9.0.layers.6  |   48x28x28  |   24x28x28   |   0.77 % |   0.05 % | Conv2d k=1 p=0 s=1 |
| layers.9.0.layers.7  |   24x28x28  |   24x28x28   |   0.06 % |   0.00 % | BatchNorm2d        |
| layers.9.1.layers.0  |   24x28x28  |   72x28x28   |   1.16 % |   0.08 % | Conv2d k=1 p=0 s=1 |
| layers.9.1.layers.1  |   72x28x28  |   72x28x28   |   0.19 % |   0.01 % | BatchNorm2d        |
| layers.9.1.layers.2  |   72x28x28  |   72x28x28   |   0.00 % |   0.00 % | ReLU               |
| layers.9.1.layers.3  |   72x28x28  |   72x28x28   |   1.21 % |   0.08 % | Conv2d k=5 p=2 s=1 |
| layers.9.1.layers.4  |   72x28x28  |   72x28x28   |   0.19 % |   0.01 % | BatchNorm2d        |
| layers.9.1.layers.5  |   72x28x28  |   72x28x28   |   0.00 % |   0.00 % | ReLU               |
| layers.9.1.layers.6  |   72x28x28  |   24x28x28   |   1.16 % |   0.08 % | Conv2d k=1 p=0 s=1 |
| layers.9.1.layers.7  |   24x28x28  |   24x28x28   |   0.06 % |   0.00 % | BatchNorm2d        |
| layers.9.2.layers.0  |   24x28x28  |   72x28x28   |   1.16 % |   0.08 % | Conv2d k=1 p=0 s=1 |
| layers.9.2.layers.1  |   72x28x28  |   72x28x28   |   0.19 % |   0.01 % | BatchNorm2d        |
| layers.9.2.layers.2  |   72x28x28  |   72x28x28   |   0.00 % |   0.00 % | ReLU               |
| layers.9.2.layers.3  |   72x28x28  |   72x28x28   |   1.21 % |   0.08 % | Conv2d k=5 p=2 s=1 |
| layers.9.2.layers.4  |   72x28x28  |   72x28x28   |   0.19 % |   0.01 % | BatchNorm2d        |
| layers.9.2.layers.5  |   72x28x28  |   72x28x28   |   0.00 % |   0.00 % | ReLU               |
| layers.9.2.layers.6  |   72x28x28  |   24x28x28   |   1.16 % |   0.08 % | Conv2d k=1 p=0 s=1 |
| layers.9.2.layers.7  |   24x28x28  |   24x28x28   |   0.06 % |   0.00 % | BatchNorm2d        |
| layers.10.0.layers.0 |   24x28x28  |  144x28x28   |   2.32 % |   0.15 % | Conv2d k=1 p=0 s=1 |
| layers.10.0.layers.1 |  144x28x28  |  144x28x28   |   0.39 % |   0.03 % | BatchNorm2d        |
| layers.10.0.layers.2 |  144x28x28  |  144x28x28   |   0.00 % |   0.00 % | ReLU               |
| layers.10.0.layers.3 |  144x28x28  |  144x14x14   |   0.60 % |   0.16 % | Conv2d k=5 p=2 s=2 |
| layers.10.0.layers.4 |  144x14x14  |  144x14x14   |   0.10 % |   0.03 % | BatchNorm2d        |
| layers.10.0.layers.5 |  144x14x14  |  144x14x14   |   0.00 % |   0.00 % | ReLU               |
| layers.10.0.layers.6 |  144x14x14  |   40x14x14   |   0.97 % |   0.26 % | Conv2d k=1 p=0 s=1 |
| layers.10.0.layers.7 |   40x14x14  |   40x14x14   |   0.03 % |   0.01 % | BatchNorm2d        |
| layers.10.1.layers.0 |   40x14x14  |  240x14x14   |   1.61 % |   0.43 % | Conv2d k=1 p=0 s=1 |
| layers.10.1.layers.1 |  240x14x14  |  240x14x14   |   0.16 % |   0.04 % | BatchNorm2d        |
| layers.10.1.layers.2 |  240x14x14  |  240x14x14   |   0.00 % |   0.00 % | ReLU               |
| layers.10.1.layers.3 |  240x14x14  |  240x14x14   |   1.01 % |   0.27 % | Conv2d k=5 p=2 s=1 |
| layers.10.1.layers.4 |  240x14x14  |  240x14x14   |   0.16 % |   0.04 % | BatchNorm2d        |
| layers.10.1.layers.5 |  240x14x14  |  240x14x14   |   0.00 % |   0.00 % | ReLU               |
| layers.10.1.layers.6 |  240x14x14  |   40x14x14   |   1.61 % |   0.43 % | Conv2d k=1 p=0 s=1 |
| layers.10.1.layers.7 |   40x14x14  |   40x14x14   |   0.03 % |   0.01 % | BatchNorm2d        |
| layers.10.2.layers.0 |   40x14x14  |  240x14x14   |   1.61 % |   0.43 % | Conv2d k=1 p=0 s=1 |
| layers.10.2.layers.1 |  240x14x14  |  240x14x14   |   0.16 % |   0.04 % | BatchNorm2d        |
| layers.10.2.layers.2 |  240x14x14  |  240x14x14   |   0.00 % |   0.00 % | ReLU               |
| layers.10.2.layers.3 |  240x14x14  |  240x14x14   |   1.01 % |   0.27 % | Conv2d k=5 p=2 s=1 |
| layers.10.2.layers.4 |  240x14x14  |  240x14x14   |   0.16 % |   0.04 % | BatchNorm2d        |
| layers.10.2.layers.5 |  240x14x14  |  240x14x14   |   0.00 % |   0.00 % | ReLU               |
| layers.10.2.layers.6 |  240x14x14  |   40x14x14   |   1.61 % |   0.43 % | Conv2d k=1 p=0 s=1 |
| layers.10.2.layers.7 |   40x14x14  |   40x14x14   |   0.03 % |   0.01 % | BatchNorm2d        |
| layers.11.0.layers.0 |   40x14x14  |  240x14x14   |   1.61 % |   0.43 % | Conv2d k=1 p=0 s=1 |
| layers.11.0.layers.1 |  240x14x14  |  240x14x14   |   0.16 % |   0.04 % | BatchNorm2d        |
| layers.11.0.layers.2 |  240x14x14  |  240x14x14   |   0.00 % |   0.00 % | ReLU               |
| layers.11.0.layers.3 |  240x14x14  |  240x14x14   |   0.36 % |   0.10 % | Conv2d k=3 p=1 s=1 |
| layers.11.0.layers.4 |  240x14x14  |  240x14x14   |   0.16 % |   0.04 % | BatchNorm2d        |
| layers.11.0.layers.5 |  240x14x14  |  240x14x14   |   0.00 % |   0.00 % | ReLU               |
| layers.11.0.layers.6 |  240x14x14  |   48x14x14   |   1.93 % |   0.51 % | Conv2d k=1 p=0 s=1 |
| layers.11.0.layers.7 |   48x14x14  |   48x14x14   |   0.03 % |   0.01 % | BatchNorm2d        |
| layers.11.1.layers.0 |   48x14x14  |  288x14x14   |   2.32 % |   0.62 % | Conv2d k=1 p=0 s=1 |
| layers.11.1.layers.1 |  288x14x14  |  288x14x14   |   0.19 % |   0.05 % | BatchNorm2d        |
| layers.11.1.layers.2 |  288x14x14  |  288x14x14   |   0.00 % |   0.00 % | ReLU               |
| layers.11.1.layers.3 |  288x14x14  |  288x14x14   |   0.44 % |   0.12 % | Conv2d k=3 p=1 s=1 |
| layers.11.1.layers.4 |  288x14x14  |  288x14x14   |   0.19 % |   0.05 % | BatchNorm2d        |
| layers.11.1.layers.5 |  288x14x14  |  288x14x14   |   0.00 % |   0.00 % | ReLU               |
| layers.11.1.layers.6 |  288x14x14  |   48x14x14   |   2.32 % |   0.62 % | Conv2d k=1 p=0 s=1 |
| layers.11.1.layers.7 |   48x14x14  |   48x14x14   |   0.03 % |   0.01 % | BatchNorm2d        |
| layers.12.0.layers.0 |   48x14x14  |  288x14x14   |   2.32 % |   0.62 % | Conv2d k=1 p=0 s=1 |
| layers.12.0.layers.1 |  288x14x14  |  288x14x14   |   0.19 % |   0.05 % | BatchNorm2d        |
| layers.12.0.layers.2 |  288x14x14  |  288x14x14   |   0.00 % |   0.00 % | ReLU               |
| layers.12.0.layers.3 |  288x14x14  |   288x7x7    |   0.30 % |   0.32 % | Conv2d k=5 p=2 s=2 |
| layers.12.0.layers.4 |   288x7x7   |   288x7x7    |   0.05 % |   0.05 % | BatchNorm2d        |
| layers.12.0.layers.5 |   288x7x7   |   288x7x7    |   0.00 % |   0.00 % | ReLU               |
| layers.12.0.layers.6 |   288x7x7   |    96x7x7    |   1.16 % |   1.23 % | Conv2d k=1 p=0 s=1 |
| layers.12.0.layers.7 |    96x7x7   |    96x7x7    |   0.02 % |   0.02 % | BatchNorm2d        |
| layers.12.1.layers.0 |    96x7x7   |   576x7x7    |   2.32 % |   2.47 % | Conv2d k=1 p=0 s=1 |
| layers.12.1.layers.1 |   576x7x7   |   576x7x7    |   0.10 % |   0.10 % | BatchNorm2d        |
| layers.12.1.layers.2 |   576x7x7   |   576x7x7    |   0.00 % |   0.00 % | ReLU               |
| layers.12.1.layers.3 |   576x7x7   |   576x7x7    |   0.60 % |   0.64 % | Conv2d k=5 p=2 s=1 |
| layers.12.1.layers.4 |   576x7x7   |   576x7x7    |   0.10 % |   0.10 % | BatchNorm2d        |
| layers.12.1.layers.5 |   576x7x7   |   576x7x7    |   0.00 % |   0.00 % | ReLU               |
| layers.12.1.layers.6 |   576x7x7   |    96x7x7    |   2.32 % |   2.47 % | Conv2d k=1 p=0 s=1 |
| layers.12.1.layers.7 |    96x7x7   |    96x7x7    |   0.02 % |   0.02 % | BatchNorm2d        |
| layers.12.2.layers.0 |    96x7x7   |   576x7x7    |   2.32 % |   2.47 % | Conv2d k=1 p=0 s=1 |
| layers.12.2.layers.1 |   576x7x7   |   576x7x7    |   0.10 % |   0.10 % | BatchNorm2d        |
| layers.12.2.layers.2 |   576x7x7   |   576x7x7    |   0.00 % |   0.00 % | ReLU               |
| layers.12.2.layers.3 |   576x7x7   |   576x7x7    |   0.60 % |   0.64 % | Conv2d k=5 p=2 s=1 |
| layers.12.2.layers.4 |   576x7x7   |   576x7x7    |   0.10 % |   0.10 % | BatchNorm2d        |
| layers.12.2.layers.5 |   576x7x7   |   576x7x7    |   0.00 % |   0.00 % | ReLU               |
| layers.12.2.layers.6 |   576x7x7   |    96x7x7    |   2.32 % |   2.47 % | Conv2d k=1 p=0 s=1 |
| layers.12.2.layers.7 |    96x7x7   |    96x7x7    |   0.02 % |   0.02 % | BatchNorm2d        |
| layers.12.3.layers.0 |    96x7x7   |   576x7x7    |   2.32 % |   2.47 % | Conv2d k=1 p=0 s=1 |
| layers.12.3.layers.1 |   576x7x7   |   576x7x7    |   0.10 % |   0.10 % | BatchNorm2d        |
| layers.12.3.layers.2 |   576x7x7   |   576x7x7    |   0.00 % |   0.00 % | ReLU               |
| layers.12.3.layers.3 |   576x7x7   |   576x7x7    |   0.60 % |   0.64 % | Conv2d k=5 p=2 s=1 |
| layers.12.3.layers.4 |   576x7x7   |   576x7x7    |   0.10 % |   0.10 % | BatchNorm2d        |
| layers.12.3.layers.5 |   576x7x7   |   576x7x7    |   0.00 % |   0.00 % | ReLU               |
| layers.12.3.layers.6 |   576x7x7   |    96x7x7    |   2.32 % |   2.47 % | Conv2d k=1 p=0 s=1 |
| layers.12.3.layers.7 |    96x7x7   |    96x7x7    |   0.02 % |   0.02 % | BatchNorm2d        |
| layers.13.0.layers.0 |    96x7x7   |   576x7x7    |   2.32 % |   2.47 % | Conv2d k=1 p=0 s=1 |
| layers.13.0.layers.1 |   576x7x7   |   576x7x7    |   0.10 % |   0.10 % | BatchNorm2d        |
| layers.13.0.layers.2 |   576x7x7   |   576x7x7    |   0.00 % |   0.00 % | ReLU               |
| layers.13.0.layers.3 |   576x7x7   |   576x7x7    |   0.22 % |   0.23 % | Conv2d k=3 p=1 s=1 |
| layers.13.0.layers.4 |   576x7x7   |   576x7x7    |   0.10 % |   0.10 % | BatchNorm2d        |
| layers.13.0.layers.5 |   576x7x7   |   576x7x7    |   0.00 % |   0.00 % | ReLU               |
| layers.13.0.layers.6 |   576x7x7   |   160x7x7    |   3.87 % |   4.12 % | Conv2d k=1 p=0 s=1 |
| layers.13.0.layers.7 |   160x7x7   |   160x7x7    |   0.03 % |   0.03 % | BatchNorm2d        |
| layers.14            |   160x7x7   |   1280x7x7   |   8.60 % |   9.15 % | Conv2d k=1 p=0 s=1 |
| layers.15            |   1280x7x7  |   1280x7x7   |   0.21 % |   0.23 % | BatchNorm2d        |
| layers.16            |   1280x7x7  |   1280x7x7   |   0.00 % |   0.00 % | ReLU               |
| classifier.0         |     1280    |     1280     |   0.00 % |   0.00 % | Dropout            |
| classifier.1         |     1280    |     1000     |   1.10 % |  57.21 % | Linear             |
| Total                |  3x224x224  |     1000     | 116.72 M |   2.24 M | MNASNet            |