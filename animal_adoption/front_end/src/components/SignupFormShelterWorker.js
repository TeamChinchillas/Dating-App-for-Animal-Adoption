import React, { Component } from 'react'

const shelter_names = []

export default class SignupFormShelterWorker extends Component {
  constructor(props) {
    super(props)
    this.state = {
      firstName: '',
      lastName: '',
      username: '',
      password: '',
      userType: 'shelter worker',
      shelterNames: [],
      shelterName: ''
    }

    this.submitForm = this.submitForm.bind(this)
    this.handleChange = this.handleChange.bind(this)
    this.handleDropDown = this.handleDropDown.bind(this)
  }

  componentDidMount() {
    fetch('/get-shelters', {
      method: 'GET',
      headers: {
        Accept: 'application/json',
        'Content-type': 'application/json',
      },
    })
      .then((results) => results.json())
      .then((data) => {
        let parsed_data = JSON.stringify(data)
        parsed_data = JSON.parse(parsed_data)
        const data_length = parsed_data.message.length
        
        for(let i = 0; i < data_length; i += 1){
          shelter_names.push(parsed_data.message[i].name)
        }

        this.setState({shelterNames: shelter_names})
      })
  }

  handleDropDown(event) {
    this.setState({
      [event.target.name]: event.target.value,
    })
  }

  handleChange(event) {
    console.log('Handle Change')
    console.log("Event Target Name")
    console.log(event.target.name)
    this.setState({
      [event.target.name]: event.target.value,
    })
    console.log(event.target.name)
  }

  submitForm(event) {
    console.log('Shelter Worker Form submitted')
    console.log(event.target.firstName.value)
    console.log(event.target.lastName.value)
    console.log(event.target.username.value)
    console.log(event.target.shelterName.value)
    // To view any field we enter "event.target.{field_name}.value"
    // Add code to connect to Flask API
    fetch('/create-user-with-all-details', {
      method: 'POST',
      headers: {
        'Content-type': 'application/json',
      },
      body: JSON.stringify(
        this.state.firstName,
        this.state.lastName,
        this.state.username,
        this.state.password,
        this.state.userType,
        this.state.shelterName
      ),
    })

    console.log('STATE STRINGIFIED')
    console.log(JSON.stringify(this.state))
  }

  render() {
    return (
      <div>
        <h1>Shelter Worker Signup Form</h1>
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
            name="username"
            placeholder="E-Mail Address"
            value={this.state.username}
            onChange={this.handleChange}
          />
          <br />
          <input
            type="password"
            name="password"
            placeholder="Password"
            value={this.state.password}
            onChange={this.handleChange}
          />
          <br />
          <label>Select Shelter:</label>
          
          <select name="shelterName" value={this.state.shelterName} onChange={this.handleDropDown}>
            {this.state.shelterNames.map(item => (
                <option key={item} value={item} >
                  {item}
                </option>
            ))}
            </select>
          <br />
          <button type="submit">Register</button>
        </form>
      </div>
    )
  }
}
