import { Box, Flex, Heading } from '@chakra-ui/react'

export default function Footer() {
  return (
    <Flex as="nav" align="center" justify="space-between" wrap="wrap" padding="1.5rem" bg="white">
      <Box>
        <Heading as="h1" size="lg" letterSpacing="-.1rem">
          Footer
        </Heading>
      </Box>
    </Flex>
  )
}
