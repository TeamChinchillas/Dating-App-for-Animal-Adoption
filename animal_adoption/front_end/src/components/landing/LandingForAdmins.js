import {
  InputGroup,
  Input,
  InputRightAddon,
  Button,
  Image,
  Box,
  Stack,
  SimpleGrid,
  Heading,
  Text,
  Badge,
  Flex,
  Spinner,
  Container,
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton,
  useDisclosure,
  Table,
  Thead,
  Th,
  Tr,
  Td,
  Tbody,
} from '@chakra-ui/react'
import { Link } from 'react-router-dom'
import { useEffect, useRef, useState } from 'react'
import User from '../../models/User'

const data = require('../../sample_data/users.json')

const FilterModal = () => {
  const { isOpen, onOpen, onClose } = useDisclosure()

  return (
    <>
      <Button colorScheme="green" onClick={onOpen}>
        Filter
      </Button>

      <Modal isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>Filter</ModalHeader>
          <ModalCloseButton />
          <ModalBody>Filter form</ModalBody>
          <ModalFooter>
            <Button colorScheme="gray" mr={3} onClick={onClose}>
              Close
            </Button>
            <Button colorScheme="green" onClick={onClose}>
              OK
            </Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  )
}

export default function LandingForAdmins() {
  const [users, setUsers] = useState(null)

  /**
   * Delete user
   *
   * @param {number} userId
   */
  const deleteUser = (userId) => {
    // TODO: pseudo implementation.
    // Send request to server-side
    const ans = window.confirm('Are you sure to delete this user?')
    if (ans) {
      setUsers(users.filter((e) => e.id !== userId))
    }
  }

  useEffect(() => {
    setUsers(data.map((e) => new User(e)))
  }, [])

  if (users === null) {
    return (
      <Container centerContent p="5">
        <Spinner size="xl" />
      </Container>
    )
  }

  return (
    <Flex justifyContent="center" mt="5">
      <Stack w="60vw">
        <Heading alignSelf="center" size="lg" mb="2">
          User lists
        </Heading>
        {(users?.length ?? 0) !== 0 ? (
          <Table border="1px">
            <Thead>
              <Tr bgColor="green.100">
                <Th border="1px">Username</Th>
                <Th border="1px">First Name</Th>
                <Th border="1px">Last Name</Th>
                <Th border="1px">Email</Th>
                <Th border="1px">User Type</Th>
                <Th border="1px">Action</Th>
              </Tr>
            </Thead>
            <Tbody>
              {users.map((user) => (
                <Tr key={user.id}>
                  <Td border="1px"> {user.username} </Td>
                  <Td border="1px"> {user.firstName} </Td>
                  <Td border="1px"> {user.lastName} </Td>
                  <Td border="1px"> {user.emailAddress} </Td>
                  <Td border="1px"> {user.userType} </Td>
                  <Td border="1px">
                    <Button mr="2" colorScheme="teal">
                      Edit
                    </Button>
                    <Button colorScheme="red" onClick={() => deleteUser(user.id)}>
                      Delete
                    </Button>
                  </Td>
                </Tr>
              ))}
            </Tbody>
          </Table>
        ) : (
          <Box bg="orange.100" p="5">
            No profiles found
          </Box>
        )}
      </Stack>
    </Flex>
  )
}
