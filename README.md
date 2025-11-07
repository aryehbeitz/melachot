# 40 Melachot

A periodic-table-style interactive grid displaying the 39 melachot (categories of work prohibited on Shabbat). Each block links to educational resources about that melacha.

## Features

- Interactive grid layout inspired by the periodic table
- Color-coded blocks representing different categories
- Responsive design that adapts to mobile devices
- JSON-driven content for easy updates
- Support for custom images per melacha

## Project Structure

```
melachot/
├── index.html          # Main HTML file
├── css/
│   └── style.css      # Styling and grid layout
├── js/
│   └── main.js        # JavaScript to load and render blocks
├── links.json         # Configuration for all melachot
├── _config.yml        # GitHub Pages configuration
└── README.md          # This file
```

## Editing Content

To update the content, colors, or links for any melacha, edit the `links.json` file. Each melacha entry follows this format:

```json
"MelachaName": {
  "displayName": "Abbreviation",
  "subtext": "Full Name",
  "colors": {
    "background": "#HexColor",
    "text": "#HexColor"
  },
  "url": "https://link-to-resource.com",
  "image": "path/to/image.png"  // Optional
}
```

## Deploying to GitHub Pages

Follow these steps to deploy this site to GitHub Pages:

### 1. Create a GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Name it `melachot` (or any name you prefer)
3. Do NOT initialize with README, .gitignore, or license (we already have these files)

### 2. Push Your Code to GitHub

Run these commands in your terminal from the project directory:

```bash
# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: 40 Melachot site"

# Add your GitHub repository as remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/melachot.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 3. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click on **Settings** (top right)
3. Scroll down to **Pages** in the left sidebar
4. Under **Source**, select **main** branch
5. Click **Save**
6. Wait a few minutes for deployment to complete

### 4. Access Your Site

Your site will be available at:
```
https://YOUR_USERNAME.github.io/melachot/
```

Replace `YOUR_USERNAME` with your actual GitHub username.

## Local Development

To test the site locally, you need to run a local web server (due to CORS restrictions on loading JSON files):

### Using Python 3:
```bash
python3 -m http.server 8000
```

### Using Node.js (with npx):
```bash
npx http-server
```

Then open your browser to `http://localhost:8000`

## Future Enhancements

- Add images for each melacha
- Implement search/filter functionality
- Add tooltips with brief descriptions
- Create a mobile app version
- Add Hebrew/English language toggle

## License

This project is open source and available for educational purposes.
