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
} from '@chakra-ui/react'
import { useEffect, useRef, useState } from 'react'
import Animal from '../../models/Animal'

const data = require('../../sample_data/animals.json')

const AnimalCard = ({ animal }) => {
  return (
    <Box flex={{ md: '1 1 30%' }} borderWidth="1px" borderRadius="lg" overflow="hidden" m="2">
      <Image src={animal.imageLink} />

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
          <Box as="span" color="gray.600" fontSize="sm"></Box>
        </Box>

        <Box d="flex" mt="2" alignItems="center">
          <Box as="span" ml="2" color="gray.600" fontSize="sm">
            disposition
          </Box>
        </Box>
      </Box>
    </Box>
  )
}

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
    setAnimals(
      data.map((e) => {
        const res = new Animal(e)
        return res
      })
    )
  }, [])

  const search = () => {
    // TODO: Send search request
    setAnimals(animals.filter((e) => e.name === searchInputRef.current.value))
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

      <Stack>
        <SimpleGrid columns={2} spacing={10}>
          <Box height="80px">
            <Heading size="lg">Animal Profiles</Heading>
          </Box>
          <Box height="80px" textAlign="right">
            <FilterModal />
          </Box>
        </SimpleGrid>

        <Flex flexDirection={{ md: 'row', sm: 'column' }} flexWrap="wrap" justifyContent="center">
          {animals.map((animal) => (
            <AnimalCard animal={animal} key={animal.id} />
          ))}
        </Flex>
      </Stack>
    </Container>
  )
}
