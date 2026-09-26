# Photo Album Generator

A utility script for generating HTML code blocks for photo album galleries.
Last updated September 26, 2026.

## Overview

`photo-album-generator.py` scans the subdirectories of the folder it is placed in and generates a photo gallery template file (`gallery_code.ejs`) inside each one.  The generated code consists of ready-to-paste HTML blocks using Bootstrap grid classes and glightbox markup that can be inserted into an EJS file for a photo album website.

The script was written to work with this template: [PhotoFolio - Bootstrap Photography Website Template](https://bootstrapmade.com/photofolio-bootstrap-photography-website-template/).

## Requirements

- Python 3.x
- No third-party packages are required — the script uses only the Python
  standard library (`os`).

## How It Works

1. Run the script from the parent directory that contains your photo album subdirectories.
2. The script iterates through each subdirectory of the current working directory.
3. Within each subdirectory, it lists all regular (non-hidden) files.
4. Files are sorted alphabetically, and an HTML gallery item block is built for each one, referencing the file at `<base_path>/<subdirectory>/<filename>`.
5. All blocks are written out to a `gallery_code.ejs` file **inside that subdirectory**, which you can then copy and paste into your site's template.

## Usage

1. Place `photo-album-generator.py` in the parent directory containing your photo subdirectories:
   ```bash
   parent-dir/ 
    ├── photos-master.py
    ├── album-one/ 
    │ ├── photo1.jpg 
    │ └── photo2.jpg 
    └── album-two/ 
       ├── photo-a.jpg 
       └── photo-b.jpg


2. Open the script and adjust the `base_path` variable in the `__main__` section if your images are not served from `img`.

3. Run the script:

   ```bash
   python3 photo-album-generator.py

4. Each subdirectory will now contain a gallery_code.ejs file. Open it, copy its contents, and paste them into the appropriate place in your EJS template for that album page.

## Important Notes and Limitations
⚠️ Non-recursive: The script does not recurse into nested directories. Only the immediate subdirectories of the working directory are processed, and only files directly inside each one are included.

⚠️ All files become gallery items: The script assumes that the only files in each subdirectory are image files you want in the album. The only files skipped are hidden files (beginning with a dot), the script itself, and previously generated gallery_code.ejs files. Please delete any files from these directories that you do not want published in the photo album before running the script — anything left behind will be linked in the generated gallery.
The script must be run from the parent directory (it uses the current working directory to find subdirectories).
Overwrite warning: any existing gallery_code.ejs file in a subdirectory will be overwritten each time the script runs.

## Output Format
Each photo produces a block like the following:

```<!-- Begin Gallery Item -->
<div class="col-xl-3 col-lg-4 col-md-6">
    <div class="gallery-item h-100">
        <a href="img/<album>/<photo>.jpg" title="" class="glightbox preview-link">
            <img src="img/<album>/<photo>.jpg" class="img-fluid" alt="">
            <div class="gallery-links d-flex align-items-center justify-content-center"></div>
        </a>
    </div>
</div><!-- End Gallery Item -->
```

The markup uses Bootstrap responsive column classes (col-xl-3 col-lg-4 col-md-6) for the grid layout and glightbox for the lightbox previews. Photos appear in alphabetical order by filename.

## Customization
Customizations a user may want to make include:
1. Base image path: edit base_path at the top of the __main__ block (default: 'img').
2. Output filename: edit output_file inside the html_code() function (default: 'gallery_code.ejs').
3. Grid layout / link classes: edit the gallery_item template string inside html_code().
