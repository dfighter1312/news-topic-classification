import React, { useState } from "react";
import "./App.css";
import PizZip from "pizzip";
import Docxtemplater from "docxtemplater";
import { Drawer, Button } from "antd";
import { Upload, message, Spin } from "antd";
import { InboxOutlined } from "@ant-design/icons";

const { Dragger } = Upload;

function App() {
  const [title, setTitle] = useState("");
  const [body, setBody] = useState("");
  const [classPoints, setClassPoints] = useState([]);
  const [bestClass, setBestClass] = useState(null);
  const [visible, setVisible] = useState(false);
  const [loading, setLoading] = useState(false);
  const showDrawer = () => {
    setVisible(true);
  };

  const onClose = () => {
    setVisible(false);
  };

  const propsDrag = {
    name: "file",
    multiple: true,
    action: "https://www.mocky.io/v2/5cc8019d300000980a055e76",
    onChange(info) {
      const { status } = info.file;
      if (status !== "uploading") {
        console.log(info.file, info.fileList);
      }
      if (status === "done") {
        message.success(`${info.file.name} file uploaded successfully.`);
      } else if (status === "error") {
        message.error(`${info.file.name} file upload failed.`);
      }
    },
    onDrop(e) {
      console.log("Dropped files", e.dataTransfer.files);
    },
  };

  const findArgmax = (obj) => {
    console.log("OBBB", obj);
    for (let i = 0; i < obj.length; i++) {
      if (obj[i].bestClass) return obj[i];
    }
  };

  const handleClick = () => {
    console.log("click run analysis button");
    var raw = JSON.stringify({ title: title, body: body });
    var myHeaders = new Headers();

    myHeaders.append("Content-Type", "application/json");

    var requestOptions = {
      method: "POST",
      body: raw,
      headers: myHeaders,
      redirect: "follow",
    };

    if (body.length > 10000) {
      message.error("Body text need to smaller 10000 characters");
      return;
    }
    if (body.length < 100) {
      message.error("Body text need to greater 100 characters");
      return;
    }

    try {
      setLoading(true);
      fetch("http://localhost:5000/v1/predict", requestOptions)
        .then((res) => res.json())
        .then((result) => {
          setLoading(false);
          console.log(result, "Ahihi");
          setClassPoints(result);
          console.log("Best", findArgmax(result));
          setBestClass(findArgmax(result));
        });
    } catch (err) {
      console.log(err);
    }

    console.log(bestClass);
  };

  const showFile = async (e) => {
    e.preventDefault();
    const reader = new FileReader();
    reader.onload = async (e) => {
      const content = e.target.result;
      var doc = new Docxtemplater(new PizZip(content), {
        paragraphLoop: true,
        linebreaks: true,
      });
      var text = doc.getFullText();

      console.log("Test", text);
      setBody(text);
    };
    reader.readAsBinaryString(e.target.files[0]);
  };

  const Topic = ({ data }) => {
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
            {data.className}
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
          {data.score.toFixed(4)}
        </p>
      </div>
    );
  };

  return (
    <Spin spinning={loading} size="large">
      <Drawer
        title="Multi-level drawer"
        width={1024}
        closable={false}
        onClose={onClose}
        visible={visible}
      >
        <Dragger {...propsDrag}>
          <p className="ant-upload-drag-icon">
            <InboxOutlined />
          </p>
          <p className="ant-upload-text">
            Click or drag file to this area to upload
          </p>
          <p className="ant-upload-hint">
            Support for a single or bulk upload. Strictly prohibit from
            uploading company data or other band files
          </p>
        </Dragger>
      </Drawer>
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
      <div
        style={{
          padding: 100,
          paddingTop: 30,
          paddingRight: 200,
          paddingLeft: 200,
        }}
      >
        <div
          style={{
            backgroundColor: "#EDF4FF",
            borderRadius: 39,
            height: 50,
            padding: 30,
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
              fontSize: "16px",
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
            height: 500,
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
              right: 240,
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
            }}
            // onClick={showDrawer}
          >
            <input
              type="file"
              style={{
                width: 63,
                height: 63,
                position: "absolute",
                opacity: 0,
              }}
              onChange={(e) => showFile(e)}
            />

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
              fontSize: "24px",
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
              fontSize: "16px",
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
              marginTop: 10,
            }}
          >
            <div
              style={{
                color:
                  body.length > 10000 || body.length < 100
                    ? "#FF1414"
                    : "#333132",
              }}
            >{`${body.length}/10000`}</div>
            <div style={{ flex: 1 }}></div>
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
          {bestClass && (
            <p style={{ margin: 0, padding: 0, fontSize: "30px" }}>
              Your article is classified as{" "}
              <span style={{ fontWeight: "bold", color: "#DC143C" }}>
                {bestClass.className}
              </span>
            </p>
          )}

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
              return <Topic data={e} />;
            })}
          </div>
        </div>
      </div>
    </Spin>
  );
}

export default App;
