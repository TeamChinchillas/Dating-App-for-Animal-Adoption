import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom'
import Landing from './pages/Landing'
import { Flex, Box } from '@chakra-ui/react'
import Signup_Page from './pages/Signup_Page'
import Header from './components/Header'
import Footer from './components/Footer'

function App() {
  return (
    <Router>
      <Flex direction="column" flexFlow="column" minH="100vh">
        <Header />

        <Box as="main" flex="1" bg="gray.50">
          {/* main */}
          <Switch>
            <Route path="/account">
              <div>Account page</div>
            </Route>
            <Route path="/signup">
              <Signup_Page/>
            </Route>
            <Route path="/login">
              <div>Login page</div>
            </Route>
            <Route path="/about">
              <Box as="p" p="5">
                This is a capstone project for OSU CS467.
                <br />
                This is a dating app project that matches shelter animals up with prospective owners.
              </Box>
            </Route>
            <Route path="/">
              <Landing />
            </Route>
          </Switch>
        </Box>

        <Footer />
      </Flex>
    </Router>
  )
}

export default App
