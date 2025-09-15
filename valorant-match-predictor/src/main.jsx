import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import TeamSelect from './components/TeamSelectPage/TeamSelect.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    {/* <App /> */}
    <TeamSelect />
  </StrictMode>,
)
