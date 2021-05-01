export default class User {
  constructor(data) {
    console.log(data);
    this.username = data.username
    this.firstName = data.firstName
    this.lastName = data.lastName
    this.emailAddress = data.username
    this.userType = data.userType
  }

  get isShelterWorker() {
    return this.userType === 'shelter worker'
  }

  get isAdopter() {
    return this.userType === 'adopter'
  }

  get isAdministrator() {
    return this.userType === 'administrator'
  }
}
