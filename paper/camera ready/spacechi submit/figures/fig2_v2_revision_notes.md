# Figure 2 v2 revision provenance

## Built-in image-generation prompt

The raster base was edited with the built-in image-generation tool using this production specification:

> Rebuild Figure 2 as a physically plausible layered wearable system matching Figure 1. Show a removable outer photovoltaic shell on the left half and a soft inner compression garment on the right-half cutaway. Do not place exposed circuit boards or live copper traces against skin. Route insulated flexible conductors through seam channels to protected waist electronics. Place charge regulation, electrical isolation, and the stimulator/controller in one sealed removable waist module; place solid-state storage in a separate sealed removable waist module. Show small contact, impedance, temperature, and motion sensor nodes on the inner garment, plus soft red-outlined NMES electrode pads over quadriceps and calf regions. Put one large red physical emergency-stop button on the left wrist/forearm. Use realistic textile seams, flexible PV laminates, strain relief, and detachable modules; avoid fantasy armor.
>
> Preserve the academic infographic panels and wording. The logical energy path is illumination -> photovoltaic shell -> charge regulation -> storage -> controller/stimulator -> NMES electrodes. Sensing and user command point into the controller; stimulation output points from the controller to the electrodes. The physical-stop panel remains independent of the display. No watermark.

The resulting realistic base then received an erasure-only image-generation pass:

> Remove every ambiguous leader between the exploded components, suit, and descriptive paragraphs, plus the ambiguous external red path and bottom controller-area arrows. Preserve the suit, modules, sensor nodes, electrodes, wrist stop, panels, icons, titles, labels, and main green energy chain. Leave clean white space for deterministic vector leaders. Do not add replacement arrows or alter the garment.

## Deterministic vector overlay

The final leaders and arrows are defined in `fig2_suit_design_detail.svg`. Their endpoints are fixed as follows:

1. photovoltaic shell -> blue chest PV panel;
2. controller -> protected left waist module;
3. storage -> separate right waist battery module;
4. sensing -> inner-garment sensor node;
5. NMES -> red-outlined thigh electrode;
6. emergency stop -> red wrist button.

Bottom arrows are similarly constrained: sensing and user command enter the controller, while stimulation leaves the controller and terminates at the NMES electrodes.
