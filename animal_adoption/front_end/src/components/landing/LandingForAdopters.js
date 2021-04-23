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
import { Link, useParams } from 'react-router-dom'
import Animal from '../../models/Animal'

const data = require('../../sample_data/animals.json')

const AnimalCard = ({ animal }) => (
  <Box borderWidth="1px" borderRadius="lg" overflow="hidden" m="2" cursor="pointer">
    <Image w="100%" src={animal.imageLink} />

    <Box p="6">
      <Box d="flex" alignItems="baseline">
        <Badge borderRadius="full" px="2" colorScheme="teal">
          New
        </Badge>
      </Box>

      <Box mt="1" fontWeight="semibold" as="h4" lineHeight="tight" isTruncated>
        {animal.name}
      </Box>

      <Box>
        <Box as="span" color="gray.600" fontSize="sm" />
      </Box>

      <Box d="flex" mt="2" alignItems="center">
        <Box as="span" ml="2" color="gray.600" fontSize="sm">
          disposition
        </Box>
      </Box>
    </Box>
  </Box>
)

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

export default function LandingForAdopters() {
  const searchInputRef = useRef()

  const [animals, setAnimals] = useState(null)

  useEffect(() => {
    setAnimals(data.map((e) => new Animal(e)))
  }, [])

  const search = () => {
    const allAnimals = data.map((e) => new Animal(e))
    const searchWord = searchInputRef.current.value.toLowerCase()
    // TODO: Send an actual search request to the server-side
    setAnimals(allAnimals.filter((e) => e.name.toLowerCase().includes(searchWord)))
  }

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
        <Input placeholder="Find a pet" rounded="xl" ref={searchInputRef} />
        <InputRightAddon as="button" rounded="xl" onClick={search}>
          Search
        </InputRightAddon>
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
            <FilterModal />
          </Box>
        </Grid>

        <Grid templateColumns="repeat(auto-fit, minmax(160px, 270px))" justifyContent="center">
          {animals.map((animal) => (
            <Link to={`/animals/${animal.id}`} key={animal.id}>
              <AnimalCard animal={animal} />
            </Link>
          ))}
        </Grid>
      </Stack>
    </Container>
  )
}
