# tinydrm_show

This repo automates the process of compiling and installation of tiny DRM display driver with its overlay. A display driver is compiled only when it isn't installed by default in your raspbian installation.

## Setup
Download or clone this repo and run configure script. cd to the generated build folder and run inst script as sudo.

```shell
git clone https://github.com/akhilharihar/tinydrm_show.git

cd tinydrm_show
```

Run `./configure -h` to get a list of available drivers


```shell
./configure driver_name

cd build

sudo ./inst
```

To enable overlay, add `dtoverlay=driver_name` at the end of `/boot/config.txt`.

Reboot your system for the changes to take effect.

## Testing

https://github.com/akhilharihar/tinydrm_show/wiki/Testing-DRM-display

## References
- Tiny DRM - https://github.com/notro/tinydrm

- DTS file specification - https://github.com/devicetree-org/devicetree-specification/releases/download/v0.3/devicetree-specification-v0.3.pdf

- DTS file examples - https://github.com/raspberrypi/linux/tree/rpi-5.4.y/arch/arm/boot/dts/overlays
