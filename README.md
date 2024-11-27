# Matka Counter

## Installations

Install NPM packages:

```bash
npm i
```

Install the python packages:

```bash
pip install -r requirements.txt
```

## Place the video

Place the video in the `raw` folder.
Name it as follows: `3.mp4`

> Replace 3 with the sequence of the video

## Update scripts

Update the scripts in `countHits.py` and `reduceNoise.js`, change the `index` to the sequence of the video.

## Run the script

First run the noise reduction script:

```bash
node reduceNoise.js
```

Then run the main script:

```bash
python countHits.py
```

## Output

The output will be saved in the `out` folder with a text file named `3.txt`.
