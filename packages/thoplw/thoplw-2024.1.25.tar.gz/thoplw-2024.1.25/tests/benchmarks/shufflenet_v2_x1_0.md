| Name               | Input shape | Output shape |     MACs |   Params | Description        |
|:------------------:|:-----------:|:------------:|:--------:|:--------:|:------------------:|
| conv1.0            |  3x224x224  |  24x112x112  |   5.32 % |   0.03 % | Conv2d k=3 p=1 s=2 |
| conv1.1            |  24x112x112 |  24x112x112  |   0.79 % |   0.00 % | BatchNorm2d        |
| conv1.2            |  24x112x112 |  24x112x112  |   0.00 % |   0.00 % | ReLU               |
| maxpool            |  24x112x112 |   24x56x56   |   0.00 % |   0.00 % | MaxPool2d k=3 s=2  |
| stage2.0.branch1.0 |   24x56x56  |   24x28x28   |   0.11 % |   0.01 % | Conv2d k=3 p=1 s=2 |
| stage2.0.branch1.1 |   24x28x28  |   24x28x28   |   0.05 % |   0.00 % | BatchNorm2d        |
| stage2.0.branch1.2 |   24x28x28  |   58x28x28   |   0.71 % |   0.06 % | Conv2d k=1 p=0 s=1 |
| stage2.0.branch1.3 |   58x28x28  |   58x28x28   |   0.12 % |   0.01 % | BatchNorm2d        |
| stage2.0.branch1.4 |   58x28x28  |   58x28x28   |   0.00 % |   0.00 % | ReLU               |
| stage2.0.branch2.0 |   24x56x56  |   58x56x56   |   2.86 % |   0.06 % | Conv2d k=1 p=0 s=1 |
| stage2.0.branch2.1 |   58x56x56  |   58x56x56   |   0.48 % |   0.01 % | BatchNorm2d        |
| stage2.0.branch2.2 |   58x56x56  |   58x56x56   |   0.00 % |   0.00 % | ReLU               |
| stage2.0.branch2.3 |   58x56x56  |   58x28x28   |   0.27 % |   0.02 % | Conv2d k=3 p=1 s=2 |
| stage2.0.branch2.4 |   58x28x28  |   58x28x28   |   0.12 % |   0.01 % | BatchNorm2d        |
| stage2.0.branch2.5 |   58x28x28  |   58x28x28   |   1.73 % |   0.15 % | Conv2d k=1 p=0 s=1 |
| stage2.0.branch2.6 |   58x28x28  |   58x28x28   |   0.12 % |   0.01 % | BatchNorm2d        |
| stage2.0.branch2.7 |   58x28x28  |   58x28x28   |   0.00 % |   0.00 % | ReLU               |
| stage2.1.branch2.0 |   58x28x28  |   58x28x28   |   1.73 % |   0.15 % | Conv2d k=1 p=0 s=1 |
| stage2.1.branch2.1 |   58x28x28  |   58x28x28   |   0.12 % |   0.01 % | BatchNorm2d        |
| stage2.1.branch2.2 |   58x28x28  |   58x28x28   |   0.00 % |   0.00 % | ReLU               |
| stage2.1.branch2.3 |   58x28x28  |   58x28x28   |   0.27 % |   0.02 % | Conv2d k=3 p=1 s=1 |
| stage2.1.branch2.4 |   58x28x28  |   58x28x28   |   0.12 % |   0.01 % | BatchNorm2d        |
| stage2.1.branch2.5 |   58x28x28  |   58x28x28   |   1.73 % |   0.15 % | Conv2d k=1 p=0 s=1 |
| stage2.1.branch2.6 |   58x28x28  |   58x28x28   |   0.12 % |   0.01 % | BatchNorm2d        |
| stage2.1.branch2.7 |   58x28x28  |   58x28x28   |   0.00 % |   0.00 % | ReLU               |
| stage2.2.branch2.0 |   58x28x28  |   58x28x28   |   1.73 % |   0.15 % | Conv2d k=1 p=0 s=1 |
| stage2.2.branch2.1 |   58x28x28  |   58x28x28   |   0.12 % |   0.01 % | BatchNorm2d        |
| stage2.2.branch2.2 |   58x28x28  |   58x28x28   |   0.00 % |   0.00 % | ReLU               |
| stage2.2.branch2.3 |   58x28x28  |   58x28x28   |   0.27 % |   0.02 % | Conv2d k=3 p=1 s=1 |
| stage2.2.branch2.4 |   58x28x28  |   58x28x28   |   0.12 % |   0.01 % | BatchNorm2d        |
| stage2.2.branch2.5 |   58x28x28  |   58x28x28   |   1.73 % |   0.15 % | Conv2d k=1 p=0 s=1 |
| stage2.2.branch2.6 |   58x28x28  |   58x28x28   |   0.12 % |   0.01 % | BatchNorm2d        |
| stage2.2.branch2.7 |   58x28x28  |   58x28x28   |   0.00 % |   0.00 % | ReLU               |
| stage2.3.branch2.0 |   58x28x28  |   58x28x28   |   1.73 % |   0.15 % | Conv2d k=1 p=0 s=1 |
| stage2.3.branch2.1 |   58x28x28  |   58x28x28   |   0.12 % |   0.01 % | BatchNorm2d        |
| stage2.3.branch2.2 |   58x28x28  |   58x28x28   |   0.00 % |   0.00 % | ReLU               |
| stage2.3.branch2.3 |   58x28x28  |   58x28x28   |   0.27 % |   0.02 % | Conv2d k=3 p=1 s=1 |
| stage2.3.branch2.4 |   58x28x28  |   58x28x28   |   0.12 % |   0.01 % | BatchNorm2d        |
| stage2.3.branch2.5 |   58x28x28  |   58x28x28   |   1.73 % |   0.15 % | Conv2d k=1 p=0 s=1 |
| stage2.3.branch2.6 |   58x28x28  |   58x28x28   |   0.12 % |   0.01 % | BatchNorm2d        |
| stage2.3.branch2.7 |   58x28x28  |   58x28x28   |   0.00 % |   0.00 % | ReLU               |
| stage3.0.branch1.0 |  116x28x28  |  116x14x14   |   0.13 % |   0.05 % | Conv2d k=3 p=1 s=2 |
| stage3.0.branch1.1 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.0.branch1.2 |  116x14x14  |  116x14x14   |   1.73 % |   0.59 % | Conv2d k=1 p=0 s=1 |
| stage3.0.branch1.3 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.0.branch1.4 |  116x14x14  |  116x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.0.branch2.0 |  116x28x28  |  116x28x28   |   6.91 % |   0.59 % | Conv2d k=1 p=0 s=1 |
| stage3.0.branch2.1 |  116x28x28  |  116x28x28   |   0.24 % |   0.02 % | BatchNorm2d        |
| stage3.0.branch2.2 |  116x28x28  |  116x28x28   |   0.00 % |   0.00 % | ReLU               |
| stage3.0.branch2.3 |  116x28x28  |  116x14x14   |   0.13 % |   0.05 % | Conv2d k=3 p=1 s=2 |
| stage3.0.branch2.4 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.0.branch2.5 |  116x14x14  |  116x14x14   |   1.73 % |   0.59 % | Conv2d k=1 p=0 s=1 |
| stage3.0.branch2.6 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.0.branch2.7 |  116x14x14  |  116x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.1.branch2.0 |  116x14x14  |  116x14x14   |   1.73 % |   0.59 % | Conv2d k=1 p=0 s=1 |
| stage3.1.branch2.1 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.1.branch2.2 |  116x14x14  |  116x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.1.branch2.3 |  116x14x14  |  116x14x14   |   0.13 % |   0.05 % | Conv2d k=3 p=1 s=1 |
| stage3.1.branch2.4 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.1.branch2.5 |  116x14x14  |  116x14x14   |   1.73 % |   0.59 % | Conv2d k=1 p=0 s=1 |
| stage3.1.branch2.6 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.1.branch2.7 |  116x14x14  |  116x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.2.branch2.0 |  116x14x14  |  116x14x14   |   1.73 % |   0.59 % | Conv2d k=1 p=0 s=1 |
| stage3.2.branch2.1 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.2.branch2.2 |  116x14x14  |  116x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.2.branch2.3 |  116x14x14  |  116x14x14   |   0.13 % |   0.05 % | Conv2d k=3 p=1 s=1 |
| stage3.2.branch2.4 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.2.branch2.5 |  116x14x14  |  116x14x14   |   1.73 % |   0.59 % | Conv2d k=1 p=0 s=1 |
| stage3.2.branch2.6 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.2.branch2.7 |  116x14x14  |  116x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.3.branch2.0 |  116x14x14  |  116x14x14   |   1.73 % |   0.59 % | Conv2d k=1 p=0 s=1 |
| stage3.3.branch2.1 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.3.branch2.2 |  116x14x14  |  116x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.3.branch2.3 |  116x14x14  |  116x14x14   |   0.13 % |   0.05 % | Conv2d k=3 p=1 s=1 |
| stage3.3.branch2.4 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.3.branch2.5 |  116x14x14  |  116x14x14   |   1.73 % |   0.59 % | Conv2d k=1 p=0 s=1 |
| stage3.3.branch2.6 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.3.branch2.7 |  116x14x14  |  116x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.4.branch2.0 |  116x14x14  |  116x14x14   |   1.73 % |   0.59 % | Conv2d k=1 p=0 s=1 |
| stage3.4.branch2.1 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.4.branch2.2 |  116x14x14  |  116x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.4.branch2.3 |  116x14x14  |  116x14x14   |   0.13 % |   0.05 % | Conv2d k=3 p=1 s=1 |
| stage3.4.branch2.4 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.4.branch2.5 |  116x14x14  |  116x14x14   |   1.73 % |   0.59 % | Conv2d k=1 p=0 s=1 |
| stage3.4.branch2.6 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.4.branch2.7 |  116x14x14  |  116x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.5.branch2.0 |  116x14x14  |  116x14x14   |   1.73 % |   0.59 % | Conv2d k=1 p=0 s=1 |
| stage3.5.branch2.1 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.5.branch2.2 |  116x14x14  |  116x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.5.branch2.3 |  116x14x14  |  116x14x14   |   0.13 % |   0.05 % | Conv2d k=3 p=1 s=1 |
| stage3.5.branch2.4 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.5.branch2.5 |  116x14x14  |  116x14x14   |   1.73 % |   0.59 % | Conv2d k=1 p=0 s=1 |
| stage3.5.branch2.6 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.5.branch2.7 |  116x14x14  |  116x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.6.branch2.0 |  116x14x14  |  116x14x14   |   1.73 % |   0.59 % | Conv2d k=1 p=0 s=1 |
| stage3.6.branch2.1 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.6.branch2.2 |  116x14x14  |  116x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.6.branch2.3 |  116x14x14  |  116x14x14   |   0.13 % |   0.05 % | Conv2d k=3 p=1 s=1 |
| stage3.6.branch2.4 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.6.branch2.5 |  116x14x14  |  116x14x14   |   1.73 % |   0.59 % | Conv2d k=1 p=0 s=1 |
| stage3.6.branch2.6 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.6.branch2.7 |  116x14x14  |  116x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.7.branch2.0 |  116x14x14  |  116x14x14   |   1.73 % |   0.59 % | Conv2d k=1 p=0 s=1 |
| stage3.7.branch2.1 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.7.branch2.2 |  116x14x14  |  116x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage3.7.branch2.3 |  116x14x14  |  116x14x14   |   0.13 % |   0.05 % | Conv2d k=3 p=1 s=1 |
| stage3.7.branch2.4 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.7.branch2.5 |  116x14x14  |  116x14x14   |   1.73 % |   0.59 % | Conv2d k=1 p=0 s=1 |
| stage3.7.branch2.6 |  116x14x14  |  116x14x14   |   0.06 % |   0.02 % | BatchNorm2d        |
| stage3.7.branch2.7 |  116x14x14  |  116x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage4.0.branch1.0 |  232x14x14  |   232x7x7    |   0.07 % |   0.09 % | Conv2d k=3 p=1 s=2 |
| stage4.0.branch1.1 |   232x7x7   |   232x7x7    |   0.03 % |   0.04 % | BatchNorm2d        |
| stage4.0.branch1.2 |   232x7x7   |   232x7x7    |   1.73 % |   2.35 % | Conv2d k=1 p=0 s=1 |
| stage4.0.branch1.3 |   232x7x7   |   232x7x7    |   0.03 % |   0.04 % | BatchNorm2d        |
| stage4.0.branch1.4 |   232x7x7   |   232x7x7    |   0.00 % |   0.00 % | ReLU               |
| stage4.0.branch2.0 |  232x14x14  |  232x14x14   |   6.91 % |   2.35 % | Conv2d k=1 p=0 s=1 |
| stage4.0.branch2.1 |  232x14x14  |  232x14x14   |   0.12 % |   0.04 % | BatchNorm2d        |
| stage4.0.branch2.2 |  232x14x14  |  232x14x14   |   0.00 % |   0.00 % | ReLU               |
| stage4.0.branch2.3 |  232x14x14  |   232x7x7    |   0.07 % |   0.09 % | Conv2d k=3 p=1 s=2 |
| stage4.0.branch2.4 |   232x7x7   |   232x7x7    |   0.03 % |   0.04 % | BatchNorm2d        |
| stage4.0.branch2.5 |   232x7x7   |   232x7x7    |   1.73 % |   2.35 % | Conv2d k=1 p=0 s=1 |
| stage4.0.branch2.6 |   232x7x7   |   232x7x7    |   0.03 % |   0.04 % | BatchNorm2d        |
| stage4.0.branch2.7 |   232x7x7   |   232x7x7    |   0.00 % |   0.00 % | ReLU               |
| stage4.1.branch2.0 |   232x7x7   |   232x7x7    |   1.73 % |   2.35 % | Conv2d k=1 p=0 s=1 |
| stage4.1.branch2.1 |   232x7x7   |   232x7x7    |   0.03 % |   0.04 % | BatchNorm2d        |
| stage4.1.branch2.2 |   232x7x7   |   232x7x7    |   0.00 % |   0.00 % | ReLU               |
| stage4.1.branch2.3 |   232x7x7   |   232x7x7    |   0.07 % |   0.09 % | Conv2d k=3 p=1 s=1 |
| stage4.1.branch2.4 |   232x7x7   |   232x7x7    |   0.03 % |   0.04 % | BatchNorm2d        |
| stage4.1.branch2.5 |   232x7x7   |   232x7x7    |   1.73 % |   2.35 % | Conv2d k=1 p=0 s=1 |
| stage4.1.branch2.6 |   232x7x7   |   232x7x7    |   0.03 % |   0.04 % | BatchNorm2d        |
| stage4.1.branch2.7 |   232x7x7   |   232x7x7    |   0.00 % |   0.00 % | ReLU               |
| stage4.2.branch2.0 |   232x7x7   |   232x7x7    |   1.73 % |   2.35 % | Conv2d k=1 p=0 s=1 |
| stage4.2.branch2.1 |   232x7x7   |   232x7x7    |   0.03 % |   0.04 % | BatchNorm2d        |
| stage4.2.branch2.2 |   232x7x7   |   232x7x7    |   0.00 % |   0.00 % | ReLU               |
| stage4.2.branch2.3 |   232x7x7   |   232x7x7    |   0.07 % |   0.09 % | Conv2d k=3 p=1 s=1 |
| stage4.2.branch2.4 |   232x7x7   |   232x7x7    |   0.03 % |   0.04 % | BatchNorm2d        |
| stage4.2.branch2.5 |   232x7x7   |   232x7x7    |   1.73 % |   2.35 % | Conv2d k=1 p=0 s=1 |
| stage4.2.branch2.6 |   232x7x7   |   232x7x7    |   0.03 % |   0.04 % | BatchNorm2d        |
| stage4.2.branch2.7 |   232x7x7   |   232x7x7    |   0.00 % |   0.00 % | ReLU               |
| stage4.3.branch2.0 |   232x7x7   |   232x7x7    |   1.73 % |   2.35 % | Conv2d k=1 p=0 s=1 |
| stage4.3.branch2.1 |   232x7x7   |   232x7x7    |   0.03 % |   0.04 % | BatchNorm2d        |
| stage4.3.branch2.2 |   232x7x7   |   232x7x7    |   0.00 % |   0.00 % | ReLU               |
| stage4.3.branch2.3 |   232x7x7   |   232x7x7    |   0.07 % |   0.09 % | Conv2d k=3 p=1 s=1 |
| stage4.3.branch2.4 |   232x7x7   |   232x7x7    |   0.03 % |   0.04 % | BatchNorm2d        |
| stage4.3.branch2.5 |   232x7x7   |   232x7x7    |   1.73 % |   2.35 % | Conv2d k=1 p=0 s=1 |
| stage4.3.branch2.6 |   232x7x7   |   232x7x7    |   0.03 % |   0.04 % | BatchNorm2d        |
| stage4.3.branch2.7 |   232x7x7   |   232x7x7    |   0.00 % |   0.00 % | ReLU               |
| conv5.0            |   464x7x7   |   1024x7x7   |  15.25 % |  20.71 % | Conv2d k=1 p=0 s=1 |
| conv5.1            |   1024x7x7  |   1024x7x7   |   0.13 % |   0.18 % | BatchNorm2d        |
| conv5.2            |   1024x7x7  |   1024x7x7   |   0.00 % |   0.00 % | ReLU               |
| fc                 |     1024    |     1000     |   0.67 % |  44.67 % | Linear             |
| Total              |  3x224x224  |     1000     | 152.71 M |   2.29 M | ShuffleNetV2       |