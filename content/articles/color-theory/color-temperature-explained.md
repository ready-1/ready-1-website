Title: Color Temperature in Cameras and Displays
Date: 10/24/24, 7:41 PM
Category: Concepts
tags: color theory, lighting
og_image:
slug: the-history-and-science-of-color-temperature
Summary: A practical explanation of color temperature, white balance, and display white point for video systems.

## What the Kelvin number describes

Color temperature describes the color of light by comparing it with the light emitted by a heated black body. As that reference gets hotter, its light moves from red through orange and white toward blue. The temperature is measured in kelvins.

This is why a 3200 K source looks warmer and a 5600 K source looks cooler, even though the higher physical temperature is associated with the bluer light.

Common reference points include:

- **2000-3000 K:** candles and tungsten-style sources
- **3200 K:** a common reference for studio tungsten lighting
- **4000-5000 K:** neutral and cool-white fixtures
- **5600 K:** a common daylight reference for cameras and lighting
- **6500 K and above:** overcast sky and other blue daylight conditions

Real fixtures do not always sit perfectly on the black-body curve. Two lights can report the same correlated color temperature and still render color differently because of tint and spectral differences.

## White balance in a camera

A camera uses white balance to decide what should be neutral under the current light. If the setting does not match the source, the image shifts orange or blue. A green or magenta error may remain even when the Kelvin value looks correct.

Matching cameras therefore takes more than entering the same number. Start with a common reference, compare the cameras on a chart or known neutral subject, and use waveform and vectorscope measurements alongside the pictures.

Mixed lighting needs a deliberate choice. A camera can be balanced for one source, but it cannot make tungsten, daylight, and an off-axis LED fixture behave like the same light at once.

## White point in a display

A display white point defines the chromaticity that the display treats as white. D65 is the standard reference used by many video systems. Its correlated color temperature is roughly 6500 K, but D65 is a defined chromaticity rather than a generic 6500 K setting.

Display picture modes, color-temperature controls, and ambient light can all change the apparent result. Camera matching is only one part of the chain; the destinations also need known settings.

## A practical signal-chain check

On a show site, I separate the problem into three parts:

1. **Source:** What light is actually on the subject, and is it consistent?
2. **Camera:** What white balance, tint, matrix, and paint settings are active?
3. **Display:** What picture mode and white point are the final destinations using?

Work from a shared reference and change one stage at a time. Confirm the result at the scopes and at the destination. That process makes it much easier to identify whether a mismatch begins in the lighting, the camera, signal processing, or the display.
