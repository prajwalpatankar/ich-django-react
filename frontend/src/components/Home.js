import React, { Component } from 'react';
import axios from 'axios';

class Home extends Component {

  state = {
    dicomFile: null
  };

  handleImageChange = (e) => {
    this.setState({
      dicomFile: e.target.files[0]
    })
  };

  handleSubmit = (e) => {
    e.preventDefault();
    console.log(this.state);
    let form_data = new FormData();
    form_data.append('dicomFile', this.state.dicomFile, this.state.dicomFile.name);
    let url = 'http://localhost:8000/uploaddicom/';
    axios.post(url, form_data, {
      headers: {
        'content-type': 'multipart/form-data',
        'Access-Control-Allow-Origin':  'http://127.0.0.1:3000'
      }
    })
      .then(res => {
        console.log("Response => ")
        console.log(res);
      //   let get_url = 'http://localhost:8000/model_output?id=' + res.data.id
      //   console.log(get_url)
      //   axios.get(get_url)
      //     .then(res => {
      //       console.log(res);
      //     })
      //     .catch(err => console.log(err))
      })
      .catch(err => console.log(err))
  };

  render() {
    return (
      <div className="App">
        <div className="App-header">
          <br /><br /><br /><br /><br />
          <form onSubmit={this.handleSubmit}>
            <p>
              <input type="file"
                id="model_pic"
                // accept="image/png, image/jpeg" 
                onChange={this.handleImageChange} required />
            </p>
            <input type="submit" />
          </form>
        </div>
      </div>
    );
  }
}

export default Home;