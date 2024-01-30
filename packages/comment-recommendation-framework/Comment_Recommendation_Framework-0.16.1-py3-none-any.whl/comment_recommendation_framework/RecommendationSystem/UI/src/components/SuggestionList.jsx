import React from 'react'
import {Icon, List} from 'semantic-ui-react'
import Avatar from '@mui/material/Avatar';
import Stack from '@mui/material/Stack';
import DeleteIcon from '@mui/icons-material/Delete';
import IconButton from '@mui/material/IconButton';
import { styled } from '@mui/material/styles';
import Tooltip, { tooltipClasses } from '@mui/material/Tooltip';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';




const CustomTextButton = styled(Button)({
    fontSize: 11,
    color: "black"
})

const HtmlTooltip = styled(({ className, ...props }) => (
  <Tooltip {...props} classes={{ popper: className }} />
))(({ theme }) => ({
  [`& .${tooltipClasses.tooltip}`]: {
    backgroundColor: '#f5f5f9',
    color: 'rgba(0, 0, 0, 0.87)',
    maxWidth: 550,
    fontSize: theme.typography.pxToRem(12),
    border: '1px solid #dadde9',
  },
}));

/**
* Single suggestion element for a suggestion from the backend.
*/
function suggestionElement(text) {

    if(text === "NO_SUITABLE_RECOMMENDATIONS"){
        return (<List.Item style={{padding: "1em"}}>
            <List.Content>
            <Stack direction="column" spacing={2}>
                <Avatar alt="No recommendations" sx={{ width: 80, height: 80 }} src={"icons8-search-not-found.png"} />
                <List.Description as='a'>Es tut uns leid, aber wir konnten keine guten Vorschläge finden!</List.Description>
            </Stack>
            </List.Content>
        </List.Item>)
    }


    return (<List.Item style={{padding: "1em"}}>
        <List.Content>
        <Stack direction="row" spacing={2}>
       <HtmlTooltip
        title={
          <React.Fragment>
            <Typography color="inherit">Article Information</Typography>
            <List>
            <List.Item>
            <List.Content>
            {"Artikel Titel: " + text[2]}
            </List.Content>
            </List.Item>
            <List.Item>
            <List.Content>
            {"Artikel Url: "}
            <a href={text[3]}>{text[3]}</a>
            </List.Content>
            </List.Item>
            </List>
          </React.Fragment>
        }
      >
        <CustomTextButton>
        <List.Description as='a'><Card variant='outlined'>{text[0]}</Card></List.Description>
        </CustomTextButton>
      </HtmlTooltip>


        </Stack>
        </List.Content>
    </List.Item>)
}

/**
* Maps list of suggestions to single suggestion element.
*/
function renderListItems(suggestions) {
    return suggestions.map((text) => suggestionElement(text))
}

/**
* List of suggestions from the backend server
*/
function SuggestionList(props) {
    return (
        <div id="suggestion-list">
            <Icon id="extension-logo" name='searchengin' size='huge'/>
            <List divided relaxed>
                {renderListItems(props.suggestions)}
            </List>
        </div>
    )
}

export default SuggestionList;
