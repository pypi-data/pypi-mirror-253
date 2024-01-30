/*global chrome*/

console.log("Background script is running");


/**
 * background.js coordinates the communication of the plugin with the backend server.
 */

let backendServerAddress = 'http://127.0.0.1:8000'


/**
 * Listens for 'send_request' message to send selected comment and keywords to backend server and waits for response.
 */
chrome.runtime.onMessage.addListener(
    function (request, sender, sendResponse) {
        if (request.message === "send_to_api") {
            let extracted_data = new Map(request.data);
            console.log(extracted_data)

            let keywords = extracted_data.get("keywords");
            let user_comment = extracted_data.get("comment_selection");

            // Create url by adding information the model needs like this. Here we encoded a comment the user selected and the keywords of the article the user is reading
            let url = backendServerAddress + '/comments/?user_comment=' + encodeURIComponent(user_comment)
                + "&keywords=" + encodeURIComponent(JSON.stringify(keywords));

            console.log("Sending request to backend");
            fetch(url).then(response => response.json()).then(response => sendResponse(response)).catch(() => sendResponse({farewell: {"message": ["error"]}}))

            return true;
        }
    }
)
