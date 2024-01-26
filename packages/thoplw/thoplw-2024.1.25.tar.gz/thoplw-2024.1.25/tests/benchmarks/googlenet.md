| Name                       | Input shape | Output shape |     MACs |   Params | Description        |
|:--------------------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| conv1.conv                 |  3x224x224  |  64x112x112  |   7.81 % |   0.14 % | Conv2d k=7 p=3 s=2 |
| conv1.bn                   |  64x112x112 |  64x112x112  |   0.21 % |   0.00 % | BatchNorm2d        |
| maxpool1                   |  64x112x112 |   64x56x56   |   0.00 % |   0.00 % | MaxPool2d k=3 s=2  |
| conv2.conv                 |   64x56x56  |   64x56x56   |   0.85 % |   0.06 % | Conv2d k=1 p=0 s=1 |
| conv2.bn                   |   64x56x56  |   64x56x56   |   0.05 % |   0.00 % | BatchNorm2d        |
| conv3.conv                 |   64x56x56  |  192x56x56   |  22.95 % |   1.67 % | Conv2d k=3 p=1 s=1 |
| conv3.bn                   |  192x56x56  |  192x56x56   |   0.16 % |   0.01 % | BatchNorm2d        |
| maxpool2                   |  192x56x56  |  192x28x28   |   0.00 % |   0.00 % | MaxPool2d k=3 s=2  |
| inception3a.branch1.conv   |  192x28x28  |   64x28x28   |   0.64 % |   0.19 % | Conv2d k=1 p=0 s=1 |
| inception3a.branch1.bn     |   64x28x28  |   64x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| inception3a.branch2.0.conv |  192x28x28  |   96x28x28   |   0.96 % |   0.28 % | Conv2d k=1 p=0 s=1 |
| inception3a.branch2.0.bn   |   96x28x28  |   96x28x28   |   0.02 % |   0.01 % | BatchNorm2d        |
| inception3a.branch2.1.conv |   96x28x28  |  128x28x28   |   5.74 % |   1.67 % | Conv2d k=3 p=1 s=1 |
| inception3a.branch2.1.bn   |  128x28x28  |  128x28x28   |   0.03 % |   0.01 % | BatchNorm2d        |
| inception3a.branch3.0.conv |  192x28x28  |   16x28x28   |   0.16 % |   0.05 % | Conv2d k=1 p=0 s=1 |
| inception3a.branch3.0.bn   |   16x28x28  |   16x28x28   |   0.00 % |   0.00 % | BatchNorm2d        |
| inception3a.branch3.1.conv |   16x28x28  |   32x28x28   |   0.24 % |   0.07 % | Conv2d k=3 p=1 s=1 |
| inception3a.branch3.1.bn   |   32x28x28  |   32x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| inception3a.branch4.0      |  192x28x28  |  192x28x28   |   0.00 % |   0.00 % | MaxPool2d k=3 s=1  |
| inception3a.branch4.1.conv |  192x28x28  |   32x28x28   |   0.32 % |   0.09 % | Conv2d k=1 p=0 s=1 |
| inception3a.branch4.1.bn   |   32x28x28  |   32x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| inception3b.branch1.conv   |  256x28x28  |  128x28x28   |   1.70 % |   0.49 % | Conv2d k=1 p=0 s=1 |
| inception3b.branch1.bn     |  128x28x28  |  128x28x28   |   0.03 % |   0.01 % | BatchNorm2d        |
| inception3b.branch2.0.conv |  256x28x28  |  128x28x28   |   1.70 % |   0.49 % | Conv2d k=1 p=0 s=1 |
| inception3b.branch2.0.bn   |  128x28x28  |  128x28x28   |   0.03 % |   0.01 % | BatchNorm2d        |
| inception3b.branch2.1.conv |  128x28x28  |  192x28x28   |  11.47 % |   3.33 % | Conv2d k=3 p=1 s=1 |
| inception3b.branch2.1.bn   |  192x28x28  |  192x28x28   |   0.04 % |   0.01 % | BatchNorm2d        |
| inception3b.branch3.0.conv |  256x28x28  |   32x28x28   |   0.42 % |   0.12 % | Conv2d k=1 p=0 s=1 |
| inception3b.branch3.0.bn   |   32x28x28  |   32x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| inception3b.branch3.1.conv |   32x28x28  |   96x28x28   |   1.43 % |   0.42 % | Conv2d k=3 p=1 s=1 |
| inception3b.branch3.1.bn   |   96x28x28  |   96x28x28   |   0.02 % |   0.01 % | BatchNorm2d        |
| inception3b.branch4.0      |  256x28x28  |  256x28x28   |   0.00 % |   0.00 % | MaxPool2d k=3 s=1  |
| inception3b.branch4.1.conv |  256x28x28  |   64x28x28   |   0.85 % |   0.25 % | Conv2d k=1 p=0 s=1 |
| inception3b.branch4.1.bn   |   64x28x28  |   64x28x28   |   0.01 % |   0.00 % | BatchNorm2d        |
| maxpool3                   |  480x28x28  |  480x14x14   |   0.00 % |   0.00 % | MaxPool2d k=3 s=2  |
| inception4a.branch1.conv   |  480x14x14  |  192x14x14   |   1.20 % |   1.39 % | Conv2d k=1 p=0 s=1 |
| inception4a.branch1.bn     |  192x14x14  |  192x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| inception4a.branch2.0.conv |  480x14x14  |   96x14x14   |   0.60 % |   0.69 % | Conv2d k=1 p=0 s=1 |
| inception4a.branch2.0.bn   |   96x14x14  |   96x14x14   |   0.00 % |   0.01 % | BatchNorm2d        |
| inception4a.branch2.1.conv |   96x14x14  |  208x14x14   |   2.33 % |   2.71 % | Conv2d k=3 p=1 s=1 |
| inception4a.branch2.1.bn   |  208x14x14  |  208x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| inception4a.branch3.0.conv |  480x14x14  |   16x14x14   |   0.10 % |   0.12 % | Conv2d k=1 p=0 s=1 |
| inception4a.branch3.0.bn   |   16x14x14  |   16x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| inception4a.branch3.1.conv |   16x14x14  |   48x14x14   |   0.09 % |   0.10 % | Conv2d k=3 p=1 s=1 |
| inception4a.branch3.1.bn   |   48x14x14  |   48x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| inception4a.branch4.0      |  480x14x14  |  480x14x14   |   0.00 % |   0.00 % | MaxPool2d k=3 s=1  |
| inception4a.branch4.1.conv |  480x14x14  |   64x14x14   |   0.40 % |   0.46 % | Conv2d k=1 p=0 s=1 |
| inception4a.branch4.1.bn   |   64x14x14  |   64x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| inception4b.branch1.conv   |  512x14x14  |  160x14x14   |   1.06 % |   1.23 % | Conv2d k=1 p=0 s=1 |
| inception4b.branch1.bn     |  160x14x14  |  160x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| inception4b.branch2.0.conv |  512x14x14  |  112x14x14   |   0.74 % |   0.86 % | Conv2d k=1 p=0 s=1 |
| inception4b.branch2.0.bn   |  112x14x14  |  112x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| inception4b.branch2.1.conv |  112x14x14  |  224x14x14   |   2.93 % |   3.40 % | Conv2d k=3 p=1 s=1 |
| inception4b.branch2.1.bn   |  224x14x14  |  224x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| inception4b.branch3.0.conv |  512x14x14  |   24x14x14   |   0.16 % |   0.19 % | Conv2d k=1 p=0 s=1 |
| inception4b.branch3.0.bn   |   24x14x14  |   24x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| inception4b.branch3.1.conv |   24x14x14  |   64x14x14   |   0.18 % |   0.21 % | Conv2d k=3 p=1 s=1 |
| inception4b.branch3.1.bn   |   64x14x14  |   64x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| inception4b.branch4.0      |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | MaxPool2d k=3 s=1  |
| inception4b.branch4.1.conv |  512x14x14  |   64x14x14   |   0.42 % |   0.49 % | Conv2d k=1 p=0 s=1 |
| inception4b.branch4.1.bn   |   64x14x14  |   64x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| inception4c.branch1.conv   |  512x14x14  |  128x14x14   |   0.85 % |   0.99 % | Conv2d k=1 p=0 s=1 |
| inception4c.branch1.bn     |  128x14x14  |  128x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| inception4c.branch2.0.conv |  512x14x14  |  128x14x14   |   0.85 % |   0.99 % | Conv2d k=1 p=0 s=1 |
| inception4c.branch2.0.bn   |  128x14x14  |  128x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| inception4c.branch2.1.conv |  128x14x14  |  256x14x14   |   3.82 % |   4.44 % | Conv2d k=3 p=1 s=1 |
| inception4c.branch2.1.bn   |  256x14x14  |  256x14x14   |   0.01 % |   0.02 % | BatchNorm2d        |
| inception4c.branch3.0.conv |  512x14x14  |   24x14x14   |   0.16 % |   0.19 % | Conv2d k=1 p=0 s=1 |
| inception4c.branch3.0.bn   |   24x14x14  |   24x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| inception4c.branch3.1.conv |   24x14x14  |   64x14x14   |   0.18 % |   0.21 % | Conv2d k=3 p=1 s=1 |
| inception4c.branch3.1.bn   |   64x14x14  |   64x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| inception4c.branch4.0      |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | MaxPool2d k=3 s=1  |
| inception4c.branch4.1.conv |  512x14x14  |   64x14x14   |   0.42 % |   0.49 % | Conv2d k=1 p=0 s=1 |
| inception4c.branch4.1.bn   |   64x14x14  |   64x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| inception4d.branch1.conv   |  512x14x14  |  112x14x14   |   0.74 % |   0.86 % | Conv2d k=1 p=0 s=1 |
| inception4d.branch1.bn     |  112x14x14  |  112x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| inception4d.branch2.0.conv |  512x14x14  |  144x14x14   |   0.96 % |   1.11 % | Conv2d k=1 p=0 s=1 |
| inception4d.branch2.0.bn   |  144x14x14  |  144x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| inception4d.branch2.1.conv |  144x14x14  |  288x14x14   |   4.84 % |   5.62 % | Conv2d k=3 p=1 s=1 |
| inception4d.branch2.1.bn   |  288x14x14  |  288x14x14   |   0.01 % |   0.02 % | BatchNorm2d        |
| inception4d.branch3.0.conv |  512x14x14  |   32x14x14   |   0.21 % |   0.25 % | Conv2d k=1 p=0 s=1 |
| inception4d.branch3.0.bn   |   32x14x14  |   32x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| inception4d.branch3.1.conv |   32x14x14  |   64x14x14   |   0.24 % |   0.28 % | Conv2d k=3 p=1 s=1 |
| inception4d.branch3.1.bn   |   64x14x14  |   64x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| inception4d.branch4.0      |  512x14x14  |  512x14x14   |   0.00 % |   0.00 % | MaxPool2d k=3 s=1  |
| inception4d.branch4.1.conv |  512x14x14  |   64x14x14   |   0.42 % |   0.49 % | Conv2d k=1 p=0 s=1 |
| inception4d.branch4.1.bn   |   64x14x14  |   64x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| inception4e.branch1.conv   |  528x14x14  |  256x14x14   |   1.75 % |   2.04 % | Conv2d k=1 p=0 s=1 |
| inception4e.branch1.bn     |  256x14x14  |  256x14x14   |   0.01 % |   0.02 % | BatchNorm2d        |
| inception4e.branch2.0.conv |  528x14x14  |  160x14x14   |   1.10 % |   1.27 % | Conv2d k=1 p=0 s=1 |
| inception4e.branch2.0.bn   |  160x14x14  |  160x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| inception4e.branch2.1.conv |  160x14x14  |  320x14x14   |   5.98 % |   6.94 % | Conv2d k=3 p=1 s=1 |
| inception4e.branch2.1.bn   |  320x14x14  |  320x14x14   |   0.02 % |   0.02 % | BatchNorm2d        |
| inception4e.branch3.0.conv |  528x14x14  |   32x14x14   |   0.22 % |   0.25 % | Conv2d k=1 p=0 s=1 |
| inception4e.branch3.0.bn   |   32x14x14  |   32x14x14   |   0.00 % |   0.00 % | BatchNorm2d        |
| inception4e.branch3.1.conv |   32x14x14  |  128x14x14   |   0.48 % |   0.56 % | Conv2d k=3 p=1 s=1 |
| inception4e.branch3.1.bn   |  128x14x14  |  128x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| inception4e.branch4.0      |  528x14x14  |  528x14x14   |   0.00 % |   0.00 % | MaxPool2d k=3 s=1  |
| inception4e.branch4.1.conv |  528x14x14  |  128x14x14   |   0.88 % |   1.02 % | Conv2d k=1 p=0 s=1 |
| inception4e.branch4.1.bn   |  128x14x14  |  128x14x14   |   0.01 % |   0.01 % | BatchNorm2d        |
| maxpool4                   |  832x14x14  |   832x7x7    |   0.00 % |   0.00 % | MaxPool2d k=2 s=2  |
| inception5a.branch1.conv   |   832x7x7   |   256x7x7    |   0.69 % |   3.21 % | Conv2d k=1 p=0 s=1 |
| inception5a.branch1.bn     |   256x7x7   |   256x7x7    |   0.00 % |   0.02 % | BatchNorm2d        |
| inception5a.branch2.0.conv |   832x7x7   |   160x7x7    |   0.43 % |   2.00 % | Conv2d k=1 p=0 s=1 |
| inception5a.branch2.0.bn   |   160x7x7   |   160x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| inception5a.branch2.1.conv |   160x7x7   |   320x7x7    |   1.49 % |   6.94 % | Conv2d k=3 p=1 s=1 |
| inception5a.branch2.1.bn   |   320x7x7   |   320x7x7    |   0.00 % |   0.02 % | BatchNorm2d        |
| inception5a.branch3.0.conv |   832x7x7   |    32x7x7    |   0.09 % |   0.40 % | Conv2d k=1 p=0 s=1 |
| inception5a.branch3.0.bn   |    32x7x7   |    32x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| inception5a.branch3.1.conv |    32x7x7   |   128x7x7    |   0.12 % |   0.56 % | Conv2d k=3 p=1 s=1 |
| inception5a.branch3.1.bn   |   128x7x7   |   128x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| inception5a.branch4.0      |   832x7x7   |   832x7x7    |   0.00 % |   0.00 % | MaxPool2d k=3 s=1  |
| inception5a.branch4.1.conv |   832x7x7   |   128x7x7    |   0.35 % |   1.60 % | Conv2d k=1 p=0 s=1 |
| inception5a.branch4.1.bn   |   128x7x7   |   128x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| inception5b.branch1.conv   |   832x7x7   |   384x7x7    |   1.04 % |   4.81 % | Conv2d k=1 p=0 s=1 |
| inception5b.branch1.bn     |   384x7x7   |   384x7x7    |   0.00 % |   0.02 % | BatchNorm2d        |
| inception5b.branch2.0.conv |   832x7x7   |   192x7x7    |   0.52 % |   2.41 % | Conv2d k=1 p=0 s=1 |
| inception5b.branch2.0.bn   |   192x7x7   |   192x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| inception5b.branch2.1.conv |   192x7x7   |   384x7x7    |   2.15 % |   9.99 % | Conv2d k=3 p=1 s=1 |
| inception5b.branch2.1.bn   |   384x7x7   |   384x7x7    |   0.00 % |   0.02 % | BatchNorm2d        |
| inception5b.branch3.0.conv |   832x7x7   |    48x7x7    |   0.13 % |   0.60 % | Conv2d k=1 p=0 s=1 |
| inception5b.branch3.0.bn   |    48x7x7   |    48x7x7    |   0.00 % |   0.00 % | BatchNorm2d        |
| inception5b.branch3.1.conv |    48x7x7   |   128x7x7    |   0.18 % |   0.83 % | Conv2d k=3 p=1 s=1 |
| inception5b.branch3.1.bn   |   128x7x7   |   128x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| inception5b.branch4.0      |   832x7x7   |   832x7x7    |   0.00 % |   0.00 % | MaxPool2d k=3 s=1  |
| inception5b.branch4.1.conv |   832x7x7   |   128x7x7    |   0.35 % |   1.60 % | Conv2d k=1 p=0 s=1 |
| inception5b.branch4.1.bn   |   128x7x7   |   128x7x7    |   0.00 % |   0.01 % | BatchNorm2d        |
| avgpool                    |   1024x7x7  |   1024x1x1   |   0.00 % |   0.00 % | AdaptiveAvgPool2d  |
| dropout                    |     1024    |     1024     |   0.00 % |   0.00 % | Dropout            |
| fc                         |     1024    |     1000     |   0.07 % |  15.44 % | Linear             |
| Total                      |  3x224x224  |     1000     |   1.51 G |   6.64 M | GoogLeNet          |