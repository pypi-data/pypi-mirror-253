import React from 'react'
import { Message } from 'semantic-ui-react'

/**
* Error screen with icon and text in case when something has not worked as planed.
*/
const ErrorScreen = () => (
  <Message negative id="no-selection-hint">
            <img src="images/icons8-error-64.png" />
            <Message.Header id="no-selection-hint-header">Error</Message.Header>
            <p id="no-selection-hint-body">
                 We are very sorry! An error has occurred.
            </p>
        </Message>
)

export default ErrorScreen;