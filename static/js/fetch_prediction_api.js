function showSpinner() {
  var spinner = document.getElementById("spinner");
  spinner.style.display = "block";
}

function hideSpinner() {
  var spinner = document.getElementById("spinner");
  spinner.style.display = "none";
}

function previewImage() {
  var fileInput = document.getElementById("fileInput");
  var previewImage = document.getElementById("previewImage");
  var predictionsList = document.getElementById("predictions");
  predictionsList.innerHTML = "";

  var file = fileInput.files[0];
  if (file) {
    var reader = new FileReader();
    reader.onload = function (e) {
      previewImage.src = e.target.result;
    };
    reader.readAsDataURL(file);
  }
}

function classifyImage() {
  var fileInput = document.getElementById("fileInput");
  var img = document.getElementById("previewImage");

  if (fileInput.files.length === 0) {
    alert("Please choose an image first.");
    return;
  }
  showSpinner();
  sendImageToServer(img);
}

function sendImageToServer(img) {
  var canvas = document.createElement("canvas");
  canvas.width = 224;
  canvas.height = 224;
  var ctx = canvas.getContext("2d");
  ctx.drawImage(img, 0, 0, 224, 224);

  var imgData = canvas
    .toDataURL("image/jpeg", 1.0)
    .replace(/^data:image.+;base64,/, "");
  canvas = null;

  //var imgData = ctx.getImageData(0, 0, 224, 224).data;
  //var imgArray = new Float32Array(imgData);

  // Normalize the pixel values to be between 0 and 1
  //for (var i = 0; i < imgArray.length; i++) {
  //imgArray[i] /= 255.0;
  //}

  // Send the image data to the server for classification
  fetch("/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ image: imgData }),
  })
    .then((response) => response.json())
    .then((predictions) => {
      hideSpinner();
      displayPredictions(predictions);
    })
    .catch((error) => {
      hideSpinner();
      console.error("Error:", error);
    });
}

function displayPredictions(predictions) {
  var predictionsList = document.getElementById("predictions");
  predictionsList.innerHTML = "";

  predictions.forEach(function (prediction) {
    var listItem = document.createElement("li");
    listItem.textContent = `${prediction["image"]}`;
    predictionsList.appendChild(listItem);
  });
}
