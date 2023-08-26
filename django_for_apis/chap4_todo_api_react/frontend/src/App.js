// export default App;
import React, { Component } from 'react';
import axios from 'axios';

/*
const list = [
  {
    "id": 1,
    "title": "Learning HTTP",
    "body": "learn learn learn"
    },
    {
    "id": 2,
    "title": "Second Item",
    "body": "Second"
    }
]

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {list};  
  }

  render() {
    return(
      <div>
        {this.state.list.map(item =>(
          <div key={item.id}>
            <h1>{item.title}</h1>
            <p>{item.body}</p>
            <p>{item.id}</p>
          </div>
        ))}
      </div>
    );
  }
}
export default App;
*/

class App extends Component {
  state = {
    todos: []
  };

  componentDidMount() {
    this.getTodos();
  }

  getTodos() {
    axios
      .get('http://localhost:8000/api/')
      .then(res => {
        this.setState({ todos: res.data });
      })
      .catch(err => {
        console.log(err);
      });
  }

  render() {
    return(
      <div>
        {this.state.todos.map(item =>(
          <div key={item.id}>
            <h1>{item.title}</h1>
            <p>{item.body}</p>
            <p>{item.id}</p>
          </div>
        ))}
      </div>
    );
  }
}
export default App;
