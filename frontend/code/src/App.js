import React, {useState} from 'react';
import './App.css'

const corsAnywhere = "https://cors-anywhere.herokuapp.com/"
const exampleClassPoints = {
  'Sport': 0.3123, 
  'Food': 0.13,
  'Business': 0.2323,
  'Travel': 0.3116,
  'Medical': 0.823,
  'Trend': 0.0123,
  'Culture': 0.32423,
  'Lifestyle': 0.5523,
  'Companies': 0.2923,
  'Places': 0.12,
}


function App() {
  const [inputText, setInputText] = useState('');
  const [classPoints, setClassPoints] = useState({});
  const [bestClass, setBestClass] = useState(null);

  const findArgmax = (obj) => {
    let maxVal = 0, argmax = null;
    for(let key in obj) {
      if (obj[key] > maxVal) {
        maxVal = obj[key];
        argmax = key;
      }
    }
    return argmax;
  }

  

  const handleClick = () => {
    console.log("click run analysis button");
    
    fetch("http://localhost:5000/v1/prototype/predict")
      .then(res => res.json())
      .then((result) => {
        console.log(result);
        setClassPoints(result);
        setBestClass(findArgmax(result));
      });
    console.log(bestClass);
  }

  return (
    <div>
      <div>
        <p>NEWS ARTICLE CLASSIFICATION</p>
        
        <textarea 
          value={inputText} 
          onChange={(event) => setInputText(event.target.value)}
          placeholder="ENTER TEXT HERE..."
          cols="100"
          rows="20"
        />
        
        <br></br>
        <button
          onClick={handleClick}
        >
          RUN ANALYSIS  
        </button>

        {/* <p> {inputText}</p> */}

      </div>
      {
        (bestClass === null) ? null:
        <div>
          <p>Your article is classified as <b>{bestClass}</b></p>
          <div className='grid-container'>             
            {Object.keys(classPoints).map(key => (
              <div className='grid-item' key={key}> 
                <b>{key}</b> 
                <br></br>
                {key===bestClass? 
                  <div className='special-text'> {classPoints[key].toFixed(4)}  </div> : <div> {classPoints[key].toFixed(4)}  </div>}
                
              </div>))}
            
          </div>
        </div>
      }
    </div>
  );
}

export default App;
