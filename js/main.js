// Load the links.json file and populate the grid
async function loadMelachot() {
    try {
        const response = await fetch('links.json');
        const data = await response.json();

        const grid = document.getElementById('melachot-grid');

        // Iterate through each melacha in the JSON
        for (const [key, melacha] of Object.entries(data)) {
            // Create a link element for each melacha
            const block = document.createElement('a');
            block.className = 'melacha-block';
            block.href = melacha.url;
            block.target = '_blank';

            // Apply background color or image
            if (melacha.image) {
                block.style.backgroundImage = `url(${melacha.image})`;
            } else if (melacha.colors) {
                block.style.backgroundColor = melacha.colors.background;
                block.style.color = melacha.colors.text;
            }

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

            // Append block to grid
            grid.appendChild(block);
        }
    } catch (error) {
        console.error('Error loading melachot:', error);
    }
}

// Load melachot when the page loads
document.addEventListener('DOMContentLoaded', loadMelachot);
