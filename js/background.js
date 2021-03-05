var rule1 = {
	conditions: [new chrome.declarativeContent.PageStateMatcher({ pageUrl: { hostEquals: 'www.youtube.com', schemes: ['https'] } })
		, new chrome.declarativeContent.PageStateMatcher({ css: ["video"] })],
	actions: [new chrome.declarativeContent.ShowPageAction()]

};

chrome.runtime.onInstalled.addListener(function (details) {
	chrome.declarativeContent.onPageChanged.removeRules(undefined, function () {
		chrome.declarativeContent.onPageChanged.addRules([rule1]);
	});
});