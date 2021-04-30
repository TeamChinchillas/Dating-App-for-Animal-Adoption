import { Container, Flex } from '@chakra-ui/react'
import React, { Component } from 'react'

export default class AdopterSettings extends Component {
  constructor(props) {
    super(props)
    this.state = {
      firstName: '',
      lastName: '',
      emailAddress: '',
      password: '',
      userRole: 'adopter',
      animalPreference: '',
      goodWithAnimals: false,
      goodWithChildren: false,
      animalLeashed: false,
    }

    this.submitForm = this.submitForm.bind(this)
    this.handleChange = this.handleChange.bind(this)
    this.handleCheckbox = this.handleCheckbox.bind(this)
    this.handleDropDown = this.handleDropDown.bind(this)
  }

  componentDidMount() {
    // API GET Method
    // Make API call to get the user's information
    // setState the user's information
    fetch('/get-user-details',
    {
      method:'GET',
      headers:{
        Accept: 'application/json',
        'Content-type': 'application/json'
      },
    })
    .then((results) => results.json())
    .then((data) => {
      let parsedData = JSON.stringify(data)
      parsedData = JSON.parse(parsedData)
      console.log(parsedData)
      console.log(parsedData.message.first_name)

      this.setState({
        firstName: parsedData.message.first_name,
        lastName: parsedData.message.last_name,
        emailAddress: parsedData.message.username
      })
    })
  }

  handleDropDown(event) {
    this.setState({
      [event.target.name]: event.target.value,
    })
  }

  handleCheckbox(event) {
    this.setState({
      [event.target.name]: event.target.checked,
    })
  }

  checkClick(event) {
    const { name, checked } = event.target

    this.setState(() => {
      const animalDisposition = event.disposition_types
      animalDisposition[name] = checked
      return animalDisposition[name]
    })
  }

  handleChange(event) {
    console.log('Handle Change')
    this.setState({
      [event.target.name]: event.target.value,
    })
  }

  submitForm(event) {
    // Console.log messages are for developers to see what will be passed
    // To view any field we enter "event.target.{field_name}.value"
    console.log('Adopter Update Form submitted')
    console.log(event.target.firstName.value)
    console.log(event.target.lastName.value)
    console.log(event.target.emailAddress.value)
    console.log(event.target.animalType.value)
    console.log(event.target.goodWithAnimals.checked)
    console.log(event.target.goodWithChildren.checked)
    console.log(event.target.animalLeashed.checked)
    // Add code to connect to Flask API
    event.preventDefault()
    fetch('/update-user-details', {
      method: 'POST',
      headers: {
        'Content-type' : 'application/json',
      },
      body: JSON.stringify(this.state)
    })
  }

  render() {
    return (
      <Flex justifyContent="center" mt="5">
        <div>
          <h1>Adopter Settings Update</h1>
          <form onSubmit={this.submitForm}>
            <td>
              <input
                type="text"
                name="firstName"
                placeholder={this.state.firstName}
                defaultValue={this.state.firstName}
                onChange={this.handleChange}
              />
              <br />
              <input
                type="text"
                name="lastName"
                placeholder={this.state.lastName}
                defaultValue={this.state.lastName}
                onChange={this.handleChange}
              />
              <br />
              <input
                type="text"
                name="emailAddress"
                placeholder={this.state.emailAddress}
                defaultValue={this.state.emailAddress}
                onChange={this.handleChange}
              />
              <br />
              <input
                type="password"
                name="password"
                placeholder={this.state.password}
                defaultValue={this.state.password}
                onChange={this.handleChange}
              />
              <br />
              <input
                type="text"
                name="animalType"
                placeholder={this.state.animalType}
                defaultValue={this.state.animalType}
                onChange={this.handleChange}
              />
              <br />
              <label>Select Desired Animal Type:</label>
              <select name="animalType" value={this.state.animalType} onChange={this.handleDropDown}>
                <option value="dog">Dog</option>
                <option value="cat">Cat</option>
                <option value="other">Other</option>
              </select>
              <br />
              <label>
                Select Animal Disposition:
                <br />
                <input type="checkbox" name="goodWithAnimals" onChange={this.handleCheckbox} />
                Good with other animals
                <br />
                <input type="checkbox" name="goodWithChildren" onChange={this.handleCheckbox} />
                Good with other children
                <br />
                <input type="checkbox" name="animalLeashed" onChange={this.handleCheckbox} />
                Animal must be leashed at all times
                <br />
              </label>
            </td>
            <button type="submit">Update</button>
          </form>
        </div>
      </Flex>
    )
  }
}
