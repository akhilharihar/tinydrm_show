# tinydrm_show

To get your display working, you'll need a driver specific to your display controller and an overlay.

## Setup and Compilation
Download or clone this repo and run configure script which will create a build directory. cd to build folder and run compile script with sudo privileges.

```shell
git clone https://github.com/akhilharihar/tinydrm_show.git

cd tinydrm_show
```

Run `./configure -h` to get a list of available drv_name


```shell
./configure drv_name

cd build

sudo ./compile
```

## Installation

Copy dtbo file from `overlay` to `/boot/overlays`

If there's a `driver` folder in `build`, copy .ko files from it to tiny DRM driver directory.
```shell
sudo cp ./overlay/*.dtbo /boot/overlays/

sudo cp ./driver/*.ko /lib/modules/$(uname -r)/kernel/drivers/gpu/drm/tiny/

sudo depmod
```

To enable overlay, add `dtoverlay=overlay_name` at the end of `/boot/config.txt`. You'll need to set GL driver to full kms via raspi-config for drm drivers to work properly.

Reboot your system for the changes to take effect.

## Testing

Run `ls /dev/fb*` and `ls /dev/dri/card*`. There should be `/dev/fb1` and `/dev/dri/card1` that are linked to tiny DRM display drivers.

modetest tool - 

```
sudo apt install libdrm-tests -y
```

Visit https://github.com/notro/tinydrm/wiki/Development#modetest for instructions on how to use it.

## References
- Tiny DRM - https://github.com/notro/tinydrm

- DTS file specification - https://github.com/devicetree-org/devicetree-specification/releases/download/v0.3/devicetree-specification-v0.3.pdf

- DTS file examples - https://github.com/raspberrypi/linux/tree/rpi-5.4.y/arch/arm/boot/dts/overlays
