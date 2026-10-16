# Affiliation logo sources and credits

Retrieved and visually checked on 2026-10-16. Marks identify author affiliations and retain their respective ownership; the website-template license does not relicense them.

The header uses a compact three-column, two-row layout with complete identity artwork. Institution names are contained in the image files themselves. No HTML abbreviations, replacement fonts, cropped subtitles or newly assembled wordmarks are used. Full names also appear in accessible link labels and hover titles.

## 1. Zhejiang University

- Web asset: `static/images/affiliations/zhejiang-university-complete.jpg`
- Reference: [Zhejiang University](https://bis.zju.edu.cn/cakordb/tools/)
- Download/source: https://bis.zju.edu.cn/cakordb/static/images/home/ZJU.jpg
- Handling and credit: Complete seal, Chinese calligraphic name and English wordmark from a Zhejiang University-hosted research website. Retrieved through the weserv image proxy after a direct-host timeout. Lettering, proportions and colours are displayed as supplied.
- Asset SHA-256: `783e62726b959af3fb5ecf22c3ea71236c62437bc22a28304b195d352d9f12ff`

## 2. SAP

- Web asset: `static/images/affiliations/sap.svg`
- Reference: [SAP](https://www.sap.com/design-system/digital/foundations/identity/logo/)
- Download/source: https://commons.wikimedia.org/wiki/File:SAP_2011_logo.svg
- Handling and credit: Original SVG credited to SAP SE and sourced from the SAP Digital Design System. The SAP lettering is part of the artwork.
- Asset SHA-256: `50173e125aaa607467d0888d2ca9763742e27a86a07f6697eaab2db6bac35f34`

## 3. Central South University

- Web asset: `static/images/affiliations/central-south-university-complete.png`
- Reference: [Central South University](https://tactip.org/)
- Download/source: https://tactip.org/Partner/%E4%B8%AD%E5%8D%97%E5%A4%A7%E5%AD%A6.png
- Handling and credit: Complete university identity artwork published in the TacTip partner list, retrieved through the weserv image proxy. This is a partner-hosted copy, not a direct university download. The seal was cross-checked against https://www.csu.edu.cn/info/1417/8070.htm and the combination against a second published copy at https://www.iecube.com.cn/tmp/uploads/20221013/a38096e783767e9399d19e2ec712b510.jpg . No lettering was recreated, removed or substituted.
- Asset SHA-256: `370da224268018ceea0ad21fa14d5f0d25a0bc61acc8d4da040a0ecdd3fb8329`

## 4. HKUST (Guangzhou)

- Web asset: `static/images/affiliations/hkust-guangzhou.svg`
- Reference: [HKUST (Guangzhou)](https://brand.hkust.edu.hk/)
- Download/source: https://brand.hkust.edu.hk/sites/default/files/bm_folder/HKUST_Brand_guideline.pdf
- Handling and credit: Unmodified English combination mark extracted from PDF page 69 of the official brand guidelines (revision 20261006). The complete emblem and wordmark are displayed; hkust-guangzhou.pdf remains the vector source.
- Asset SHA-256: `dc520c88650f8c013e845a9fde387c06c4f889126a43c687efbd4e4b9f897edb`

## 5. Chalmers University of Technology

- Web asset: `static/images/affiliations/chalmers.svg`
- Reference: [Chalmers University of Technology](https://www.chalmers.se/en/)
- Download/source: https://www.chalmers.se/en/
- Handling and credit: Official complete university wordmark from the homepage inline SVG. Its inherited currentColor was resolved to the homepage text-purple-700 value rgb(71 45 190). All paths and both lines of lettering are retained. The institution introduced this new visual identity in 2026: https://www.chalmers.se/aktuellt/nyheter/ett-chalmers-ny-gemensam-identitet-for-hela-koncernen/ . No extra emblem or text is invented.
- Asset SHA-256: `869b77c818e4536edd7e1d4f99b79122090bb811d3e97dd08e2150e8fadef4d1`

## 6. Microsoft Research

- Web asset: `static/images/affiliations/microsoft-research.png`
- Reference: [Microsoft Research](https://commons.wikimedia.org/wiki/File:Segoe_msr_logo.png)
- Download/source: https://upload.wikimedia.org/wikipedia/commons/7/7b/Segoe_msr_logo.png
- Handling and credit: Established research wordmark from Wikimedia Commons, not an official Microsoft download. Credit: V-gthom; blue edition by LsnIg334. CC BY-SA 3.0, https://creativecommons.org/licenses/by-sa/3.0/ . The complete original artwork is displayed unchanged.
- Asset SHA-256: `1b1b38d84d9a732b344090fda28bb5ea67f0f590501dcd1134834ea33419c6e7`

## PDF extraction

The HKUST(GZ) mark comes from the unaltered logo shown on the “4.3.2 Combination Logo” page (printed page 66, PDF page 69). Extraction selected the page rectangle `(274, 215, 578, 292)` in PDF points, translated it to the origin, removed link annotations and set the page bounds to 304 × 77 points. Poppler `pdftocairo -svg` generated the browser asset; lettering remains vector outlines rather than substituted fonts.

- Original guidelines PDF SHA-256: `a918c53732001d99d6ed2016444dd7b9939717326823e4e212b7b832b1b4816f`
- Cropped PDF SHA-256: `a1c89b12a314424c4f9d138c321ec15ae2fd04800f3b8e556824bec1561919ce`

The original Zhejiang University identity archives were also inspected. Their AI files show a PDF-compatibility placeholder in ordinary PDF readers, so those files were not presented as usable PDF logos. No raster logo has been described as a vector or converted to PDF to imply higher resolution.


The previously downloaded standalone Zhejiang and CSU seals remain source assets; the current header uses the complete combinations above.
