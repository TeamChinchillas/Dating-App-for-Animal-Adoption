import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import { Container, Stack, Box, Image, Heading } from '@chakra-ui/react'
import Animal from '../../models/Animal'

const data = require('../../sample_data/animals.json')

/**
 * TODO: send request to the server and get animal data
 *
 * @param {number} animalId
 * @returns {Animal}
 */
function findAnimal(animalId) {
  return new Animal(data.find((e) => e.id_animal === parseInt(animalId, 10)))
}

const SUCCESS = 'SUCCESS'
const FAILURE = 'FAILURE'

export default function AnimalDetail() {
  const { animalId } = useParams()

  const [animal, setAnimal] = useState()
  const [status, setStatus] = useState()

  useEffect(() => {
    try {
      setAnimal(findAnimal(animalId))
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
        <Image w="100%" src={animal.imageLink} />
        <Box>
          <Heading size="md">age: {animal.age}</Heading>
        </Box>
        <Box>some text here...</Box>
        <Box>Shelter info?</Box>
      </Stack>
    </Container>
  )
}
