/*global chrome */
import React from 'react';
import './App.css';
import SelectTextButton from "./components/SelectTextButton";
import SuggestionList from "./components/SuggestionList";
import * as ReactDOM from "react-dom";
import NoSelectionHint from "./components/NoSelectionHint"
import Loading from "./components/Loading";
import NoSuggestions from "./components/NoSuggestions";
import ErrorScreen from "./components/ErrorScreen";


/**
 * App.js generates the UI of the plugin and renders different views depending on the response from the backend server.
 */

/**
 * Sends request with selected comment and keywords of article to background.js. Then it waits for the response to
 * render the page accordingly.
 * @param {String}selection - Selected comment from news agency comment section
 * @param {String}keywords - Keywords of the article the selected comment has appeared under
 */
/*
function sendRequest(selection, keywords) {
    chrome.runtime.sendMessage(
        {
            message: "send_request",
            selection: selection,
            keywords: keywords
        },
        function (response) {
            console.log("Received suggestions");
            console.log(response.farewell);
            if (response.farewell.suggestions[0] === "NO_SUITABLE_COMMENTS") {
                ReactDOM.render(<NoSuggestions/>, document.getElementById('root'));
            } else if (response.farewell.suggestions[0] === "error"){
                ReactDOM.render(<ErrorScreen />, document.getElementById('root'));
            }
            else {
                ReactDOM.render(<SuggestionList
                    suggestions={response.farewell.suggestions}/>, document.getElementById('root'));
            }
        });
}

 */

/**
 * Listens for message that a comment has been selected and triggers sendRequest function to send selected comment
 * and keywords to background.js. If no comment has been selected and the plugin has been triggered a hint for the
 * user will be displayed.
 */
/*
chrome.runtime.onMessage.addListener(
    function (request) {
        if (request.message === "selection") {
            ReactDOM.render(<Loading/>, document.getElementById('root'));
            console.log("Response received");
            let selection = JSON.parse(request.selection_text);
            let keywords = JSON.parse(request.keywords);
            console.log(selection);
            console.log(keywords);
            sendRequest(selection, keywords);
        } else if (request.message === "no_selection") {
            console.log("No selection");
            ReactDOM.render(<NoSelectionHint/>, document.getElementById('root'));
        }
    }
)
 */


chrome.runtime.onMessage.addListener(
    function (request) {
        console.log("bar");
        if (request.message === "Sending_recommendations") {
            let results = request.recommendations;
            console.log(results)
            ReactDOM.render(<SuggestionList
                suggestions={results}/>, document.getElementById('root'));
        }
    }
)


/**
 * Renders start page of plugin.
 * @returns {JSX.Element}
 * @constructor
 */
function App() {
    return (
        <div className="App" id="App">
            <SelectTextButton/>
        </div>
    );
}

export default App;