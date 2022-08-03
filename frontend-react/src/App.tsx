import React, { useState } from "react";
import logo from "./logo.svg";
import "./App.css";

export const App = () => {
  const [data, setData] = useState<string[]>();

  const sensorRead = async () => {
    // const uri = "http://192.168.0.15:8000";

    const temperature = String(20 + Math.floor(Math.random() * 11));
    const humidity = String(40 + Math.floor(Math.random() * 21));
    setData([temperature, humidity]);

    /* await fetch(uri + "/data", {
      method: "GET",
    })
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        console.log(data);
        setData([data.temperature, data.humidity]);
      })
      .catch((err) => {
        const temperature = String(20 + Math.floor(Math.random() * 11));
        const humidity = String(40 + Math.floor(Math.random() * 21));
        setData([temperature, humidity]);
        console.error(err);
      });*/
  };
  /*
  useEffect(() => {
    sensorRead();
  }, []);*/
  return (
    <div className="App">
      {data ? (
        <div>
          <p>気温:{data[0]}C</p>
          <p>湿度:{data[1]}%</p>
        </div>
      ) : (
        <div></div>
      )}
      <button onClick={sensorRead}>温湿度を取得する</button>
    </div>
  );
};
