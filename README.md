# Faces of Turkey
**An attempt at estimating average (male) faces of Turkey by province**

I used pictures of male football players scraped from [Transfermarkt](https://transfermarkt.com). Below are the steps I took in preparing the average pictures.

1. On Transfermarkt's [Advanced Search page](https://www.transfermarkt.com/detailsuche/spielerdetail/suche), I searched for Turkish players by selecting _Citizenship_ and _Country of Birth_ as Turkey. I then copied the search URL and gave it to my scraper (located at `tools/scraper/`). Since Transfermarkt only lets you see 250 hits, I manually played with various parameters such as _Market value_, _Age_ and _Place of birth_ to download the data of every Turkish player in chunks. This step probably took the longest.

2. I saved the output as JSON files (not included in this repository), merged them (with `tools/json_merger.py`) and converted the final JSON file to a CSV file on [ConvertCSV](https://www.convertcsv.com/json-to-csv.htm) which helped classify players according to their birthplace.

3. I wrote a script (`download_images.ipynb`) that read the database, created directories for every province, and downloaded the pictures to the directory which they belonged to.

5. I converted the pictures from WebP to JPEG with `find` and `mogrify` commands. This had to be done for [dlib](http://dlib.net/) to process the files. Even though they have various extensions such as .jpg and .png, they are all WebP files in reality.

4. I manually reviewed the pictures and deleted ones
    - [with distorted proportions](https://img.a.transfermarkt.technology/portrait/big/99872-1636309285.jpg)
    - [that are black and white](https://img.a.transfermarkt.technology/portrait/big/327843-1606337991.jpeg)
    - [that are of very low quality](https://img.a.transfermarkt.technology/portrait/big/92239-1634069098.jpeg)
    - [with players looking sideways in a way that could distort the final picture](https://img.a.transfermarkt.technology/portrait/big/92263-1633779212.jpeg)

5. I ran `create_average_faces.ipynb`, which utilizes the [facer](https://github.com/johnwmillr/Facer) library, to generate pictures of average faces.

## Gallery

![Gallery](gallery.jpg)

You can find the pictures separately in `averages` directory.

## Possible limitations

- We're assuming that football players are a representative sample of the Turkish male population in general.
- Some provinces have small sample sizes.
- Pictures have rather low resolutions.
- No females (yet).
