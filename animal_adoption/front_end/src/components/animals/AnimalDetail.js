import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import {
  Container,
  Stack,
  Box,
  Image,
  Heading,
  Table,
  Thead,
  Th,
  Tr,
  Td,
  Tbody,
} from '@chakra-ui/react'
import Animal from '../../models/Animal'

const SUCCESS = 'SUCCESS'
const FAILURE = 'FAILURE'

export default function AnimalDetail() {
  const { animalId } = useParams()

  const [animal, setAnimal] = useState()
  const [status, setStatus] = useState()

  useEffect(async () => {
    try {
      const response = await fetch(`/get-animal-details-by-id?animalId=${animalId}`).then((res) =>
        res.json()
      )
      setAnimal(new Animal(response))
      setStatus(SUCCESS)
    } catch (e) {
      setStatus(FAILURE)
    }
  }, [])

  if (!animal && !status) {
    return <div>loading...</div>
  }

  if (status === FAILURE) {
    return <div>Not Found</div>
  }

  return (
    <Container centerContent p="2">
      <Stack>
        <Box>
          <Heading size="lg">{animal.name}</Heading>
        </Box>
        <Image
          w="80%"
          src={animal.imageLink}
          fallbackSrc="https://via.placeholder.com/300?text=no%20photo"
        />
        <Box>
          <Heading size="md" mb="2">
            Status
          </Heading>
          {animal.adoptionStatus}
        </Box>
        <Box>
          <Heading size="md" mb="2">
            Age
          </Heading>
          {animal.age}
        </Box>
        <Box>
          <Heading size="md" md="2">
            Description
          </Heading>
          {animal.description}
        </Box>
        <Box>
          <Heading size="md" mb="2">
            Dispositions
          </Heading>
          <Box pl="5">
            <ul>
              {animal.dispositions.map((e) => (
                <li key={e}>{e}</li>
              ))}
            </ul>
          </Box>
        </Box>
        <Box>
          <Heading size="md" mb="2">
            Class
          </Heading>
          {animal.animalClass}
        </Box>
        <Box>
          <Heading size="md" mb="2">
            Breed
          </Heading>
          {animal.animalBreed}
        </Box>
        <Box mt="2" mb="3">
          creation date: {animal.creationDate}
        </Box>

        <hr />

        <Box>
          <Heading size="md" mt="5">
            Shelter Info
          </Heading>
          <Table variant="simple" mt="2">
            <Tbody>
              <Tr>
                <Th>Name</Th>
                <Td>{animal.shelter?.name}</Td>
              </Tr>
              <Tr>
                <Th>Physical Address</Th>
                <Td>{animal.shelter?.physical_address}</Td>
              </Tr>
              <Tr>
                <Th>Phone Number</Th>
                <Td>{animal.shelter?.phone_number}</Td>
              </Tr>
              <Tr>
                <Th>Email Address</Th>
                <Td>{animal.shelter?.email_address}</Td>
              </Tr>
            </Tbody>
          </Table>
        </Box>
      </Stack>
    </Container>
  )
}
