# Setup Instructions

## Prerequisites

1. **Python 3.7+** - Make sure Python is installed
2. **Google Chrome** - The scraper uses Chrome browser
3. **ChromeDriver** - Selenium WebDriver for Chrome

## Installation Steps

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Install ChromeDriver

Choose one of the following methods:

#### Option A: Using webdriver-manager (Automatic)

The `webdriver-manager` package will automatically download and manage ChromeDriver for you. Just run:

```bash
pip install webdriver-manager
```

#### Option B: Manual Installation

1. Check your Chrome version:
   - Open Chrome
   - Go to `chrome://version/`
   - Note the version number

2. Download ChromeDriver:
   - Visit https://chromedriver.chromium.org/downloads
   - Download the version matching your Chrome browser
   - Extract the executable

3. Add to PATH:
   - **macOS/Linux**: Move to `/usr/local/bin/` or add to your PATH
   - **Windows**: Place in a directory on your PATH or specify full path

#### Option C: Using Homebrew (macOS)

```bash
brew install chromedriver
```

### 3. Verify Installation

Test that ChromeDriver is accessible:

```bash
chromedriver --version
```

## Running the Scraper

Once everything is installed, run:

```bash
python puc_scraper.py
```

The scraper will:
1. Open Chrome browser (in headless mode)
2. Navigate to the PUC website
3. Go to page 2
4. Search for the two specific documents
5. Download them to `downloads/puc/` directory

## Troubleshooting

### Issue: "chromedriver executable needs to be in PATH"

**Solution**: Make sure ChromeDriver is installed and accessible. See Option B above.

### Issue: "session not created" or "chrome not reachable"

**Solution**: 
- Make sure Chrome browser is installed
- Try running Chrome normally to ensure it works
- Update Chrome to the latest version

### Issue: Can't find the documents

**Solution**: 
- The scraper will save `debug_page_source.html` if it can't find documents
- Check this file to see what the page actually contains
- The page structure may have changed

### Issue: Headless mode doesn't work

**Solution**: You can disable headless mode by editing `puc_scraper.py` and removing or commenting out this line:

```python
self.chrome_options.add_argument('--headless')  # Comment this out
```

## Notes

- The scraper uses headless mode by default (no visible browser window)
- If you want to see what's happening, disable headless mode
- Be patient - the scraper adds delays to be respectful to the website
- If the page structure changes, you may need to update the selectors

