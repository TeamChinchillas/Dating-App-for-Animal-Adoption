export default class Animal {
  constructor(data) {
    this.id = data?.id_animal ?? ''
    this.name = data?.name ?? ''
    this.age = data?.age
    this.description = data?.description ?? ''
    this.animalClass = data?.animal_class ?? 'other'
    this.animalBreed = data?.animal_breed ?? 'other'
    this.dispositions = data?.dispositions ?? []
    this.adoptionStatus = data?.adoption_status ?? 'Available'

    this.shelter = data?.shelter

    this.imageData = null // for submit an image file
    this.imageLink = data?.image_path?.replace('animal_adoption/front_end/public', '') ?? ''
  }
}
