import {
  InputGroup,
  Input,
  InputRightAddon,
  Button,
  Image,
  Box,
  Stack,
  Heading,
  Badge,
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
  Grid,
} from '@chakra-ui/react'
import { useEffect, useRef, useState } from 'react'
import { Link } from 'react-router-dom'
import Animal from '../../models/Animal'

const AnimalCard = ({ animal }) => (
  <Box borderWidth="1px" borderRadius="lg" overflow="hidden" m="2" cursor="pointer">
    <Image w="100%" src={animal.imageLink} />

    <Box p="6">
      <Box d="flex" alignItems="baseline">
        <Badge borderRadius="full" px="2" colorScheme="teal">
          {animal.animalClass} - {animal.animalBreed}
        </Badge>
      </Box>

      <Box mt="1" fontWeight="semibold" as="h4" lineHeight="tight" isTruncated>
        {animal.name} (Age: {animal.age})
      </Box>

      <Box>
        <Box as="span" color="gray.600" fontSize="sm" />
      </Box>

      <Box d="flex" mt="2" alignItems="center">
        <Box as="span" ml="2" color="gray.600" fontSize="sm">
          <ul>
            {animal.dispositions.map((e) => (
              <li key={e}>{e}</li>
            ))}
          </ul>
        </Box>
      </Box>
    </Box>
  </Box>
)

export default function LandingForAdopters() {
  const [animals, setAnimals] = useState(null)

  useEffect(async () => {
    try {
      const { message } = await fetch('/get-animals').then((res) => res.json())
      if (message) {
        setAnimals(JSON.parse(message).map((e) => new Animal(e)))
      }
    } catch (e) {
      setAnimals([])
      console.error(e)
    }
  }, [])

  const fetchMatchingAnimals = async () => {
    try {
      const { message } = await fetch('/get-matching-animals').then((res) => res.json())
      if (message) {
        setAnimals(JSON.parse(message).map((e) => new Animal(e)))
      }
    } catch (e) {
      setAnimals([])
      console.error(e)
    }
  }

  const [searchWord, setSearchWord] = useState('')

  const filteredAnimals = () => {
    if (searchWord === '') {
      return animals
    }
    return animals.filter((e) => e.name.toLowerCase().includes(searchWord))
  }

  const handleSearchWordChange = (event) => setSearchWord(event.target.value.toLowerCase())

  if (animals === null) {
    return (
      <Container centerContent p="5">
        <Spinner size="xl" />
      </Container>
    )
  }

  return (
    <Container centerContent>
      <InputGroup m="5" size="md">
        <Input placeholder="Find a pet" rounded="xl" onChange={handleSearchWordChange} />
      </InputGroup>

      <Stack w="60vw">
        <Grid templateColumns="repeat(auto-fit, minmax(180px, 1fr))">
          <Box>
            <Heading size="lg" textAlign={{ base: 'center', sm: 'center' }}>
              Animal Profiles
            </Heading>
          </Box>
          <Box
            mt={{ sm: 5, md: 0, base: 0 }}
            mr={{ sm: 0, base: 10 }}
            textAlign={{ base: 'right', sm: 'center' }}
          >
            <Button colorScheme="green" onClick={fetchMatchingAnimals}>Find Matching animals</Button>
          </Box>
        </Grid>

        <Grid templateColumns="repeat(auto-fit, minmax(160px, 270px))" justifyContent="center">
          {filteredAnimals().map((animal) => (
            <Link to={`/animals/${animal.id}`} key={animal.id}>
              <AnimalCard animal={animal} />
            </Link>
          ))}
        </Grid>
      </Stack>
    </Container>
  )
}
