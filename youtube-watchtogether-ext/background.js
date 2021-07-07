var rule1 = {
	conditions: [new chrome.declarativeContent.PageStateMatcher({
		pageUrl: {
			hostEquals: 'www.youtube.com',
			schemes: ['https']
		}
	}), new chrome.declarativeContent.PageStateMatcher({
		css: ["video"]
	})],
	actions: [new chrome.declarativeContent.ShowPageAction()]

};


chrome.runtime.onInstalled.addListener((reason) => {
	console.log("Installed");
	chrome.declarativeContent.onPageChanged.removeRules(undefined, function () {
		chrome.declarativeContent.onPageChanged.addRules([rule1]);
	});
	console.log("Set Rules");
	/*
	if (reason === chrome.runtime.OnInstalledReason.INSTALL) {
	  chrome.tabs.create({
		url: 'onboarding.html'
	  });
	}*/

	var socket = io.connect('http://127.0.0.1:5000');
	
	try {
		socket.on('connect', function() {
			console.log("socketio imported");
			socket.emit('test event', {data: 'pls work'});
		});
	  } catch (error) {
		console.error(error);
		// expected output: ReferenceError: nonExistentFunction is not defined
		// Note - error messages will vary depending on browser
	  }
});

