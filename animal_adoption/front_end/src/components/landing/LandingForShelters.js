import {
  Button,
  Image,
  Box,
  Stack,
  Heading,
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
import Animal from '../../models/Animal'

const data = require('../../sample_data/animals.json')

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

export default function LandingForShelters() {
  const [animals, setAnimals] = useState(null)

  /**
   * Delete animal from animals
   *
   * @param {Animal} animal
   */
  const deleteAnimal = (animal) => {
    // TODO: pseudo implementation.
    // Send request to server-side
    const ans = window.confirm('Are you sure to delete this animal from your profiles?')
    if (ans) {
      setAnimals(animals.filter((e) => e.id !== animal.id))
    }
  }

  useEffect(() => {
    setAnimals(
      data.map((e) => {
        const res = new Animal(e)
        return res
      })
    )
  }, [])

  if (animals === null) {
    return (
      <Container centerContent p="5">
        <Spinner size="xl" />
      </Container>
    )
  }

  return (
    <Flex justifyContent="center" mt="5">
      <Stack>
        <Heading alignSelf="center" size="lg">
          Animal Profiles
        </Heading>
        <Box height="80px" textAlign="right">
          <Link to="/animals/create">
            <Button colorScheme="blue">Create new profile</Button>
          </Link>
        </Box>

        <Table border="1px">
          <Thead>
            <Tr bgColor="green.100">
              <Th border="1px">Photo</Th>
              <Th border="1px">Name</Th>
              <Th border="1px">Age</Th>
              <Th border="1px">Description</Th>
              <Th border="1px">Status</Th>
              <Th border="1px">Action</Th>
            </Tr>
          </Thead>
          <Tbody>
            {animals.map((animal) => (
              <Tr key={animal.id}>
                <Td border="1px">
                  <Link to={`animals/${animal.id}`}>
                    <Image src={animal.imageLink} />
                  </Link>
                </Td>
                <Td border="1px"> {animal.name} </Td>
                <Td border="1px"> {animal.age} </Td>
                <Td border="1px"> {animal.description} </Td>
                <Td border="1px"> {animal.status} </Td>
                <Td border="1px">
                  <Link to={`animals/${animal.id}/edit`}>
                    <Button mr="2" colorScheme="teal">
                      Edit
                    </Button>
                  </Link>
                  <Button colorScheme="red" onClick={() => deleteAnimal(animal)}>
                    Delete
                  </Button>
                </Td>
              </Tr>
            ))}
          </Tbody>
        </Table>
      </Stack>
    </Flex>
  )
}
