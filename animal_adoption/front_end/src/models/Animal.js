export default class Animal {
  constructor(data) {
    this.id = data.id_animal
    this.name = data.name
    this.age = data.age
    this.description = data.description
    this.imageLink = data.image_link
    this.adoptionStatus = data.adoption_status
    this.shelter = data.shelter
  }
}
