/*global chrome */
import React from "react";
import SearchIcon from '@mui/icons-material/Search';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import * as ReactDOM from "react-dom";
import Loading from "./Loading";
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';



/**
* Sends message to start retrieval of comment suggestions.
*/
function sendMessage(commentText) {
    ReactDOM.render(<Loading/>, document.getElementById('root'));
    chrome.tabs.query({active: true, currentWindow: true}, function (tabs) {
        chrome.tabs.sendMessage(tabs[0].id, {message: "select_text", commentText: commentText});
    });
}


/**
* Start page of the plugin with search icon the user can click to get suggestions for the selected comment.
*/
function SelectTextButton() {
    //return <Button id="selection_button" variant="text" onClick={sendMessage}><SearchIcon /></Button>;

    const [value, setValue] = React.useState('');
    return <Box>
        <TextField
          id="outlined-multiline-static"
          label="Comment Text"
          multiline
          rows={8}
          value={value}
          onChange={(e) => {
            setValue(e.target.value);
          }}
        />
        <IconButton id="search-button" aria-label="search" size="large" onClick={() => sendMessage(value)}><SearchIcon/></IconButton>
    </Box>
}

export default SelectTextButton;