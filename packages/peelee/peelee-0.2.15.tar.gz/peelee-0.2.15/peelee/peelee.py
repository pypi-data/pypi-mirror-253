#!/usr/bin/env python3
"""peelee is one module to generate random palette and colors.
"""
import colorsys
import getopt
import random
import sys
from enum import Enum

from loguru import logger

COLOR_RANGE_DENOMINATOR = 12


class PaletteMode(Enum):
    """Palette mode"""

    DARK = 0
    LIGHT = 1
    RANDOM = 2


class ColorSliceType(Enum):
    """Color slice types"""

    DARKER = 0
    LIGHTER = 1


class ColorName(Enum):
    """Color names"""

    RED = 0
    GREEN = 1
    BLUE = 2
    YELLOW = 3
    CYAN = 4
    VIOLET = 5
    BLACK = 6
    RANDOM = 7


def fg(hex_color, msg):
    """Decorate msg with hex_color in foreground."""
    _rgb = hex2rgb(hex_color)
    return f"\x01\x1b[38;2;{_rgb[0]};{_rgb[1]};{_rgb[2]}m\x02{msg}\x01\x1b[0m"


def bg(hex_color, msg):
    """Decorate msg with hex_color in background."""
    _rgb = hex2rgb(hex_color)
    return f"\x01\x1b[48;2;{_rgb[0]};{_rgb[1]};{_rgb[2]}m\x02{msg}\x01\x1b[0m"


def hex2rgb(hex_color):
    """ "Convert."""
    hex_color = hex_color.lstrip("#")
    rgb_color = tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))
    return rgb_color


def hex2hls(hex_color):
    """ "Convert."""
    rgb_color = hex2rgb(hex_color)
    normalized_rgb = (
        rgb_color[0] / 255.0,
        rgb_color[1] / 255.0,
        rgb_color[2] / 255.0,
    )
    hls_color = colorsys.rgb_to_hls(
        normalized_rgb[0], normalized_rgb[1], normalized_rgb[2]
    )
    return hls_color


def hls2hex(hls_color):
    """
    Convert HSL color to HEX code.

    Parameter:
    hls_color - tuple containing hue, lightness, and saturation color codes
    such as (0.5277777777777778, 0.04, 1).
    """
    rgb_color = colorsys.hls_to_rgb(hls_color[0], hls_color[1], hls_color[2])
    scaled_rgb = tuple(int(c * 255) for c in rgb_color)
    return rgb2hex(scaled_rgb)


def rgb2hex(rgb_color):
    """ "Convert."""
    scaled_rgb = rgb_color
    if isinstance(rgb_color[0], float):
        scaled_rgb = tuple(int(c * 255) for c in rgb_color)
    hex_color = f"#{scaled_rgb[0]:02X}{scaled_rgb[1]:02X}{scaled_rgb[2]:02X}"
    return hex_color


def calculate_relative_luminance(hex_color):
    """Calculate relative luminance for hex color codes.

    Refer to:
    https://www.w3.org/TR/WCAG20-TECHS/G17.html

    Parameter:
    hex_color - hex color code
    """

    rgb_8bit = hex2rgb(hex_color)
    rgb_srgb = tuple(_8bit / 255.0 for _8bit in rgb_8bit)
    r, g, b = tuple(
        _srgb / 12.92 if _srgb <= 0.03928 else ((_srgb + 0.055) / 1.055) ** 2.4
        for _srgb in rgb_srgb
    )

    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def calculate_contrast_ratio(hex_light_color, hex_dark_color):
    """Calculate contrast ratio for hex color codes.

    Parameter:
    hex_light_color - hex color code of the lighter of the foreground or background color
    hex_dark_color - hex color code of the darker of the foreground or background color

    Refer to:
    https://www.w3.org/TR/WCAG20-TECHS/G17.html
    """
    relative_luminance_light = calculate_relative_luminance(hex_light_color)
    relative_luminance_dark = calculate_relative_luminance(hex_dark_color)
    return (relative_luminance_light + 0.05) / (relative_luminance_dark + 0.05)


