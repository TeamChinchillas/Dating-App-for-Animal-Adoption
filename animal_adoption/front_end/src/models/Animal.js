export const animalBreeds = ['golden retriever', 'border collie', 'tabby', 'bengal', 'other']
export const animalClasses = ['dog', 'cat', 'other']

/**
 * @param {string|null} imagePath 
 * @returns {string}
 */
function getImageLink(imagePath) {
  if (!imagePath) {
    return ''
  }

  if (imagePath.startsWith('animal_adoption/front_end/public')) {
    return imagePath.replace('animal_adoption/front_end/public', '')
  }

  if (imagePath.startsWith('animal_adoption/front_end/build')) {
    return imagePath.replace('animal_adoption/front_end/build', '')
  }

  return ''
}

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
    this.imageLink = getImageLink(data?.image_path)
  }
}
