// Load the links.json file and populate the grid
async function loadMelachot() {
    try {
        const response = await fetch('links.json');
        const data = await response.json();

        const grid = document.getElementById('melachot-grid');

        // Define the order of melachot to match the periodic table layout
        const order = [
            // Row 1: 6 cyan blocks, 1 gap, 2 orange blocks
            'Choresh', 'Zoreah', 'Kotzair', 'Ma\'amir', 'Dush', 'Zoreh', null, 'Ma\'avir', 'Mechabeh',
            // Row 2: 5 light purple blocks, 2 gaps, 2 orange blocks
            'Borer', 'Tochain', 'Miraked', 'Lush', 'Ofeh', null, null, 'Kotaiv', 'Mechait',
            // Row 3: 7 darker purple blocks, 1 orange block
            'Goez', 'Melabain', 'Menafetz', 'Tzovayah', 'Toveh', 'Maisach', 'Oseh Bei Batel Neirin', 'Boneh',
            // Row 4: 7 magenta blocks, 1 orange block
            'Oraig', 'Potzi\'ah', 'Koshair', 'Matir', 'Memacheik', 'Tofair', 'Ko\'reah', 'Soiser',
            // Row 5: 8 yellow-green blocks
            'Tzud', 'Shochet', 'Mafshit', 'Ma\'aboid', 'Mechateich', 'Meshartois', 'Hatza\'ah', 'Makeh b\'Potash'
        ];

        // Iterate through the order array
        for (const key of order) {
            if (key === null) {
                // Create an empty grid cell for spacing
                const spacer = document.createElement('div');
                spacer.className = 'grid-spacer';
                grid.appendChild(spacer);
            } else {
                const melacha = data[key];
                if (!melacha) {
                    console.warn(`Melacha not found: ${key}`);
                    continue;
                }

                // Create a link element for each melacha
                const block = document.createElement('a');
                block.className = 'melacha-block';
                block.href = melacha.url;
                block.target = '_blank';

                // Apply background color or image
                if (melacha.image) {
                    // Use the image as the entire block content
                    block.style.backgroundImage = `url(${melacha.image})`;
                    block.style.backgroundSize = 'cover';
                    block.style.backgroundPosition = 'center';
                } else if (melacha.colors) {
                    // Use colors and text for blocks without images
                    block.style.backgroundColor = melacha.colors.background;
                    block.style.color = melacha.colors.text;

                    // Create display name element
                    const displayName = document.createElement('div');
                    displayName.className = 'display-name';
                    displayName.textContent = melacha.displayName;

                    // Create subtext element
                    const subtext = document.createElement('div');
                    subtext.className = 'subtext';
                    subtext.textContent = melacha.subtext;

                    // Append elements to the block
                    block.appendChild(displayName);
                    block.appendChild(subtext);
                }

                // Append block to grid
                grid.appendChild(block);
            }
        }
    } catch (error) {
        console.error('Error loading melachot:', error);
    }
}

// Update the last updated timestamp with Israel time
function updateLastUpdated() {
    const now = new Date();

    // Format date and time in Israel timezone
    const options = {
        timeZone: 'Asia/Jerusalem',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: false
    };

    const israelTime = now.toLocaleString('en-US', options);
    const lastUpdatedElement = document.getElementById('last-updated');

    if (lastUpdatedElement) {
        lastUpdatedElement.textContent = israelTime + ' (Israel Time)';
    }
}

// Load melachot when the page loads
document.addEventListener('DOMContentLoaded', () => {
    loadMelachot();
    updateLastUpdated();
});
