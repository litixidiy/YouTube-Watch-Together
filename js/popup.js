let changeTime = document.getElementById('changeTime');

changeTime.onclick = function (element) {
  let color = element.target.value;
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    chrome.tabs.executeScript(
      tabs[0].id,

      { code: 'document.querySelector(\'.video-stream\').currentTime=100;' });
  });
};

//document.querySelector('.video-stream').getCurrentTime(); to get time - float
//document.querySelector('.video-stream').currentTime=100; to set time - float 