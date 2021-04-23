import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom'
import { Flex, Box } from '@chakra-ui/react'
import { useState, useEffect } from 'react'
import Landing from './pages/Landing'
import SignupPage from './pages/SignupPage'
import Header from './components/Header'
import Footer from './components/Footer'
import UserContext from './components/users/UserContext'

function App() {
  const [user, setUser] = useState()

  return (
    <UserContext.Provider value={{ user, setUser }}>
      <Flex direction="column" flexFlow="column" minH="100vh">
        <Header />

        <Box as="main" flex="1" bg="gray.50">
          <Switch>
            <Route path="/account">
              <div>Account page</div>
            </Route>
            <Route path="/signup">
              <SignupPage />
            </Route>
            <Route path="/login">
              <div>Login page</div>
            </Route>
            <Route path="/about">
              <Box as="p" p="5">
                This is a capstone project for OSU CS467.
                <br />
                This is a dating app project that matches shelter animals up with prospective
                owners.
              </Box>
            </Route>
            <Route path="/">
              <Landing />
            </Route>
          </Switch>
        </Box>

        <Footer />
      </Flex>
    </UserContext.Provider>
  )
}

export default App
