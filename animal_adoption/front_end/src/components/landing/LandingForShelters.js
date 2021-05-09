import {
  Button,
  Image,
  Box,
  Stack,
  Heading,
  Flex,
  Spinner,
  Container,
  useDisclosure,
  Table,
  Thead,
  Th,
  Tr,
  Td,
  Tbody,
} from '@chakra-ui/react'
import { Link } from 'react-router-dom'
import { useEffect, useState } from 'react'
import Animal from '../../models/Animal'
import Drawer from '../common/Drawer'
import FormEditAnimal from '../animals/FormEditAnimal'

export default function LandingForShelters() {
  const [animals, setAnimals] = useState(null)
  const [selectedAnimal, setSelectedAnimal] = useState()
  const { isOpen, onOpen, onClose: _onClose } = useDisclosure()

  useEffect(async () => {
    try {
      const { message } = await fetch('/get-animals-of-shelter').then((res) => res.json())
      if (message) {
        setAnimals(JSON.parse(message).map((e) => new Animal(e)))
      }
    } catch (e) {
      setAnimals([])
      console.error(e)
    }
  }, [])

  const editAnimal = (animal) => {
    setSelectedAnimal({ ...animal })
    onOpen()
  }

  const onClose = () => {
    setSelectedAnimal()
    _onClose()
  }

  const onSave = () => {
    // TODO: actually send request to the server
    setAnimals(animals.map((e) => (e.id === selectedAnimal.id ? selectedAnimal : e)))
    setSelectedAnimal()
    _onClose()
  }

  /**
   * Delete animal from animals
   *
   * @param {Animal} animal
   */
  const deleteAnimal = (animal) => {
    // TODO: pseudo implementation. Send request to server-side
    const ans = window.confirm('Are you sure to delete this animal from your profiles?')
    if (ans) {
      setAnimals(animals.filter((e) => e.id !== animal.id))
    }
  }

  if (!animals) {
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
              <Th border="1px">class</Th>
              <Th border="1px">breed</Th>
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
                <Td border="1px"> {animal.animalClass} </Td>
                <Td border="1px"> {animal.animalBreed} </Td>
                <Td border="1px"> {animal.adoptionStatus} </Td>
                <Td border="1px">
                  <Button mr="2" colorScheme="teal" onClick={() => editAnimal(animal)}>
                    Edit
                  </Button>
                  <Button colorScheme="red" onClick={() => deleteAnimal(animal)}>
                    Delete
                  </Button>
                </Td>
              </Tr>
            ))}
          </Tbody>
        </Table>

        {/* Edit animal profile */}
        <Drawer isOpen={isOpen} onClose={onClose} onSave={onSave} header="Edit animal profile">
          <FormEditAnimal animal={selectedAnimal} setAnimal={setSelectedAnimal} />
        </Drawer>
      </Stack>
    </Flex>
  )
}
