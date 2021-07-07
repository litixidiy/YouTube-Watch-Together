let changeTime = document.getElementById('changeTime');

changeTime.addEventListener("click", async () => {
  chrome.tabs.query({
    active: true,
    currentWindow: true
  }, function (tabs) {
    chrome.tabs.executeScript(
      tabs[0].id, {
        code: "document.querySelector('.video-stream').currentTime = 100;"
      });
  });
});

// The body of this function will be executed as a content script inside the
// current page
function setTime(newTime) {
  document.querySelector('.video-stream').currentTime = newTime;
  //});
}



// method that checks and changes the time:


//code: 'document.querySelector(\'.video-stream\').currentTime=100;'
//document.querySelector('.video-stream').getCurrentTime(); to get time - float
//document.querySelector('.video-stream').currentTime=100; to set time - float 