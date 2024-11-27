const ffmpeg = require('fluent-ffmpeg');
const fs = require('fs');
const path = require('path');

const index = 2;
// Input and output file paths
const file = `./raw/${index}.mp4`;
const mp3File = `./out/${index}.mp3`;

// Convert MP4 to MP3 with noise reduction
const convert = () => {
  return new Promise((resolve, reject) => {
    ffmpeg(file)
      .audioFilter('afftdn=nf=-25') // Apply noise reduction
      .output(mp3File)
      .on('end', () => {
        console.log('MP3 conversion complete.');
        resolve();
      })
      .on('error', (err) => {
        console.error('Error during MP3 conversion:', err);
        reject(err);
      })
      .run();
  });
};

// Main function to execute the workflow
const run = async () => {
  try {
    await convert(); // Convert MP4 to MP3
  } catch (err) {
    console.error('An error occurred:', err);
  }
};

run();
