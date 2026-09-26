#!/usr/bin/env python3

"""
Last updated on September 26, 2026
@author: Lawyneer

"""

## Import needed modules
import os

## Define functions
def html_code(base_path, directory_name):

    # define varables
    output_file = 'gallery_code.ejs' # name for output file
    photos = [] # empty list for file names of photos in a directory
    html_content = []   # empty list for html content needed for photo gallery        
        
    # generate a list of photos in the directory
    for photo in os.listdir():

        # skip hidden files and this script        
        if photo == "photos-master.py" or photo == "gallery_code.ejs" or photo.startswith('.'):
            continue

        # skip directories
        if os.path.isfile(photo):
            photos.append(photo)

    # sort the list so the photos appear in alphabetical order based on the file names
    photos = sorted(photos)

    # populate the html content
    for photo in photos:
        # Create the gallery item HTML block
        gallery_item = f"""
                    <!-- Begin Gallery Item -->
                    <div class="col-xl-3 col-lg-4 col-md-6">
                        <div class="gallery-item h-100">
                            <a href="{base_path}/{directory_name}/{photo}" title="" class="glightbox preview-link">
                                <img src="{base_path}/{directory_name}/{photo}" class="img-fluid" alt="">
                                <div class="gallery-links d-flex align-items-center justify-content-center"></div>
                            </a>
                        </div>
                    </div><!-- End Gallery Item -->
            """
        
        # add the new gallery block item to the list of gallery blocks
        html_content.append(gallery_item)
    # end for
        
    # write to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(''.join(html_content))

    return
## End html_code function

if __name__ == "__main__":

    ## Define varables
    base_path = 'img'   # the base image where images are stored on server
    
    # Generate list of subdirectories
    subdirectories = [item for item in os.listdir('.') if os.path.isdir(item)]

    for dir in subdirectories:
        
        # set path for next directory
        new_dir = "./" + dir

        # Change the directory
        os.chdir(new_dir)
        directory_name = os.path.basename(os.getcwd())
        
        # generate the html code
        html_code(base_path, directory_name)

        # move up to the main directory for the next iteration
        os.chdir("..")
    # end for
    
## end main