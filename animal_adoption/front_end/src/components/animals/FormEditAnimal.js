import { Input, FormControl, FormLabel, Image } from '@chakra-ui/react'

function PreviewImage({ animal }) {
  if (animal?.imageLink) {
    return <Image src={animal.imageLink} />
  }
  return <div>Preview: No data</div>
}

export default function FormEditAnimal({ animal, setAnimal }) {
  const handleImageFile = (event) => {
    const file = event.target.files[0]
    setAnimal({
      ...animal,
      imageLink: URL.createObjectURL(file),
      file,
    })
  }

  const handleChange = (event) => {
    setAnimal({
      ...animal,
      [event.target.name]: event.target.value,
    })
  }

  return (
    <FormControl>
      <FormLabel>Name</FormLabel>
      <Input type="text" name="name" defaultValue={animal?.name} onChange={handleChange} />
      <FormLabel>Age</FormLabel>
      <Input type="number" name="age" defaultValue={animal?.age} onChange={handleChange} />
      <FormLabel>Description</FormLabel>
      <Input
        type="number"
        name="description"
        defaultValue={animal?.description}
        onChange={handleChange}
      />
      <FormLabel>Image</FormLabel>
      <Input type="file" name="image" mb="1" onChange={handleImageFile} />
      <PreviewImage animal={animal} />
    </FormControl>
  )
}
