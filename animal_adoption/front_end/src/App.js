import { Switch, Route } from 'react-router-dom'
import Landing from './pages/Landing'
import { Flex, Box } from '@chakra-ui/react'
import Header from './components/Header'
import Footer from './components/Footer'
import UserContext from './components/users/UserContext'

import { useState, useEffect } from 'react'

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
              <div>Sign up page</div>
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
    </UserContext.Provider>
  )
}

export default App
