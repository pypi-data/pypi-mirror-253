/*global chrome */
import React from "react";
import SearchIcon from '@mui/icons-material/Search';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import * as ReactDOM from "react-dom";
import Loading from "./Loading";

/**
* Sends message to start retrieval of comment suggestions.
*/
function sendMessage() {
    ReactDOM.render(<Loading/>, document.getElementById('root'));

    chrome.tabs.query({active: true, currentWindow: true}, function (tabs) {
        chrome.tabs.sendMessage(tabs[0].id, {message: "select_text"});
    });
}


/**
* Start page of the plugin with search icon the user can click to get suggestions for the selected comment.
*/
function SelectTextButton() {
    //return <Button id="selection_button" variant="text" onClick={sendMessage}><SearchIcon /></Button>;
    return <IconButton id="search-button" aria-label="search" size="large" onClick={sendMessage}><SearchIcon/></IconButton>
}

export default SelectTextButton;