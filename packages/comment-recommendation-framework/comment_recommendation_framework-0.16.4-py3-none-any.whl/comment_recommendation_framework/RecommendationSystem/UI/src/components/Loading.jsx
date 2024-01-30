import * as React from 'react';
import CircularProgress from '@mui/material/CircularProgress';
import Box from '@mui/material/Box';

/**
* Loading animation to indicate that the extension is still working while suggestions retrieved from the backend.
*/
const LoaderExampleIndeterminate = () => (
      <Box id="loading" sx={{ display: 'flex' }}>
      <CircularProgress />
    </Box>
)

export default LoaderExampleIndeterminate