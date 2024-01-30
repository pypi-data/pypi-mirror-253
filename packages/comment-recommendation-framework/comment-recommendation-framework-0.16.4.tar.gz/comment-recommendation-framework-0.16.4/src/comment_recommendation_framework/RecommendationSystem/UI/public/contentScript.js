/*global chrome */


/**
 * This functions reads the news agency website the user is currently reading and would like to have recommendations for.
 * @return  {Map} Store extracted data in map
 */
function read_website() {
    let extracted_data = new Map();
    // Add here the methods to read the information the recommendation model needs from the news agency website and
    // store them in the extracted_data map

    extracted_data.set("keywords", read_keywords())

    return extracted_data
}

function read_keywords() {
    let url = window.location.href;
    let urlParts = url.split("/");
    let keywords = null;

    if(urlParts[urlParts.length - 1].length == 0){
        keywords = urlParts[urlParts.length - 2].split("_")[0];
    }else{
        keywords = urlParts[urlParts.length - 1].split("_")[0];
    }
    return keywords
}
/**
 * Listens for message 'select_text' to read selected comment and keywords from article and sends them to 'App.js'.
 */
chrome.runtime.onMessage.addListener(
    function (request, sender, sendResponse) {
        if (request.message === "select_text") {
            let extracted_data = read_website();
            console.log("Data from text field")
            console.log(request.commentText);
            extracted_data.set("comment_selection", request.commentText);

            console.log("Send message");
            console.log(extracted_data)
            chrome.runtime.sendMessage({
                    message: "send_to_api",
                    "data": [...extracted_data]
                },
                function (response) {
                    console.log("Sending Recommendations");
                    chrome.runtime.sendMessage({
                           message: "Sending_recommendations",
                           "recommendations": response.suggestions
                        }
                    );
                });
        } else {
            chrome.runtime.sendMessage({message: "no_selection"});
        }
        sendResponse();
    }
);
