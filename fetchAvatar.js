const https = require('https');
const fs = require('fs');

const url = 'https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds=1640644089&size=420x420&format=Png&isCircular=false';

https.get(url, (res) => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => {
    try {
      const json = JSON.parse(data);
      if (json.data && json.data[0] && json.data[0].imageUrl) {
        const imageUrl = json.data[0].imageUrl;
        console.log("Found image URL:", imageUrl);
        
        // Download it
        const file = fs.createWriteStream('./assets/avatar.png');
        https.get(imageUrl, (response) => {
          response.pipe(file);
          file.on('finish', () => {
            file.close();
            console.log("Image downloaded to assets/avatar.png");
          });
        });
      } else {
        console.log("Could not parse image URL:", json);
      }
    } catch (e) {
      console.log("Error parsing JSON:", e);
    }
  });
}).on('error', err => {
  console.log("Error:", err.message);
});
