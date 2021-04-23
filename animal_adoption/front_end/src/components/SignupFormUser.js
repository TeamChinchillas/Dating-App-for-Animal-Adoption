import React, { Component } from 'react'

export default class SignupFormUser extends Component {
  constructor(props) {
    super(props)
    this.state = {
      firstName: '',
      lastName: '',
      emailAddress: '',
      animalType: '',
      goodWithAnimals: false,
      goodWithChildren: false,
      animalLeashed: false,
    }

    this.submitForm = this.submitForm.bind(this)
    this.handleChange = this.handleChange.bind(this)
  }

  checkClick(event) {
    const { name, checked } = event.target

    this.setState(() => {
      const animalDisposition = event.disposition_types
      animalDisposition[name] = checked
      return animalDisposition[name]
    })
  }

  submitForm(event) {
    // Console.log messages are for developers to see what will be passed
    // To view any field we enter "event.target.{field_name}.value"
    console.log('Adopter Form submitted')
    console.log(event.target.firstName.value)
    console.log(event.target.lastName.value)
    console.log(event.target.emailAddress.value)
    console.log(event.target.animalType.value)
    console.log(event.target.goodWithAnimals.checked)
    console.log(event.target.goodWithChildren.checked)
    console.log(event.target.animalLeashed.checked)
    // Add code to connect to Flask API
    event.preventDefault()
  }

  handleChange(event) {
    console.log('Handle Change')
    this.setState({
      [event.target.name]: event.target.value,
    })
    console.log(event.target.name)
  }

  // Add required later
  render() {
    return (
      <div>
        <h1> Adopter Registration Form</h1>
        <form onSubmit={this.submitForm}>
          <input
            type="text"
            name="firstName"
            placeholder="First Name"
            value={this.state.firstName}
            onChange={this.handleChange}
          />
          <br />
          <input
            type="text"
            name="lastName"
            placeholder="Last Name"
            value={this.state.lastName}
            onChange={this.handleChange}
          />
          <br />
          <input
            type="email"
            name="emailAddress"
            placeholder="Email Address"
            value={this.state.email}
            onChange={this.handleChange}
          />
          <br />
          <label>Select Desired Animal Type:</label>
          <select name="animalType" value={this.state.animalType} onChange={this.handleChange}>
            <option value="dog">Dog</option>
            <option value="cat">Cat</option>
            <option value="other">Other</option>
          </select>
          <br />
          <label>
            Select Animal Disposition:
            <br />
            <input type="checkbox" name="goodWithAnimals" onChange={this.handleChange} />
            Good with other animals
            <br />
            <input type="checkbox" name="goodWithChildren" onChange={this.handleChange} />
            Good with other children
            <br />
            <input type="checkbox" name="animalLeashed" onChange={this.handleChange} />
            Animal must be leashed at all times
            <br />
            <br />
          </label>
          <button type="submit">Register</button>
        </form>
      </div>
    )
  }
}
