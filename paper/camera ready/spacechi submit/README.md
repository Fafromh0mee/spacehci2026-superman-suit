# SpaceCHI 2026 paper package

`main.tex` is an LLNCS/Springer proceedings manuscript positioned as a SpaceCHI 2026 design-science position paper. `spacechi_submit.pdf` is the rendered PDF produced with Tectonic.

Camera-ready status:

1. `main.tex` contains the camera-ready author names and separate affiliations.
2. Figure 1 is present as `figures/fig1_suit_design.pdf` (and PNG) before the abstract.
3. Figure 2 is present as `figures/fig2_suit_design_detail.pdf` (and PNG), recreated to use Figure 1's suit architecture and visual language.
4. Recompile with:

   ```sh
   tectonic --keep-logs --synctex --outdir build main.tex
   cp build/main.pdf spacechi_submit.pdf
   ```

The paper uses the official Springer proceedings template supplied for SpaceCHI 2026. The computational probe is explicitly labeled exploratory; it does not claim physiological efficacy, clinical safety, or flight qualification.

Guide images generated for tracing or replacement are provided as both PNG and PDF:

- `figures/fig1_suit_design_guide.png` / `.pdf` — overall suit architecture, exact slot ratio `5490:2123` (about `2.586:1`).
- `figures/fig2_suit_design_detail_guide.png` / `.pdf` — layered detail and interaction states, exact slot ratio `549:193` (about `2.845:1`).

These are design guides, not validated engineering drawings. Verify labels, geometry, electrode placement, materials, and safety controls with the engineering and clinical teams before treating them as a final figure.
