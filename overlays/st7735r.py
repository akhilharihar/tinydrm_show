from . import Overlay

"""
Device Tree overlay generator for st7735r displays
"""


class ST7735R(Overlay):

    def __init__(self) -> None:
        print("this is working")
        self.get_input()

    @property
    def resolutions(self) -> dict:
        return {
            "128x160": "jianda,jd-t18003-t01",
            "128x128": "okaya,rh128128t"
        }

    def dts(self) -> str:
        return """/dts-v1/;
/plugin/;

/ {{

    compatible = "brcm,bcm2835";

    fragment@0 {{
        target = <&spi0>;
        __overlay__ {{
            status = "okay";

            spidev@0{{
                status = "disabled";
            }};

        }};
    }};

    fragment@1 {{
        target = <&gpio>;
        __overlay__ {{
            st7735r_pins: st7735r_pins {{
                brcm,pins = <23 24 25>;
                brcm,function = <1 1 1>; /* in out out out */
            }};
        }};
    }};

    fragment@2 {{
        target = <&spi0>;
        __overlay__ {{
            /* needed to avoid dtc warning */
            #address-cells = <1>;
            #size-cells = <0>;

            st7735r: st7735r@0{{
                compatible = "{drv_name}";
                pinctrl-names = "default";
                pinctrl-0 = <&st7735r_pins>;

                reg = <0>;
                spi-max-frequency = <16000000>;

                rotation = <0>;
                reset-gpios = <&gpio 24 0>;
                dc-gpios = <&gpio 25 0>;
                backlight = <&backlight>;
            }};
        }};
    }};

    fragment@3 {{
        target-path = "/soc";
        __overlay__ {{
            backlight: backlight {{
                compatible = "gpio-backlight";
                gpios = <&gpio 23 0>;
            }};
        }};
    }};

    __overrides__ {{
        speed =		<&st7735r>,"spi-max-frequency:0";
        rotation =	<&st7735r>,"rotation:0";
        bl = <&st7735r_pins>,"brcm,pins:0",<&backlight>,"gpios:4";
        rst = <&st7735r_pins>,"brcm,pins:4",<&st7735r>,"reset-gpios:4";
        dc = <&st7735r_pins>,"brcm,pins:8",<&st7735r>,"dc-gpios:4";
    }};
}};
""".format(drv_name=self.resolutions[self.res])
