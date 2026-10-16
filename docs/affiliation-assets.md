# Affiliation logo sources and credits

Retrieved and visually checked on 2026-10-16. These marks identify the authors’ affiliations; they do not indicate institutional endorsement. All institution names and marks remain the property of their respective owners. The website-template license does not relicense institutional marks.

## 1. Zhejiang University

- Web asset: `static/images/affiliations/zhejiang-university.png`
- Reference: [Zhejiang University](https://www.zju.edu.cn/514/listm.htm)
- Download/source: https://www.zju.edu.cn/_upload/article/images/c3/98/1fb1d281492eb477a098ef7a2901/05966b26-ab45-470d-94c1-99b1e02d12f4.png
- Handling and credit: Official seal (PNG); the adjacent university name is live HTML, not a newly drawn wordmark.
- Asset SHA-256: `dc914cc634bdcd9b871c84686817c12287c6bafd309f083a1054040aee806fca`

## 2. SAP

- Web asset: `static/images/affiliations/sap.svg`
- Reference: [SAP](https://www.sap.com/design-system/digital/foundations/identity/logo/)
- Download/source: https://commons.wikimedia.org/wiki/File:SAP_2011_logo.svg
- Handling and credit: SVG supplied by Wikimedia Commons, credited there to SAP SE and sourced from the official SAP Digital Design System. The gradient anvil mark was checked against the official primary-logo example.
- Asset SHA-256: `50173e125aaa607467d0888d2ca9763742e27a86a07f6697eaab2db6bac35f34`

## 3. Central South University

- Web asset: `static/images/affiliations/central-south-university.png`
- Reference: [Central South University](https://www.csu.edu.cn/zjzn/xxbs/xh.htm)
- Download/source: https://www.csu.edu.cn/__local/5/85/66/A8DA6D0E8DD76C7FDDB81792C28_F0410DE8_8BDF4.png
- Handling and credit: Official seal (PNG); the adjacent university name is live HTML. Downloaded through the weserv image proxy because the university host closed direct connections. The open PNG was used without attempting the verification-code-protected VIS archive.
- Asset SHA-256: `765ac787fa918486d4d8cd92d8f865291fad8c32b1d636ba16ad402191bb32a4`

## 4. HKUST (Guangzhou)

- Web asset: `static/images/affiliations/hkust-guangzhou.svg`
- Reference: [HKUST (Guangzhou)](https://brand.hkust.edu.hk/)
- Download/source: https://brand.hkust.edu.hk/sites/default/files/bm_folder/HKUST_Brand_guideline.pdf
- Handling and credit: Unmodified English combination mark extracted from PDF page 69 of the official HKUST Brand Guidelines (revision 20261006). A cropped vector PDF is retained as hkust-guangzhou.pdf; the website uses its vector SVG rendering.
- Asset SHA-256: `dc520c88650f8c013e845a9fde387c06c4f889126a43c687efbd4e4b9f897edb`

## 5. Chalmers University of Technology

- Web asset: `static/images/affiliations/chalmers.svg`
- Reference: [Chalmers University of Technology](https://www.chalmers.se/en/)
- Download/source: https://www.chalmers.se/en/
- Handling and credit: Official inline SVG from the university homepage, with its inherited currentColor resolved to the homepage text-purple-700 value rgb(71 45 190). Paths and proportions are unchanged.
- Asset SHA-256: `869b77c818e4536edd7e1d4f99b79122090bb811d3e97dd08e2150e8fadef4d1`

## 6. Microsoft Research

- Web asset: `static/images/affiliations/microsoft-research.png`
- Reference: [Microsoft Research](https://commons.wikimedia.org/wiki/File:Segoe_msr_logo.png)
- Download/source: https://upload.wikimedia.org/wikipedia/commons/7/7b/Segoe_msr_logo.png
- Handling and credit: Established research wordmark from Wikimedia Commons (PNG), not an official Microsoft download. Credit: V-gthom; current blue edition uploaded by LsnIg334. Licensed CC BY-SA 3.0, https://creativecommons.org/licenses/by-sa/3.0/ . Image unchanged.
- Asset SHA-256: `1b1b38d84d9a732b344090fda28bb5ea67f0f590501dcd1134834ea33419c6e7`

## PDF extraction

The HKUST(GZ) mark comes from the unaltered logo shown on the “4.3.2 Combination Logo” page (printed page 66, PDF page 69). Extraction selected the page rectangle `(274, 215, 578, 292)` in PDF points, translated it to the origin, removed link annotations and set the page bounds to 304 × 77 points. Poppler `pdftocairo -svg` generated the browser asset; lettering remains vector outlines rather than substituted fonts.

- Original guidelines PDF SHA-256: `a918c53732001d99d6ed2016444dd7b9939717326823e4e212b7b832b1b4816f`
- Cropped PDF SHA-256: `a1c89b12a314424c4f9d138c321ec15ae2fd04800f3b8e556824bec1561919ce`

The original Zhejiang University identity archives were also inspected. Their AI files show a PDF-compatibility placeholder in ordinary PDF readers, so those files were not presented as usable PDF logos. No raster logo has been described as a vector or converted to PDF to imply higher resolution.

## Compact header presentation (2026-10-16)

All six affiliations now share one row. The original source files above and their hashes are unchanged; CSS viewports remove unused canvas space without raster resampling or redrawing marks. Full institution names remain in link titles and accessible labels. ZJU, CSU and HKUST(GZ) are live-text affiliation abbreviations, not newly designed official wordmarks.

- Zhejiang: display the seal within source bounds `(66, 43, 243, 220)` instead of the full 318 × 253 white canvas.
- CSU and SAP: retain the existing artwork and reduce its display size.
- HKUST(GZ): show the original emblem within `(9, 8, 45, 67)` of the 304 × 77 vector canvas beside the campus abbreviation. The complete official combination logo and PDF remain retained as source assets.
- Chalmers: show the primary CHALMERS lettering (top 21.4 of 37 source units); the long university subtitle is outside the display viewport.
- Microsoft Research: remove outer padding using source bounds `(13, 6, 1271, 358)`. Existing CC BY-SA 3.0 credit remains applicable to this cropped presentation.
- Narrow screens retain all six institutions in one row, with compact labels underneath the marks.
