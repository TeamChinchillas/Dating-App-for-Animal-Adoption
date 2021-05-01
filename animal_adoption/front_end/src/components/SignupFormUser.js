import { Button, Input, FormControl, FormLabel, Select} from '@chakra-ui/react'
import React, { Component } from 'react'

export default class SignupFormUser extends Component {
  constructor(props) {
    super(props)
    this.state = {
      firstName: '',
      lastName: '',
      username: '',
      password: '',
      userType: 'adopter',
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

  handleChange(event) {
    this.setState({
      [event.target.name]: event.target.value,
    })
  }

  submitForm(event) {
    // Console.log messages are for developers to see what will be passed
    // To view any field we enter "event.target.{field_name}.value"
    console.log('Adopter Form submitted')
    console.log(event.target.firstName.value)
    console.log(event.target.lastName.value)
    console.log(event.target.username.value)
    console.log(event.target.password.value)
    console.log(event.target.animalPreference.value)
    console.log(event.target.goodWithAnimals.checked)
    console.log(event.target.goodWithChildren.checked)
    console.log(event.target.animalLeashed.checked)
    event.preventDefault()
    fetch('/create-user-with-all-details', {
      method: 'POST',
      headers: {
        'Content-type': 'application/json',
      },
      body: JSON.stringify(
        this.state
        // this.state.firstName.value,
        // this.state.lastName.value,
        // this.state.username.value,
        // this.state.password.value,
        // this.state.animalType.value,
        // this.state.goodWithAnimals.value,
        // this.state.goodWithChildren.value,
        // this.state.animalLeashed.value
        ),
    })
    console.log(this.state)
    // console.log('STATE STRINGIFIED')
    // console.log(JSON.stringify(this.state))
    // Add code to connect to Flask API
  }

  // Add required later
  render() {
    return (
      <div>
        <h1> Adopter Registration Form</h1>
        <FormControl>
        <form onSubmit={this.submitForm}>
          <FormLabel>First Name</FormLabel>
          <input
            type="text"
            name="firstName"
            placeholder="First Name"
            value={this.state.firstName}
            onChange={this.handleChange}
          />
          <br />
          <FormLabel>Last Name</FormLabel>
          <input
            type="text"
            name="lastName"
            placeholder="Last Name"
            value={this.state.lastName}
            onChange={this.handleChange}
          />
          <br />
          <FormLabel>E-Mail Address</FormLabel>
          <input
            type="email"
            name="username"
            placeholder="Email Address"
            value={this.state.username}
            onChange={this.handleChange}
          />
          <br />
          <FormLabel>Password</FormLabel>
          <input
            type="password"
            name="password"
            placeholder="Password"
            value={this.state.password}
            onChange={this.handleChange}
          />
          <br />
          <FormLabel>Select Desired Animal Type:</FormLabel>
          <Select name="animalPreference" value={this.state.animalPreference} onChange={this.handleDropDown}>
            <option value="dog">Dog</option>
            <option value="cat">Cat</option>
            <option value="other">Other</option>
          </Select>
          <br />
          <FormLabel>Select Animal Disposition:</FormLabel>
            <br />
            <input
              type="checkbox"
              name="goodWithAnimals"
              value={this.state.goodWithAnimals}
              onChange={this.handleCheckbox}
            />
            <FormLabel>Good with other animals</FormLabel>
            <br />
            <input
              type="checkbox"
              name="goodWithChildren"
              value={this.state.goodWithChildren}
              onChange={this.handleCheckbox}
            />
            <FormLabel>Good with other children</FormLabel>
            <br />
            <input
              type="checkbox"
              name="animalLeashed"
              value={this.state.animalLeashed}
              onChange={this.handleCheckbox}
            />
            <FormLabel>Animal must be leashed at all times</FormLabel>
            <br />
          <Button type="submit" colorScheme="green">Register</Button>
        </form>
        </FormControl>
      </div>
    )
  }
}
