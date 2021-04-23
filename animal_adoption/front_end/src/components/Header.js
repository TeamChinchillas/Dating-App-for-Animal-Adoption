import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import { Box, Flex, Text, Button, Heading, Spacer } from '@chakra-ui/react'

const MenuItem = (props) => {
  const { to, children } = props
  return (
    <Text mt="{{ base: 5, md: 0 }}" mr={6}>
      <Link to={to}>{children}</Link>
    </Text>
  )
}

export default function Header() {
  const [show, setShow] = useState(false)
  const handleToggle = () => setShow(!show)

  return (
    <Flex as="nav" align="center" justify="space-between" wrap="wrap" padding="1.5rem" bg="white">
      <Box>
        <Heading as="h1" size="lg" letterSpacing="-.1rem">
          Animal Adoption
        </Heading>
      </Box>

      <Spacer />

      <Box display={{ base: 'block', md: 'none' }} onClick={handleToggle}>
        <svg fill="green" width="20px" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
          <title>Menu</title>
          <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" />
        </svg>
      </Box>

      <Box display={{ sm: show ? 'block' : 'none', md: 'flex' }} width={{ sm: 'full', md: 'auto' }}>
        <MenuItem to="/">Home</MenuItem>
        <MenuItem to="/about">About</MenuItem>
      </Box>

      <Box display={{ sm: show ? 'block' : 'none', md: 'block' }} mt={{ base: 4, md: 0 }}>
        <Button colorScheme="green">
          <Link to="/signup">Sign up</Link>
        </Button>
        <Button colorScheme="green">
          <Link to="/login">Login</Link>
        </Button>
      </Box>
    </Flex>
  )
}
