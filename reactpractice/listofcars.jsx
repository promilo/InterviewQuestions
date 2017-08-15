function Title(props) {
        return (
                <h1>{props.message}</h1>
        )
    }
 function Header(props) {
        return (
                <div>
                    <Title message={props.title}/>
                    <p>{props.message}</p>
                </div>
        )
    }

function InputCheck(props) {
      return (
          <div>
            New Only: <input type = 'checkbox'/>
          </div>
        )
}

function Dropdown(props) {
  var options = props.items.map((item) =>
    <option value={item}> {item} </option>
  )
  return (
    <div>
      {props.message} <select> {options} </select>
    </div>

  )
}

function TableHeader(props){
  return (
                <tr>
                    <th>Year</th>
                    <th>Model</th>
                    <th>Price</th>
                    <th>Buy</th>
                </tr>
        )
}

function TableValues(props) {
  return (
        <tr>
          <td> {props.car.year}</td>
          <td> {props.car.model}</td>
          <td> {props.car.price}</td>
          <td> <button> buy now </button></td>
        </tr>
  )
}

function TableSection(props) {
       var values = props.cars.map((item) => <TableValues car = {item} />)
            return (
              <div>
                  <Title message= {props.title}/>
                  <table>
                    <TableHeader/>
                    {values}
                  </table>

                </div>

  )
}


   function Main() {
        return (
                <div>
                    <Header title="Welcome to React Transportation"
                               message="The best place to buy vehicles online"/>
                    <Title message= "Choose Options" />
                    <InputCheck/>
                    <Dropdown message = "Select Type" items = {["All", "Cars", "Trucks", "Convertibles"]}/>
                    <TableSection title="Cars"
                                  cars={[
                                      {year: "2014", model: "Ford", price: "$32455"},
                                      {year: "2011", model: "GM", price: "$12000"},
                                      {year: "1999", model: "Honda", price: "$11111"}
                                  ]}/>
                    <TableSection title="Trucks"
                                  cars={[
                                      {year: "2014", model: "Ford", price: "$32455"},
                                      {year: "2011", model: "GM", price: "$12000"}
                                  ]}/>
                    <TableSection title="Convertibles"
                                  cars={[
                                      {year: "2014", model: "Ford", price: "$32455"},
                                      {year: "2011", model: "GM", price: "$12000"},
                                      {year: "1999", model: "Honda", price: "$11111"},
                                      {year: "2009", model: "Nissan", price: "40000"}
                                  ]}/>
                </div>
        )
    }


    ReactDOM.render(
            <Main/>,
        document.getElementById('root')
    )

// https://codepen.io/promilo/pen/qXVZGW?editors=0010
