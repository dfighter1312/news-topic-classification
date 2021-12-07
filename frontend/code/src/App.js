import React, { useState } from "react";
import "./App.css";

const corsAnywhere = "https://cors-anywhere.herokuapp.com/";
const exampleClassPoints = {
  Sport: 0.3123,
  Food: 0.13,
  Business: 0.2323,
  Travel: 0.3116,
  Medical: 0.823,
  Trend: 0.0123,
  Culture: 0.32423,
  Lifestyle: 0.5523,
  Companies: 0.2923,
  Places: 0.12,
};

function App() {
  const [title, setTitle] = useState("");
  const [body, setBody] = useState("");
  const [classPoints, setClassPoints] = useState([{}, {}, {}, {}, {}, {}, {}]);
  const [bestClass, setBestClass] = useState(null);

  const findArgmax = (obj) => {
    let maxVal = 0,
      argmax = null;
    for (let key in obj) {
      if (obj[key] > maxVal) {
        maxVal = obj[key];
        argmax = key;
      }
    }
    return argmax;
  };

  const handleClick = () => {
    console.log("click run analysis button");
    var raw = JSON.stringify({ title: title, body: body });
    var requestOptions = {
      method: "POST",
      body: raw,
      redirect: "follow",
    };

    fetch("http://localhost:5000/v1/prototype/predict", requestOptions)
      .then((res) => res.json())
      .then((result) => {
        console.log(result, "Ahihi");
        setClassPoints(result);
        setBestClass(findArgmax(result));
      });
    console.log(bestClass);
  };

  const Topic = () => {
    return (
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          flexDirection: "column",
          marginRight: 60,
          marginTop: 20,
        }}
      >
        <div
          style={{
            width: 200,
            height: 50,
            backgroundColor: "#3D85C6",
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            borderRadius: 15,
          }}
        >
          <p
            style={{
              padding: 0,
              margin: 0,
              fontSize: "24px",
              color: "white",
              fontWeight: "bold",
            }}
          >
            Sport
          </p>
        </div>
        <p
          style={{
            padding: 0,
            margin: 0,
            marginTop: 10,
            fontSize: "24px",
          }}
        >
          0.999
        </p>
      </div>
    );
  };

  return (
    <div>
      <header>
        <img
          width="100%"
          height="200"
          src="https://www.desktopbackground.org/download/o/2013/12/23/690042_free-for-pc-download-wallpaper-lifestyle-keren_1341x739_h.jpg"
          alt="logo"
          style={{ objectFit: "cover" }}
        />
        <div
          style={{
            width: "100%",
            height: "200px",
            backgroundColor: "rgba(52, 58, 64, 0.5)",
            position: "absolute",
            top: 0,
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            flexDirection: "column",
          }}
        >
          <h
            style={{
              fontFamily: "Roboto",
              fontStyle: "normal",
              fontWeight: "normal",
              fontSize: "48px",
              // lineHeight: "48px",
              color: "white",
            }}
          >
            NEWS ARTICLE CLASSIFICATION
          </h>
          <p
            style={{
              fontFamily: "Roboto",
              fontStyle: "normal",
              fontWeight: 100,
              fontSize: "32px",
              // lineHeight: "34px",
              color: "white",
              padding: 0,
              margin: 0,
            }}
          >
            Intelligent System Project
          </p>
        </div>
      </header>
      <div style={{ padding: 100, paddingTop: 30 }}>
        <div
          style={{
            backgroundColor: "#EDF4FF",
            borderRadius: 39,
            height: 100,
            padding: 20,
            paddingRight: 5,
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <p
            style={{
              fontStyle: "normal",
              fontWeight: 500,
              fontSize: "24px",
              // lineHeight: "34px",
              color: "#000000",
              padding: 0,
              margin: 0,
            }}
          >
            This site is an application project of Intelligent System design.
            The model we use classify news article content into VNExpress tags.
            To test the model, enter your article’s title and content in the
            text box below and view the result.
          </p>
        </div>
        <div
          style={{
            height: 779,
            border: "1px solid #999999",
            marginTop: 40,
            borderRadius: 15,
            padding: 20,
            display: "flex",
            flexDirection: "column",
            boxShadow: "0px 4px 8px rgba(0, 0, 0, 0.25)",
            boxSizing: "border-box",
          }}
        >
          <div
            style={{
              position: "absolute",
              right: 140,
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <p style={{ margin: 0, padding: 0, marginRight: 20 }}>
              ... OR upload a .docx file
            </p>
            <svg
              width="63"
              height="63"
              viewBox="0 0 63 63"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <circle cx="31.5" cy="31.5" r="31.5" fill="#3D85C6" />
              <path
                d="M26.0857 38.5206H36.7143V28.1265H43.8L31.4 16L19 28.1265H26.0857V38.5206ZM19 41.9853H43.8V45.45H19V41.9853Z"
                fill="white"
                fill-opacity="0.87"
              />
            </svg>
          </div>

          <input
            style={{
              width: "80%",
              border: "none",
              fontSize: "32px",
              color: "#434142",
              fontWeight: 200,
              outline: "none",
            }}
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Your article"
          ></input>
          <div
            style={{
              width: 180,
              height: 1,
              backgroundColor: "#999999",
              marginTop: 10,
              marginBottom: 30,
            }}
          ></div>
          <textarea
            style={{
              border: "none",
              height: "100%",
              overFlow: "hidden",
              overflowY: "scroll",
              fontSize: "24px",
              borderWidth: 0,
              padding: 0,
              margin: 0,
              outline: "none",
              resize: "none",
            }}
            value={body}
            onChange={(e) => setBody(e.target.value)}
            placeholder="ENTER TEXT HERE"
          ></textarea>
          <div
            style={{
              display: "flex",
              justifyContent: "flex-end",
              paddingRight: 20,
            }}
          >
            <button
              style={{
                backgroundColor: "#3D85C6",
                color: "white",
                fontWeight: "bold",
                width: 250,
                height: 50,
                borderRadius: 10,
                borderWidth: 0,
                fontSize: "20px",
              }}
              onClick={handleClick}
            >
              RUN ANALYSIS
            </button>
          </div>
        </div>
        <div
          style={{
            display: "flex",
            // justifyContent: "center",
            alignItems: "center",
            width: "100%",
            marginTop: 50,
            flexDirection: "column",
          }}
        >
          <p style={{ margin: 0, padding: 0, fontSize: "30px" }}>
            Your article is classified as{" "}
            <span style={{ fontWeight: "bold" }}>Sport</span>
          </p>
          <div
            style={{
              display: "flex",
              width: "100%",
              flexWrap: "wrap",
              justifyContent: "center",
              alignContent: "center",
              marginTop: 20,
            }}
          >
            {classPoints.map((e) => {
              return <Topic />;
            })}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
