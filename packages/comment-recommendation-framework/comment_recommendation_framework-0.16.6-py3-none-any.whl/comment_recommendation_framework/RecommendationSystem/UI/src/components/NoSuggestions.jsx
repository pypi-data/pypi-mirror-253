import React from 'react'
import { Message } from 'semantic-ui-react'


/**
* If no suitable comments has been found, this view is rendered for the user.
*/
const NoSuggestions = () => (
<Message warning id="no-selection-hint">
            <img src="images/icons8-404-64.png" />
            <Message.Header id="no-selection-hint-header">No Suggestions</Message.Header>
            <p id="no-selection-hint-body">
               I am sorry, but we can not find any suitable comment suggestions!
            </p>
</Message>
)

export default NoSuggestions;