import {Message} from "semantic-ui-react";
import React from "react";

/**
* Hint for the user if the extension is triggered while no comment has been selected.
*/
function NoSelectionHint(){
    return(
        <Message negative id="no-selection-hint">
            <Message.Header id="no-selection-hint-header">No Selection</Message.Header>
            <p id="no-selection-hint-body">
                It seems that you don't have selected any text.
            </p>
        </Message>
    )
}

export default NoSelectionHint;