def get_scheme_colors(hex_color, n_colors=7):
    """
    Generate a list of n_colors triadic colors based on the given hex_color.

    Args:
        hex_color (str): The hexadecimal color code.
        n_colors (int): The number of triadic colors to generate. Default is 7.

    Returns:
        list: A list of n_colors triadic color codes.

    Raises:
        AssertionError: If hex_color is None or n_colors is not an integer greater than 0.
    """
    assert hex_color is not None, "Invalid argument: hex_color is None."
    assert (
        n_colors is not None and isinstance(n_colors, int) and n_colors > 0
    ), f"Invalid argument: n_colors = {n_colors}"
    hls_color = hex2hls(hex_color)
    triadic_colors = []
    for offset in range(0, 360, 360 // n_colors):
        triadic_colors.append(
            ((hls_color[0] + offset / 360) % 1.0, hls_color[1], hls_color[2])
        )
    base_colors = [hls2hex(hls_color) for hls_color in triadic_colors][0:n_colors]

    # the following line is to solve the deviation issue caused by 360 //n_colors (e.g. if n_colors = 7, and base color is #130613, then the base color would be changed to #130612.)
    base_colors.insert(1, hex_color)
    base_colors = base_colors[1:]

    # reverse the list to make sure the base color is the last - normally it
    # will be used as the main color of the workbench theme
    base_colors.reverse()
    return base_colors


def padding(num, target_length=2):
    """
    Padding left for number to make it's string format length reaches the target length.

    This is mainly used to construct valid hex color number in R,G,B
    position. Example, if the given num is a hex number 0xf and the
    target length is 2, then the padding result is 0f.
    """
    str_num = str(num)
    target_length = target_length if target_length and target_length > 2 else 2
    if str_num.startswith("0x"):
        str_num = str_num[2:]
    if len(str_num) < target_length:
        str_num = (
            f"{''.join(['0' for _ in range(target_length - len(str_num))])}{str_num}"
        )
    return str_num


def get_slice_colors(
    base_color, n_slices, color_slice_type: ColorSliceType = ColorSliceType.DARKER
):
    """Given base color, return 'n' color hex codes from base color to darkest
    color."""
    rgb_base_color = hex2rgb(base_color)
    is_black_or_white_gray = max(rgb_base_color) == min(rgb_base_color)
    hls_base_color = hex2hls(base_color)
    lightness_decimal_length = max(len(str(hls_base_color[1])[2:]), 16)
    full_lightness = 10**lightness_decimal_length
    lightness = hls_base_color[1] * full_lightness
    int_lightness = int(lightness)

    saturation_decimal_length = max(len(str(hls_base_color[2])[2:]), 16)
    full_saturation = 10**saturation_decimal_length
    saturation = hls_base_color[2] * full_saturation
    int_saturation = int(saturation)

    if color_slice_type == ColorSliceType.LIGHTER:
        _min_lightness = int_lightness
        _max_lightness = full_lightness
        _lightness_slice_length = (full_lightness - int_lightness) // n_slices

        _min_saturation = int_saturation
        _max_saturation = full_saturation
        _saturation_slice_length = (full_saturation - int_saturation) // n_slices
    else:
        _max_lightness = int_lightness
        _min_lightness = 0
        _lightness_slice_length = int_lightness // n_slices

        _max_saturation = int_saturation
        _min_saturation = 0
        _saturation_slice_length = int_saturation // n_slices

    if int_lightness == 0 and color_slice_type == ColorSliceType.DARKER:
        lightness_list = [0 for _ in range(n_slices)]
    elif _lightness_slice_length == 0:
        lightness_list = [int_lightness for _ in range(n_slices)]
    else:
        lightness_list = list(
            range(_min_lightness, _max_lightness, _lightness_slice_length)[0:n_slices]
        )
    # cannot be darker or won't change black to other color (e.g. red)
    if int_saturation == 0 and (
        color_slice_type == ColorSliceType.DARKER or is_black_or_white_gray
    ):
        saturation_list = [0 for _ in range(n_slices)]
    elif int_saturation >= full_saturation and (
        color_slice_type == ColorSliceType.LIGHTER or is_black_or_white_gray
    ):
        saturation_list = [full_saturation for _ in range(n_slices)]
    elif _saturation_slice_length == 0:
        logger.error(
            {
                "base_color": base_color,
                "hls_base_color": hls_base_color,
                "_min_lightness": _min_lightness,
                "_max_lightness": _max_lightness,
                "_lightness_slice_length": _lightness_slice_length,
                "n_slices": n_slices,
                "_min_saturation": _min_saturation,
                "_max_saturation": _max_saturation,
                "_saturation_slice_length": _saturation_slice_length,
                "color_slice_type": color_slice_type,
            }
        )
        saturation_list = [int_lightness for _ in range(n_slices)]
    else:
        try:
            saturation_list = list(
                range(_min_saturation, _max_saturation, _saturation_slice_length)[
                    0:n_slices
                ]
            )
        except ValueError as exc:
            logger.error(
                (
                    base_color,
                    hls_base_color,
                    _min_lightness,
                    _max_lightness,
                    _lightness_slice_length,
                    n_slices,
                    _min_saturation,
                    _max_saturation,
                    _saturation_slice_length,
                )
            )
            raise exc
    try:
        hls_slice_colors = [
            (
                hls_base_color[0],
                lightness_list[index] / full_lightness,
                saturation_list[index] / full_saturation,
            )
            for index in range(n_slices)
        ]
    except IndexError as exc:
        logger.error(
            (
                base_color,
                hls_base_color,
                _min_lightness,
                _max_lightness,
                _lightness_slice_length,
                n_slices,
                _min_saturation,
                _max_saturation,
                _saturation_slice_length,
            )
        )
        raise exc

    hex_slice_colors = [hls2hex(hls_color) for hls_color in hls_slice_colors]
    if base_color not in hex_slice_colors:
        if color_slice_type == ColorSliceType.DARKER:
            hex_slice_colors = hex_slice_colors[0:-1]
            hex_slice_colors.append(base_color)
        else:
            hex_slice_colors.insert(0, base_color)
            hex_slice_colors = hex_slice_colors[0:-1]
    return hex_slice_colors


def darker(base_color, n_color):
    """Given base color, return 'n' color hex codes from base color to darkest
    color."""
    return get_slice_colors(base_color, n_color, ColorSliceType.DARKER)


def lighter(base_color, n_color):
    """Given base color, return 'n' color hex codes from base color to lightest
    color."""
    return get_slice_colors(base_color, n_color, ColorSliceType.LIGHTER)


def set_hue(hex_color, hue):
    """Set saturation."""
    if hue is None:
        return hex_color
    hls_color = hex2hls(hex_color)
    new_hls_color = (hue, hls_color[1], hls_color[2])
    return hls2hex(new_hls_color)


def set_saturation(hex_color, saturation):
    """Set saturation."""
    if saturation is None:
        return hex_color
    hls_color = hex2hls(hex_color)
    new_hls_color = (hls_color[0], hls_color[1], saturation)
    return hls2hex(new_hls_color)


def set_lightness(hex_color, lightness):
    """Set saturation."""
    if lightness is None:
        return hex_color
    hls_color = hex2hls(hex_color)
    new_hls_color = (hls_color[0], lightness, hls_color[2])
    return hls2hex(new_hls_color)


def set_hls_values(hex_color, hue, saturation, lightness):
    """Set saturation."""
    hls_color = hex2hls(hex_color)
    new_hls_color = (
        hue or hls_color[0],
        lightness or hls_color[1],
        saturation or hls_color[2],
    )
    return hls2hex(new_hls_color)


def generate_random_colors(
    min_color=0,
    max_color=231,
    colors_total=7,
    color_gradations=24,
    base_color_name=None,
    base_color=None,
    hue=None,
    saturation=None,
    lightness=None,
    palette_mode=PaletteMode.LIGHT,
):
    """
    Generate random color hex codes.

    Firstly, it will generate random integer from min_color (0-(255 - colors_gradations - 1)) to max_color (0-(255 - colors_gradations)).
    The max_color should be less than (255 - colors_gradations) because it needs the room to generate lighter colors.

    To generate darker colors, use smaller value for max_color.
    To generate ligher colors, use bigger value for min_color.

    It's recommended to use default values.
    If you want to make change, please make sure what you are doing.

    Secondly, it will generate 'colors_gradations' different hex color codes from base color to the lightest color.

        min_color - minimum color code. default: 0.
        max_color - maximum color code. default: 254 (cannot be bigger value).
        colors_total - how many base colors to generate. default: 7.
        colors_gradations - how many lighter colors to generate. default: 24.
        base_color_name - color name. default: None. If None, then use random color name. it's used to generate the 'seed' random color which will be used to get more triadic colors.
        base_color - base color hex code. default: None. it has higher priority than base_color-name.
        saturation - saturation value to set for each base color. default: None.
        lightness - lightness value to set for each base color. default: None.

    Retrun:
        Generated random base colors and all lighter colors of each base color.
        The returned value is a two-dimention list. First dimention length is the value of base_colors_total. Second dimention length is colors_gradations.
    """
    if color_gradations < 0 or color_gradations > 253:
        color_gradations = 24
    if min_color < 0 or min_color > (255 - color_gradations - 1):
        min_color = 0
    if max_color <= min_color or max_color >= (255 - color_gradations):
        max_color = 255 - color_gradations - 1
    # if base color is given, set hls values if they are given
    if base_color:
        base_color = set_hls_values(base_color, hue, saturation, lightness)
    random_color = base_color or generate_random_hex_color_code(
        min_color,
        max_color,
        color_name=base_color_name,
        hue=hue,
        saturation=saturation,
        lightness=lightness,
    )
    if palette_mode == PaletteMode.DARK:
        color_slice_type = ColorSliceType.DARKER
    else:
        color_slice_type = ColorSliceType.LIGHTER
    logger.debug(f"Random Color: {random_color}")
    base_colors = generate_base_colors(random_color, colors_total)
    logger.debug(f"Base Colors: {base_colors}")

    random_colors_list = []
    for _base_color in base_colors:
        slice_colors = get_slice_colors(_base_color, color_gradations, color_slice_type)
        random_colors_list.append(slice_colors)

    return random_colors_list


def generate_random_hex_color_code(
    min_color,
    max_color,
    color_name: ColorName = None,
    hue=None,
    saturation=None,
    lightness=None,
):
    """
    Generates a list of base colors based on the given minimum and maximum
    color values and the total number of colors.

    Parameters:
    - min_color (int): The minimum value of the color range.
    - max_color (int): The maximum value of the color range.
    - total (int): The total number of base colors to generate.

    Returns:
    - base_colors (list): A list of base colors generated based on the given parameters.
    """
    hex_color_code_header = "#"
    random_hex_color_code = []

    # Old solution - only used for dark colors which needs dynamic colors.
    # By new solution, the dark color might be always the black color since
    # the max value is not big enough to have room to generate random colors
    # after divide by COLOR_RANGE_DENOMINATOR.
    # The old solution is usually used for workbench colors.
    diff = max_color - min_color
    if diff < COLOR_RANGE_DENOMINATOR:
        for index in range(0, 3):
            random_int = random.randint(min_color, max_color)
            _random_color = padding(hex(random_int))
            random_hex_color_code.append(_random_color)
    else:
        # New solution - 2023.12.19(Stockholm.Kungsängen.TibbleTorg) -in this
        # way, the generated colors are in the 'best' range and the theme
        # effection will be stable. The 'best' range will generate colors
        # that are comfortable for human eyes. E.g. #3c6464 or rgb(60,100,
        # 100). This is usually used for syntax(token) colors.
        step = diff // COLOR_RANGE_DENOMINATOR
        for index in range(
            1, COLOR_RANGE_DENOMINATOR, int(COLOR_RANGE_DENOMINATOR / 3.0)
        ):
            random_int = random.randint(
                min_color + (index * step), min_color + ((index + 2) * step)
            )
            _random_color = padding(hex(random_int))
            random_hex_color_code.append(_random_color)

    random_hex_color_code = sorted(random_hex_color_code)

    # By new solution, in default, the values of R,G,B is increased.
    # To generate the target color, need to swap the values of R,G,B
    if color_name is None or color_name == ColorName.RANDOM:
        color_name = random.choice(list(ColorName))
    # assume the color rgb is #223344
    random_int = random.randint(0, 255)
    if color_name == ColorName.RED:  # 442222 or 443333
        random_hex_color_code = swap_list(random_hex_color_code, 0, 2)
        if random_int % 2 == 0:
            random_hex_color_code[1] = random_hex_color_code[2]
        else:
            random_hex_color_code[2] = random_hex_color_code[1]
    elif color_name == ColorName.GREEN:  # 224422 or 334433
        random_hex_color_code = swap_list(random_hex_color_code, 1, 2)
        if random_int % 2 == 0:
            random_hex_color_code[2] = random_hex_color_code[0]
        else:
            random_hex_color_code[0] = random_hex_color_code[2]
    elif color_name == ColorName.YELLOW:  # 444422 or 444433
        random_hex_color_code = swap_list(random_hex_color_code, 0, 2)
        if random_int % 2 == 0:
            random_hex_color_code[1] = random_hex_color_code[0]
        else:
            random_hex_color_code[0] = random_hex_color_code[1]
    elif color_name == ColorName.CYAN:  # 224444 or 334444
        if random_int % 2 == 0:
            random_hex_color_code[1] = random_hex_color_code[2]
        else:
            random_hex_color_code = swap_list(random_hex_color_code, 0, 1)
            random_hex_color_code[1] = random_hex_color_code[2]
    elif color_name == ColorName.BLUE:  # 222244
        random_hex_color_code[1] = random_hex_color_code[0]
    elif color_name == ColorName.VIOLET:  # 442244 or 443344
        random_hex_color_code[0] = random_hex_color_code[2]
    elif color_name == ColorName.BLACK:  # 222222
        random_hex_color_code[1] = random_hex_color_code[0]
        random_hex_color_code[2] = random_hex_color_code[0]

    random_hex_color = hex_color_code_header + "".join(random_hex_color_code)
    if color_name == ColorName.VIOLET:
        # to have one grayish violet(magenta) color which is more proper
        # for the background color and human eyes
        random_rgb_color = hex2rgb(random_hex_color)
        random_rgb_color = (
            random_rgb_color[0],
            round(random_rgb_color[0] * 0.98),
            random_rgb_color[2],
        )
        random_hex_color = rgb2hex(random_rgb_color)
    random_hex_color = set_hls_values(random_hex_color, hue, saturation, lightness)
    return random_hex_color


def swap_list(_list, _from_index, _to_index):
    """Swap items in _from_index and _to_index in the list."""
    _tmp = _list[_from_index]
    _list[_from_index] = _list[_to_index]
    _list[_to_index] = _tmp
    return _list


def generate_base_colors(hex_color_code, total):
    """Generate base colors by the given hex color code and total number."""
    base_colors = get_scheme_colors(hex_color_code, total)[0:total]
    return base_colors


class Palette:
    """Generate palette colors."""

    def __init__(
        self,
        colors_total=7,
        colors_gradations=60,
        colors_min=120,
        colors_max=180,
        colors_saturation=0.35,
        colors_lightness=0.35,
        dark_colors_gradations_total=60,
        dark_colors_min=15,
        dark_colors_max=20,
        dark_colors_total=7,
        dark_colors_saturation=0.2,
        dark_colors_lightness=0.05,
        **kwargs,
    ):
        """
        Generate random palette.
        Parameters:
            base_colors_total - how many base colors to generate. default: 5.
            colors_gradations - how many lighter colors to generate. default: 6.
            general_max_color - maximum color code. default: 200.
            dark_max_color - maximum color code. default: 30.
            dark_colors_total - how many dark colors to generate. default: 5.
            dark_base_color - base color for dark theme and it's used to generate triadic colors for dark theme. with it, user can generate predictable colors for dark theme.
            Note: (1) the value of dark_base_color is a list.
            (2) the value of dark_base_color will not be used as color of
             pelette, only their lighter colors will be used.
            (3) if this parameter is given, then dark_colors_total will be ignored.
        """
        # random colors are used for sections, components, and pieces
        self.colors_total = colors_total
        self.colors_gradations = colors_gradations
        assert self.colors_total > 0, "colors_total must be greater than 0."
        assert self.colors_gradations > 0, "colors_gradations must be greater than 0."
        self.colors_min = colors_min
        self.colors_max = colors_max
        assert (
            self.colors_min <= self.colors_max
        ), "colors_min must be less than colors_max."
        self.colors_hue = kwargs.get("colors_hue", random.randint(0, 360) / 360)
        self.colors_saturation = colors_saturation
        self.colors_lightness = colors_lightness
        assert (
            self.colors_hue >= 0 and self.colors_hue <= 1
        ), "colors_hue must be greater than 0 and less than 1."
        assert (
            self.colors_saturation >= 0 and self.colors_saturation <= 1
        ), "colors_saturation must be greater than 0 and less than 1."
        assert (
            self.colors_lightness >= 0 and self.colors_lightness <= 1
        ), "colors_lightness must be greater than 0 and less than 1."

        self.dark_colors_total = dark_colors_total
        self.dark_colors_colors_gradations = dark_colors_gradations_total
        assert self.dark_colors_total > 0, "dark_colors_total must be greater than 0."
        assert (
            self.dark_colors_colors_gradations > 0
        ), "dark_colors_colors_gradations must be greater than 0."
        self.dark_colors_min = dark_colors_min
        self.dark_colors_max = dark_colors_max
        assert (
            self.dark_colors_min <= self.dark_colors_max
        ), "dark_colors_min must be less than dark_colors_max."
        self.dark_colors_hue = kwargs.get(
            "dark_colors_hue", random.randint(0, 360) / 360
        )
        self.dark_colors_saturation = dark_colors_saturation
        self.dark_colors_lightness = dark_colors_lightness
        if self.dark_colors_hue is not None:
            assert (
                self.dark_colors_hue >= 0 and self.dark_colors_hue <= 1
            ), "dark_colors_hue must be greater than 0 and less than 1."
        if self.dark_colors_saturation is not None:
            assert (
                self.dark_colors_saturation >= 0 and self.dark_colors_saturation <= 1
            ), "dark_colors_saturation must be greater than 0 and less than 1."
        if self.dark_colors_lightness is not None:
            assert (
                self.dark_colors_lightness >= 0 and self.dark_colors_lightness <= 1
            ), "dark_colors_lightness must be greater than 0 and less than 1."
        self.dark_base_color_name = kwargs.get("dark_base_color_name")
        if not any(member.name == self.dark_base_color_name for member in ColorName):
            self.dark_base_color_name = None
        else:
            self.dark_base_color_name = ColorName[self.dark_base_color_name]
        self.palette_mode = kwargs.get("palette_mode", "DARK")
        if not any(member.name == self.palette_mode for member in PaletteMode):
            self.palette_mode = None
        else:
            self.palette_mode = PaletteMode[self.palette_mode]
        self.dark_base_color = kwargs.get("dark_base_color", None)

    def generate_palette_colors(self):
        """
        Generate random palette.

        6 group base colors: 5 base colors + dark gray color. echo base
        color has 6 different colors from dark to light. placeholders
        are from light to dark, so need to reverse the order.
        """
        colors_list = []
        normal_colors = generate_random_colors(
            min_color=self.colors_min,
            max_color=self.colors_max,
            colors_total=self.colors_total,
            color_gradations=self.colors_gradations,
            hue=self.colors_hue,
            saturation=self.colors_saturation,
            lightness=self.colors_lightness,
        )
        if self.palette_mode == PaletteMode.LIGHT:
            for r_colors in normal_colors:
                r_colors.reverse()
        colors_list.extend(normal_colors)

        dark_colors = generate_random_colors(
            min_color=self.dark_colors_min,
            max_color=self.dark_colors_max,
            colors_total=self.dark_colors_total,
            color_gradations=self.dark_colors_colors_gradations,
            base_color_name=self.dark_base_color_name,
            base_color=self.dark_base_color,
            hue=self.dark_colors_hue,
            saturation=self.dark_colors_saturation,
            lightness=self.dark_colors_lightness,
        )

        if self.palette_mode == PaletteMode.DARK:
            for r_colors in dark_colors:
                r_colors.reverse()
        colors_list.extend(dark_colors)
        return [color for r_colors in colors_list for color in r_colors]

    def generate_palette(self):
        """
        Generate palette content.

        Palette contains a list of colors. Each color is a pair of color
        name and color code.
        The format is "C_[base color sequence]_[colormap sequence]".

        For example, "C_1_1":"#8f67ff".

        Note:
        The 'base color sequence' starts from 1 to base_colors_total (not
        included)
        The 'colormap sequence' starts from 0 to colors_gradations (not
        included)
        When "colormap sequence" is 0, then it represents the lightest color.

        One continuous colormap is for one base color and consists of a
        group of colors from lightest color to the base color.

        Return:
        A list of palette colors.
        """
        palette_color_codes = self.generate_palette_colors()
        color_sequence = 1
        sub_color_sequence = 0
        palette_colors = {}
        colors_gradations = self.colors_gradations
        for index, color in enumerate(palette_color_codes):
            sub_color_sequence = index % (self.colors_gradations)
            # the remaining colors codes belong to dark colors
            if color_sequence > self.colors_total:
                colors_gradations = self.dark_colors_colors_gradations
                sub_color_sequence = (
                    index - (self.colors_total * self.colors_gradations)
                ) % (self.dark_colors_colors_gradations)
            str_base_color_sequence = padding(
                color_sequence, max(len(str(self.colors_total)), 2)
            )
            str_colormap_sequence = padding(
                sub_color_sequence, max(len(str(colors_gradations)), 2)
            )
            color_name = f"C_{str_base_color_sequence}_{str_colormap_sequence}"
            palette_colors[color_name] = color
            if sub_color_sequence == colors_gradations - 1:
                color_sequence += 1
        return palette_colors


def generate_palette():
    """Generate palette colors."""
    return Palette().generate_palette()


def main():
    """Test."""
    opts, _ = getopt.getopt(
        sys.argv[1:],
        "b:B:d:g:G:m:M:",
        [
            "--base_colors_total=",
            "--dark_base_color=",
            "--colors_gradations=",
            "--dark_color_colors_gradations=",
            "--general_max_color=",
            "--dark_max_color=",
        ],
    )
    base_colors_total = 5
    colors_gradations = 6
    dark_color_colors_gradations = 6
    general_max_color = 200
    dark_max_color = 30
    dark_colors_total = 5
    dark_base_color = None
    for option, value in opts:
        if option in ("-b", "--base_colors_total"):
            base_colors_total = int(value)
        if option in ("-B", "--dark_base_color"):
            dark_base_color = value.split(",")
        if option in ("-d", "--dark_colors_total"):
            dark_colors_total = int(value)
        if option in ("-g", "--colors_gradations"):
            colors_gradations = int(value)
        if option in ("-G", "--dark_color_colors_gradations"):
            dark_color_colors_gradations = int(value)
        if option in ("-m", "--general_max_color"):
            general_max_color = int(value)
        if option in ("-M", "--dark_max_color"):
            dark_max_color = int(value)
    palette = Palette(
        colors_total=base_colors_total,
        colors_gradations=colors_gradations,
        dark_colors_gradations_total=dark_color_colors_gradations,
        colors_min=0,
        colors_max=general_max_color,
        dark_colors_min=0,
        dark_colors_max=dark_max_color,
        dark_colors_total=dark_colors_total,
        dark_colors=dark_base_color,
    )
    for color_id, color_hex in palette.generate_palette().items():
        logger.info(bg(color_hex, f"{color_id}({color_hex})"))


if __name__ == "__main__":
    main()
