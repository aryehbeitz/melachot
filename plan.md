# 39 Melachot GitHub Pages Site

Create a GitHub Pages site with a periodic-table-style grid for the 39 melachot, driven by a JSON configuration whose keys are the full melacha names.

## JSON Configuration

The `links.json` file will drive block content, colors, optional images, and target URLs. Initial content based on the provided design, with a sample image entry:

```json
{
  "Choresh": {
    "displayName": "Ch",
    "subtext": "Choresh",
    "colors": { "background": "#00D5FF", "text": "#000000" },
    "url": "https://www.chabad.org/library/article_cdo/aid/4739406/jewish/Choresh-Plowing.htm",
    "image": "images/choresh.png"
  },
  "Zoreah": {
    "displayName": "Zo",
    "subtext": "Zoreah",
    "colors": { "background": "#00D5FF", "text": "#000000" },
    "url": "https://www.example.com/zoreah"
  },
  "Kotzair": {
    "displayName": "Ko",
    "subtext": "Kotzair",
    "colors": { "background": "#00D5FF", "text": "#000000" },
    "url": "https://www.example.com/kotzair"
  },
  "Ma'amir": {
    "displayName": "Mm",
    "subtext": "Ma'amir",
    "colors": { "background": "#00D5FF", "text": "#000000" },
    "url": "https://www.example.com/maamir"
  },
  "Dush": {
    "displayName": "Du",
    "subtext": "Dush",
    "colors": { "background": "#00D5FF", "text": "#000000" },
    "url": "https://www.example.com/dush"
  },
  "Zoreh": {
    "displayName": "Zr",
    "subtext": "Zoreh",
    "colors": { "background": "#00D5FF", "text": "#000000" },
    "url": "https://www.example.com/zoreh"
  },
  "Ma'avir": {
    "displayName": "Mv",
    "subtext": "Ma'avir",
    "colors": { "background": "#FFC107", "text": "#000000" },
    "url": "https://www.example.com/maavir"
  },
  "Mechabeh": {
    "displayName": "Mc",
    "subtext": "Mechabeh",
    "colors": { "background": "#FFC107", "text": "#000000" },
    "url": "https://www.example.com/mechabeh"
  },
  "Borer": {
    "displayName": "Bo",
    "subtext": "Borer",
    "colors": { "background": "#D8A8FF", "text": "#000000" },
    "url": "https://www.example.com/borer"
  },
  "Tochain": {
    "displayName": "To",
    "subtext": "Tochain",
    "colors": { "background": "#D8A8FF", "text": "#000000" },
    "url": "https://www.example.com/tochain"
  },
  "Miraked": {
    "displayName": "Mi",
    "subtext": "Miraked",
    "colors": { "background": "#D8A8FF", "text": "#000000" },
    "url": "https://www.example.com/miraked"
  },
  "Lush": {
    "displayName": "Lu",
    "subtext": "Lush",
    "colors": { "background": "#D8A8FF", "text": "#000000" },
    "url": "https://www.example.com/lush"
  },
  "Ofeh": {
    "displayName": "Of",
    "subtext": "Ofeh",
    "colors": { "background": "#D8A8FF", "text": "#000000" },
    "url": "https://www.example.com/ofeh"
  },
  "Kotaiv": {
    "displayName": "Kt",
    "subtext": "Kotaiv",
    "colors": { "background": "#FFC107", "text": "#000000" },
    "url": "https://www.example.com/kotaiv"
  },
  "Mechait": {
    "displayName": "Mk",
    "subtext": "Mechait",
    "colors": { "background": "#FFC107", "text": "#000000" },
    "url": "https://www.example.com/mechait"
  },
  "Goez": {
    "displayName": "Go",
    "subtext": "Goez",
    "colors": { "background": "#A566FF", "text": "#000000" },
    "url": "https://www.example.com/goez"
  },
  "Melabain": {
    "displayName": "Me",
    "subtext": "Melabain",
    "colors": { "background": "#A566FF", "text": "#000000" },
    "url": "https://www.example.com/melabain"
  },
  "Menafetz": {
    "displayName": "Mn",
    "subtext": "Menafetz",
    "colors": { "background": "#A566FF", "text": "#000000" },
    "url": "https://www.example.com/menafetz"
  },
  "Tzovayah": {
    "displayName": "Tz",
    "subtext": "Tzovayah",
    "colors": { "background": "#A566FF", "text": "#000000" },
    "url": "https://www.example.com/tzovayah"
  },
  "Toveh": {
    "displayName": "Tv",
    "subtext": "Toveh",
    "colors": { "background": "#A566FF", "text": "#000000" },
    "url": "https://www.example.com/toveh"
  },
  "Maisach": {
    "displayName": "Ma",
    "subtext": "Maisach",
    "colors": { "background": "#A566FF", "text": "#000000" },
    "url": "https://www.example.com/maisach"
  },
  "Oseh Bei Batel Neirin": {
    "displayName": "Ob",
    "subtext": "Oseh Bei Batel Neirin",
    "colors": { "background": "#A566FF", "text": "#000000" },
    "url": "https://www.example.com/oseh-bei-batel-neirin"
  },
  "Boneh": {
    "displayName": "Bn",
    "subtext": "Boneh",
    "colors": { "background": "#FFC107", "text": "#000000" },
    "url": "https://www.example.com/boneh"
  },
  "Oraig": {
    "displayName": "Or",
    "subtext": "Oraig",
    "colors": { "background": "#C345C6", "text": "#000000" },
    "url": "https://www.example.com/oraig"
  },
  "Potzi'ah": {
    "displayName": "Po",
    "subtext": "Potzi'ah",
    "colors": { "background": "#C345C6", "text": "#000000" },
    "url": "https://www.example.com/potziah"
  },
  "Koshair": {
    "displayName": "Ko",
    "subtext": "Koshair",
    "colors": { "background": "#C345C6", "text": "#000000" },
    "url": "https://www.example.com/koshair"
  },
  "Matir": {
    "displayName": "Mr",
    "subtext": "Matir",
    "colors": { "background": "#C345C6", "text": "#000000" },
    "url": "https://www.example.com/matir"
  },
  "Memacheik": {
    "displayName": "Mt",
    "subtext": "Memacheik",
    "colors": { "background": "#C345C6", "text": "#000000" },
    "url": "https://www.example.com/memacheik"
  },
  "Tofair": {
    "displayName": "Tf",
    "subtext": "Tofair",
    "colors": { "background": "#C345C6", "text": "#000000" },
    "url": "https://www.example.com/tofair"
  },
  "Ko'reah": {
    "displayName": "Kr",
    "subtext": "Ko'reah",
    "colors": { "background": "#C345C6", "text": "#000000" },
    "url": "https://www.example.com/koreah"
  },
  "Soiser": {
    "displayName": "So",
    "subtext": "Soiser",
    "colors": { "background": "#FFC107", "text": "#000000" },
    "url": "https://www.example.com/soiser"
  },
  "Tzud": {
    "displayName": "Td",
    "subtext": "Tzud",
    "colors": { "background": "#B7FF3C", "text": "#000000" },
    "url": "https://www.example.com/tzud"
  },
  "Shochet": {
    "displayName": "Sc",
    "subtext": "Shochet",
    "colors": { "background": "#B7FF3C", "text": "#000000" },
    "url": "https://www.example.com/shochet"
  },
  "Mafshit": {
    "displayName": "Mf",
    "subtext": "Mafshit",
    "colors": { "background": "#B7FF3C", "text": "#000000" },
    "url": "https://www.example.com/mafshit"
  },
  "Ma'aboid": {
    "displayName": "Mb",
    "subtext": "Ma'aboid",
    "colors": { "background": "#B7FF3C", "text": "#000000" },
    "url": "https://www.example.com/maaboid"
  },
  "Mechateich": {
    "displayName": "Mi",
    "subtext": "Mechateich",
    "colors": { "background": "#B7FF3C", "text": "#000000" },
    "url": "https://www.example.com/mechateich"
  },
  "Meshartois": {
    "displayName": "Mh",
    "subtext": "Meshartois",
    "colors": { "background": "#B7FF3C", "text": "#000000" },
    "url": "https://www.example.com/meshartois"
  },
  "Hatza'ah": {
    "displayName": "Ha",
    "subtext": "Hatza'ah",
    "colors": { "background": "#B7FF3C", "text": "#000000" },
    "url": "https://www.example.com/hatzah"
  },
  "Makeh b'Potash": {
    "displayName": "MP",
    "subtext": "Makeh b'Potash",
    "colors": { "background": "#B7FF3C", "text": "#000000" },
    "url": "https://www.example.com/makeh-b-potash"
  }
}
```

Any `image` key is optional; when present, the view will use the supplied file instead of generated colors. URLs can be updated later to the authoritative sources.

## Implementation Overview

- Build single-page `index.html` rendering blocks in a CSS grid that mirrors the reference layout.
- Use JavaScript to load `links.json` and create elements dynamically, applying colors or image URLs as configured.
- Provide responsive styling in `css/style.css` so the grid adapts to smaller screens while preserving the visual grouping.
- Maintain `links.json` as the single source of truth for block content, colors, and outbound URLs.
- Include `_config.yml` for GitHub Pages setup and `README.md` with editing instructions.

## Todos

- [x] Create index.html with grid container and placeholder cells for 39 melachot blocks.
- [x] Create CSS file with grid layout, color scheme matching design, and responsive styles.
- [x] Create links.json with all 39 melachot abbreviations mapped to placeholder URLs.
- [x] Create JavaScript to load links.json and apply click handlers to each melacha block.
- [x] Populate HTML with all 39 melachot (abbreviations and Hebrew names) from the design.
- [x] Add _config.yml and ensure proper structure for GitHub Pages deployment.
- [x] Create README.md with project description and setup instructions.

